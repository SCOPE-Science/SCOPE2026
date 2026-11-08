#!/usr/bin/env python3
"""Reproduce exact threefold convolution counts for dyadic parabolae.

Standard-library-only finite checks. The mathematical argument for arbitrary
exponents is separate from and stronger than these finite computations.
"""
from collections import Counter
import cmath
from math import pi


def prediction(k, s, t):
    n = 1 << k
    h = (s * pow(3, -1, n)) % n
    delta = (t - 3 * h * h) % n
    if delta & 1:
        return 0
    m = k - 1
    if not m:
        return 4
    c = delta // 2
    if c == 0:
        return (1 if k % 2 == 0 else 2) * n
    valuation = (c & -c).bit_length() - 1
    return 3 * n if valuation % 2 == 0 else 0


def predicted_hist(k):
    n = 1 << k
    if k % 2 == 0:
        return {0: 2 * n * (n - 1) // 3, n: n, 3 * n: n * (n - 1) // 3}
    return {0: n * (2 * n - 1) // 3, 2 * n: n, 3 * n: n * (n - 2) // 3}


def exhaustive(k):
    n = 1 << k
    counts = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            for z in range(n):
                s = (x + y + z) % n
                t = (x*x + y*y + z*z) % n
                counts[s][t] += 1
    observed = Counter(value for row in counts for value in row)
    expected = Counter({a:b for a,b in predicted_hist(k).items() if b})
    assert observed == expected, (k, observed, expected)
    for s in range(n):
        for t in range(n):
            assert counts[s][t] == prediction(k, s, t), (k, s, t, counts[s][t])
    assert sum(observed.values()) == n*n
    assert sum(value * mult for value,mult in observed.items()) == n**3
    assert sum(value*value * mult for value,mult in observed.items()) == n**3 * (3*n-2)
    return dict(sorted(observed.items()))


def direct_fourier_check(k):
    n = 1 << k
    omega = [cmath.exp(2j*pi*j/n) for j in range(n)]
    total = 0.
    for a in range(n):
        for b in range(n):
            s = sum(omega[(a*x+b*x*x)%n] for x in range(n))
            total += abs(s)**6
    numerical = total / (n*n)
    exact = n**3 * (3*n-2)
    assert abs(numerical-exact)/exact < 1e-9, (k,numerical,exact)


if __name__ == '__main__':
    for k in range(1,8):
        hist = exhaustive(k)
        print(f'k={k}: {hist}')
    for k in range(1,7):
        direct_fourier_check(k)
    print('DYADIC_PARABOLA_TRIPLE_CONVOLUTION_CHECK_PASS')
