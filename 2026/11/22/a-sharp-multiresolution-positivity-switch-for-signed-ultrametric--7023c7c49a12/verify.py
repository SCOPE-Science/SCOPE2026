#!/usr/bin/env python3
"""Independent finite-character checks for signed p-adic exponential kernels.

Run: python3 verify.py. Uses only the Python standard library.
The analytical infinite-conductor and uniqueness arguments are in RESULT.md.
"""
import cmath
import math


def mean_kernel(p, a):
    return (1.0 - 1.0 / p) * sum(
        p ** (-j) * math.exp(-a * p ** (-j)) for j in range(220)
    )


def conductor_coefficient(p, a, n):
    assert n >= 1
    return sum(
        p ** (-j) * math.exp(-a * p ** (-j))
        * (-math.expm1(-a * (p - 1) * p ** (-j)))
        for j in range(n, n + 220)
    )


def valuation(x, p):
    k = 0
    while x and x % p == 0:
        x //= p
        k += 1
    return k


def averaged_profile(p, N, a, x):
    if x == 0:
        return mean_kernel(p, a * p ** (-N))
    return math.exp(-a * p ** (-valuation(x, p)))


def finite_fourier(p, N, a, k):
    size = p ** N
    return sum(
        averaged_profile(p, N, a, x)
        * cmath.exp(-2j * math.pi * k * x / size)
        for x in range(size)
    ) / size


count = 0
for p in [2, 3, 5]:
    for a, b in [(0.5, 1.0), (1.0, 2.0), (3.0, 1.0), (8.0, 0.1)]:
        m_a = mean_kernel(p, a)
        m_b = mean_kernel(p, b)
        r0 = m_a / m_b
        ratios = [conductor_coefficient(p, a, n) / conductor_coefficient(p, b, n)
                  for n in range(1, 10)]
        if a > b:
            assert r0 < ratios[0]
            assert all(x < y for x, y in zip(ratios, ratios[1:]))
            assert ratios[-1] < a / b
            threshold = r0
        else:
            assert r0 > ratios[0]
            assert all(x > y for x, y in zip(ratios, ratios[1:]))
            assert ratios[-1] > a / b
            threshold = a / b
        count += 22
        for N in [1, 2, 3]:
            size = p ** N
            for k in range(size):
                n = 0 if k == 0 else N - valuation(k, p)
                direct = finite_fourier(p, N, a, k)
                exact = m_a if n == 0 else conductor_coefficient(p, a, n)
                assert abs(direct - exact) < 5e-12, (p, N, a, k, direct, exact)
                count += 1
            lamb_N = r0 if a > b else ratios[N - 1]
            # The cutoff eigenvalue is zero, and all other eigenvalues nonnegative.
            for n in range(N + 1):
                da = m_a if n == 0 else conductor_coefficient(p, a, n)
                db = m_b if n == 0 else conductor_coefficient(p, b, n)
                assert da - lamb_N * db >= -2e-13
                if (a > b and n == 0) or (a < b and n == N):
                    assert abs(da - lamb_N * db) < 2e-13
                count += 1

# Verify the first-order geometric finite-resolution asymptotic.
for p in [2, 3, 5]:
    for a, b in [(0.4, 1.3), (1.0, 3.0)]:
        gamma = (p + 1) * (1 - p ** (-2)) / (2 * (1 - p ** (-3)))
        predicted = (a / b) * (b - a) * gamma
        for N in [7, 8, 9]:
            rN = conductor_coefficient(p, a, N) / conductor_coefficient(p, b, N)
            observed = (rN - a / b) * p ** N
            assert abs(observed - predicted) / predicted < 0.05
            count += 1

print(f"PASS: {count} spectral, monotonicity and asymptotic assertions")
