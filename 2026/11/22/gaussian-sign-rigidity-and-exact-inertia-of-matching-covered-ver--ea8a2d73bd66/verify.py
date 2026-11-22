#!/usr/bin/env python3
"""Exact finite checks for signed matching-covered-vertex Fourier transforms.

Run: python3 verify.py
No packages outside Python's standard library are required.
"""
from functools import lru_cache
from math import comb


def covered_masks_by_matching(n):
    """Return the exact multiplicity vector by explicit matching recursion."""
    result = [0] * (1 << n)

    def rec(available, covered):
        if not available:
            result[covered] += 1
            return
        bit = available & -available
        rest = available ^ bit
        rec(rest, covered)
        w = rest
        while w:
            bit2 = w & -w
            rec(rest ^ bit2, covered | bit | bit2)
            w ^= bit2

    rec((1 << n) - 1, 0)
    return result


def walsh(values):
    a = values[:]
    step = 1
    while step < len(a):
        for start in range(0, len(a), step * 2):
            for j in range(start, start + step):
                u, v = a[j], a[j + step]
                a[j], a[j + step] = u + v, u - v
        step *= 2
    return a


def elementary_sign_transform(n, k):
    """Independent weighted-subset sum, using integer binomial arithmetic."""
    p = n - k
    total = 0
    double_factorial = 1
    for j in range(n // 2 + 1):
        if j:
            double_factorial *= 2 * j - 1
        a = sum((-1) ** t * comb(k, t) * comb(p, 2*j-t)
                for t in range(max(0, 2*j-p), min(k, 2*j)+1))
        total += double_factorial * a
    return total


def centered_chisquare_moments(n):
    """Moments of Z**2-1 from the exact cumulants, no integration."""
    moments = [0] * (n + 1)
    moments[0] = 1
    for m in range(1, n + 1):
        moments[m] = sum(comb(m-1, r-1) * (2**(r-1)) *
                         __import__('math').factorial(r-1) * moments[m-r]
                         for r in range(2, m+1))
    return moments


def positive_formula(n, k, moment):
    q = min(k, n-k)
    d = n - 2*q
    magnitude = sum(comb(d, 2*r) *
                    sum(comb(r, j) * moment[q+j] for j in range(r+1))
                    for r in range(d//2+1))
    return (-1)**q * magnitude


def predicted_sign(n, k):
    q = min(k, n-k)
    if (n, q) in ((2, 1), (3, 1)):
        return 0
    return 1 if q % 2 == 0 else -1


def check():
    tests = 0
    moment = centered_chisquare_moments(50)
    for q in range(2, 51):
        assert moment[q] > 0
        tests += 1
    assert moment[0] == 1 and moment[1] == 0
    tests += 2

    for n in range(0, 51):
        for k in range(n+1):
            value = elementary_sign_transform(n, k)
            assert value == positive_formula(n, k, moment), (n,k,value)
            assert (value > 0) - (value < 0) == predicted_sign(n, k)
            tests += 2
        if n >= 4:
            plus = sum(comb(n,k) for k in range(n+1) if predicted_sign(n,k) == 1)
            minus = (1 << n) - plus
            if n % 2 == 0:
                assert plus == minus == 2 ** (n-1)
            else:
                m = (n-1) // 2
                assert plus == 2**(n-1) + (-1)**m * comb(2*m,m)
                assert minus == 2**(n-1) - (-1)**m * comb(2*m,m)
            tests += 2

    for n in range(0, 13):
        counts = covered_masks_by_matching(n)
        transform = walsh(counts)
        assert sum(counts) == elementary_sign_transform(n, 0)
        tests += 1
        for freq, value in enumerate(transform):
            k = freq.bit_count()
            expected = elementary_sign_transform(n, k)
            assert value == expected, (n, freq, value, expected)
            tests += 1
        assert sum(v*v for v in transform) == (1 << n)*sum(v*v for v in counts)
        tests += 1

    print(f'PASS: {tests} exact assertions; all frequencies enumerated through n=12; binomial and centered-moment checks through n=50')

if __name__ == '__main__':
    check()
