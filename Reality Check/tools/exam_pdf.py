#!/usr/bin/env python3
"""Собирает PDF с условиями экзамена Reality Check (без карты навыков, интерпретации и ключа).

    python3 "Reality Check/tools/exam_pdf.py" "Reality Check/Exams/<Область>/<экзамен>.md" -o "Reality Check/Students/<Имя>/<Код>/<дата>/exam.pdf"
    python3 "Reality Check/tools/exam_pdf.py" "Reality Check/Variants/<Код>/vN.md" --variant vN -o <exam.pdf>
    python3 "Reality Check/tools/exam_pdf.py" --zip "Reality Check/exams_math_and_phys.zip"

Основные экзамены лежат в Reality Check/Exams/<Область>/, варианты — в Reality Check/Variants/<Код>/.

Нужен pdfLaTeX (TeX Live) с кириллицей: babel-russian, cm-super (T2A), amsmath, adjustbox, newunicodechar, enumitem, titlesec, fancyhdr, lastpage.
Источник берётся из рабочей копии; в колонтитул пишется последний коммит файла
(если в файле есть незакоммиченные изменения, скрипт отказывается работать).
"""
import argparse, glob, os, re, shutil, subprocess, sys, tempfile, zipfile

STOP_HEADING = '## Карта навыков'

TEXT_SPECIAL = {'\\': r'\textbackslash{}', '{': r'\{', '}': r'\}', '#': r'\#', '$': r'\$',
                '%': r'\%', '&': r'\&', '_': r'\_', '~': r'\textasciitilde{}', '^': r'\textasciicircum{}'}
MATH_UNICODE = {'≤': r'\le ', '≥': r'\ge ', '→': r'\to ', '∞': r'\infty ', '…': r'\dots ', '−': '-',
                '×': r'\times ', '·': r'\cdot ', '≈': r'\approx ', '≠': r'\ne ', '∈': r'\in ', '—': r'\text{---}'}

PREAMBLE = r"""\documentclass[11pt,a4paper]{article}
\usepackage{cmap}
\usepackage[T2A]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[russian]{babel}
\usepackage{amsmath,amssymb,mathtools,mathrsfs}
\usepackage{adjustbox}
\usepackage{newunicodechar}
\newunicodechar{≈}{\ensuremath{\approx}}
\newunicodechar{≤}{\ensuremath{\le}}
\newunicodechar{≥}{\ensuremath{\ge}}
\newunicodechar{·}{\ensuremath{\cdot}}
\newunicodechar{→}{\ensuremath{\to}}
\newunicodechar{⇒}{\ensuremath{\Rightarrow}}
\newunicodechar{×}{\ensuremath{\times}}
\newunicodechar{−}{\ensuremath{-}}
\usepackage[a4paper,margin=2.2cm,top=2cm,bottom=2.4cm]{geometry}
\usepackage{enumitem}
\setlist{itemsep=0.35em,topsep=0.4em,leftmargin=2.2em}
\usepackage{titlesec}
\titleformat{\section}{\large\bfseries}{}{0pt}{}
\titlespacing*{\section}{0pt}{1.4em}{0.6em}
\usepackage{xcolor}
\usepackage{fancyhdr,lastpage}
\pagestyle{fancy}\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\fancyfoot[L]{\parbox[b]{0.84\textwidth}{\raggedright\scriptsize\color{black!60}<<FOOTER>>}}
\fancyfoot[R]{\footnotesize\color{black!60}\thepage\ из \pageref{LastPage}}
\usepackage[hidelinks]{hyperref}
\setlength{\parindent}{0pt}\setlength{\parskip}{0.55em}
\emergencystretch=5em\tolerance=1500
\allowdisplaybreaks
\begin{document}
"""


def esc_text(s):
    return ''.join(TEXT_SPECIAL.get(ch, ch) for ch in s)


def fix_math(m):
    """Формула из markdown → корректный LaTeX для pdfLaTeX."""
    for k, v in MATH_UNICODE.items():
        m = m.replace(k, v)
    # Кириллица и прочие не-ASCII буквы в формуле (вне \text{...}) — в \text{}
    return re.sub(r'(\\text\{[^{}]*\})|([^\x00-\x7f]+(?:\s+[^\x00-\x7f]+)*)',
                  lambda mm: mm.group(1) if mm.group(1) else r'\text{' + mm.group(2) + '}', m)


def inline(s, store):
    """Строка markdown → LaTeX. Формулы и код прячутся в store и возвращаются плейсхолдерами."""
    def keep(latex):
        store.append(latex); return f'\x00{len(store) - 1}\x00'
    s = re.sub(r'\$`(.*?)`\$', lambda m: keep('$' + fix_math(m.group(1)) + '$'), s)
    s = re.sub(r'``\s?(.+?)\s?``|`([^`]+)`', lambda m: keep(r'\texttt{' + esc_text(m.group(1) or m.group(2)) + '}'), s)
    s = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', s)          # ссылки → текст
    s = re.sub(r'<[^>]+>', '', s)                            # HTML-теги
    s = esc_text(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', s)
    s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'\\emph{\1}', s)
    return s


def restore(s, store):
    while '\x00' in s:
        s = re.sub(r'\x00(\d+)\x00', lambda m: store[int(m.group(1))], s)
    return s


def convert(md, footer):
    body = md.split('\n' + STOP_HEADING)[0]
    body = body.replace('Ключ в конце файла открывать только после окончания времени.',
                        'Ключ (в файле экзамена на GitHub) открывать только после окончания времени.')
    body = body.replace('Записать баллы по частям в таблицу результатов в конце и прочитать интерпретацию.',
                        'Записать баллы по частям в таблицу результатов в файле экзамена на GitHub и прочитать интерпретацию.')
    lines = body.split('\n')
    store, out, para, lst = [], [], [], None   # lst: 'enumerate' | 'itemize' | None

    def flush_para():
        if para:
            out.append(' \\\\\n'.join(para) + '\n\n'); para.clear()

    def close_list():
        nonlocal lst
        if lst:
            out.append(f'\\end{{{lst}}}\n'); lst = None

    i = 0
    while i < len(lines):
        l = lines[i]; st = l.strip()
        if st.startswith('```math'):
            flush_para()
            j = i + 1; buf = []
            while not lines[j].strip().startswith('```'):
                buf.append(lines[j]); j += 1
            out.append('\\[\\adjustbox{max width=\\linewidth}{$\\displaystyle\n' + fix_math('\n'.join(buf)) + '\n$}\\]\n'); i = j + 1; continue
        if not st:
            flush_para(); i += 1
            # список продолжается, если следующий непустой элемент — тоже пункт
            nxt = next((x for x in lines[i:] if x.strip()), '')
            if lst and not re.match(r'\s*(\d+\.|-)\s', nxt):
                close_list()
            continue
        if st.startswith('# '):
            flush_para(); close_list()
            out.append('{\\centering\\LARGE\\bfseries ' + inline(st[2:].replace(' — диагностика', ''), store) + '\\par}\n\\vspace{0.8em}\n')
        elif st.startswith('## '):
            flush_para(); close_list(); out.append('\\section*{' + inline(st[3:], store) + '}\n')
        elif st.startswith('### '):
            flush_para(); close_list(); out.append('\\subsection*{' + inline(st[4:], store) + '}\n')
        elif st.startswith('>'):
            flush_para(); close_list()
            t = st[1:].strip()
            if t: out.append('{\\small ' + inline(t, store) + '\\par}\n')
        elif re.match(r'\d+\.\s', st) or re.match(r'-\s', st):
            flush_para()
            kind = 'enumerate' if st[0].isdigit() else 'itemize'
            if lst != kind:
                close_list(); out.append(f'\\begin{{{kind}}}\n'); lst = kind
            label, text = (st.split('.', 1)[0] + '.', st.split('.', 1)[1].strip()) if kind == 'enumerate' else ('', st[1:].strip())
            item = '\\item' + (f'[{label}]' if label else '') + ' ' + inline(text, store)
            # продолжение пункта на следующих строках
            while i + 1 < len(lines) and lines[i + 1].strip() and not re.match(r'\s*(\d+\.|-|#|>|```)', lines[i + 1].strip()):
                i += 1; item += ' \\\\\n' + inline(lines[i].strip(), store)
            out.append(item + '\n')
        else:
            if lst and not l.startswith(' '):
                close_list()
            para.append(inline(st, store))
        i += 1
    flush_para(); close_list()
    tex = PREAMBLE.replace('<<FOOTER>>', esc_text(footer)) + restore(''.join(out), store) + '\\end{document}\n'
    return tex


def git_info(path):
    d = os.path.dirname(os.path.abspath(path))
    root = subprocess.run(['git', '-C', d, 'rev-parse', '--show-toplevel'], capture_output=True, text=True).stdout.strip()
    rel = os.path.relpath(os.path.abspath(path), root)
    dirty = subprocess.run(['git', '-C', root, 'status', '--porcelain', '--', rel], capture_output=True, text=True).stdout.strip()
    commit = subprocess.run(['git', '-C', root, 'log', '-1', '--format=%h', '--', rel], capture_output=True, text=True).stdout.strip()
    return rel, commit, dirty


def build(exam, output, variant='v1', keep_tex=False, allow_dirty=False):
    """Собирает один PDF. Возвращает список предупреждений; при ошибке завершает работу."""
    rel, commit, dirty = git_info(exam)
    if dirty and not allow_dirty:
        sys.exit(f'{rel}: есть незакоммиченные изменения — сначала закоммитьте, чтобы PDF ссылался на точную версию')
    code = os.path.basename(exam).split('_')[0].split('.')[0]
    if re.fullmatch(r'v\d+', code):   # Variants/<Код>/vN.md — код берётся из имени папки
        code = os.path.basename(os.path.dirname(os.path.abspath(exam)))
    shown = rel.split('Reality Check/', 1)[-1]   # путь внутри Reality Check — короче
    footer = f'{code} · вариант {variant} · {shown} · коммит {commit or "—"}'
    tex = convert(open(exam, encoding='utf-8').read(), footer)
    with tempfile.TemporaryDirectory() as tmp:
        tf = os.path.join(tmp, 'exam.tex')
        open(tf, 'w', encoding='utf-8').write(tex)
        for _ in range(2):   # второй проход — для «стр. N из M»
            r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'exam.tex'], cwd=tmp, capture_output=True, text=True, errors='replace')
            if r.returncode:
                log = open(os.path.join(tmp, 'exam.log'), encoding='utf-8', errors='replace').read()
                errs = re.findall(r'^!.*(?:\n.*){0,3}', log, flags=re.M)
                if keep_tex: shutil.copy(tf, os.path.splitext(output)[0] + '.tex')
                sys.exit(f'{rel}: ошибка pdfLaTeX:\n' + '\n'.join(errs[:5]))
        log = open(os.path.join(tmp, 'exam.log'), encoding='utf-8', errors='replace').read()
        missing = sorted(set(re.findall(r'Missing character: There is no (.) ', log)))
        overfull = [float(x) for x in re.findall(r'Overfull \\hbox \(([\d.]+)pt too wide\)', log) if float(x) > 10]
        os.makedirs(os.path.dirname(os.path.abspath(output)), exist_ok=True)
        shutil.copy(os.path.join(tmp, 'exam.pdf'), output)
        if keep_tex: shutil.copy(tf, os.path.splitext(output)[0] + '.tex')
    print(f'{output}: {footer}')
    warnings = []
    if missing:
        warnings.append(f'{rel}: нет глифов для символов: ' + ' '.join(missing))
    if overfull:
        warnings.append(f'{rel}: {len(overfull)} строк(и) вылезают за поле (до {max(overfull):.0f} pt) — посмотрите PDF')
    for w in warnings:
        print('ВНИМАНИЕ: ' + w)
    return warnings


def build_zip(zip_path):
    """PDF основных вариантов всех экзаменов Reality Check → один zip, по папкам областей."""
    rc = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # папка Reality Check
    exams = sorted(f for f in glob.glob(os.path.join(rc, 'Exams', '*', '*.md'))
                   if re.match(r'[A-Z]+\d+_', os.path.basename(f)))
    warnings = []
    with tempfile.TemporaryDirectory() as out:
        names = []
        for f in exams:
            name = os.path.join(os.path.basename(os.path.dirname(f)), os.path.basename(f)[:-3] + '.pdf')
            warnings += build(f, os.path.join(out, name))
            names.append(name)
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
            for name in names:
                z.write(os.path.join(out, name), name)
    print(f'{zip_path}: {len(names)} PDF')
    return warnings


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('exam', nargs='?', help='файл экзамена (.md)')
    ap.add_argument('-o', '--output', help='куда сохранить PDF')
    ap.add_argument('--variant', default='v1', help='v1 — основной экзамен, v2, v3 … — варианты из Variants/')
    ap.add_argument('--keep-tex', action='store_true', help='сохранить .tex рядом с PDF')
    ap.add_argument('--allow-dirty', action='store_true', help='разрешить незакоммиченные изменения в файле экзамена')
    ap.add_argument('--zip', metavar='ZIP', help='собрать PDF всех экзаменов (основные варианты) в один архив')
    a = ap.parse_args()
    if a.zip:
        warnings = build_zip(a.zip)
    elif a.exam and a.output:
        warnings = build(a.exam, a.output, a.variant, a.keep_tex, a.allow_dirty)
    else:
        ap.error('нужно указать экзамен и -o, либо --zip')
    sys.exit(1 if warnings else 0)


if __name__ == '__main__':
    main()
