#!/usr/bin/env python3
"""Finite quadrature diagnostics for the Gaussian variation formula.

The checks are diagnostics only, not a proof of an asymptotic theorem.
No third-party packages are required.
"""
import math

def phi(x):
    return (1 + math.erf(x / math.sqrt(2))) / 2

def center_scale(m, alpha):
    u = (2 * (m + 1) / alpha) ** (1 / (alpha - 1))
    s = (alpha * (alpha - 1) * u ** (alpha - 2)) ** (-0.5)
    return u, s

def distance(m, alpha, q, size=24000):
    a, sa = center_scale(m, alpha)
    b, sb = center_scale(m + q, alpha)
    low = max(0., min(a - 16 * sa, b - 16 * sb))
    high = max(a + 16 * sa, b + 16 * sb)
    h = (high - low) / size
    points = [low + k * h for k in range(size + 1)]
    densities = []
    for n in [m, m + q]:
        u, s = center_scale(n, alpha)
        peak = 2 * (n + 1) * u - u ** alpha
        values = [math.exp(2 * (n + 1) * x - x ** alpha - peak) for x in points]
        integral = h * (sum(values) - (values[0] + values[-1]) / 2)
        densities.append([v / integral for v in values])
    dist = h * (sum(abs(x - y) for x, y in zip(*densities))
                - (abs(densities[0][0] - densities[1][0])
                   + abs(densities[0][-1] - densities[1][-1])) / 2)
    eta = q * sa
    return dist, 4 * phi(eta) - 2

if __name__ == '__main__':
    tests = [(1.5, 30, 1), (1.5, 30, 2),
             (2., 60, 1), (2., 60, 2),
             (3., 100000, 1), (3., 100000, 6),
             (3., 100000, 20), (3., 100000, 40),
             (4., 100000, 1), (4., 100000, 7),
             (4., 100000, 15), (4., 100000, 30)]
    for alpha, m, q in tests:
        actual, predicted = distance(m, alpha, q)
        difference = abs(actual - predicted)
        assert difference < .001, (alpha, m, q, actual, predicted)
        print(f'alpha={alpha:g} m={m} q={q} '
              f'L1={actual:.6f} asymptotic={predicted:.6f} '
              f'abs_error={difference:.6f}')
    print(f'{len(tests)} finite diagnostics passed')
