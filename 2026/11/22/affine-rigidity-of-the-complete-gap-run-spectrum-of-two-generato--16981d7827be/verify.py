#!/usr/bin/env python3
"""Exact checks for the affine gap-run spectrum of coprime two-coin semigroups.

Run with Python >=3.8: python verify.py
No packages or external files are required.
"""
from collections import Counter
from math import gcd


def coefficients(a, d):
    """Return slope/intercept counters of all maximal gap-run lengths."""
    assert a >= 2 and 1 <= d < a and gcd(a, d) == 1
    tau = [0] * (a + 1)
    for t in range(1, a):
        tau[(d * t) % a] = t
    slopes, intercepts = Counter(), Counter()
    for ell in range(1, a):
        for r in range(1, a - ell + 1):
            low = min(tau[r:r + ell])
            high = max(tau[r - 1], tau[r + ell])
            if low > high:
                slopes[ell] += low - high
                intercepts[ell] += d * low // a - d * high // a
    return slopes, intercepts


def from_theorem(a, d, q):
    slopes, intercepts = coefficients(a, d)
    return Counter({ell: q * slopes[ell] + intercepts[ell]
                    for ell in range(1, a) if slopes[ell]})


def independent_coin_dp(a, b):
    """Membership is obtained by adding coins, not Apéry residues."""
    cutoff = a * b
    seen = bytearray(cutoff + 1)
    seen[0] = 1
    for n in range(cutoff + 1):
        if seen[n]:
            if n + a <= cutoff:
                seen[n + a] = 1
            if n + b <= cutoff:
                seen[n + b] = 1
    runs = Counter()
    n = 0
    while n <= cutoff:
        if seen[n]:
            n += 1
            continue
        start = n
        while n <= cutoff and not seen[n]:
            n += 1
        runs[n - start] += 1
    assert all(seen[n] for n in range(a * b - a - b + 1, cutoff + 1))
    return runs


def checks():
    total = 0
    for a in range(2, 50):
        for d in range(1, a):
            if gcd(a, d) != 1:
                continue
            slopes, intercepts = coefficients(a, d)
            e = pow(d, -1, a)
            assert sum(slopes.values()) == e * (a - e)
            assert sum(ell * count for ell, count in slopes.items()) == a * (a - 1) // 2
            assert sum(ell * count for ell, count in intercepts.items()) == (a - 1) * (d - 1) // 2
            assert slopes[a - 1] == 1 and intercepts[a - 1] == 0
            assert all(intercepts[ell] >= 0 for ell in slopes)
            assert sum(intercepts.values()) == sum(
                ((t + e) * d) // a - (t * d) // a for t in range(a - e))
            for q in range(1, 6):
                expected = from_theorem(a, d, q)
                actual = independent_coin_dp(a, q * a + d)
                assert expected == actual, (a, d, q, expected, actual)
                assert sum(ell * c for ell, c in expected.items()) == (
                    (a - 1) * (q * a + d - 1) // 2)
                assert expected[a - 1] == q
                total += 1
    assert from_theorem(8, 3, 1) == Counter({1: 12, 2: 6, 4: 1, 7: 1})
    assert from_theorem(8, 3, 2) == Counter({1: 21, 2: 10, 4: 2, 7: 2})
    print('PASS:', total, 'independent exact semigroup comparisons;')
    print('all coefficient sums, genus, support, and longest-run checks passed.')


if __name__ == '__main__':
    checks()
