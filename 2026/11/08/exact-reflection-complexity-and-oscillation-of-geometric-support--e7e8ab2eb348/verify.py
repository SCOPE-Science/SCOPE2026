#!/usr/bin/env python3
"""Finite, independent diagnostics for geometric-support reflection classes.

No packages other than the Python standard library are required.
"""
from math import isclose


def expected(base, n):
    assert base >= 2 and n >= 0
    if n == 0:
        return 1
    single = (n + 1) // 2
    if n < base:
        return 1 + single
    if n <= base * (base - 1):
        return 1 + single + (1 if n <= base + 1 else 2)
    k = 1
    while n > (base - 1) * base ** (k + 1):
        k += 1
    s = base ** k
    h = base ** (k - 1)
    m = n - 1 - (base - 1) * s
    a = s - h - 1
    u = min(h + m + 2, s + 1)
    p = max(0, min((m + 1) // 2, a - m // 2))
    return 1 + single + u - p - int(base == 2 and n == 3)


def brute(base, n):
    """Build a sufficient finite prefix, then independently enumerate factors."""
    if n == 0:
        return 1
    # An isolated power p supplies every single-1 offset and an all-zero factor.
    # All multi-1 factors begin before the first power whose gap is >= n,
    # hence before n. The prefix ending at p+n includes them all.
    p = 1
    while p - p // base <= n:
        p *= base
    span = p + n + 1
    symbols = bytearray(span)
    v = 1
    while v < span:
        symbols[v] = 1
        v *= base
    factors = set()
    for i in range(span - n + 1):
        f = bytes(symbols[i:i + n])
        factors.add(min(f, f[::-1]))
    return len(factors)


def asymptotic(base, peak=False):
    lo = .5 + 1 / (base * (base - 1))
    hi = .5 + base / ((base - 1) * (base + 2))
    s = base ** 8
    m = 2 * (s - s // base) if peak else 0
    n = (base - 1) * s + 1 + m
    ratio = expected(base, n) / n
    target = hi if peak else lo
    assert abs(ratio - target) < 10 / s, (base, ratio, target)
    return ratio


def main():
    tests = 0
    assert expected(2, 0) == 1
    for base in range(2, 11):
        for n in range(1, 151):
            got = brute(base, n)
            want = expected(base, n)
            assert got == want, (base, n, got, want)
            tests += 1
        asymptotic(base, False)
        asymptotic(base, True)
        tests += 2
    for n in range(4, 100001):
        assert expected(2, n) == 2 * ((n + 1) // 2) + 2, n
        tests += 1
    print('VERIFY_OK', 'brute_cases=1350', 'base2_formula_cases=99997', 'asymptotic_cases=18', 'total_checks=', tests)


if __name__ == '__main__':
    main()
