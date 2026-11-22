#!/usr/bin/env python3
"""Exact finite verification for a theorem on interior Narayana-row content.

Only the Python standard library is required. Finite tests do not prove the
unbounded result; the number-theoretic proof is in RESULT.md.
"""
from math import comb, gcd, isqrt


def prime_power(m):
    """Return (prime base, exponent) or None for an integer >= 2."""
    if m < 2:
        return None
    d = 2
    while d * d <= m:
        if m % d == 0:
            t, exponent = m, 0
            while t % d == 0:
                t //= d
                exponent += 1
            return (d, exponent) if t == 1 else None
        d += 1 if d == 2 else 2
    return (m, 1)


def predicted_content(n):
    assert n >= 3
    e = prime_power(n)
    f = prime_power(n - 1)
    ans = e[0] if e is not None else 1
    if f is not None:
        q, b = f
        exponent = min(2, b) - int(q == 2 and b <= 2)
        ans *= q ** exponent
    return ans


def direct_content(n):
    acc = 0
    for k in range(2, n):
        x = comb(n, k) * comb(n, k - 1)
        assert x % n == 0
        acc = gcd(acc, x // n)
    return acc


def vp_factorial(n, p):
    out = 0
    while n:
        n //= p
        out += n
    return out


def vp_narayana(n, k, p):
    # Independent prime-adic path: Legendre's factorial valuation.
    a = vp_factorial(n, p)
    v = 2 * a - vp_factorial(k, p) - vp_factorial(n - k, p)
    j = k - 1
    v -= vp_factorial(j, p) + vp_factorial(n - j, p)
    t = n
    while t % p == 0:
        t //= p
        v -= 1
    return v


def prime_factors(n):
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out.append(n)
    return out


def verify():
    direct_checks = 0
    for n in range(3, 601):
        assert direct_content(n) == predicted_content(n), n
        direct_checks += 1

    # Compare all local valuation minima against an independently computed
    # factorial-valuation formula; include primes supported by n and n-1
    # and test unrelated primes, which must have minimum zero.
    valuation_checks = 0
    witnesses = 0
    for n in range(3, 701):
        expected = predicted_content(n)
        trial_primes = sorted(set(prime_factors(n * (n - 1))) | {2, 3, 5, 7, 11, 13})
        for p in trial_primes:
            pp = expected
            v_expected = 0
            while pp % p == 0:
                pp //= p
                v_expected += 1
            v_actual = min(vp_narayana(n, k, p) for k in range(2, n))
            assert v_actual == v_expected, (n, p, v_actual, v_expected)
            valuation_checks += 1
            witnesses += 1

    for n, expected in [
        (3, 3), (4, 6), (5, 10), (8, 14), (9, 12),
        (10, 9), (16, 2), (17, 68), (25, 5),
        (26, 25), (28, 9), (32, 62), (33, 4),
        (50, 49), (65, 4), (82, 9), (128, 254),
        (256, 2), (289, 17), (344, 49), (512, 2)
    ]:
        assert direct_content(n) == expected, n
    print('VERIFY_OK direct_rows=%d local_minima=%d special_cases=21' %
          (direct_checks, valuation_checks))

if __name__ == '__main__':
    verify()
