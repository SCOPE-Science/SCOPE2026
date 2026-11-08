#!/usr/bin/env python3
"""Exact finite certificate for coordinate controllability of the Fano incidence graph.

Python standard library only. All matrix computations use finite fields with exact
integer arithmetic; the determinant bound in the accompanying proof lifts the
7-by-7 finite-field test to characteristic zero.
"""
from itertools import combinations, product
from collections import Counter


def inner(a, b):
    return (a & b).bit_count() % 2


LABELS = range(1, 8)
N = [[int(inner(a, x) == 0) for a in LABELS] for x in LABELS]
assert all(sum(row) == 3 for row in N)
assert all(sum(N[i][j] * N[k][j] for j in range(7)) == (3 if i == k else 1)
           for i in range(7) for k in range(7))


def rank_mod(A, prime):
    matrix = [[x % prime for x in row] for row in A]
    rows, cols = len(matrix), len(matrix[0])
    rank = 0
    for j in range(cols):
        pivot = next((i for i in range(rank, rows) if matrix[i][j]), None)
        if pivot is None:
            continue
        matrix[pivot], matrix[rank] = matrix[rank], matrix[pivot]
        inv = pow(matrix[rank][j], -1, prime)
        for k in range(j, cols):
            matrix[rank][k] = matrix[rank][k] * inv % prime
        for i in range(rank + 1, rows):
            multiple = matrix[i][j]
            if multiple:
                for k in range(j, cols):
                    matrix[i][k] = (matrix[i][k] - multiple * matrix[rank][k]) % prime
        rank += 1
        if rank == rows:
            break
    return rank


def control_rows(S):
    return [[1] * 7] + [([int(j == i) for j in range(7)] if i < 7
                           else [N[j][i - 7] for j in range(7)]) for i in S]


sets = list(combinations(range(14), 6))
valid = {S: rank_mod(control_rows(S), 101) == 7 for S in sets}
counts = [sum(valid[S] for S in sets if sum(i < 7 for i in S) == k) for k in range(7)]
assert counts == [7, 84, 420, 868, 420, 84, 7]
assert sum(valid.values()) == 1890 and len(sets) == 3003


def transform(columns, x):
    result = 0
    for k in range(3):
        if (x >> k) & 1:
            result ^= columns[k]
    return result


def compatible_line_image(columns, original):
    return next(a for a in LABELS if all(
        inner(a, transform(columns, x)) == inner(original, x) for x in LABELS))


group = []
for c in product(LABELS, repeat=3):
    if len({transform(c, x) for x in LABELS}) != 7:
        continue
    g = tuple([transform(c, x) - 1 for x in LABELS] +
              [compatible_line_image(c, a) + 6 for a in LABELS])
    assert len(set(g)) == 14
    assert all(N[x][a] == N[g[x]][g[a + 7] - 7]
               for x in range(7) for a in range(7))
    group.append(g)
assert len(group) == len(set(group)) == 168
swap = tuple(range(7, 14)) + tuple(range(7))
group += [tuple(swap[g[i]] for i in range(14)) for g in group]
assert len(set(group)) == 336

seen = set()
orbit_sizes = Counter()
valid_representatives = []
for S in sets:
    if S in seen:
        continue
    orbit = {tuple(sorted(g[i] for i in S)) for g in group}
    assert not (seen & orbit)
    assert len({valid[T] for T in orbit}) == 1
    seen.update(orbit)
    orbit_sizes[(len(orbit), valid[S])] += 1
    if valid[S]:
        valid_representatives.append((len(orbit), S))
assert len(seen) == 3003
assert len(valid_representatives) == 14
assert Counter(k for k, _ in valid_representatives) == Counter({14: 1, 28: 2, 56: 1, 84: 1, 168: 8, 336: 1})

# Independently replay the Kalman controllability criterion using the full
# integer 14-by-14 Laplacian, over a different prime. The minimal polynomial
# has degree four, since L has exactly four distinct eigenvalues.
L = [[0] * 14 for _ in range(14)]
for i in range(7):
    for j in range(7):
        if N[i][j]:
            L[i][i] += 1
            L[j + 7][j + 7] += 1
            L[i][j + 7] -= 1
            L[j + 7][i] -= 1
for S in sets:
    col_vectors = []
    for v in S:
        x = [int(i == v) for i in range(14)]
        for _ in range(4):
            col_vectors.append(x)
            x = [sum(L[i][j] * x[j] for j in range(14)) for i in range(14)]
    K = [[col[i] for col in col_vectors] for i in range(14)]
    assert (rank_mod(K, 1009) == 14) == valid[S]

print('PASS: 3003 exactly enumerated six-vertex sets, 1890 controllable')
print('Selected-point profile:', counts)
print('PASS: full automorphism group order 336; 14 controllable orbits')
print('Controllable orbit sizes:', sorted(k for k, _ in valid_representatives))
print('Orbit representatives (size, zero-based vertex labels):')
for item in sorted(valid_representatives):
    print(item)
print('PASS: 3003 independent full-Laplacian, four-Krylov-block rank comparisons')
