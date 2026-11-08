#!/usr/bin/env python3
"""Exact algebraic and periodic-quadrature checks of the critical cube Fourier residues."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb, pi, sin


def signed_mean(freq):
    """Square-sum of signed exponential coefficients, exact for integral freq."""
    k = len(freq)
    signed = defaultdict(int)
    for signs in product((-1, 1), repeat=k):
        signed[sum(x * s for x, s in zip(freq, signs))] += (-1) ** signs.count(-1)
    return Fraction(sum(v * v for v in signed.values()), 4 ** k)


def ternary_mean(freq):
    """Independent trinomial expansion (each sin^2 contributes 0,+2a,-2a)."""
    k = len(freq)
    weight = 0
    for eps in product((-1, 0, 1), repeat=k):
        if sum(a * e for a, e in zip(freq, eps)) == 0:
            count = sum(e != 0 for e in eps)
            weight += Fraction((-1) ** count, 2 ** count)
    return weight / (2 ** k)


def trig_mean(freq, samples=4096):
    total = 0.0
    for j in range(samples):
        r = (j + .5) * (2 * pi / samples)
        value = 1.0
        for a in freq:
            value *= sin(a * r) ** 2
        total += value
    return total / samples


def three_prediction(a, b, c):
    a, b, c = sorted((a, b, c))
    eq = (a == b) + (b == c) + (a == c)
    additive = int(c == a + b)
    return Fraction(1, 8) + Fraction(eq, 16) - Fraction(additive, 32)


def main():
    count = 0
    possible = set()
    for freq in product(range(1, 13), repeat=3):
        m1 = signed_mean(freq)
        m2 = ternary_mean(freq)
        assert m1 == m2 == three_prediction(*freq), (freq, m1, m2)
        possible.add(m1)
        assert m1 <= Fraction(5, 16)
        count += 1
    assert possible == {Fraction(3, 32), Fraction(1, 8), Fraction(5, 32), Fraction(3, 16), Fraction(5, 16)}
    for k in range(1, 7):
        maximum = Fraction(comb(2 * k, k), 4 ** k)
        for freq in product(range(1, 5), repeat=k):
            m = signed_mean(freq)
            assert m == ternary_mean(freq)
            assert 0 < m <= maximum
            assert (m == maximum) == (len(set(freq)) == 1)
            count += 1
    trials = ((1,), (1, 2), (1, 1), (1, 2, 3), (1, 1, 2), (1, 1, 1), (2, 3, 7), (1, 2, 3, 5), (2, 2, 3, 4), (1, 2, 4, 5, 7))
    for freq in trials:
        observed = trig_mean(freq)
        predicted = float(signed_mean(freq))
        assert abs(observed - predicted) < 5e-13, (freq, observed, predicted)
        count += 1
    print('FOURIER_CUBE_CRITICAL_RESIDUES_OK', count)

if __name__ == '__main__':
    main()
