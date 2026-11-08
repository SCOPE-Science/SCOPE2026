#!/usr/bin/env python3
"""Exact, self-contained certificates for suspension spheres in AG(3,2)."""
from itertools import combinations
from collections import Counter

V = tuple(range(8))
QUADS = list(combinations(V, 4))
PLANES = tuple(q for q in QUADS if q[0] ^ q[1] ^ q[2] ^ q[3] == 0)
FACETS = tuple(q for q in QUADS if q not in PLANES)
FI = {f: j for j, f in enumerate(FACETS)}
TRIPLES = tuple(combinations(V, 3))
TI = {f: j for j, f in enumerate(TRIPLES)}

def sign(v):
    return -1 if sum(v[i] > v[j] for i in range(len(v)) for j in range(i + 1, len(v))) % 2 else 1

def sphere(P, pair):
    result = [0] * len(FACETS)
    for k, a in enumerate(pair):
        for j in range(4):
            ordered = [a] + [P[i] for i in range(4) if i != j]
            result[FI[tuple(sorted(ordered))]] += (-1 if k else 1) * (-1 if j % 2 else 1) * sign(ordered)
    return tuple(result)

INDEX = tuple((P, pair) for P in PLANES for pair in combinations(tuple(x for x in V if x not in P), 2))
CYCLES = tuple(sphere(P, pair) for P, pair in INDEX)

def boundary(c):
    out = [0] * len(TRIPLES)
    for i, val in enumerate(c):
        if val:
            f = FACETS[i]
            for j in range(4):
                out[TI[f[:j] + f[j + 1:]]] += val * (-1 if j % 2 else 1)
    return tuple(out)

def rank_mod2(rows):
    pivots = {}
    for vec in rows:
        x = sum((1 << i) for i, v in enumerate(vec) if v & 1)
        for j in sorted(pivots, reverse=True):
            if x & (1 << j):
                x ^= pivots[j]
        if x:
            pivots[x.bit_length() - 1] = x
    return len(pivots)

def det_bareiss(a):
    a = [list(map(int, row)) for row in a]
    n = len(a)
    s, prev = 1, 1
    for k in range(n - 1):
        if not a[k][k]:
            pivot = next((i for i in range(k + 1, n) if a[i][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            s = -s
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                q, r = divmod(pivot * a[i][j] - a[i][k] * a[k][j], prev)
                assert r == 0, (i, j, k)
                a[i][j] = q
        for i in range(k + 1, n):
            a[i][k] = 0
        prev = pivot
    return s * a[-1][-1]

assert len(PLANES) == 14 and len(FACETS) == 56 and len(CYCLES) == 84
assert all(boundary(c) == (0,) * len(TRIPLES) for c in CYCLES)
assert all(Counter(abs(v) for v in c) == {0: 48, 1: 8} for c in CYCLES)
# On each six-element subset, all three contained planes give a sphere; each pair of these cycles is independent.
for S in combinations(V, 6):
    local = [(P, sphere(P, tuple(x for x in S if x not in P))) for P in PLANES if set(P).issubset(S)]
    assert len(local) == 3, (S, local)
    assert rank_mod2([z for _, z in local]) == 2, S
    assert all(rank_mod2([local[i][1], local[j][1]]) == 2 for i,j in combinations(range(3),2)), S
    assert all(not any(z[i] for i, f in enumerate(FACETS) if not set(f).issubset(S)) for _, z in local)
# For five-element subsets, exactly one affine plane is present.
assert all(sum(set(P).issubset(S) for P in PLANES) == 1 for S in combinations(V, 5))
# The following lexicographic 21 columns, 21 rows form an integral unit minor.
COLS = (0, 1, 2, 6, 7, 8, 12, 13, 14, 18, 19, 20, 24, 25, 26, 30, 31, 32, 36, 37, 38)
ROWS = (0, 1, 2, 4, 5, 6, 8, 12, 13, 14, 16, 20, 24, 28, 29, 30, 32, 36, 40, 44, 48)
minor = [[CYCLES[j][i] for j in COLS] for i in ROWS]
assert det_bareiss(minor) == -1
# All affine automorphisms of the eight points: eight translations and 168 invertible linear maps.
def linear_map(x, basis):
    return (basis[0] if x & 1 else 0) ^ (basis[1] if x & 2 else 0) ^ (basis[2] if x & 4 else 0)
BASIS = [(a, b, c) for a in range(1, 8) for b in range(1, 8) if b != a for c in range(1, 8) if c not in (a, b, a ^ b)]
assert len(BASIS) == 168
supp = {tuple(sorted(P + pair)) for P, pair in INDEX}
assert len(supp) == 28
# Labels (plane, pair) give 84 distinct embedded sphere supports of the same six-set but different cycle directions.
labels = set(INDEX)
seen = set()
for B in BASIS:
    for t in V:
        P, pair = INDEX[0]
        PP = tuple(sorted(linear_map(x, B) ^ t for x in P))
        pq = tuple(sorted(linear_map(x, B) ^ t for x in pair))
        assert (PP, pq) in labels
        seen.add((PP, pq))
assert len(seen) == 84
print('AG32_AFFINE_SPHERE_CYCLES_PASS')
print('planes=14 tetrahedra=56 simplicial_sphere_cycles=84')
print('all_cycles_boundary_zero=true support_tetrahedra_each=8')
print('six_element_subsets=28 each_local_rank=2 each_three_planes=true')
print('five_element_subsets=56 each_one_plane=true')
print('basis_columns_zero_based=' + str(list(COLS)))
print('minor_rows_zero_based=' + str(list(ROWS)))
print('integral_minor_determinant=-1')
print('affine_automorphisms=1344 sphere_orbit_size=84')
