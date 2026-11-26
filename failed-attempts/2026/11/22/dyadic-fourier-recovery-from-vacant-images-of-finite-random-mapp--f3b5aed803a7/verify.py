#!/usr/bin/env python3
"""Exact arithmetic checks for empty-image-set Walsh spectra.

Requires only the Python 3 standard library. No floating point calculations.
"""
from itertools import product
from math import comb, factorial


def v2(x):
    assert x != 0
    x = abs(x)
    return (x & -x).bit_length() - 1


def multiplier(n, k):
    return sum(comb(k, j) * (-2) ** j * (n-j) ** n
               for j in range(k + 1))


def stirling_second(n, r):
    table = [[0] * (n+1) for _ in range(n+1)]
    table[0][0] = 1
    for i in range(1, n+1):
        for j in range(1, i+1):
            table[i][j] = j * table[i-1][j] + table[i-1][j-1]
    return table[n][r]


def transform(values):
    out = list(values)
    step = 1
    while step < len(out):
        for start in range(0, len(out), 2*step):
            for j in range(step):
                a, b = out[start+j], out[start+j+step]
                out[start+j], out[start+j+step] = a+b, a-b
        step *= 2
    return out


def main():
    checks = 0
    def check(x):
        nonlocal checks
        if not x:
            raise AssertionError('exact check failed after %d assertions' % checks)
        checks += 1

    # Independent raw enumeration of the n^n maps and their exact vacant sets.
    for n in range(1, 7):
        weights = [0] * (1 << n)
        for images in product(range(n), repeat=n):
            vacant = (1 << n) - 1
            for image in images:
                vacant &= ~(1 << image)
            weights[vacant] += 1
        check(sum(weights) == n ** n)
        spectral = transform(weights)
        for mask in range(1 << n):
            k = mask.bit_count()
            check(spectral[mask] == multiplier(n, k))
            r = mask.bit_count()
            exact_weight = factorial(n-r) * stirling_second(n, n-r)
            check(weights[mask] == exact_weight)
        check(spectral[0] == n ** n)

    # Exact spectral and dyadic claims far beyond direct enumeration.
    for n in range(1, 121):
        vals = [multiplier(n, k) for k in range(n+1)]
        check(vals[0] == n ** n)
        if n % 2:
            for x in vals:
                check(x != 0 and x % 2 == 1)
        elif n == 2:
            check(vals == [4, 2, 0])
        else:
            for k in range(1, n+1):
                check(vals[k] != 0)
                check(v2(vals[k]) == 1 + v2(k))
                check((vals[k] // (2 ** (1 + v2(k)))) % 2 == 1)
            check(v2(vals[0]) == n * v2(n))
            det_val = n * v2(n) + sum(comb(n,k)*(1+v2(k)) for k in range(1,n+1))
            check(det_val > 0)
    print('PASS: %d exact assertions; exhaustive map enumeration n=1..6; all degree multipliers n=1..120.' % checks)


if __name__ == '__main__':
    main()
