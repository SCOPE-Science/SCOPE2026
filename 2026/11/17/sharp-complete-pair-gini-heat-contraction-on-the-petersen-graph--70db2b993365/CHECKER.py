#!/usr/bin/env python3
"""Exact finite cut certificate for the Petersen Markov heat Gini norm.

Mathematical model: vertices are two-subsets of {0,...,4}; two are
adjacent exactly when disjoint. This program uses only integer and
rational arithmetic in its finite certificates.
"""
from itertools import combinations, permutations
from fractions import Fraction

V = list(combinations(range(5), 2))
N = len(V)
A = [[int(set(u).isdisjoint(v)) for v in V] for u in V]
assert N == 10 and all(sum(row) == 3 for row in A)
for i in range(N):
    for j in range(N):
        assert sum(A[i][k] * A[k][j] for k in range(N)) == 2 * (i == j) - A[i][j] + 1

m = {v: j for j, v in enumerate(V)}
perms = [[m[tuple(sorted((p[u], p[v])))] for u, v in V]
         for p in permutations(range(5))]
seen = set()
orbits = []
for mask in range(1, 2**N - 1):
    if mask in seen:
        continue
    orb = {sum(((mask >> i) & 1) << pm[i] for i in range(N)) for pm in perms}
    assert not (orb & seen)
    seen.update(orb)
    orbits.append(orb)
assert len(seen) == 1022 and len(orbits) == 32

max_by_s = [Fraction(0) for _ in range(N + 1)]
maximizers = [[] for _ in range(N + 1)]
by_s = [0 for _ in range(N + 1)]

for mask in range(1, 2**N - 1):
    x = [(mask >> j) & 1 for j in range(N)]
    s = sum(x)
    y = [2 * x[i] + sum(A[i][j] * x[j] for j in range(N)) for i in range(N)]
    z = [x[i] - sum(A[i][j] * x[j] for j in range(N)) for i in range(N)]
    g = sum(abs(y[i] - y[j]) for i in range(N) for j in range(i + 1, N))
    assert 3 * g <= 11 * s * (N - s), (mask, s, g)
    if 1 < s < N - 1:
        assert 3 * g < 11 * s * (N - s)
    ratio = Fraction(g, s * (N - s))
    if ratio > max_by_s[s]:
        max_by_s[s] = ratio
        maximizers[s] = [mask]
    elif ratio == max_by_s[s]:
        maximizers[s].append(mask)
    by_s[s] += 1
    for r in (Fraction(0), Fraction(1, 7), Fraction(1, 3),
              Fraction(1, 2), Fraction(2, 3), Fraction(1)):
        observed = sum(abs((y[i] - y[j]) + r * (z[i] - z[j]))
                       for i in range(N) for j in range(i + 1, N))
        target = (Fraction(11, 3) * (1 - r) + 3 * r) * s * (N - s)
        assert observed <= target
        if s == 1 or s == N - 1:
            assert observed == target

expected = ['11/3', '7/2', '67/21', '37/12', '3', '37/12', '67/21', '7/2', '11/3']
assert [str(v) for v in max_by_s[1:N]] == expected
assert [len(maximizers[s]) for s in range(1, N)] == [10,15,30,60,12,60,30,15,10]
print('PETERSEN_GRAPH_A2_RELATION_PASS')
print('EXACT_32_SYMMETRY_ORBITS_COVER_ALL_1022_NONTRIVIAL_CUTS_PASS')
for s in range(1, N):
    print(f'SIZE_{s}_CUTS_{by_s[s]}_MAX_{max_by_s[s]}_NUM_EXTREMIZERS_{len(maximizers[s])}')
print('UNIFORM_ENDPOINT_CERTIFICATE_STRICT_EXCEPT_SINGLETON_COMPLEMENT_PASS')
print('ALL_6_RATIONAL_INTERPOLATION_TESTS_PER_CUT_PASS')
print('PETERSEN_GINI_ALL_CHECKS_PASS')
