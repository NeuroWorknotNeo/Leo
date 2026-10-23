#!/usr/bin/env python3
"""Гейт качества для экзамена в новом формате: структура, формат, формулы, рендер GitHub, PDF.

    python3 -I "Reality Check/tools/verify_exam.py" [--no-render] [--no-pdf] <файл.md> ...

Печатает OK или FAIL с причинами для каждого файла; код возврата 1, если есть FAIL.
Рендер проверяется через `gh api markdown` (нужна авторизация gh), PDF — скриптом exam_pdf.py.
"""
import re, subprocess, sys, os, tempfile

EXAM_PDF = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'exam_pdf.py')
HEADS = ['## Часть A. Определения и формулировки (≈ 20 мин, 10 баллов)',
         '## Часть B. Верно или неверно? (≈ 25 мин, 15 баллов)',
         '## Часть C. Стандартные задачи (≈ 60 мин, 30 баллов)',
         '## Часть D. Ключевые доказательства (≈ 45 мин, 30 баллов)',
         '## Часть E. Задачи повышенной сложности (≈ 30 мин, 15 баллов)',
         '## Карта навыков', '## Результаты и интерпретация', '## Ключ для самопроверки']
MUST = ['Ключ в конце файла открывать только после окончания времени.',
        'Записать баллы по частям в таблицу результатов в конце и прочитать интерпретацию.',
        '**Время:** 180 минут', '<summary>Открыть только после окончания экзамена</summary>']
BAD = [('контрольная точка', re.I), ('контрольной точк', re.I), ('README.md#physics', 0), ('два захода', re.I), ('\\operatorname', 0), ('$$', 0),
       ('расширенн', re.I), ('plan.md', 0)]


def section(s, a, b):
    i = s.index(a); j = s.index(b, i) if b else len(s)
    return s[i:j]


def check(path, render=True, pdf=True):
    s = open(path, encoding='utf-8').read()
    code = os.path.basename(path).split('_')[0]
    if re.fullmatch(r'v\d+', code.split('.')[0]):   # вариант Variants/<Код>/vN.md
        code = os.path.basename(os.path.dirname(os.path.abspath(path)))
    errs, warns = [], []
    for h in HEADS:
        if s.count(h) != 1: errs.append(f'заголовок не ровно один раз: {h}')
    pos = [s.find(h) for h in HEADS]
    if pos != sorted(pos): errs.append('порядок разделов нарушен')
    for m in MUST:
        if m not in s: errs.append(f'нет обязательной фразы: {m[:50]}')
    if not re.search(rf'\]\((\.\./)+PLAN\.md#{code.lower()}\)', s): errs.append('нет ссылки на PLAN.md#код')
    for b, fl in BAD:
        if (re.search(re.escape(b), s, fl) if fl else (b in s)): errs.append(f'запрещённый фрагмент: {b}')
    if not re.match(rf'# {code}\. .+ — диагностика', s): errs.append('заголовок файла не по шаблону')
    try:
        A = section(s, HEADS[0], HEADS[1]); B = section(s, HEADS[1], HEADS[2]); C = section(s, HEADS[2], HEADS[3])
        D = section(s, HEADS[3], HEADS[4]); E = section(s, HEADS[4], HEADS[5]); K = section(s, HEADS[7], None)
        R = section(s, HEADS[6], HEADS[7])
        nA = len(re.findall(r'^\d+\. ', A, re.M)); nB = len(re.findall(r'^\d+\. ', B, re.M))
        nC = len(set(re.findall(r'\*\*C(\d)\.?\*\*', C))); nD = len(set(re.findall(r'\*\*D(\d)\.?\*\*', D))); nE = len(set(re.findall(r'\*\*E(\d)\.?\*\*', E)))
        if (nA, nB, nC, nD, nE) != (5, 5, 5, 3, 3): errs.append(f'число задач A/B/C/D/E = {nA}/{nB}/{nC}/{nD}/{nE}, нужно 5/5/5/3/3')
        for row in ['| 10 |', '| 15 |', '| 30 |', '**100**']:
            if row not in R: errs.append(f'в таблице результатов нет {row}')
        if '≥ 75' not in R and 'не меньше 75' not in R: errs.append('правило галочки без порога 75')
        if re.search('половин', R): errs.append('раздел «Результаты» упоминает половину баллов по частям')
        for part in 'ABCDE':
            if f'### Часть {part}' not in K: errs.append(f'в ключе нет раздела Часть {part}')
        kC = len(set(re.findall(r'\*\*C(\d)\.?\*\*', K))); kD = len(set(re.findall(r'\*\*D(\d)\.?\*\*', K))); kE = len(set(re.findall(r'\*\*E(\d)\.?\*\*', K)))
        if (kC, kD, kE) != (5, 3, 3): warns.append(f'в ключе найдено C/D/E = {kC}/{kD}/{kE} меток задач')
        if '```math' in K: errs.append('блок ```math внутри <details> (нужен <div align="center">)')
        if re.search(r'</div>\n(?!\n)', K): errs.append('после </div> нет пустой строки')
        if re.search(r'<summary>[^\n]*</summary>\n(?!\n)', s): errs.append('после <summary> нет пустой строки')
    except ValueError as e:
        errs.append(f'разделы не найдены: {e}')
    if s.count('$`') != s.count('`$'): errs.append(f"несбалансированные $` / `$: {s.count('$`')} / {s.count('`$')}")
    body = re.sub(r'```.*?```', '', s, flags=re.S)
    body = re.sub(r'\$`.*?`\$', '', body, flags=re.S)
    if '$' in body: errs.append('голый $ вне формул: ' + body[max(0, body.index('$') - 30):body.index('$') + 30].replace('\n', ' '))
    if render and not errs:
        r = subprocess.run(['gh', 'api', 'markdown', '-f', 'mode=gfm', '-f', 'context=NeuroWorknotNeo/Leo', '-F', f'text=@{path}'], capture_output=True, text=True)
        if r.returncode: errs.append('gh api markdown: ' + r.stderr[:200])
        else:
            html = r.stdout
            inner = re.findall(r'<math-renderer[^>]*>(.*?)</math-renderer>', html, re.S)
            bad = [x for x in inner if '<em>' in x or '<code>' in x or '`' in x]
            if bad: errs.append(f'в {len(bad)} формулах рендера есть <em>/<code>/`: ' + bad[0][:80])
            if '$`' in re.sub(r'<math-renderer.*?</math-renderer>', '', html, flags=re.S): errs.append('в рендере остались необработанные $`')
            warns.append(f'формул в рендере: {html.count("<math-renderer")}')
    if pdf and not errs:
        with tempfile.TemporaryDirectory() as td:
            out_pdf = os.path.join(td, 'exam.pdf')
            r = subprocess.run(['python3', EXAM_PDF, path, '-o', out_pdf, '--allow-dirty'], capture_output=True, text=True)
            out = r.stdout + r.stderr
            if r.returncode and 'ВНИМАНИЕ' not in out: errs.append('PDF не собрался: ' + out[-300:])
            for w in re.findall(r'ВНИМАНИЕ: .*', out): warns.append(w)
            if os.path.exists(out_pdf):
                pg = subprocess.run(['pdfinfo', out_pdf], capture_output=True, text=True).stdout
                pm = re.search(r'Pages:\s+(\d+)', pg); warns.append(f'страниц PDF: {pm.group(1) if pm else "?"}')
    return errs, warns


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    render = '--no-render' not in sys.argv; pdf = '--no-pdf' not in sys.argv
    fail = 0
    for p in args:
        errs, warns = check(p, render, pdf)
        print(('FAIL ' if errs else 'OK   ') + os.path.basename(p))
        for e in errs: print('   ОШИБКА:', e)
        for w in warns: print('   инфо:', w)
        fail += bool(errs)
    sys.exit(1 if fail else 0)
