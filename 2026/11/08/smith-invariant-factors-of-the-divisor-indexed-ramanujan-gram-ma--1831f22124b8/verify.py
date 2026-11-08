#!/usr/bin/env python3
"""Exact finite checks of the divisor-indexed Ramanujan Gram Smith formula.
Uses only the Python standard library. The mathematical proof is separate.
"""
from itertools import combinations
from math import gcd, prod


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def factor(n):
    ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            a = 0
            while n % d == 0:
                n //= d
                a += 1
            ans.append((d, a))
        d += 1
    if n > 1:
        ans.append((n, 1))
    return ans


def mobius(n):
    if n == 1:
        return 1
    sign = 1
    for p, a in factor(n):
        if a > 1:
            return 0
        sign = -sign
    return sign


def ramanujan(d, t):
    return sum(e * mobius(d // e) for e in divisors(gcd(d, t)))


def gram(n):
    ds = divisors(n)
    c = [[ramanujan(d, t) for t in ds] for d in ds]
    m = len(ds)
    return [[sum(c[i][k] * c[j][k] for k in range(m))
             for j in range(m)] for i in range(m)]


def det_bareiss(mat):
    n = len(mat)
    if not n:
        return 1
    a = [list(row) for row in mat]
    sign, previous = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            r = next((r for r in range(k + 1, n) if a[r][k]), None)
            if r is None:
                return 0
            a[k], a[r] = a[r], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def independent_smith_from_minors(mat):
    n = len(mat)
    ds = [1]
    for size in range(1, n + 1):
        g = 0
        for rr in combinations(range(n), size):
            for cc in combinations(range(n), size):
                sub = [[mat[i][j] for j in cc] for i in rr]
                g = gcd(g, abs(det_bareiss(sub)))
        assert g % ds[-1] == 0
        ds.append(g)
    assert ds[-1] != 0
    invariant = [ds[i] // ds[i - 1] for i in range(1, n + 1)]
    assert all(invariant[i + 1] % invariant[i] == 0 for i in range(n - 1))
    return invariant


def local_exponents(p, a):
    out = []
    i = 0
    while i <= a:
        if (a - i + 1) % p == 0:
            assert i < a
            out.extend((2 * i + 1, 2 * i + 1))
            i += 2
        else:
            out.append(2 * i)
            i += 1
    assert len(out) == a + 1
    return out


def predicted_smith(n):
    factors = factor(n)
    if not factors:
        return [1]
    size = prod(a + 1 for p, a in factors)
    ans = [1] * size
    for p, a in factors:
        local = local_exponents(p, a)
        repeated = sorted(local * (size // (a + 1)))
        for j, e in enumerate(repeated):
            ans[j] *= p ** e
    return ans


def rank_mod(mat, p):
    x = [[entry % p for entry in row] for row in mat]
    m = len(x)
    rank = 0
    for j in range(m):
        k = next((i for i in range(rank, m) if x[i][j]), None)
        if k is None:
            continue
        x[rank], x[k] = x[k], x[rank]
        z = pow(x[rank][j], -1, p)
        for v in range(j, m):
            x[rank][v] = x[rank][v] * z % p
        for i in range(rank + 1, m):
            q = x[i][j]
            for v in range(j, m):
                x[i][v] = (x[i][v] - q * x[rank][v]) % p
        rank += 1
    return rank


def main():
    cases = [1] + [p ** a for p, bound in ((2, 6), (3, 5), (5, 4), (7, 3), (11, 2))
                     for a in range(1, bound + 1)] + [6, 10, 12, 18, 20, 30]
    minors = 0
    for n in cases:
        mat = gram(n)
        observed = independent_smith_from_minors(mat)
        expected = predicted_smith(n)
        assert observed == expected, (n, observed, expected)
        assert prod(observed) == n ** len(observed)
        assert observed[-1] == n * n // (2 if n % 2 == 0 else 1)
        for p, a in factor(n):
            target_rank = 0 if (a + 1) % p == 0 else len(mat) // (a + 1)
            assert rank_mod(mat, p) == target_rank, (n, p)
        m = len(mat)
        minors += sum(__import__('math').comb(m, i) ** 2 for i in range(1, m + 1))
    print('VERIFY_OK cases=%d determinant_minors=%d independent_smith=PASS determinant=PASS cokernel_exponent=PASS modular_ranks=PASS' % (len(cases), minors))

if __name__ == '__main__':
    main()
