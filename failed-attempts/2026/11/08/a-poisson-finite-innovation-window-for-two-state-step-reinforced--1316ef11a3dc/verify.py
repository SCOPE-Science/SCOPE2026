#!/usr/bin/env python3
"""Independent exact finite recurrences for a binary reinforced walk and its forest.

Run: python3 verify.py
Only finite identities and numerical illustrations are checked; the limits in the
paper require their separate analytical proof.
"""
from collections import defaultdict, Counter
from fractions import Fraction
from math import log, exp


def binary_odd_count_distribution(n, alpha):
    """Number of 1 increments. Exact, based on the walk's one-step rule."""
    p = [Fraction(1, 2), Fraction(1, 2)]
    for m in range(1, n):
        next_p = [Fraction(0)] * (m + 2)
        for j, pr in enumerate(p):
            b = (1 - alpha) / 2 + alpha * Fraction(j, m)
            next_p[j] += pr * (1 - b)
            next_p[j + 1] += pr * b
        p = next_p
    return sum(p[::2]) - sum(p[1::2])


def forest_even_probability(n, alpha):
    """Exact forest evolution aggregated by component-size multiset."""
    states = {(1,): Fraction(1)}
    for m in range(1, n):
        nxt = defaultdict(Fraction)
        for sizes, weight in states.items():
            nxt[tuple(sorted(sizes + (1,)))] += weight * (1 - alpha)
            for size, mult in Counter(sizes).items():
                new_sizes = list(sizes)
                new_sizes.remove(size)
                new_sizes.append(size + 1)
                nxt[tuple(sorted(new_sizes))] += weight * alpha * Fraction(size * mult, m)
        assert sum(nxt.values()) == 1
        states = nxt
    return sum(v for sizes, v in states.items() if all(k % 2 == 0 for k in sizes))


def float_bias(n, lam):
    alpha = max(0.0, 1.0 - lam / n)
    p = [0.5, 0.5]
    for m in range(1, n):
        nxt = [0.0] * (m + 2)
        for j, value in enumerate(p):
            b = (1.0 - alpha) * 0.5 + alpha * j / m
            nxt[j] += value * (1.0 - b)
            nxt[j + 1] += value * b
        p = nxt
    return sum(p[::2]) - sum(p[1::2])


def main():
    assertions = 0
    for n in range(1, 13):
        for alpha in (Fraction(0), Fraction(1, 4), Fraction(1, 2),
                      Fraction(3, 4), Fraction(1)):
            bias = binary_odd_count_distribution(n, alpha)
            forest = forest_even_probability(n, alpha)
            assert bias == forest, (n, alpha, bias, forest)
            assertions += 1
            if n % 2:
                assert bias == 0
                assertions += 1
            else:
                assert 0 <= bias <= alpha ** (n // 2)
                assertions += 1
    for lam in (0.5, 1.0, 2.0, 4.0):
        for n in (200, 500, 1000):
            observed = float_bias(n, lam)
            predicted = exp(-lam * log(2))
            assert abs(observed - predicted) < 0.015, (lam, n, observed, predicted)
            assertions += 1
    # Exact telescoping harmonic identity for even-size probabilities.
    for m in (10, 100, 1000):
        even = sum(Fraction(1, (2*k) * (2*k+1)) for k in range(1,m+1))
        assert 0 < (1 - log(2)) - float(even) < 1/(2*m)
        assertions += 1
    print(f'{assertions} finite exact/numeric assertions passed')
    for lam in (0.5, 1.0, 2.0, 4.0):
        print(f'lambda={lam}: n=1000 bias={float_bias(1000,lam):.9f}; limit={2**(-lam):.9f}')

if __name__ == '__main__':
    main()
