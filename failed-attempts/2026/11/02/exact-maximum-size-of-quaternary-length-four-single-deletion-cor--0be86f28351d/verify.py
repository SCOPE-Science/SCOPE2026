"""Self-contained exact checks for a quaternary four-symbol deletion code."""
from collections import Counter
from itertools import product
from fractions import Fraction

ALPHABET = '0123'
CODE = '''
0000 0011 0022 0033 0213 0320
1010 1111 1122 1133 1230 1321
2031 2102 2200 2211 2222 2233
3012 3103 3232 3300 3311 3333
'''.split()

def descendants(w):
    return {w[:i] + w[i+1:] for i in range(len(w))}

def weight(v):
    if v[0] == v[1] == v[2]:
        return Fraction(1)
    if v[0] == v[1] or v[1] == v[2]:
        return Fraction(1, 2)
    return Fraction(1, 4)

def pattern(w):
    rename = {}
    return ''.join(str(rename.setdefault(s, len(rename))) for s in w)

assert len(CODE) == 24 == len(set(CODE))
assert all(len(w) == 4 and set(w) <= set(ALPHABET) for w in CODE)
seen = {}
for w in CODE:
    for v in descendants(w):
        assert v not in seen, (v, w, seen.get(v))
        seen[v] = w

universe = [''.join(v) for v in product(ALPHABET, repeat=3)]
assert len(universe) == 64
assert sum((weight(v) for v in universe), Fraction(0)) == 25
pattern_scores = {}
for tup in product(ALPHABET, repeat=4):
    w = ''.join(tup)
    p = pattern(w)
    score = sum((weight(v) for v in descendants(w)), Fraction(0))
    assert score >= 1, (w, p, score)
    if p in pattern_scores:
        assert pattern_scores[p] == score
    pattern_scores[p] = score

assert len(pattern_scores) == 15
expected_tight = {'0000', '0011', '0120', '0123'}
assert {p for p,s in pattern_scores.items() if s == 1} == expected_tight
palindromes = [v for v in universe if v[0] == v[2] != v[1]]
assert len(palindromes) == 12
for w in product(ALPHABET, repeat=4):
    w = ''.join(w)
    if pattern(w) in expected_tight:
        pal = sorted(v for v in descendants(w) if v[0] == v[2] != v[1])
        if pattern(w) == '0120':
            assert len(pal) == 2 and pal[0][0] == pal[1][0] == w[0]
        else:
            assert pal == [], (w, pal)

print('codewords:', len(CODE))
print('distinct nonoverlapping outputs:', len(seen))
print('all three-symbol outputs:', len(universe))
print('total fractional dual weight:', sum((weight(v) for v in universe), Fraction(0)))
print('four-symbol words tested:', 4**4)
print('restricted-growth equality cases:', ','.join(sorted(expected_tight)))
print('restricted-growth score table (pattern: four-times-weight):')
for p,score in sorted(pattern_scores.items()):
    print(' ',p, int(score*4))
print('nonconstant palindromic descendants:', len(palindromes))
print('certificate: PASS')
