# Заменяет ссылки вида 7.4, 7.8a, 3.11 в тексте глав на \rf{...} (вне формул, TikZ, меток и номеров утверждений).
# Запуск: python3 convert_refs.py ch7/s0_intro.tex ...  (пути относительно папки konspekt). Повторный запуск безопасен.
import re, sys, io, collections
PROT = [
    r'\\begin\{(tikzpicture|tikzcd|equation\*?|align\*?|gather\*?|multline\*?)\}.*?\\end\{\1\}',
    r'\\\[.*?\\\]', r'\\\(.*?\\\)', r'(?<!\\)\$(?:[^$\\]|\\.)*\$',
    r'\\(?:label|ref|eqref|cite|href|url|input|rf|hyperref)\{[^{}]*\}', r'\\hyperref\[[^\]]*\]',
    r'(?<!\\)%[^\n]*',
]
REF = re.compile(r'(?<![\w.\\])([1-7])\.(\d{1,2}[a-z]?)(?!\w)')
def protected_spans(s):
    spans = []
    for p in PROT:
        for m in re.finditer(p, s, flags=re.S):
            spans.append((m.start(), m.end()))
    for m in re.finditer(r'\\begin\{\w+\*?\}\[', s):          # optional argument of environments
        i, depth = m.end(), 0
        while i < len(s):
            c = s[i]
            if c == '{': depth += 1
            elif c == '}': depth -= 1
            elif c == ']' and depth == 0: break
            i += 1
        spans.append((m.start(), i + 1))
    spans.sort(); merged = []
    for a, b in spans:
        if merged and a <= merged[-1][1]: merged[-1] = (merged[-1][0], max(b, merged[-1][1]))
        else: merged.append((a, b))
    return merged
stat = collections.Counter()
for fn in sys.argv[1:]:
    s = io.open(fn, encoding='utf-8').read()
    out, pos = [], 0
    for a, b in protected_spans(s) + [(len(s), len(s))]:
        seg = s[pos:a]
        def rep(m):
            stat[m.group(1) + '.' + m.group(2)] += 1
            return r'\rf{%s.%s}' % (m.group(1), m.group(2))
        out.append(REF.sub(rep, seg)); out.append(s[a:b]); pos = b
    io.open(fn, 'w', encoding='utf-8').write(''.join(out))
print(sum(stat.values()), 'ссылок;', ' '.join('%s×%d' % (k, v) if v > 1 else k for k, v in
      sorted(stat.items(), key=lambda kv: (int(kv[0].split('.')[0]), int(re.match(r'\d+', kv[0].split('.')[1]).group()), kv[0]))))
