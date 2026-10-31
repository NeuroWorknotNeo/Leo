#!/usr/bin/env python3
"""Собирает PDF с описанием программы: атлас дисциплин (Часть III PLAN.md, без банков КТ) и боковые ветви (Часть V).

    python3 -I "Reality Check/tools/atlas_pdf.py" -o "Reality Check/program_atlas.pdf"

Вёрстка — HTML/CSS, печать в PDF — headless Chromium (путь берётся из переменной CHROME, из PATH
или из кэша Playwright ~/.cache/ms-playwright). Шрифты: P052 и Nimbus Sans (fonts-urw-base35),
недостающие символы (ℝ, 𝔽ₚ …) Chromium берёт из FreeSerif / DejaVu. Нужен pdftotext (poppler-utils):
первый проход определяет страницы карточек, второй печатает оглавление с номерами страниц.
Текст берётся из рабочей копии PLAN.md; этап каждой дисциплины — из словаря STAGE в tools/toc.py.
"""
import argparse, glob, html, os, re, shutil, subprocess, sys, tempfile
from datetime import date

TOOLS = os.path.dirname(os.path.abspath(__file__))
RC = os.path.dirname(TOOLS)
sys.path.insert(0, TOOLS)
sys.dont_write_bytecode = True   # не оставлять __pycache__ в репозитории
from toc import STAGE   # noqa: E402

# Цвета областей: приглушённые, различимые и на экране, и при печати
COLORS = {'F': '#5B6770', 'A': '#2C4A7C', 'N': '#A23B3B', 'R': '#2A7F62', 'D': '#6B7A2A', 'T': '#5E4B8B',
          'G': '#B5652A', 'L': '#9A7B1C', 'X': '#9C3D7A', 'P': '#7A5236', 'Q': '#3E7CB1', 'V': '#3A3A3A'}
MONTHS = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
LINK_FIELDS = ('Требует', 'Нужна для', 'Связь с целями')

CSS = """
@page { size: A4; margin: 19mm 18mm 20mm 18mm;
  @bottom-left { content: "Атлас современной математики"; font: 8pt "Nimbus Sans", sans-serif; color: #8a8a8a; }
  @bottom-right { content: counter(page); font: 8.5pt "Nimbus Sans", sans-serif; color: #8a8a8a; } }
@page cover { margin: 0; @bottom-left { content: none; } @bottom-right { content: none; } }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { margin: 0; font-family: "P052", "FreeSerif", "DejaVu Serif", serif; font-size: 10.6pt; line-height: 1.38; color: #262626; }
a { color: inherit; text-decoration: none; }
.code { font-family: "Nimbus Sans", "DejaVu Sans", sans-serif; font-weight: bold; font-size: 0.92em; }
.marker { position: absolute; left: 0; top: 0; font-size: 1px; color: #fff; }

/* Обложка */
.cover { page: cover; position: relative; width: 210mm; height: 297mm; background: #F6F3EC; padding: 52mm 26mm 24mm 26mm; overflow: hidden; }
.cover .strip { display: flex; margin-bottom: 14mm; }
.cover .strip span { flex: 1; height: 5mm; }
.cover .kicker { font-family: "Nimbus Sans", sans-serif; letter-spacing: 0.18em; text-transform: uppercase; font-size: 10pt; color: #7a7a7a; }
.cover h1 { font-size: 40pt; line-height: 1.08; margin: 6mm 0 6mm 0; font-weight: bold; color: #1f1f1f; }
.cover .sub { font-size: 16pt; font-style: italic; color: #444; margin-bottom: 16mm; }
.cover .lead { font-size: 13pt; line-height: 1.5; max-width: 140mm; color: #333; }
.cover .letters { position: absolute; left: 26mm; right: 26mm; bottom: 42mm; display: flex; flex-wrap: wrap; gap: 3mm 4mm; }
.cover .letters div { font-family: "Nimbus Sans", sans-serif; font-size: 9pt; color: #555; display: flex; align-items: center; gap: 2mm; width: 48mm; }
.cover .letters b { display: inline-block; width: 6mm; height: 6mm; line-height: 6mm; text-align: center; color: #fff; border-radius: 1.2mm; font-size: 9.5pt; flex: none; }
.cover .foot { position: absolute; left: 26mm; right: 26mm; bottom: 20mm; font-family: "Nimbus Sans", sans-serif; font-size: 9pt; color: #7a7a7a;
               border-top: 0.6pt solid #cfc8b8; padding-top: 3mm; display: flex; justify-content: space-between; }

/* Заголовки страниц */
h2.page-title { font-family: "Nimbus Sans", sans-serif; font-size: 20pt; margin: 0 0 6mm 0; color: #1f1f1f; }
.newpage { break-before: page; }

/* Оглавление */
.toc { columns: 2; column-gap: 9mm; font-size: 8.9pt; }
.toc .area { break-inside: avoid; margin-bottom: 2.6mm; }
.toc .ah { font-family: "Nimbus Sans", sans-serif; font-weight: bold; font-size: 9.4pt; display: flex; align-items: baseline; margin-bottom: 0.6mm; }
.toc .row { display: flex; align-items: baseline; line-height: 1.26; }
.toc .row .c { width: 9mm; flex: none; }
.toc .row .t { flex: 0 1 auto; }
.toc .dots { flex: 1 0 4mm; border-bottom: 0.7pt dotted #b9b9b9; margin: 0 1.5mm; transform: translateY(-0.9mm); }
.toc .pg { font-family: "Nimbus Sans", sans-serif; font-size: 8pt; color: #777; flex: none; min-width: 4.5mm; text-align: right; }

/* Как читать */
.intro p { margin: 0 0 3mm 0; }
.box { background: #F6F3EC; border-radius: 3mm; padding: 4.5mm 6mm; margin: 5mm 0; }
.box ul { margin: 1.5mm 0 2.5mm 0; padding-left: 5mm; }
.box li { margin-bottom: 1mm; }
.legend { display: grid; grid-template-columns: 1fr 1fr; gap: 2.2mm 8mm; margin-top: 3mm; }
.legend div { display: flex; align-items: center; gap: 3mm; }
.sq { display: inline-block; width: 6.5mm; height: 6.5mm; line-height: 6.5mm; text-align: center; color: #fff; border-radius: 1.3mm;
      font-family: "Nimbus Sans", sans-serif; font-weight: bold; font-size: 10pt; flex: none; }
.chip { display: inline-block; font-family: "Nimbus Sans", sans-serif; font-size: 7.4pt; padding: 0.5mm 1.8mm; border-radius: 1mm;
        white-space: nowrap; vertical-align: 0.15em; margin-left: 1.2mm; }

/* Области */
.area-head { break-before: page; break-after: avoid; position: relative; display: flex; align-items: center; gap: 5mm;
             padding-bottom: 3.5mm; margin-bottom: 5mm; border-bottom: 1pt solid; }
.area-head .big { width: 15mm; height: 15mm; line-height: 15mm; text-align: center; color: #fff; border-radius: 2.2mm;
                  font-family: "Nimbus Sans", sans-serif; font-weight: bold; font-size: 28pt; flex: none; }
.area-head h2 { font-family: "Nimbus Sans", sans-serif; font-size: 21pt; margin: 0; }
.area-head .count { margin-left: auto; font-family: "Nimbus Sans", sans-serif; font-size: 9pt; color: #8a8a8a; }

/* Карточки */
.card { position: relative; break-inside: avoid; border: 0.6pt solid; border-left-width: 3.2pt; border-radius: 2.2mm;
        padding: 3.4mm 5mm 3.2mm 5mm; margin: 0 0 4.2mm 0; background: #fff; }
.card .head { display: flex; align-items: baseline; gap: 3mm; margin-bottom: 1.4mm; }
.card .head .cc { font-family: "Nimbus Sans", sans-serif; font-weight: bold; font-size: 15pt; flex: none; }
.card .head h3 { font-size: 12.6pt; margin: 0; line-height: 1.25; flex: 1; }
.card .head .chips { flex: none; white-space: nowrap; }
.field { margin-top: 1.5mm; }
.field .lab { font-family: "Nimbus Sans", sans-serif; font-size: 7.2pt; font-weight: bold; letter-spacing: 0.09em; text-transform: uppercase; color: #8a8a8a; }
.field .txt { margin-top: 0.2mm; }
.field.lit .txt { font-size: 9.6pt; color: #3a3a3a; }

/* Боковые ветви */
.side-intro { margin: 0 0 2mm 0; }
table.side { width: 100%; border-collapse: collapse; font-size: 9.6pt; margin-top: 4mm; }
table.side th { font-family: "Nimbus Sans", sans-serif; font-size: 7.6pt; letter-spacing: 0.08em; text-transform: uppercase; color: #8a8a8a;
                text-align: left; padding: 1.5mm 2.5mm; border-bottom: 0.8pt solid #bbb; }
table.side td { padding: 2.2mm 2.5mm; vertical-align: top; border-bottom: 0.5pt solid #e4e0d6; }
table.side tr { break-inside: avoid; }
table.side tbody tr:nth-child(odd) td { background: #FAF8F3; }
table.side td.d { width: 31%; }
table.side td.w { width: 14%; }
"""


def inline(s, cards, autolink=False):
    """Строка markdown → HTML: ссылки на карточки становятся внутренними ссылками, прочие ссылки — текстом."""
    store = []

    def keep(x):
        store.append(x); return f'\x00{len(store) - 1}\x00'

    def code_link(code, text=None):
        col = COLORS[code[0]]
        if text is None or text == code:
            return f'<a class="code" style="color:{col}" href="#card-{code}">{code}</a>'
        return f'<a href="#card-{code}" style="color:{col}">{html.escape(text)}</a>'

    def link(m):
        text, target = m.group(1), m.group(2)
        code = target[1:].upper() if target.startswith('#') else ''
        return keep(code_link(code, text) if code in cards else html.escape(text))
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link, s)
    if autolink:   # коды дисциплин в полях «Требует», «Нужна для», «Связь с целями» — тоже ссылки
        s = re.sub(r'(?<![\w#])([A-Z]\d{1,2})(?!\w)',
                   lambda m: keep(code_link(m.group(1))) if m.group(1) in cards else m.group(1), s)
    s = re.sub(r'`([^`]+)`', lambda m: keep('<code>' + html.escape(m.group(1)) + '</code>'), s)
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<i>\1</i>', s)
    while '\x00' in s:
        s = re.sub(r'\x00(\d+)\x00', lambda m: store[int(m.group(1))], s)
    return s


def parse(plan):
    lines = plan.split('\n')
    find = lambda prefix: next(i for i, l in enumerate(lines) if l.startswith(prefix))
    i3, i4, i5, i6 = find('## Часть III'), find('## Часть IV'), find('## Часть V.'), find('## Часть VI')
    subtitle = next(l for l in lines[1:] if l.strip() and not l.startswith('#'))
    areas, card = [], None
    for l in lines[i3:i4]:
        m = re.match(r'### ([A-Z])\. (.+)', l)
        if m:
            areas.append({'letter': m.group(1), 'name': m.group(2).strip(), 'cards': []}); card = None; continue
        m = re.match(r'#### <a id="([a-z0-9]+)"></a>([A-Z]\d+)\. (.+)', l)
        if m:
            card = {'code': m.group(2), 'title': m.group(3).strip(), 'fields': []}
            areas[-1]['cards'].append(card); continue
        m = re.match(r'- \*\*(.+?):?\*\*:?\s*(.*)', l)
        if card and m:
            label = m.group(1).rstrip(':')
            # банк КТ вместе с его нумерованными пунктами пропускается
            card['fields'].append(None if label.startswith(('КТ', 'Контрольные точки')) else [label, m.group(2).strip()])
            continue
        if card and card['fields'] and card['fields'][-1] is not None and l.startswith('  ') and l.strip():
            card['fields'][-1][1] += ' ' + l.strip()   # перенос строки внутри поля
    for a in areas:
        for c in a['cards']:
            c['fields'] = [f for f in c['fields'] if f]
    part5 = lines[i5 + 1:i6]
    intro5 = ' '.join(l.strip() for l in part5 if l.strip() and not l.startswith(('|', '---', '<a')))
    rows = [[x.strip() for x in l.strip().strip('|').split('|')] for l in part5 if l.startswith('|')][2:]
    return subtitle, areas, intro5, rows


def split_title(code, title):
    """Название без «(боковая ветвь …)» и метки для заголовка карточки."""
    tags = []
    if STAGE.get(code):
        tags.append('Этап ' + STAGE[code].split(' ')[0])
    m = re.search(r'\s*\((боковая ветвь[^)]*)\)\s*$', title)
    if m:
        title = title[:m.start()]
        tags.append(m.group(1))
    return title, tags


def chip(text, col):
    return f'<span class="chip" style="color:{col};background:{col}1c">{html.escape(text)}</span>'


def plural(n, forms):
    n10, n100 = n % 10, n % 100
    return forms[0] if n10 == 1 and n100 != 11 else forms[1] if 2 <= n10 <= 4 and not 12 <= n100 <= 14 else forms[2]


def disciplines(n):
    return f'{n} {plural(n, ("дисциплина", "дисциплины", "дисциплин"))}'


def build_html(plan, pages=None, markers=True):
    subtitle, areas, intro5, rows = parse(plan)
    cards = {c['code'] for a in areas for c in a['cards']}
    pg = lambda key: str(pages.get(key, '')) if pages else '00'
    mark = lambda key: f'<span class="marker">@@{key}@@</span>' if markers else ''
    today = date.today()
    out = ['<!doctype html><html lang="ru"><head><meta charset="utf-8"><title>Атлас современной математики</title><style>',
           CSS, '</style></head><body>']

    # Обложка
    strip = ''.join(f'<span style="background:{COLORS[a["letter"]]}"></span>' for a in areas)
    letters = ''.join(f'<div><b style="background:{COLORS[a["letter"]]}">{a["letter"]}</b>{html.escape(a["name"])}</div>' for a in areas)
    out.append(f'''<section class="cover"><div class="strip">{strip}</div>
<div class="kicker">Reality Check · программа изучения</div>
<h1>Атлас современной<br>математики</h1>
<div class="sub">Описание дисциплин программы</div>
<div class="lead">{inline(subtitle, cards)}</div>
<div class="letters">{letters}</div>
<div class="foot"><span>{disciplines(len(cards))} в {len(areas)} областях · боковые ветви</span>
<span>Leo · {today.day} {MONTHS[today.month - 1]} {today.year}</span></div></section>''')

    # Оглавление
    toc = ['<section class="newpage"><h2 class="page-title">Содержание</h2><div class="toc">',
           '<div class="area"><div class="row ah"><a href="#how">Как читать атлас</a><span class="dots"></span>'
           f'<span class="pg">{pg("how")}</span></div></div>']
    for a in areas:
        col = COLORS[a['letter']]
        toc.append(f'<div class="area"><div class="ah" style="color:{col}"><a href="#area-{a["letter"]}">{a["letter"]}&ensp;{html.escape(a["name"])}</a></div>')
        for c in a['cards']:
            t, _ = split_title(c['code'], c['title'])
            toc.append(f'<div class="row"><span class="c code" style="color:{col}">{c["code"]}</span>'
                       f'<a class="t" href="#card-{c["code"]}">{html.escape(t)}</a><span class="dots"></span><span class="pg">{pg(c["code"])}</span></div>')
        toc.append('</div>')
    toc.append('<div class="area"><div class="row ah"><a href="#side">V&ensp;Боковые ветви</a><span class="dots"></span>'
               f'<span class="pg">{pg("side")}</span></div></div></div></section>')
    out += toc

    # Как читать атлас
    legend = ''.join(f'<div><span class="sq" style="background:{COLORS[a["letter"]]}">{a["letter"]}</span>{html.escape(a["name"])}</div>' for a in areas)
    out.append(f'''<section class="newpage intro" id="how" style="position:relative">{mark("how")}<h2 class="page-title">Как читать атлас</h2>
<p>Атлас — это карточки всех дисциплин программы, сгруппированные по областям. Каждая дисциплина имеет код: букву области и номер,
например {inline("[A4](#a4)", cards)} или {inline("[G9](#g9)", cards)}. По коду дисциплина ищется в атласе, в плане и в экзаменах <i>Reality Check</i>.
Коды в карточках — ссылки: по ним можно переходить между дисциплинами.</p>
<div class="box"><b>Поля карточки</b><ul>
<li><b>Требует</b> — что нужно знать заранее;</li>
<li><b>Нужна для</b> — куда ведёт (у боковых ветвей вместо этого — <b>Связь с целями</b>);</li>
<li><b>Содержание</b> — минимальный список тем;</li>
<li><b>Литература</b> — сначала основной учебник, затем альтернативы.</li></ul>
<p style="margin:0 0 2mm 0">Метки в заголовке карточки: {chip("Этап N", "#5B6770")} — этап программы: 0 — вход, 1 — базовый курс, 2 — ядро,
3 — продвинутое ядро, 4 — языки современной математики, 5 — вершины прошлого, 6 — современные направления;
{chip("боковая ветвь", "#5B6770")} — дисциплина вне критического пути к шести вершинам (см. «Боковые ветви» в конце).</p>
<p style="margin:0">Каждая дисциплина завершается трёхчасовым письменным экзаменом <i>Reality Check</i> на 100 баллов;
дисциплина считается пройденной при 75 баллах и выше.</p></div>
<p style="margin-top:6mm"><b>Области</b></p><div class="legend">{legend}</div></section>''')

    # Карточки по областям
    for a in areas:
        col = COLORS[a['letter']]
        out.append(f'<div class="area-head" id="area-{a["letter"]}" style="border-color:{col}"><span class="big" style="background:{col}">{a["letter"]}</span>'
                   f'<h2 style="color:{col}">{html.escape(a["name"])}</h2><span class="count">{disciplines(len(a["cards"]))}</span></div>')
        for c in a['cards']:
            title, tags = split_title(c['code'], c['title'])
            chips = ''.join(chip(t, col) for t in tags)
            out.append(f'<div class="card" id="card-{c["code"]}" style="border-color:{col}55;border-left-color:{col}">{mark(c["code"])}'
                       f'<div class="head"><span class="cc" style="color:{col}">{c["code"]}</span><h3>{html.escape(title)}</h3>'
                       f'<span class="chips">{chips}</span></div>')
            for label, text in c['fields']:
                cls = ' lit' if label == 'Литература' else ''
                out.append(f'<div class="field{cls}"><div class="lab">{html.escape(label)}</div>'
                           f'<div class="txt">{inline(text, cards, autolink=label in LINK_FIELDS)}</div></div>')
            out.append('</div>')

    # Часть V. Боковые ветви
    col = COLORS['V']
    out.append(f'<div class="area-head" id="side" style="border-color:{col}">{mark("side")}<span class="big" style="background:{col}">V</span>'
               f'<h2 style="color:{col}">Боковые ветви</h2><span class="count">{disciplines(len(rows))}</span></div>')
    out.append(f'<p class="side-intro">{inline(intro5, cards)}</p>')
    out.append('<table class="side"><thead><tr><th>Дисциплина</th><th>Когда</th><th>Где пересекается с основным путём</th></tr></thead><tbody>')
    for disc, when, where in rows:
        m = re.match(r'\[([A-Z]\d+)\]\(#[a-z0-9]+\)\s*(.*)', disc)
        cell = (inline(f'[{m.group(1)}](#{m.group(1).lower()})', cards) + '&ensp;' + inline(m.group(2), cards)) if m else inline(disc, cards)
        out.append(f'<tr><td class="d">{cell}</td><td class="w">{inline(when, cards, autolink=True)}</td><td>{inline(where, cards, autolink=True)}</td></tr>')
    out.append('</tbody></table></body></html>')
    return '\n'.join(out)


def find_chrome():
    cands = [os.environ.get('CHROME', '')] + [shutil.which(x) or '' for x in ('chromium', 'chromium-browser', 'google-chrome', 'chrome')]
    cands += sorted(glob.glob(os.path.expanduser('~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome')), reverse=True)
    for c in cands:
        if c and os.path.isfile(c) and os.access(c, os.X_OK):
            return c
    sys.exit('не найден Chromium: укажите путь в переменной CHROME')


def print_pdf(chrome, html_path, pdf_path):
    r = subprocess.run([chrome, '--headless', '--no-sandbox', '--disable-gpu', '--no-pdf-header-footer',
                        '--generate-pdf-document-outline', f'--print-to-pdf={pdf_path}', 'file://' + html_path],
                       capture_output=True, text=True, timeout=180)
    if not os.path.isfile(pdf_path):
        sys.exit('Chromium не создал PDF:\n' + r.stderr[-2000:])


def page_count(pdf_path):
    info = subprocess.run(['pdfinfo', pdf_path], capture_output=True, text=True).stdout
    return int(re.search(r'Pages:\s+(\d+)', info).group(1))


def marker_pages(pdf_path):
    pages = {}
    for p in range(1, page_count(pdf_path) + 1):
        txt = subprocess.run(['pdftotext', '-f', str(p), '-l', str(p), pdf_path, '-'], capture_output=True, text=True).stdout
        for key in re.findall(r'@@(\w+)@@', txt):
            pages.setdefault(key, p)
    return pages


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('-o', '--output', required=True, help='куда сохранить PDF')
    ap.add_argument('--keep-html', action='store_true', help='сохранить HTML рядом с PDF')
    a = ap.parse_args()
    plan = open(os.path.join(RC, 'PLAN.md'), encoding='utf-8').read()
    expected = {c['code'] for ar in parse(plan)[1] for c in ar['cards']} | {'how', 'side'}
    chrome = find_chrome()
    with tempfile.TemporaryDirectory() as tmp:
        h, p = os.path.join(tmp, 'atlas.html'), os.path.join(tmp, 'atlas.pdf')
        open(h, 'w', encoding='utf-8').write(build_html(plan))          # проход 1: на каких страницах карточки
        print_pdf(chrome, h, p)
        pages, n1 = marker_pages(p), page_count(p)
        if expected - set(pages):
            sys.exit('не найдены страницы для: ' + ' '.join(sorted(expected - set(pages))))
        os.remove(p)
        open(h, 'w', encoding='utf-8').write(build_html(plan, pages, markers=False))   # проход 2: оглавление с номерами
        print_pdf(chrome, h, p)
        if page_count(p) != n1:
            sys.exit(f'число страниц изменилось между проходами ({n1} → {page_count(p)})')
        os.makedirs(os.path.dirname(os.path.abspath(a.output)), exist_ok=True)
        shutil.copy(p, a.output)
        if a.keep_html:
            shutil.copy(h, os.path.splitext(a.output)[0] + '.html')
    print(f'{a.output}: {n1} страниц, {len(expected) - 2} карточек')


if __name__ == '__main__':
    main()
