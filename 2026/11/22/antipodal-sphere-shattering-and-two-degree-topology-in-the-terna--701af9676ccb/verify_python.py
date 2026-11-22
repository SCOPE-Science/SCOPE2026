#!/usr/bin/env python3
"""Exact finite certificate for the 27-point ternary antipodal relation.
No external dependencies; Python 3.9+.
"""
import itertools
from collections import Counter

X = list(itertools.product(range(3), repeat=3))
assert len(X) == 27
D = lambda x, y: sum(a != b for a, b in zip(x, y))
C = [sum(1 << i for i, x in enumerate(X) if D(c, x) == 3) for c in X]
assert len(set(C)) == 27 and all(m.bit_count() == 8 for m in C)

def traces(subset):
    return {sum(((mask >> i) & 1) << j for j, i in enumerate(subset)) for mask in C}

def shattered(subset):
    return len(traces(subset)) == (1 << len(subset))

F = [[] for _ in range(5)]
for k in range(5):
    F[k] = [s for s in itertools.combinations(range(27), k) if shattered(s)]
assert tuple(map(len, F)) == (1, 27, 351, 216, 0)

def special(triple):
    return all(D(X[triple[i]], X[triple[j]]) == 2 for i in range(3) for j in range(i+1, 3)) and all(len({X[t][j] for t in triple}) == 2 for j in range(3))
assert all(shattered(s) == special(s) for s in itertools.combinations(range(27), 3))

# Every pair at distance two belongs to four shattered triangles.
incidence = Counter(pair for triple in F[3] for pair in itertools.combinations(triple, 2))
for i, j in F[2]:
    assert incidence.get((i,j), 0) == (4 if D(X[i], X[j]) == 2 else 0)
assert sum(z == 0 for z in [incidence.get(s,0) for s in F[2]]) == 189

# A boundary-column over GF(2) is represented by a Python integer;
# pivot reduction evaluates the exact algebraic rank, not a numerical estimate.
edgeid = {e: j for j, e in enumerate(F[2])}
pivots = {}
for s in F[3]:
    v = 0
    for e in itertools.combinations(s, 2):
        v ^= 1 << edgeid[e]
    while v:
        bit = v.bit_length() - 1
        if bit in pivots:
            v ^= pivots[bit]
        else:
            pivots[bit] = v
            break
rank2 = len(pivots)
assert rank2 == 133
rank1 = 26 # full 27-vertex one-skeleton of a connected simplicial complex
betti1 = len(F[2]) - rank1 - rank2
betti2 = len(F[3]) - rank2
assert (betti1, betti2) == (192, 83)
print('PASS Python: faces 1,27,351,216; maximal edges 189; triangles 216; boundary rank 133; mod-2 reduced Betti numbers 192,83')
