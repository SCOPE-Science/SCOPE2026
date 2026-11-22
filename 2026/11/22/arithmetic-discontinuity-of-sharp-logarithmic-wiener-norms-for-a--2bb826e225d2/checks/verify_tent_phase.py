#!/usr/bin/env python3
"""Finite consistency checks for Fourier coefficients of two-slope tent phases.

This script does not test the infinite limit or certify novelty.
Only the Python standard library is required.
"""
import cmath
import math


def phase(alpha, x):
    a = 2 * math.pi * alpha
    return x if x <= a else alpha * (2 * math.pi - x) / (1 - alpha)


def direct_coefficient(alpha, n, k, intervals=16000):
    """Separate midpoint quadratures on the two affine arcs."""
    a = 2 * math.pi * alpha
    value = 0j
    for left, right in ((0.0, a), (a, 2 * math.pi)):
        dx = (right - left) / intervals
        for j in range(intervals):
            x = left + (j + .5) * dx
            value += cmath.exp(1j * (n * phase(alpha, x) - k * x)) * dx
    return value / (2 * math.pi)


def predicted_absolute_coefficient(alpha, n, k):
    L = n / (1 - alpha)
    t = n - k
    if t == 0:
        return alpha
    if abs(t - L) < 1e-11:
        return 1 - alpha
    return (L / math.pi) * abs(math.sin(math.pi * alpha * t)) / (abs(t) * abs(L-t))


def truncated_wiener(alpha, n, cutoff):
    return sum(predicted_absolute_coefficient(alpha, n, k)
               for k in range(-cutoff, cutoff + 1))


def run():
    comparisons = 0
    for alpha in (0.5, 1 / 3, 2 / 5, math.sqrt(2)-1):
        for n in (1, 2, 4):
            for k in (-7, -1, 0, 1, 2, 3, 4, 7):
                target = predicted_absolute_coefficient(alpha, n, k)
                observed = abs(direct_coefficient(alpha, n, k))
                assert abs(target-observed) < 2e-6, (alpha,n,k,target,observed)
                comparisons += 1
    for q in range(2, 15):
        for p in range(1, q):
            if math.gcd(p, q) != 1:
                continue
            s = sum(abs(math.sin(math.pi*p*j/q)) for j in range(q))/q
            exact = 1/math.tan(math.pi/(2*q))/q
            assert abs(s-exact) < 1e-12, (p,q,s,exact)
            comparisons += 1
    for n in (1, 2, 3, 8):
        exact = 1 + (4/math.pi)*sum(1/(2*j-1) for j in range(1,n+1))
        approx = truncated_wiener(0.5, n, 15000)
        assert 0 <= exact-approx < .002, (n,exact,approx)
        comparisons += 1
    print(f'PASS: {comparisons} direct-integral/root-mean/finite-norm checks')
    print('Infinite asymptotics require the analytic harmonic-mean proof.')


if __name__ == '__main__':
    run()
