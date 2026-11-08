#!/usr/bin/env python3
"""Reproduce exact finite checks for the occupancy frequency/collision theorem.

All finite comparisons are integer or rational. Enumeration is independent of
conditional-expectation formulas; the infinite theorem rests on its proof.
"""
from fractions import Fraction
from itertools import product
from math import comb, isqrt


def sign(x):
    return (x > 0) - (x < 0)


def qpoly(m, n, r):
    return m * m * r * r - m * (2 * n + m - 2) * r + n * (n - 1)


def derived_covariance(m, n, r):
    expectation = Fraction(m * comb(n, r) * (m - 1) ** (n - r), m ** n)
    e_given = Fraction(r * (r - 1), 2) + Fraction((n - r) * (n - r - 1), 2 * (m - 1))
    e_collision = Fraction(n * (n - 1), 2 * m)
    assert e_given - e_collision == Fraction(qpoly(m, n, r), 2 * m * (m - 1))
    return expectation * (e_given - e_collision)


def enumerated_covariances(m, n):
    denominator = m ** n
    frequency_totals = [0] * (n + 1)
    cross_totals = [0] * (n + 1)
    pair_total = 0
    for word in product(range(m), repeat=n):
        counts = [0] * m
        for letter in word:
            counts[letter] += 1
        fs = [0] * (n + 1)
        for c in counts:
            fs[c] += 1
        pairs = sum(c * (c - 1) // 2 for c in counts)
        pair_total += pairs
        for r in range(n + 1):
            frequency_totals[r] += fs[r]
            cross_totals[r] += fs[r] * pairs
    return [Fraction(c, denominator) - Fraction(f * pair_total, denominator ** 2)
            for c, f in zip(cross_totals, frequency_totals)]


def test():
    checked = 0
    for m in range(2, 6):
        for n in range(2, 8):
            if m ** n > 100000:
                continue
            actual = enumerated_covariances(m, n)
            for r in range(n + 1):
                assert derived_covariance(m, n, r) == actual[r], (m, n, r)
                checked += 1
                assert sign(actual[r]) == sign(qpoly(m, n, r))
                checked += 1
            assert sum(actual) == 0
            checked += 1
    for m in range(2, 41):
        for n in range(2, 91):
            sequence = [sign(qpoly(m, n, r)) for r in range(n + 1)]
            assert sequence[0] == 1 and sequence[-1] == 1
            checked += 1
            negative = [r for r in range(n + 1) if sequence[r] == -1]
            assert negative and negative == list(range(negative[0], negative[-1] + 1))
            checked += 1
            assert sign(qpoly(m, n, 1)) == sign(n - 2 * m)
            checked += 1
            d = (m - 2) ** 2 + 4 * n * (m - 1)
            s = isqrt(d)
            for r in range(n + 1):
                # The zero test uses an integer discriminant and root equation.
                root = s * s == d and (2 * m * r == 2 * n + m - 2 + s or
                                           2 * m * r == 2 * n + m - 2 - s)
                assert (qpoly(m, n, r) == 0) == root
                checked += 1
    for m in range(2, 21):
        for r in range(2, 13):
            vals = [sign(qpoly(m, n, r)) for n in range(r, 12 * m * r + 5)]
            # Every fixed r >= 2 has a reentrant positive-negative-positive phase.
            assert vals[0] == 1 and vals[-1] == 1 and -1 in vals
            checked += 1
            negatives = [i for i, v in enumerate(vals) if v == -1]
            assert negatives == list(range(negatives[0], negatives[-1] + 1))
            checked += 1
    for t in range(7, 100, 2):
        if t % 3 == 0:
            continue
        r = (t * t - 1) // 24
        assert 24 * r + 1 == t * t
        n1 = 3 * r + (1 - t) // 2
        n2 = 3 * r + (1 + t) // 2
        assert n1 >= r >= 2 and n2 > n1
        assert qpoly(3, n1, r) == qpoly(3, n2, r) == 0
        checked += 3
    print('PASS:', checked, 'exact integer/rational assertions')


if __name__ == '__main__':
    test()
