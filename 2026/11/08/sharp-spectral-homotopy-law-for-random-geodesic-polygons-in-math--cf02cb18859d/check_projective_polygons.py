#!/usr/bin/env python3
"""Reproduce the random real-projective geodesic-polygon parity law.

Analytic proof, scope, and convergence bounds are in RESULT.md.
This script provides independent spherical Monte Carlo and spectral-series checks.
"""
import math
import random


def lambda_one(d):
    return math.exp(math.lgamma(d / 2) - 0.5 * math.log(math.pi) - math.lgamma((d + 1) / 2))


def harmonic_dimension(d, degree):
    return (2 * degree + d - 2) * math.comb(degree + d - 3, d - 3) // (d - 2)


def polygon_probability(d, m, cutoff=1600):
    if d < 3 or m < 3:
        raise ValueError('d and m must be at least three')
    eig = lambda_one(d)
    weighted_trace = d * eig ** m
    for j in range(1, cutoff + 1):
        eig *= -(2 * j - 1) / (d + 2 * j - 1)
        weighted_trace += harmonic_dimension(d, 2 * j + 1) * eig ** m
    return (1 - weighted_trace) / 2


def triangle_probability(d, n=50000):
    h = math.pi / (2 * n)
    denominator = numerator = 0.0
    for k in range(n):
        theta = (k + 0.5) * h
        weight = math.sin(theta) ** (d - 2)
        numerator += theta * weight
        denominator += weight
    return numerator / (math.pi * denominator)


def direct_sampling(d, m, trials, rng):
    count = 0
    for _ in range(trials):
        pts = [[rng.gauss(0.0, 1.0) for _ in range(d)] for _ in range(m)]
        parity = 1
        for j in range(m):
            x, y = pts[j], pts[(j + 1) % m]
            product = sum(a * b for a, b in zip(x, y))
            if product < 0.0:
                parity = -parity
        if parity < 0:
            count += 1
    return count / trials


def main():
    assert abs(lambda_one(3) - 0.5) < 1e-14
    assert abs(lambda_one(4) - 4/(3*math.pi)) < 1e-14
    assert harmonic_dimension(3, 7) == 15
    assert harmonic_dimension(4, 5) == 36
    for d in range(3, 11):
        val = polygon_probability(d, 3)
        independent = triangle_probability(d)
        assert abs(val - independent) < 5e-9, (d, val, independent)
    for d in (3, 4, 5, 8):
        first = lambda_one(d)
        for m in (4, 6, 12):
            p = polygon_probability(d, m)
            remainder = abs(p - (0.5 - 0.5 * d * first ** m))
            second = first / (d + 1)
            bound = 0.5 * (1-d * first * first) * second ** (m - 2)
            assert remainder < bound * (1+1e-8)+1e-14, (d, m, remainder, bound)
    rng = random.Random(14921)
    total = 0
    for d, m, n in ((3,3,55000),(3,4,55000),(3,5,55000),(4,4,55000),(5,6,55000),(8,8,55000)):
        measured = direct_sampling(d, m, n, rng)
        exact = polygon_probability(d, m)
        sigma = math.sqrt(exact*(1-exact)/n)
        assert abs(measured-exact) < 6*sigma, (d,m,exact,measured,sigma)
        print(f'd={d}, m={m}, exact={exact:.10f}, sampled={measured:.10f}, sigma={sigma:.5f}')
        total += n
    print('PROJECTIVE_POLYGON_SPECTRAL_PARITY_OK', total)


if __name__ == '__main__':
    main()
