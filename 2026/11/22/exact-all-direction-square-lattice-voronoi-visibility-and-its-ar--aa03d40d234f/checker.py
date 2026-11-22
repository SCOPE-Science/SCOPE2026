#!/usr/bin/env python3
"""Reproduce exact, finite checks for square-cell visibility arithmetic.

Requires only the Python standard library. These finite checks supplement,
but do not replace, the analytic proof of the infinite-radius law.
"""
from fractions import Fraction
from itertools import permutations
from math import gcd


def intermediate_count(a, b):
    a, b = abs(a), abs(b)
    if a + b == 0:
        raise ValueError('Distinct sites required')
    if not (a and b):
        return a + b - 1
    g = gcd(a, b)
    common = g if (a // g) % 2 and (b // g) % 2 else 0
    return a + b - common - 1


def independent_intermediate_count(a, b):
    a, b = abs(a), abs(b)
    if a + b == 0:
        raise ValueError('Distinct sites required')
    times = set()
    for k in range(a):
        times.add(Fraction(2 * k + 1, 2 * a))
    for k in range(b):
        times.add(Fraction(2 * k + 1, 2 * b))
    ordered = [Fraction(0)] + sorted(times) + [Fraction(1)]
    centers = []
    for l, r in zip(ordered[:-1], ordered[1:]):
        mid = (l + r) / 2
        x, y = mid * a, mid * b
        # Exact closest integer in each coordinate (no tie at these midpoints).
        u, v = (x.numerator * 2 + x.denominator) // (2 * x.denominator), (y.numerator * 2 + y.denominator) // (2 * y.denominator)
        assert 0 <= u <= a and 0 <= v <= b and u + v <= a + b
        centers.append((u, v))
    assert len(centers) == len(set(centers))
    assert centers[0] == (0, 0) and centers[-1] == (a, b)
    return len(centers) - 2


def direct_expected_degree(R):
    total = Fraction(0)
    for a in range(-R, R + 1):
        for b in range(-R, R + 1):
            if 0 < abs(a) + abs(b) <= R:
                m = intermediate_count(a, b)
                total += Fraction(2, (m + 1) * (m + 2))
    return total


def totient_expected_degree(R):
    phi = list(range(R + 1))
    for prime in range(2, R + 1):
        if phi[prime] == prime:
            for j in range(prime, R + 1, prime):
                phi[j] -= phi[j] // prime
    base = 8 * sum((Fraction(1, j + 1) for j in range(1, R + 1)), Fraction())
    correction = Fraction()
    for k in range(1, R // 2 + 1):
        for g in range(1, R // (2 * k) + 1):
            A, B = g * (2 * k - 1), 2 * k * g
            correction += phi[2 * k] * (Fraction(1, A * (A + 1)) - Fraction(1, B * (B + 1)))
    return base + 8 * correction


def test_rank_probability(M):
    valid = 0
    for rank_assignment in permutations(range(M + 2)):
        if min(rank_assignment[0], rank_assignment[1]) > max(rank_assignment[2:], default=-1):
            valid += 1
    from math import factorial
    return Fraction(valid, factorial(M + 2))


def main():
    crossings = 0
    for a in range(26):
        for b in range(26):
            if a + b:
                assert intermediate_count(a, b) == independent_intermediate_count(a, b), (a, b)
                crossings += 1
    for M in range(7):
        assert test_rank_probability(M) == Fraction(2, (M + 1) * (M + 2))
    results = []
    for R in range(1, 17):
        direct = direct_expected_degree(R)
        arithmetic = totient_expected_degree(R)
        assert direct == arithmetic, (R, direct, arithmetic)
        results.append((R, direct))
    assert results[0] == (1, Fraction(4))
    assert results[1] == (2, Fraction(28, 3))
    assert results[2] == (3, Fraction(34, 3))
    assert results[3] == (4, Fraction(72, 5))
    print('PASS: %d independent exact cell-crossing cases' % crossings)
    print('PASS: rank probabilities for M=0,...,6 by permutation enumeration')
    print('PASS: all exact finite-degree identities for R=1,...,16')
    print('Samples:', [(R, str(x)) for R, x in results[:4]])
    print('Note: these finite tests do not establish the infinite-radius asymptotic.')


if __name__ == '__main__':
    main()
