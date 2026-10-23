#!/usr/bin/env python3
"""Пересобирает оглавление в Reality Check/README.md между маркерами <!-- TOC:BEGIN --> и <!-- TOC:END -->.

    python3 -I "Reality Check/tools/toc.py"

Столбец «Формат»: «новый» — экзамен в формате 180 минут / 10-15-30-30-15 и в строке «Изменения» есть
пометка «Независимая рецензия»; «новый, ждёт рецензии» — переведён, но рецензия не проводилась;
«прежний (…)» — ещё не переведён (время берётся из шапки). Когда все экзамены переведены и отрецензированы,
столбец можно убрать, удалив его из этого скрипта.
"""
import re, glob, os, urllib.parse

RC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # папка Reality Check
AREAS = [('Foundations', 'Фундамент'), ('Algebra', 'Алгебра'), ('Number Theory', 'Теория чисел'), ('Analysis', 'Анализ'),
         ('Differential Equations', 'Дифференциальные уравнения'), ('Topology', 'Топология'), ('Geometry', 'Геометрия'),
         ('Lie Theory', 'Группы и алгебры Ли'), ('Algebraic Geometry', 'Алгебраическая геометрия'), ('Probability', 'Вероятность'),
         ('Mathematical Physics', 'Физика для математиков')]
SIDE = '(боковая ветвь)'
STAGE = {'F1': '0', 'A1': '1', 'A2': '1', 'A3': '2', 'A4': '2', 'A5': '2', 'A6': '2', 'A7': '3', 'A8': '2', 'A9': '4 ' + SIDE,
         'N1': '0–1', 'N2': '2', 'N3': '3', 'N4': '3', 'N5': '3', 'N6': '4', 'N7': '4', 'N8': '5', 'N9': '6',
         'R1': '1', 'R2': '2', 'R3': '2', 'R4': '2', 'R5': '2', 'R7': '2 ' + SIDE, 'R8': '3 ' + SIDE, 'R9': '4 ' + SIDE,
         'D1': '1', 'D2': '3 ' + SIDE, 'D3': '3', 'D4': '5', 'T1': '1', 'T2': '2', 'T3': '2', 'T4': '3', 'T5': '3', 'T6': '3',
         'T7': '4', 'T8': '4', 'T9': '5', 'G1': '2', 'G2': '3', 'G3': '3', 'G4': '3', 'G5': '3', 'G6': '4', 'G7': '4', 'G8': '4',
         'G9': '5', 'G10': '4', 'G11': '6', 'L1': '2', 'L2': '3', 'L3': '4', 'L4': '6', 'X1': '3', 'X2': '4', 'X3': '4', 'X4': '4',
         'X5': '4 ' + SIDE, 'X6': '6', 'X7': '4', 'X8': '6', 'X9': '6', 'P1': '2 ' + SIDE, 'P2': '4 ' + SIDE, 'P3': '3 ' + SIDE,
         'P4': '4 ' + SIDE, 'Q1': '2', 'Q2': '4', 'Q3': '4', 'Q4': '6', 'Q5': '6', 'Q6': '6', 'Q7': '4 ' + SIDE, 'Q8': '4 ' + SIDE,
         'Q9': '4 ' + SIDE, 'Q10': '4 ' + SIDE}


def key(f):
    code = os.path.basename(f).split('_')[0]
    return (re.match(r'[A-Z]+', code).group(), int(re.search(r'\d+', code).group()))


def fmt(txt):
    new = ('## Часть D. Ключевые доказательства (≈ 45 мин, 30 баллов)' in txt
           and '## Часть A. Определения и формулировки (≈ 20 мин, 10 баллов)' in txt)
    if new:
        return 'новый' if 'Независимая рецензия' in txt else 'новый, ждёт рецензии'
    time = re.search(r'\*\*Время:\*\* ([^·]*?) ·', txt).group(1).strip()
    return 'прежний (' + re.sub(r' \(.*', '', time).replace('минут', 'мин') + ')'


def main():
    out, n = [], 0
    for folder, rus in AREAS:
        out += [f'### {folder} — {rus}\n', '| Код | Экзамен | Этап плана | Формат |', '|---|---|---|---|']
        for f in sorted(glob.glob(os.path.join(RC, 'Exams', folder, '*.md')), key=key):
            code = os.path.basename(f).split('_')[0]
            txt = open(f, encoding='utf-8').read()
            title = re.match(r'# [A-Z]+\d+\. (.*?) — диагностика', txt).group(1)
            rel = 'Exams/' + urllib.parse.quote(folder) + '/' + os.path.basename(f)
            out.append(f'| [{code}](PLAN.md#{code.lower()}) | [{title}]({rel}) | {STAGE[code]} | {fmt(txt)} |')
            n += 1
        out.append('')
    toc = '\n'.join(out).rstrip('\n')
    p = os.path.join(RC, 'README.md')
    s = open(p, encoding='utf-8').read()
    s2 = re.sub(r'<!-- TOC:BEGIN -->.*<!-- TOC:END -->', '<!-- TOC:BEGIN -->\n' + toc + '\n<!-- TOC:END -->', s, flags=re.S)
    open(p, 'w', encoding='utf-8').write(s2)
    print(f'оглавление: {n} экзаменов; новых: {toc.count("| новый |")}, ждут рецензии: {toc.count("ждёт рецензии")}')


if __name__ == '__main__':
    main()
