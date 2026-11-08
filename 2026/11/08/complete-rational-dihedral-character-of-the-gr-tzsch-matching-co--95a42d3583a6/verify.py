#!/usr/bin/env python3
"""Reproduce the rational D5-character calculation for the Grötzsch matching complex.

Only the Python standard library is used. Finite exact calculations, not sampling.
"""
from itertools import combinations
from collections import Counter

M = 5
V = tuple(range(11))
E = sorted(
    {tuple(sorted((i, (i + 1) % M))) for i in range(M)}
    | {tuple(sorted((i, 5 + (i + 1) % M))) for i in range(M)}
    | {tuple(sorted((i, 5 + (i - 1) % M))) for i in range(M)}
    | {(5 + i, 10) for i in range(M)}
)
assert len(E) == 20 and len(set(E)) == 20
neighbor = {v: set() for v in V}
for u, v in E:
    neighbor[u].add(v)
    neighbor[v].add(u)
assert Counter(map(len, neighbor.values())) == Counter({4: 5, 3: 5, 5: 1})
assert all(u not in neighbor[u] for u in V)

# Each face is a tuple of pairwise disjoint graph-edge indices.
faces = []
for k in range(1, 6):
    fs = [c for c in combinations(range(20), k)
          if len({vertex for ei in c for vertex in E[ei]}) == 2 * k]
    faces.append(fs)
assert [len(a) for a in faces] == [20, 135, 365, 360, 87]
assert not any(len({v for ei in c for v in E[ei]}) == 12
               for c in combinations(range(20), 6))
index = [{f: j for j, f in enumerate(fs)} for fs in faces]

# Signed face boundary of a simplex in each positive degree.
boundary = [None]
for d in range(1, 5):
    boundary.append([
        {index[d - 1][f[:i] + f[i + 1:]]: (-1) ** i
         for i in range(len(f))}
        for f in faces[d]
    ])
for d in range(2, 5):
    for col in boundary[d]:
        composed = {}
        for row, coef in col.items():
            for lower_row, term in boundary[d - 1][row].items():
                composed[lower_row] = composed.get(lower_row, 0) + coef * term
        assert all(c == 0 for c in composed.values())


def rank_mod_prime(columns, prime):
    pivots = {}
    for column in columns:
        current = {k: v % prime for k, v in column.items() if v % prime}
        while current:
            row = min(current)
            if row not in pivots:
                factor = pow(current[row], -1, prime)
                pivots[row] = {k: factor * v % prime for k, v in current.items()
                               if factor * v % prime}
                break
            factor = current[row]
            for k, v in pivots[row].items():
                val = (current.get(k, 0) - factor * v) % prime
                if val:
                    current[k] = val
                else:
                    current.pop(k, None)
    return len(pivots)

rank_table = {}
for p in (2, 3, 101):
    rank_table[p] = tuple(rank_mod_prime(boundary[d], p) for d in range(1, 5))
assert all(r == (19, 116, 249, 87) for r in rank_table.values())
# The field ranks are LOWER bounds on rational ranks. They are also
# simultaneously sharp UPPER bounds: rank(d1)<=20-1,
# rank(d2)<=135-rank(d1), rank(d3)<=365-rank(d2), rank(d4)<=87.
r1, r2, r3, r4 = rank_table[101]
assert r1 == 20 - 1 and r2 == 135 - r1
assert r3 == 365 - r2 and r4 == 87
assert (20 - r1 - 1, 135 - r1 - r2, 365 - r2 - r3,
        360 - r3 - r4, 87 - r4) == (0, 0, 0, 24, 0)


def perm_vertex(a, b, v):
    if v == 10:
        return v
    return (a * (v % M) + b) % M + (5 if v >= 5 else 0)


def sign_of_order(arr):
    inversions = sum(arr[i] > arr[j]
                     for i in range(len(arr)) for j in range(i + 1, len(arr)))
    return (-1) ** (inversions % 2)

emap = {e: i for i, e in enumerate(E)}
rows = {}
for a in (1, -1):
    for b in range(5):
        g = [perm_vertex(a, b, v) for v in V]
        assert set(g) == set(V)
        assert all(tuple(sorted((g[u], g[v]))) in emap for u, v in E)
        ge = [emap[tuple(sorted((g[u], g[v])))] for u, v in E]
        assert sorted(ge) == list(range(20))
        traces = []
        for fs in faces:
            trace = 0
            for f in fs:
                image = [ge[i] for i in f]
                if set(image) == set(f):
                    trace += sign_of_order(image)
            traces.append(trace)
        # Lefschetz on reduced chains: -1 from the empty face.
        reduced_lefschetz = -1 + sum((-1) ** d * tr for d, tr in enumerate(traces))
        # Reduced rational homology occurs only in degree 3.
        chi_h3 = -reduced_lefschetz
        rows[(a, b)] = (tuple(traces), chi_h3)
        if (a, b) == (1, 0):
            assert (tuple(traces), chi_h3) == ((20, 135, 365, 360, 87), 24)
        elif a == 1:
            assert (tuple(traces), chi_h3) == ((0, 0, 0, 0, 2), -1)
        else:
            assert (tuple(traces), chi_h3) == ((2, -3, -5, 0, 1), 0)

assert len(rows) == 10
assert sum(chi for _, chi in rows.values()) == 20
assert sum((chi if a == 1 else -chi) for (a, b), (_, chi) in rows.items()) == 20
assert (sum(chi for (a, b), (_, chi) in rows.items() if a == 1)) == 20
# D5-invariant homology is 2-dimensional; reflection sign isotypic is also 2.
assert 20 // 10 == 2
# Two regular modules and Q(zeta5) contribute respectively:
# identity 20+4=24, rotations 0-1=-1, reflections 0+0=0.
for (a, b), (_, ch) in rows.items():
    reg = 10 if (a, b) == (1, 0) else 0
    cyclo = 4 if (a, b) == (1, 0) else (-1 if a == 1 else 0)
    assert ch == 2 * reg + cyclo

print('GRAPH_VERTICES 11 GRAPH_EDGES', len(E))
print('MATCHING_FACE_VECTOR', *(len(x) for x in faces))
print('BOUNDARY_RANKS_BY_PRIME', rank_table)
print('REDUCED_RATIONAL_BETTI', (0, 0, 0, 24, 0))
print('SIGNED_CHAIN_TRACES_IDENTITY', rows[(1, 0)][0])
print('SIGNED_CHAIN_TRACES_NONIDENTITY_ROTATION', rows[(1, 1)][0])
print('SIGNED_CHAIN_TRACES_REFLECTION', rows[(-1, 0)][0])
print('H3_CHARACTER_IDENTITY_ROTATION_REFLECTION', 24, -1, 0)
print('QUOTIENT_BETTI3', 2)
print('GROTZSCH_MATCHING_D5_EXACT_PASS')
