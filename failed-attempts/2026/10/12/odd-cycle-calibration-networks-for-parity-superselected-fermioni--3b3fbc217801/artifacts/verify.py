#!/usr/bin/env python3
from fractions import Fraction
import math


def edges_cycle(q):
    return [(i, (i + 1) % q) for i in range(q)]


def responses(edges, b):
    return [b[i] + b[j] for i, j in edges]


def solve_linear(A, y):
    A = [[Fraction(x) for x in row] for row in A]
    y = [Fraction(x) for x in y]
    n = len(A)
    M = [A[i] + [y[i]] for i in range(n)]
    for c in range(n):
        pivot = next(r for r in range(c, n) if M[r][c] != 0)
        M[c], M[pivot] = M[pivot], M[c]
        piv = M[c][c]
        M[c] = [z / piv for z in M[c]]
        for r in range(n):
            if r == c:
                continue
            fac = M[r][c]
            if fac:
                M[r] = [M[r][k] - fac * M[c][k] for k in range(n + 1)]
    return [M[i][-1] for i in range(n)]


def normal_matrix(q, edges):
    Q = [[Fraction(0) for _ in range(q)] for _ in range(q)]
    for i, j in edges:
        Q[i][i] += 1
        Q[j][j] += 1
        Q[i][j] += 1
        Q[j][i] += 1
    return Q


def rhs(q, edges, s):
    z = [Fraction(0) for _ in range(q)]
    for (i, j), val in zip(edges, s):
        z[i] += val
        z[j] += val
    return z

# Odd cycles recover arbitrary marker corrections exactly from pair sums.
for q in (3, 5, 7, 9):
    E = edges_cycle(q)
    b = [Fraction((i + 2) * (-1 if i % 3 == 1 else 1), i + 3) for i in range(q)]
    s = responses(E, b)
    Q = normal_matrix(q, E)
    rec = solve_linear(Q, rhs(q, E, s))
    assert rec == b

    # The signless-Laplacian least eigenvalue of an odd cycle.
    eigs = [2.0 + 2.0 * math.cos(2.0 * math.pi * k / q) for k in range(q)]
    expected = 4.0 * math.sin(math.pi / (2.0 * q)) ** 2
    assert abs(min(eigs) - expected) < 1e-12

# An even cycle has the alternating kernel, so calibration is non-identifiable.
q = 6
E = edges_cycle(q)
x = [Fraction(1 if i % 2 == 0 else -1) for i in range(q)]
assert responses(E, x) == [0] * q

# The triangle is the smallest simple calibration graph with full column rank.
# One or two marker vertices admit no non-bipartite simple graph.
assert len(edges_cycle(3)) == 3

print('VERIFY_OK')
