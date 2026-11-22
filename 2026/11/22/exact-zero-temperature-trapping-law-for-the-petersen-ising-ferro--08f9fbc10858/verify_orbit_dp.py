"""Symmetry-quotient exact proof certificate for Petersen majority flips.

Kneser graph KG(5,2); spin-complement and S5 act on the 1024 masks.
The quotient has 18 classes; each orbit has an exact directed transition
count to the next cut level. Python 3 standard library only.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations
from math import comb

pairs = list(combinations(range(5), 2))
pos = {pair: i for i, pair in enumerate(pairs)}
neighbors = [sum(1 << j for j, b in enumerate(pairs)
                 if set(a).isdisjoint(b)) for a in pairs]
assert len(pairs) == 10 and all(x.bit_count() == 3 for x in neighbors)
FULL = 1023
perms = [tuple(pos[tuple(sorted((p[a], p[b])))] for a, b in pairs)
         for p in permutations(range(5))]

def orbit(mask):
    states = {sum(((mask >> i) & 1) << pi[i] for i in range(10))
              for pi in perms}
    return states | {FULL ^ m for m in states}

lookup = {}
rows = []
for mask in range(1024):
    if mask in lookup:
        continue
    images = orbit(mask)
    idx = len(rows)
    for m in images:
        assert m not in lookup
        lookup[m] = idx
    rows.append({'rep': mask, 'images': images, 'size': len(images)})
assert len(rows) == 18 and len(lookup) == 1024
assert sum(row['size'] for row in rows) == 1024

def moves(mask):
    ans = []
    for i in range(10):
        same_plus = (mask & neighbors[i]).bit_count()
        is_plus = (mask >> i) & 1
        if (is_plus and same_plus < 2) or (not is_plus and same_plus > 1):
            ans.append(mask ^ (1 << i))
    return ans

def cut(mask):
    return sum(((mask >> i) & 1) != ((mask >> j) & 1)
               for i in range(10) for j in range(i + 1, 10)
               if neighbors[i] & (1 << j))

for row in rows:
    m = row['rep']
    row['cut'] = cut(m)
    row['to'] = dict(sorted(Counter(lookup[x] for x in moves(m)).items()))
    row['degree'] = sum(row['to'].values())
    for other in row['images']:
        assert cut(other) == row['cut']
        assert Counter(lookup[x] for x in moves(other)) == Counter(row['to'])
for row in rows:
    assert all(rows[j]['cut'] < row['cut'] for j in row['to'])

@lru_cache(maxsize=None)
def trap(idx):
    row = rows[idx]
    if row['degree'] == 0:
        return Fraction(row['cut'] > 0)
    return sum((Fraction(v, row['degree']) * trap(j)
                for j, v in row['to'].items()), Fraction(0))

weight = [sum((trap(i) * sum(m.bit_count() == k for m in row['images'])
               for i, row in enumerate(rows)), Fraction(0))
          for k in range(11)]
expected = [Fraction(0), Fraction(0), Fraction(0), Fraction(88, 9),
            Fraction(8242, 189), Fraction(12788, 189),
            Fraction(8242, 189), Fraction(88, 9),
            Fraction(0), Fraction(0), Fraction(0)]
assert weight == expected
assert sum(weight, Fraction(0)) / 1024 == Fraction(4121, 24192)
assert sum(row['size'] for row in rows if row['degree'] == 0) == 14
stable_mixed = {m for m in range(1024) if not moves(m) and m not in (0, FULL)}
rep = min(stable_mixed)
s5_images = {sum(((rep >> i) & 1) << pi[i] for i in range(10)) for pi in perms}
assert len(s5_images) == 12 and s5_images == stable_mixed
for i in range(11):
    p = Fraction(i, 10)
    x = p * (1-p)
    total = sum((weight[k]*p**k*(1-p)**(10-k) for k in range(11)), Fraction(0))
    assert total == Fraction(2, 189)*x**3*(924+425*x)

print('symmetry-orbit dynamic programming: PASS')
print('orbit classes:', len(rows))
print('orbit entries: class, representative mask, size, cut, transition counts, trap')
for i, row in enumerate(rows):
    print(i, row['rep'], row['size'], row['cut'], row['to'], trap(i))
print('unnormalized Bernstein coefficients:', *(str(x) for x in weight))
print('unbiased frozen probability:', str(sum(weight) / 1024))
