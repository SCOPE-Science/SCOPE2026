#!/usr/bin/env python3
"""Exact finite checks for the smooth Fermat logarithmic-bundle jumping divisor.
Only Python's standard library is needed. Checks complement, not replace, the proof.
"""
from math import comb, factorial
from fractions import Fraction


def det_bareiss(M):
    m = [list(map(int, row)) for row in M]
    n = len(m)
    if n == 0:
        return 1
    assert all(len(row) == n for row in m)
    sign = 1
    prior = 1
    for k in range(n - 1):
        if m[k][k] == 0:
            j = next((j for j in range(k + 1, n) if m[j][k]), None)
            if j is None:
                return 0
            m[k], m[j] = m[j], m[k]
            sign = -sign
        pivot = m[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                val = m[i][j] * pivot - m[i][k] * m[k][j]
                assert val % prior == 0
                m[i][j] = val // prior
        for i in range(k + 1, n):
            m[i][k] = 0
        prior = pivot
    return sign * m[-1][-1]


def binom(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def gram(r):
    return [[binom(2 * r, r + i - j) for j in range(r)] for i in range(r)]


def binary_map(r, A, B):
    # On line A*x+B*y+z=0, z^{2r}=(A*x+B*y)^{2r}.
    k = 2 * r
    s = r - 1
    N = k + s + 1
    M = [[0] * (3 * (s + 1)) for _ in range(N)]
    for j in range(s + 1):
        M[k + j][j] = 1             # x^k * x^j y^(s-j)
        M[j][s + 1 + j] = 1       # y^k * x^j y^(s-j)
        for e in range(N):
            u = e - j
            if 0 <= u <= k:
                M[e][2 * (s + 1) + j] = binom(k, u) * A**u * B**(k-u)
    return M


def integer_det_product(r):
    ans = Fraction(1)
    for i in range(r):
        ans *= Fraction(factorial(i) * factorial(2 * r + i), factorial(r + i)**2)
    assert ans.denominator == 1
    return int(ans)


def run():
    triples = [(1, 1), (2, 3), (3, -1)]
    checked = 0
    for r in range(1, 9):
        P = [[binom(r, t-i) for t in range(2*r)] for i in range(r)]
        G = gram(r)
        assert all(G[i][j] == sum(P[i][t] * P[j][t] for t in range(2*r))
                   for i in range(r) for j in range(r))
        # The first r columns of P form an upper triangular matrix with diagonal 1;
        # hence the Gram matrix is positive definite.
        assert all(P[i][i] == 1 and all(P[j][i] == 0 for j in range(i+1,r)) for i in range(r))
        D = det_bareiss(G)
        assert D == integer_det_product(r) and D > 0
        assert (2*r + 1)**2 - 3*(2*r + 1) + 3 - (r - 1)**2 == 3*r*r
        checked += 1
        if r <= 5:
            for A, B in triples:
                M = binary_map(r, A, B)
                assert len(M) == 3*r and all(len(row) == 3*r for row in M)
                det = det_bareiss(M)
                assert abs(det) == D * abs(A*B)**(r*r)
                checked += 1
        print(f'r={r} degree={2*r+1} Gram_det={D} normalized_c2={3*r*r} finite_cases_checked')
    print(f'VERIFY_OK: {checked} exact determinant/Gram/Chern test sets')

if __name__ == '__main__':
    run()
