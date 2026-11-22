#!/usr/bin/env python3
"""Independent integer verification of Catalan nearest-neighbor valuations.
No third-party packages. Exact rational arithmetic only.
"""
from collections import Counter
from fractions import Fraction
from math import comb


def valuation(n, p):
    count = 0
    while n and n % p == 0:
        n //= p
        count += 1
    return count


def legendre_factorial(n, p):
    out = 0
    while n:
        n //= p
        out += n
    return out


def catalan_valuation(n, p):
    return legendre_factorial(2 * n, p) - 2 * legendre_factorial(n, p) - valuation(n + 1, p)


def expected_jump_counts(p, k):
    size = p**k
    if p == 3:
        if k == 1:
            return {0: 3}
        out = {0: 7 * 3 ** (k - 2)}
        for j in range(1, k):
            n = 2 * 3 ** (k - j - 2) if j < k - 1 else 1
            out[-j] = n
            out[j] = n
        return out
    out = {0: (p - 2) * p ** (k - 1)}
    for j in range(1, k + 1):
        n = (p - 1) * p ** (k - j - 1) if j < k else 1
        out[-j] = n
        out[j] = n
    return out


def expected_cov(p, k):
    if p == 3:
        return -Fraction(1, 3) + Fraction(k, 3**k)
    return -Fraction((p + 1) * (p**k - 1) - 2 * k * (p - 1), (p - 1) ** 2 * p**k)


def check(p, k):
    size = p**k
    census = Counter()
    sx = sdelta = sxdelta = 0
    for n in range(size):
        x = catalan_valuation(n, p)
        y = catalan_valuation(n + 1, p)
        delta = y - x
        # Independent comparison to the elementary exact Catalan ratio
        assert delta == valuation(2 * n + 1, p) - valuation(n + 2, p)
        census[delta] += 1
        sx += x
        sdelta += delta
        sxdelta += x * delta
    assert sum(census.values()) == size
    assert dict(census) == expected_jump_counts(p, k), (p,k,census,expected_jump_counts(p,k))
    result = Fraction(sxdelta, size) - Fraction(sx, size) * Fraction(sdelta, size)
    assert result == expected_cov(p, k), (p,k,result,expected_cov(p,k))
    return size


def main():
    cases = {3:8, 5:6, 7:5, 11:4, 13:4, 17:3, 19:3}
    indices = sum(check(p, k) for p, depth in cases.items() for k in range(1, depth+1))
    direct_cases=0
    for p in [3, 5, 7, 11, 13]:
        for n in range(101):
            c0 = comb(2*n,n)//(n+1)
            c1 = comb(2*(n+1),n+1)//(n+2)
            assert catalan_valuation(n,p)==valuation(c0,p)
            assert catalan_valuation(n+1,p)==valuation(c1,p)
            direct_cases += 1
    print(f'VERIFY_OK prime_depth_cases={sum(cases.values())} exact_integer_indices={indices} actual_bigint_pairs={direct_cases} jump_histograms=PASS rational_covariance=PASS')


if __name__=='__main__':
    main()
