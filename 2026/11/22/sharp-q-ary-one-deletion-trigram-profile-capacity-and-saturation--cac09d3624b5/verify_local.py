"""Exact finite census for single-deletion trigram changes; Python 3 stdlib only."""
from collections import Counter
from itertools import product
from math import comb


def signature(x):
    """Signed vector H_3(x without middle) - H_3(x), x has length five."""
    assert len(x) == 5
    old = Counter(tuple(x[i:i+3]) for i in range(3))
    z = x[:2] + x[3:]
    new = Counter(tuple(z[i:i+3]) for i in range(2))
    return tuple(sorted((t, new[t]-old[t]) for t in old.keys() | new.keys()
                        if new[t] != old[t]))


def delta(word, pos):
    old = Counter(tuple(word[i:i+3]) for i in range(len(word)-2))
    z = word[:pos] + word[pos+1:]
    new = Counter(tuple(z[i:i+3]) for i in range(len(z)-2))
    return tuple(sorted((t, new[t]-old[t]) for t in old.keys() | new.keys()
                        if new[t] != old[t]))


C = (0, 1, 8, 90, 192, 120)
for k in range(1, 6):
    universe = set(product(range(k), repeat=5))
    sigs = {signature(x) for x in universe}
    full = {s for s in sigs if len({c for tri, mult in s for c in tri}) == k}
    assert len(full) == C[k], (k, len(full), C[k])
    print(f'full-support signatures k={k}: {len(full)}; neighborhoods={len(universe)}')

for q in range(2, 7):
    mids = {signature(x) for x in product(range(q), repeat=5)}
    formula = q + 8*comb(q,2) + 90*comb(q,3) + 192*comb(q,4) + 120*comb(q,5)
    assert len(mids) == formula
    print(f'q={q}: interior signatures={len(mids)}; upper-bound={formula+4}')

for q, prefix, suffix in [(2, (0,1,0,0), (0,1,0,1)),
                           (3, (0,1,0,0), (0,0,1,2))]:
    mid = {signature(x) for x in product(range(q), repeat=5)}
    boundary = [delta(prefix[:3],0),delta(prefix,1),
                delta(suffix,2),delta(suffix[1:],2)]
    assert len(set(boundary)) == 4
    assert all(d not in mid for d in boundary)
    print('q=',q,'boundary changes=',boundary)
print('ALL_LOCAL_CHECKS_PASS')
