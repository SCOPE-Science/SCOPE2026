#!/usr/bin/env python3
"""Finite exact-arithmetic diagnostics for periodic Cesaro sandwich identities.

No finite test proves compactness or an infinite-dimensional essential norm.
All matrix indices in the computation start from one.
"""
from fractions import Fraction as F
from math import sqrt


def matmul(A, B):
    n = len(A)
    return [[sum((A[i][k] * B[k][j] for k in range(n)), F(0))
             for j in range(n)] for i in range(n)]


def cesaro(n):
    return [[F(1, i + 1) if j <= i else F(0)
             for j in range(n)] for i in range(n)]


def diagonal(items):
    n = len(items)
    return [[F(items[i]) if i == j else F(0)
             for j in range(n)] for i in range(n)]


def verify_period(c, N):
    q = len(c)
    m = sum((F(v) for v in c), F(0)) / q
    mu = sum((F(v*v) for v in c), F(0)) / q
    seq = [c[i % q] for i in range(N)]
    C = cesaro(N)
    Dc = diagonal(seq)
    R = matmul(Dc, C)
    R2 = matmul(R, R)
    C2 = matmul(C, C)
    # Exact finite-matrix formula, valid even when a nonzero Cesaro tail is cut off.
    for i in range(N):
        for k in range(N):
            if k <= i:
                lhs = R2[i][k] - m * seq[i] * C2[i][k]
                rhs = F(seq[i], i + 1) * sum(
                    (F(seq[j], j + 1) - m / (j + 1)
                     for j in range(k, i + 1)), F(0))
                assert lhs == rhs
            else:
                assert R2[i][k] == 0
    # The squared-modulus Gram identity is a finite exact tail identity.
    G = matmul(matmul(list(zip(*C)), diagonal([v*v-mu for v in seq])), C)
    for i in range(N):
        for k in range(N):
            tail = sum(((F(seq[j]*seq[j]) - mu) / ((j + 1)**2)
                        for j in range(max(i, k), N)), F(0))
            assert G[i][k] == tail
    return 2*N*N


def main():
    cases = [[1, -1], [1, 2, -3], [2, 0, -2, 0], [1, 2, 3], [1, 0, 0, -3]]
    total = 0
    for c in cases:
        for N in [2, 3, 5, 9, 13]:
            total += verify_period(c, N)
    # The Cesaro lower-bound sequence is a weakly null approximate norm-two packet.
    for n in [100, 500, 2000, 8000]:
        h = sum(1/k for k in range(1, n + 1))
        partial = 0.0
        normsq = 0.0
        for k in range(1, n + 1):
            partial += 1/sqrt(k)
            normsq += (partial/k)**2 / h
        assert 1.4 < sqrt(normsq) < 2.01
        total += 1
    print(f"PASS: {total} exact entrywise identities and lower-bound diagnostics")


if __name__ == '__main__':
    main()
