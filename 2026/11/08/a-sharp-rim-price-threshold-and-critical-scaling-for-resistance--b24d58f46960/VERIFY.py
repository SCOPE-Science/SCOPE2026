#!/usr/bin/env python3
"""Exact rational checks for the price-sensitive wheel Kirchhoff-index identity.

Only Python's standard library is needed.  These finite checks complement,
but do not substitute for, the analytic proof in RESULT.md.
"""
from fractions import Fraction as Q
from math import sin, pi, sqrt, isclose

checks = 0

def inverse(matrix):
    n = len(matrix)
    M = [[Q(z) for z in row] + [Q(i == j) for j in range(n)]
         for i, row in enumerate(matrix)]
    for k in range(n):
        r = next((r for r in range(k, n) if M[r][k]), None)
        if r is None:
            raise AssertionError('Singular input matrix')
        M[k], M[r] = M[r], M[k]
        pivot = M[k][k]
        M[k] = [x / pivot for x in M[k]]
        for r in range(n):
            if r != k and M[r][k]:
                mul = M[r][k]
                M[r] = [x - mul*y for x, y in zip(M[r], M[k])]
    return [row[n:] for row in M]

def trace(matrix):
    return sum((matrix[i][i] for i in range(len(matrix))), Q(0))

def laplacian(n, edges):
    L = [[Q(0) for _ in range(n)] for _ in range(n)]
    for u, v, w in edges:
        L[u][u] += w
        L[v][v] += w
        L[u][v] -= w
        L[v][u] -= w
    return L

def wheel_and_cycle(m, x, y):
    wheel = [(0, i, x) for i in range(1, m+1)]
    wheel += [(i, i+1 if i < m else 1, y) for i in range(1, m+1)]
    cycle = [(i, (i+1) % m, Q(1)) for i in range(m)]
    return laplacian(m+1, wheel), laplacian(m, cycle)

def kirchhoff(L):
    n = len(L)
    X = [[L[i][j] + Q(1, n) for j in range(n)] for i in range(n)]
    return n * (trace(inverse(X)) - 1)

for m in (3, 4, 5, 6, 8, 10):
    for x in (Q(1), Q(3, 2), Q(2)):
        for y in (Q(0), Q(1, 3), Q(2, 5), Q(1)):
            L, C = wheel_and_cycle(m, x, y)
            N = m+1
            actual = kirchhoff(L)
            inv = inverse([[x*Q(i == j) + y*C[i][j] for j in range(m)] for i in range(m)])
            expected = Q(1, x) + N*(trace(inv)-Q(1, x))
            assert actual == expected, (m, x, y, actual, expected)
            checks += 1
    # These trace identities encode the first two rim Laplacian moments.
    _, C = wheel_and_cycle(m, Q(1), Q(0))
    second = sum(C[i][j]*C[j][i] for i in range(m) for j in range(m))
    assert trace(C) == 2*m and second == 6*m
    checks += 1

# Check the closed Fourier-root-of-unity identity independently, over
# a selection of times and cycle lengths.
for m in (3, 4, 5, 7, 10, 20, 51):
    for t in (0.01, 0.1, 0.5, 1.0, 2.0, 4.0):
        s = sqrt(1+4*t)
        q = (s-1)/(s+1)
        lhs = sum(1/(1+4*t*sin(pi*k/m)**2) for k in range(m))
        rhs = m/s*(1+q**m)/(1-q**m)
        assert isclose(lhs, rhs, rel_tol=3e-12, abs_tol=3e-12)
        checks += 1

# Exact threshold marginal:  f'(0)=m^2(c-(2+2/m)).
# Evaluate from F(0)=m^2, F'(0)=-(m+1)*2m, with cycle trace.
for m in range(3, 31):
    for c in (Q(1, 2), Q(2), Q(2) + Q(2, m), Q(3), Q(7, 2)):
        marginal = c*m*m-2*m*(m+1)
        assert marginal == m*m*(c-(Q(2)+Q(2,m)))
        checks += 1

print('VERIFY_OK', checks)
