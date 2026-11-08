#!/usr/bin/env python3
"""Exact integer and rational checks for a path with one new unit link.

The infinite-family optimality claim is established in RESULT.md; this
script independently tests its finite instances and a matrix formula.
Requires only Python's standard library.
"""
from fractions import Fraction


def gain_formula(n, i, j):
    """One-based vertices; use closed-form integer sums."""
    assert n >= 3 and 1 <= i < j - 1 <= n - 1
    d, r = j - i, n - j
    S = d * (d + 1) // 2 + d * r
    Q = d * (d + 1) * (2 * d + 1) // 6 + d * d * r
    return Fraction(n * Q - S * S, d + 1)


def gain_potential(n, i, j):
    """An independent potential-vector/variance calculation."""
    ys = [min(j - i, max(0, t - i)) for t in range(1, n + 1)]
    return Fraction(n * sum(y * y for y in ys) - sum(ys) ** 2, j - i + 1)


def inverse_fraction(A):
    N = len(A)
    M = [[Fraction(A[i][j]) for j in range(N)]
         + [Fraction(int(i == j)) for j in range(N)] for i in range(N)]
    for c in range(N):
        pivot = next(r for r in range(c, N) if M[r][c])
        M[c], M[pivot] = M[pivot], M[c]
        v = M[c][c]
        M[c] = [x / v for x in M[c]]
        for r in range(N):
            if r == c:
                continue
            v = M[r][c]
            if v:
                M[r] = [M[r][j] - v * M[c][j] for j in range(2 * N)]
    return [r[N:] for r in M]


def kirchhoff_matrix(n, i, j):
    """Completely independent graph-Laplacian grounded inverse."""
    L = [[0] * n for _ in range(n)]
    for a, b in [(t, t + 1) for t in range(n - 1)] + [(i - 1, j - 1)]:
        L[a][a] += 1
        L[b][b] += 1
        L[a][b] -= 1
        L[b][a] -= 1
    A = inverse_fraction([row[:-1] for row in L[:-1]])
    ans = Fraction(0)
    for a in range(n):
        for b in range(a + 1, n):
            if b == n - 1:
                ans += A[a][a]
            else:
                ans += A[a][a] + A[b][b] - 2 * A[a][b]
    return ans


def g(n, d):
    return Fraction(n * d * (3 * n * d - 2 * d * d + 2), 12 * (d + 1))


def main():
    checks = 0
    for n in range(3, 141):
        k = (n - 2) // 8
        predicted = (k + 1, n - k)
        gain = gain_formula(n, *predicted)
        winners = []
        maximum = Fraction(-1)
        for i in range(1, n - 1):
            for j in range(i + 2, n + 1):
                cur = gain_formula(n, i, j)
                if cur > maximum:
                    maximum, winners = cur, [(i, j)]
                elif cur == maximum:
                    winners.append((i, j))
                if n <= 18:
                    assert cur == gain_potential(n, i, j)
                    checks += 1
                if n <= 9:
                    assert kirchhoff_matrix(n, i, j) == Fraction(n * (n * n - 1), 6) - cur
                    checks += 1
        assert maximum == gain and winners == [predicted], (n, winners, predicted)
        checks += 1
        d = n - 1 - 2 * k
        assert gain == g(n, d)
        checks += 1
    for n in range(5, 141):
        for k in range((n - 5) // 2 + 1):
            d = n - 1 - 2 * k
            diff = g(n, d - 2) - g(n, d)
            assert (diff > 0) == (n >= 8 * k + 10)
            assert diff != 0
            checks += 1
    print('VERIFY_OK', checks)


if __name__ == '__main__':
    main()
