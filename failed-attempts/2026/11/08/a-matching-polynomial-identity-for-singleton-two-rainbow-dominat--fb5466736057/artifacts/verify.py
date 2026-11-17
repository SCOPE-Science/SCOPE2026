#!/usr/bin/env python3
"""Exact finite checks for the singleton two-color domination enumerator of cycles.

Run with ``python3 artifacts/verify.py`` from the extracted package root.
The all-order claim rests on the accompanying combinatorial proof, not these checks.
"""

from collections import Counter, defaultdict
from itertools import product
from math import comb


def coefficient_formula(n):
    assert n >= 3
    result = Counter()
    for k in range((n - 1) // 2 + 1):
        numerator = n * comb(n - k, k) * 2 ** (n - 2 * k)
        assert numerator % (n - k) == 0
        result[n - k] = numerator // (n - k)
    if n % 4 == 0:
        result[n // 2] = 4
    return result


def direct_enumeration(n):
    result = Counter()
    for labels in product((0, 1, 2), repeat=n):
        if all(
            labels[j] != 0
            or {labels[(j - 1) % n], labels[(j + 1) % n]} == {1, 2}
            for j in range(n)
        ):
            result[sum(value != 0 for value in labels)] += 1
    return result


def transition_enumeration(n):
    """The independently constructed nine-state closed-walk enumerator."""
    states = list(product(range(3), repeat=2))
    result = Counter()
    for start in states:
        frontier = {(start, 0): 1}
        for _ in range(n):
            upcoming = defaultdict(int)
            for ((a, b), weight), ways in frontier.items():
                for c in range(3):
                    if b != 0 or {a, c} == {1, 2}:
                        upcoming[((b, c), weight + (c != 0))] += ways
            frontier = upcoming
        for (state, weight), ways in frontier.items():
            if state == start:
                result[weight] += ways
    return result


def minimum_count(n):
    if n % 4 == 0:
        return n // 2, 4
    if n % 2:
        return (n + 1) // 2, 2 * n
    return n // 2 + 1, n * n


def lucas_polynomial(n):
    """Trace polynomial for a cyclic monomer-dimer model, using a recurrence."""
    p0 = [2]
    p1 = [0, 2]
    for _ in range(2, n + 1):
        out = [0] * (max(len(p0) + 1, len(p1) + 1))
        for degree, coefficient in enumerate(p1):
            out[degree + 1] += 2 * coefficient
        for degree, coefficient in enumerate(p0):
            out[degree + 1] += coefficient
        while len(out) > 1 and out[-1] == 0:
            out.pop()
        p0, p1 = p1, out
    return p1 if n else p0


def main():
    for n in range(3, 13):
        brute = direct_enumeration(n)
        formula = coefficient_formula(n)
        assert brute == formula, (n, brute, formula)
        minimum = min(brute)
        assert (minimum, brute[minimum]) == minimum_count(n)
        print('BRUTE_CYCLE_OK', n, sum(brute.values()), minimum, brute[minimum])
    for n in range(3, 61):
        assert transition_enumeration(n) == coefficient_formula(n), n
    print('INDEPENDENT_NINE_STATE_TRANSFER_OK n=3..60')
    for n in range(3, 151):
        lucas = lucas_polynomial(n)
        if n % 2 == 0:
            lucas[n // 2] += 2 * (-1) ** (n // 2)
        coefficients = coefficient_formula(n)
        assert all(lucas[i] == coefficients.get(i, 0) for i in range(len(lucas)))
        assert (min(coefficients), coefficients[min(coefficients)]) == minimum_count(n)
    print('LUCAS_RECURRENCE_AND_MINIMUM_COUNTS_OK n=3..150')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
