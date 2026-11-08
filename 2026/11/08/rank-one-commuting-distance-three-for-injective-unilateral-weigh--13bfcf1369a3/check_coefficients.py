"""Finite exact checks of the coefficient identities used in the accompanying proof.

This is not a finite-dimensional proof of the infinite-dimensional spectral claim.
"""
from fractions import Fraction as Q


def matmul(A, B):
    n = len(A)
    return [[sum((A[i][k] * B[k][j] for k in range(n)), Q(0))
             for j in range(n)] for i in range(n)]


def matadd(A, B):
    return [[x + y for x, y in zip(row, row2)]
            for row, row2 in zip(A, B)]


def identity(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def check(n):
    w = [Q(1, 2 ** (j + 1)) for j in range(n)]
    d = [Q(1)]
    for x in w:
        d.append(d[-1] * x)
    W = [[Q(0) for _ in range(n)] for _ in range(n)]
    for j in range(n - 1):
        W[j + 1][j] = w[j]
    powers = [identity(n)]
    for _ in range(1, 5):
        powers.append(matmul(powers[-1], W))
    a = [Q(7, 4), Q(0), Q(-3, 5), Q(1, 7), Q(2, 3)]
    S = [[sum((a[k] * powers[k][i][j] for k in range(5)), Q(0))
          for j in range(n)] for i in range(n)]
    assert matmul(W, S) == matmul(S, W)
    for j in range(n):
        for k in range(min(5, n - j)):
            assert S[j + k][j] == a[k] * d[j + k] / d[j]
    P = [[Q(i == j and i % 2 == 0) for j in range(n)] for i in range(n)]
    F = [[Q(i == 0 and j == 0) for j in range(n)] for i in range(n)]
    assert matmul(powers[2], P) == matmul(P, powers[2])
    assert matmul(P, F) == matmul(F, P)
    for m in range(1, n):
        products = []
        for j in range(n - m):
            product = Q(1)
            for r in range(j, j + m):
                product *= w[r]
            products.append(product)
        assert max(products) == Q(1, 2 ** (m * (m + 1) // 2))
    return n * n + n


if __name__ == '__main__':
    totals = [check(n) for n in (6, 8, 12, 16)]
    print('Exact rational coefficient/commutation/power-product checks:',
          sum(totals), 'grouped cases, passed')
    print('Scope: finite algebraic identities only; not an infinite spectrum test.')
