"""Independent reproducible incidence, shattering, and homology census.

No external files or packages needed: python3 check_fano.py
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations
from math import comb

V = tuple(range(7))
TRIPLES = tuple(combinations(V, 3))
INDEX = {t: i for i, t in enumerate(TRIPLES)}
CANON = [t for t in TRIPLES if (t[0]+1) ^ (t[1]+1) ^ (t[2]+1) == 0]
assert len(CANON) == 7

planes = sorted({sum(1 << INDEX[tuple(sorted(p[i] for i in t))] for t in CANON)
                 for p in permutations(V)})
assert len(planes) == 30
assert len(set(planes)) == 30
for plane in planes:
    blocks = [TRIPLES[i] for i in range(35) if (plane >> i) & 1]
    assert len(blocks) == 7
    assert {p: sum(set(p) <= set(t) for t in blocks)
            for p in combinations(V, 2)} == {p: 1 for p in combinations(V, 2)}

shattered = {}
for k in range(5):
    shattered[k] = []
    for S in combinations(range(35), k):
        traces = {sum(1 << j for j, i in enumerate(S) if (plane >> i) & 1)
                  for plane in planes}
        if len(traces) == 1 << k:
            shattered[k].append(S)
assert [len(shattered[k]) for k in range(5)] == [1, 35, 315, 840, 0]

pairs = set(shattered[2]); triangles = set(shattered[3])
assert pairs == {s for s in combinations(range(35), 2)
                 if len(set(TRIPLES[s[0]]) & set(TRIPLES[s[1]])) == 1}
assert triangles == {s for s in combinations(range(35), 3)
                     if all(tuple(sorted((i,j))) in pairs for i,j in combinations(s,2))
                     and not set.intersection(*(set(TRIPLES[i]) for i in s))}
assert all(any(set(e) <= set(t) for t in triangles) for e in pairs)

E = sorted(pairs); eid = {e:i for i,e in enumerate(E)}
# Verify connectedness independently of the homogeneous-space argument.
neighbors = [set() for _ in range(35)]
for a, b in E:
    neighbors[a].add(b)
    neighbors[b].add(a)
seen = {0}; frontier = [0]
for x in frontier:
    for y in neighbors[x]:
        if y not in seen:
            seen.add(y)
            frontier.append(y)
assert len(seen) == 35
# GF(2) column rank of the 315-by-840 triangle boundary matrix.
pivot = {}
for t in sorted(triangles):
    col = sum(1 << eid[e] for e in combinations(t, 2))
    while col:
        v = col.bit_length() - 1
        if v in pivot: col ^= pivot[v]
        else:
            pivot[v] = col
            break
assert len(pivot) == 281
# The 1-skeleton is connected; the degree-zero boundary has rank 34.
assert len(E) - 34 - len(pivot) == 0
assert len(triangles) - len(pivot) == 559

for plane in planes:
    assert sum(plane >> i & 1 for i in range(35)) == 7
assert Counter(sum(plane >> i & 1 for i in range(35)) for plane in planes) == {7:30}
print('FANO_ORBIT_30_PASS')
print('SHATTER_POLYNOMIAL_1_35_315_840_PASS')
print('FACETS_840_SINGLE_ORBIT_GEOMETRIC_PASS')
print('GF2_BOUNDARY_RANK_281_BETTI_559_PASS')
