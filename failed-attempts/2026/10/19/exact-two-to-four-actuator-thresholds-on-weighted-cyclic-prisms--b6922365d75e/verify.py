#!/usr/bin/env python3
"""Exact finite-instance checks for node-actuated weighted cylindrical Laplacians.

Requires SymPy. The infinite-parameter proof is analytic; this script tests
representative rational parameters and an exact algebraic collision identity.
"""
from sympy import Matrix, zeros, Rational, sqrt, cos, pi, simplify, sin


def laplacian(n, rung):
    assert n >= 3 and rung > 0
    L = zeros(2 * n)
    for side in range(2):
        for j in range(n):
            u, v = side * n + j, side * n + (j + 1) % n
            L[u, u] += 1
            L[v, v] += 1
            L[u, v] -= 1
            L[v, u] -= 1
    for j in range(n):
        u, v = j, n + j
        L[u, u] += rung
        L[v, v] += rung
        L[u, v] -= rung
        L[v, u] -= rung
    return L


def controllability_rank(n, rung, sites):
    L = laplacian(n, rung)
    B = zeros(2 * n, len(sites))
    for i, vertex in enumerate(sites):
        B[vertex, i] = 1
    blocks = []
    term = B
    for t in range(2 * n):
        blocks.append(term)
        term = L * term
    return Matrix.hstack(*blocks).rank()


def check(n, rung, sites, expected):
    actual = controllability_rank(n, rung, sites)
    assert actual == expected, (n, rung, sites, actual, expected)
    print('PASS', n, str(rung), sites, actual, '/', 2*n)


if __name__ == '__main__':
    assert simplify(cos(2*pi/5) - cos(4*pi/5) - sqrt(5)/2) == 0
    assert sin(2*pi/5) != 0 and sin(4*pi/5) != 0
    print('PASS n=5 interior/interior eigenvalue coincidence at rung=sqrt(5)/2')
    checks = [
        (3, Rational(1, 2), [0, 1], 6),
        (3, Rational(3, 2), [0, 1], 5),
        (3, Rational(3, 2), [0, 1, 3], 6),
        (4, Rational(1, 3), [0, 1], 8),
        (4, Rational(1), [0, 1], 6),
        (4, Rational(1), [0, 1, 4], 8),
        (4, Rational(2), [0, 1], 8),
        (4, Rational(2), [0, 5], 7),
        (4, Rational(2), [0, 6], 6),
        (5, Rational(1, 3), [0, 1], 10),
        (6, Rational(1, 3), [0, 1], 12),
        (6, Rational(1), [0, 1, 6], 11),
        (6, Rational(1), [0, 1, 6, 7], 12),
        (6, Rational(2), [0, 1], 12),
        (6, Rational(2), [0, 8], 12),
        (6, Rational(2), [0, 7], 11),
        (6, Rational(1, 2), [0, 1, 6], 12),
        (6, Rational(3, 2), [0, 1, 6], 12),
    ]
    for row in checks:
        check(*row)
    print('All', len(checks), 'finite Kalman checks passed.')
