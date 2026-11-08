#!/usr/bin/env python3
"""Exact finite checks for one-vacancy diversity-seeking biclique jump games.

Run: python3 verify.py
All arithmetic uses fractions; the infinite theorems require the separate proof.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def predicted(a, b, red):
    """Number of typed occupancy configurations, agents within a type unlabelled."""
    return (a * (choose(a - 1, red - b) + choose(a - 1, red))
            + b * (choose(b - 1, red - a) + choose(b - 1, red)))


def neighbors(a, b, index):
    return range(a, a + b) if index < a else range(a)


def utility(configuration, a, b, index):
    """0 vacant, 1 red, 2 blue; use occupied neighbor denominator."""
    occupied = [configuration[j] for j in neighbors(a, b, index)
                if configuration[j] != 0]
    if not occupied:
        return Fraction(0)
    different = sum(color != configuration[index] for color in occupied)
    return Fraction(different, len(occupied))


def is_nash(configuration, a, b):
    empty = configuration.index(0)
    for i, color in enumerate(configuration):
        if color == 0:
            continue
        moved = configuration.copy()
        moved[i] = 0
        moved[empty] = color
        if utility(moved, a, b, empty) > utility(configuration, a, b, i):
            return False
    return True


def welfare(configuration, a, b):
    return sum((utility(configuration, a, b, i)
                for i, color in enumerate(configuration) if color != 0),
               Fraction(0))


def configurations(a, b, red):
    n = a + b
    for empty in range(n):
        available = tuple(i for i in range(n) if i != empty)
        for red_vertices in combinations(available, red):
            red_set = set(red_vertices)
            yield [0 if i == empty else 1 if i in red_set else 2
                   for i in range(n)]


def direct_census(a, b, red):
    count = 0
    minimum = None
    maximum = Fraction(0)
    tested = 0
    for config in configurations(a, b, red):
        tested += 1
        w = welfare(config, a, b)
        if w > maximum:
            maximum = w
        if is_nash(config, a, b):
            count += 1
            minimum = w if minimum is None else min(minimum, w)
    return count, minimum, maximum, tested


def main():
    instances = 0
    assignments = 0
    for a in range(2, 6):
        for b in range(2, 6):
            for red in range(1, a + b - 1):
                actual, _, _, tested = direct_census(a, b, red)
                assert actual == predicted(a, b, red), (a, b, red, actual)
                assert actual > 0, (a, b, red)
                instances += 1
                assignments += tested
    assert assignments == 15136, assignments
    print(f'CENSUS_OK instances={instances} assignments={assignments}')

    poa_instances = 0
    for a in range(3, 7):
        count, minimum, maximum, _ = direct_census(a, 2, 2)
        assert count == a * (1 + choose(a - 1, 2))
        assert minimum == 2 + Fraction(4, a - 1)
        assert maximum == a + 1
        assert maximum / minimum == Fraction(a - 1, 2)
        poa_instances += 1
    print(f'POA_FAMILY_OK instances={poa_instances}')

    balanced_instances = 0
    for m in range(2, 6):
        count, minimum, maximum, _ = direct_census(m, m, m)
        assert count == 2 * m
        assert minimum == maximum == 2 * m - 1
        balanced_instances += 1
    print(f'BALANCED_FAMILY_OK instances={balanced_instances}')


if __name__ == '__main__':
    main()
