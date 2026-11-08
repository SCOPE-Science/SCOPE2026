#!/usr/bin/env python3
"""Exact finite consistency checks for Perron synchronization and clipped realizations.

Runs with the Python standard library. These finite examples are not proofs of
infinite or universal assertions; the accompanying mathematical argument is.
"""
from fractions import Fraction as Q
from itertools import product

A = [[Q(0), Q(2), Q(0)],
     [Q(0), Q(0), Q(1, 2)],
     [Q(1), Q(0), Q(0)]]
u = [Q(2), Q(1), Q(2)]
w = [Q(1, 6), Q(1, 3), Q(1, 6)]
N = len(A)
P = [[A[i][j] * u[j] / u[i] for j in range(N)] for i in range(N)]
assert all(sum(row) == 1 for row in P)
assert [sum(A[i][j] * u[j] for j in range(N)) for i in range(N)] == u
assert [sum(w[i] * A[i][j] for i in range(N)) for j in range(N)] == w
assert sum(w[i] * u[i] for i in range(N)) == 1


def clip(s, a, b):
    return max(a, min(b, s))


def map_point(x, signs, a, b):
    t = [signs[i] * x[i] / u[i] for i in range(N)]
    return tuple(signs[i] * u[i] * clip(sum(P[i][j] * t[j]
                 for j in range(N)), a, b) for i in range(N))


points = [tuple(v) for v in product([Q(k, 4) for k in range(-4, 5)], repeat=N)
          if all(abs(v[i]) <= u[i] for i in range(N))]
intervals = [(Q(-1, 2), Q(3, 4)), (Q(0), Q(0)), (Q(-1), Q(1))]
checks = 0
for signs in product((-1, 1), repeat=N):
    for a, b in intervals:
        images = [map_point(p, signs, a, b) for p in points]
        for x, tx in zip(points, images):
            t = [signs[i] * x[i] / u[i] for i in range(N)]
            if tx == x:
                assert t[0] == t[1] == t[2] and a <= t[0] <= b
            if t[0] == t[1] == t[2] and a <= t[0] <= b:
                assert tx == x
            checks += 2
        # Deterministic diverse finite pairs; no randomness, no dependencies.
        for k in range(0, len(points), 13):
            x, y = points[k], points[(7 * k + 17) % len(points)]
            tx, ty = map_point(x, signs, a, b), map_point(y, signs, a, b)
            for i in range(N):
                assert abs(tx[i] - ty[i]) <= sum(A[i][j] * abs(x[j]-y[j]) for j in range(N))
                checks += 1
print('PERRON_FIXED_INTERVAL_EXACT_CONSISTENCY_OK', checks)
