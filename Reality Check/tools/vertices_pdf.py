#!/usr/bin/env python3
"""Собирает PDF-путеводитель «Шесть вершин» по V1–V6 из tools/vertices_guide.html.

    python3 -I "Reality Check/tools/vertices_pdf.py" -o "Reality Check/vertices_guide.pdf"

Текст путеводителя написан вручную и лежит в vertices_guide.html; вехи в нём совпадают с Частью IV PLAN.md,
поэтому при правке вех в плане нужно поправить и путеводитель. Скрипт раскрашивает коды [X4], [V1] … цветами
областей (как в атласе), подставляет дату и печатает PDF через headless Chromium в два прохода: первый находит
страницы разделов по меткам <!--mark:key-->, второй печатает оглавление с номерами {{pg:key}}.
Функции печати и палитра областей берутся из atlas_pdf.py; нужны pdfinfo и pdftotext (poppler-utils).
"""
import argparse, os, re, shutil, sys, tempfile
from datetime import date

TOOLS = os.path.dirname(os.path.abspath(__file__))
RC = os.path.dirname(TOOLS)
sys.path.insert(0, TOOLS)
sys.dont_write_bytecode = True   # не оставлять __pycache__ в репозитории
from atlas_pdf import COLORS, MONTHS, find_chrome, print_pdf, page_count, marker_pages   # noqa: E402

SOURCE = os.path.join(TOOLS, 'vertices_guide.html')
# Цвет вершины — цвет её «главной» области: X, N, R, G, L, Q
VCOLORS = {'V1': '#9C3D7A', 'V2': '#A23B3B', 'V3': '#2A7F62', 'V4': '#B5652A', 'V5': '#9A7B1C', 'V6': '#3E7CB1'}


def render(src, pages=None):
    def code(m):
        c = m.group(1)
        col = VCOLORS.get(c) or COLORS.get(c[0])
        if col is None:
            sys.exit(f'неизвестный код [{c}]')
        return f'<span class="code" style="color:{col}">{c}</span>'
    s = re.sub(r'\[([A-Z]\d{1,2})\]', code, src)
    today = date.today()
    s = s.replace('{{date}}', f'{today.day} {MONTHS[today.month - 1]} {today.year}')
    if pages is None:
        s = re.sub(r'<!--mark:(\w+)-->', r'<span class="marker">@@\1@@</span>', s)
        s = re.sub(r'\{\{pg:\w+\}\}', '00', s)
    else:
        s = re.sub(r'<!--mark:\w+-->', '', s)
        s = re.sub(r'\{\{pg:(\w+)\}\}', lambda m: str(pages[m.group(1)]), s)
    return s


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('-o', '--output', required=True, help='куда сохранить PDF')
    ap.add_argument('--keep-html', action='store_true', help='сохранить итоговый HTML рядом с PDF')
    ap.add_argument('--source', default=SOURCE, help='исходный HTML (по умолчанию tools/vertices_guide.html)')
    a = ap.parse_args()
    src = open(a.source, encoding='utf-8').read()
    expected = set(re.findall(r'<!--mark:(\w+)-->', src))
    wanted = set(re.findall(r'\{\{pg:(\w+)\}\}', src))
    if wanted - expected:
        sys.exit('в оглавлении есть разделы без метки: ' + ' '.join(sorted(wanted - expected)))
    chrome = find_chrome()
    with tempfile.TemporaryDirectory() as tmp:
        h, p = os.path.join(tmp, 'guide.html'), os.path.join(tmp, 'guide.pdf')
        open(h, 'w', encoding='utf-8').write(render(src))                 # проход 1: страницы разделов
        print_pdf(chrome, h, p)
        pages, n1 = marker_pages(p), page_count(p)
        if expected - set(pages):
            sys.exit('не найдены страницы для: ' + ' '.join(sorted(expected - set(pages))))
        os.remove(p)
        open(h, 'w', encoding='utf-8').write(render(src, pages))          # проход 2: оглавление с номерами
        print_pdf(chrome, h, p)
        if page_count(p) != n1:
            sys.exit(f'число страниц изменилось между проходами ({n1} → {page_count(p)})')
        os.makedirs(os.path.dirname(os.path.abspath(a.output)), exist_ok=True)
        shutil.copy(p, a.output)
        if a.keep_html:
            shutil.copy(h, os.path.splitext(a.output)[0] + '.html')
    print(f'{a.output}: {n1} страниц; разделы: ' + ', '.join(f'{k} — с. {pages[k]}' for k in sorted(pages, key=pages.get)))


if __name__ == '__main__':
    main()
