#!/usr/bin/env python3
"""Finite numerical diagnostics for a proved finite-height tetration crossover.

All analytic limiting claims require the proof in RESULT.md. This script uses
only the Python standard library and checks direct recursions and sample values.
"""
import math

E = math.e

def fixed_z(t):
    z = 1.0
    for _ in range(50):
        f = z * math.exp(z) - t
        z -= f / (math.exp(z) * (1.0 + z))
        if abs(f) < 2e-15:
            break
    return z

def odd_tower(t, k):
    z = t * math.exp(-t)
    for _ in range(k):
        z = t * math.exp(-t * math.exp(-z))
    return z / t

def H(a):
    if a == 0.0:
        return math.sqrt(3.0) / E
    return math.sqrt(6.0 * a / (-math.expm1(-2.0 * a))) / E

def two_cycle_t(s):
    q = s / math.sinh(s)
    return q * math.exp(s + q * math.exp(-s))

def limit_cdf(t):
    if t <= E:
        return fixed_z(t) / t
    lo, hi = 0.0, 1.0
    while two_cycle_t(hi) < t:
        hi *= 2.0
    for _ in range(85):
        s = (lo + hi) / 2.0
        if two_cycle_t(s) < t:
            lo = s
        else:
            hi = s
    s = (lo + hi) / 2.0
    q = s / math.sinh(s)
    return q * math.exp(-s) / t

def close(actual, expected, tolerance):
    if not (math.isfinite(actual) and abs(actual - expected) < tolerance):
        raise AssertionError((actual, expected, tolerance))


def main():
    tests = 0
    for t in (2.4, E, 2.9):
        w = fixed_z(t)
        for u in (-0.4, -0.2, -0.07, 0.04, 0.2):
            g = lambda z: t * math.exp(-z)
            T = w * math.expm1(w * (-math.expm1(-u)))
            close(T, g(g(w + u)) - w, 5e-14)
            tests += 1
        z = t * math.exp(-t)
        last = z
        for _ in range(80):
            z = t * math.exp(-t * math.exp(-z))
            if not z > last:
                raise AssertionError('odd iterates are not increasing')
            last = z
            tests += 1
    for a in (-3.0, -1.0, 0.0, 0.5, 1.0, 3.0):
        target = H(a)
        t = E * (1.0 + a / 20000.0)
        val = math.sqrt(20000.0) * (1.0 / E - odd_tower(t, 20000))
        close(val, target, 0.04)
        tests += 1
        predicted_difference = target - math.sqrt(6.0 * max(a, 0.0)) / E
        observed_difference = math.sqrt(20000.0) * (limit_cdf(t) - odd_tower(t, 20000))
        close(observed_difference, predicted_difference, 0.04)
        tests += 1
        print(f'a={a:5.1f}, finite_scaled={val:.9f}, prediction={target:.9f}, '
              f'error_scaled={observed_difference:.9f}')
    for a, b in ((-3., -1.), (-1., 0.), (0., 0.5), (0.5, 3.)):
        k = 20000
        observed = math.sqrt(k) * (odd_tower(E * (1 + a/k), k) - odd_tower(E * (1 + b/k), k))
        close(observed, H(b) - H(a), 0.06)
        tests += 1
    for s in (0.02, 0.04, 0.08, 0.12):
        t = two_cycle_t(s)
        q = s / math.sinh(s)
        lower, upper = q * math.exp(-s), q * math.exp(s)
        close(t * math.exp(-lower), upper, 2e-14)
        close(t * math.exp(-upper), lower, 2e-14)
        tests += 2
    print(f'PASS: {tests} finite diagnostics; analytic proof is in RESULT.md')

if __name__ == '__main__':
    main()
