"""Exact finite Hamming-sphere VC and mod-two homology verification.

Python 3 standard library only. Independently builds ternary words as tuples,
evaluates distance-two traces, tests every support through four points,
computes all maximal faces, symmetry orbits and binary boundary ranks.
"""
from collections import Counter
from itertools import combinations, permutations, product

X = list(product(range(3), repeat=3))
N = len(X)
assert N == 27
D = [[sum(a != b for a, b in zip(u, v)) for v in X] for u in X]
C = [sum((D[i][j] == 2) << j for j in range(N)) for i in range(N)]


def shattered(s):
    masks = {sum((D[c][i] == 2) << j for j, i in enumerate(s)) for c in range(N)}
    return len(masks) == 2 ** len(s)


def allfaces(k):
    return [s for s in combinations(range(N), k) if shattered(s)]

faces = {k: allfaces(k) for k in range(1, 5)}
assert tuple(len(faces[k]) for k in range(1, 5)) == (27, 351, 2808, 3402)
covered = set(t for q in faces[4] for t in combinations(q, 3))
facets3 = [s for s in faces[3] if s not in covered]
assert len(facets3) == 540

G = []
for perm in permutations(range(3)):
    for p0, p1, p2 in product(tuple(permutations(range(3))), repeat=3):
        ps = (p0, p1, p2)
        G.append(tuple(X.index(tuple(ps[j][x[perm[j]]] for j in range(3))) for x in X))
assert len(G) == 1296 and len(set(G)) == 1296


def orbits(ss):
    remaining = set(ss)
    sizes = []
    while remaining:
        rep = min(remaining)
        orbit = {tuple(sorted(p[x] for x in rep)) for p in G}
        assert orbit <= remaining
        remaining -= orbit
        sizes.append(len(orbit))
    return sorted(sizes)

assert orbits(faces[4]) == [162, 648, 1296, 1296]
assert orbits(facets3) == [216, 324]


def gf2rank(vectors):
    pivots = {}
    for value in vectors:
        while value:
            pivot = value.bit_length() - 1
            if pivot in pivots:
                value ^= pivots[pivot]
            else:
                pivots[pivot] = value
                break
    return len(pivots)


def boundary_rank(k):
    subidx = {t: j for j, t in enumerate(faces[k-1])}
    columns = [sum(1 << subidx[t] for t in combinations(s, k-1)) for s in faces[k]]
    return gf2rank(columns)

r2 = boundary_rank(3)
r3 = boundary_rank(4)
assert (r2, r3) == (325, 1913)
assert (351 - 26 - r2, 2808 - r2 - r3, 3402 - r3) == (0, 570, 1489)
print('CONCEPTS=27')
print('FACES=1,27,351,2808,3402')
print('FACETS_3=540')
print('ORBIT_4=162,648,1296,1296')
print('ORBIT_FACET_3=216,324')
print('BOUNDARY_RANKS_1_2_3=26,325,1913')
print('BETTI_1_2_3=0,570,1489')
print('PASS')
