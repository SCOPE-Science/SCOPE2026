#!/usr/bin/env python3
"""Exact-integer reproducibility checks for binary radius-three ball convolution.
This finite computation corroborates, but does not replace, the all-length proof.
"""
from fractions import Fraction
from math import comb, isqrt


def walsh_transform(values):
    a = values.copy()
    n = len(a)
    step = 1
    while step < n:
        for i in range(0, n, 2 * step):
            for j in range(i, i + step):
                x, y = a[j], a[j + step]
                a[j], a[j + step] = x + y, x - y
        step *= 2
    return a


def eigenvalue(n, k):
    u = n - 2 * k + 1
    numerator = u * (u * u - (3 * n - 5))
    assert numerator % 6 == 0
    return numerator // 6


def krawtchouk(n, degree, x):
    return sum((-1)**j * comb(x, j) * comb(n - x, degree - j)
               for j in range(max(0, degree - (n-x)), min(degree, x) + 1))


def predicted_zeros(n):
    return {k for k in range(n + 1) if eigenvalue(n, k) == 0}


def generic(n):
    q = 3 * n - 5
    return n % 2 == 1 and isqrt(q)**2 != q


def expected_norm(n):
    m = (n - 1) // 2
    r = comb(n, m + 1)
    return 1 + Fraction(r, 2**m) - Fraction(r, 2**(2*m))


def check():
    compared = 0
    constants = 0
    for n in range(3, 16):
        M = 1 << n
        a = [int(x.bit_count() <= 3) for x in range(M)]
        actual = walsh_transform(a)
        for u, v in enumerate(actual):
            assert v == eigenvalue(n, u.bit_count()), (n, u, v)
        compared += M
        z = predicted_zeros(n)
        zcount = sum(comb(n, k) for k in z)
        assert zcount == sum(v == 0 for v in actual)
        if n & 1:
            assert (n + 1) // 2 in z
        if generic(n):
            assert z == {(n+1)//2}
            zeros_as_frequency_set = [int(v == 0) for v in actual]
            raw_idempotent = walsh_transform(zeros_as_frequency_set)
            numerator = sum(abs((M if x == 0 else 0) - v)
                            for x, v in enumerate(raw_idempotent))
            assert Fraction(numerator, M) == expected_norm(n), n
            constants += 1
    # Independent Krawtchouk generating-series and duality tests.
    identities = 0
    for n in range(3, 81):
        h = (n + 1) // 2
        for x in range(n + 1):
            assert comb(n, x) * krawtchouk(n, h, x) == comb(n, h) * krawtchouk(n, x, h)
            identities += 1
    print("HAMMING_RADIUS3_RANGE_PROJECTION_PASS", "walsh=", compared,
          "norms=", constants, "dualities=", identities)

if __name__ == '__main__':
    check()
