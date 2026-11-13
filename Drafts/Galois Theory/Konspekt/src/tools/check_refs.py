# Проверка ссылок после сборки общего файла: python3 tools/check_refs.py (в папке konspekt).
# Ошибка — ссылка на номер из ГОТОВОЙ главы, которого там нет. Ссылки на ненаписанные главы просто перечисляются.
import re, glob, io, collections
aux = io.open('Konspekt.aux', encoding='utf-8', errors='replace').read()
labels = set(re.findall(r'\\newlabel\{st:([^}]*)\}', aux))
chapters = {l.split('.')[0].split('-')[0] for l in labels}
refs = collections.defaultdict(list)
for fn in sorted(glob.glob('ch*/s*.tex')):
    for i, line in enumerate(io.open(fn, encoding='utf-8'), 1):
        for r in re.findall(r'\\rf\{([^}]*)\}', line):
            refs[r].append('%s:%d' % (fn, i))
bad = {r: w for r, w in refs.items() if r.split('.')[0] in chapters and r not in labels}
later = sorted({r for r in refs if r.split('.')[0] not in chapters})
print('утверждений с метками:', len(labels), '| готовые главы:', ', '.join(sorted(chapters)))
print('ссылок \\rf:', sum(len(w) for w in refs.values()), 'на', len(refs), 'номеров')
print('ОШИБКИ (нет такого номера в готовой главе):', bad if bad else 'нет')
print('ссылки на ещё не написанные главы:', ', '.join(later) if later else 'нет')
