#!/usr/bin/env python3
"""Exact finite distribution certificate for Quicksort split-order boundary.

Run with Python 3.9+: python checker.py
No external packages or external data are required.
"""
from collections import Counter
from functools import lru_cache
from fractions import Fraction
from itertools import permutations
from math import comb, factorial


@lru_cache(maxsize=None)
def cost_counts(n):
    """Counts of permutations by total pivot comparisons."""
    if n <= 1:
        return Counter({0: 1})
    out = Counter()
    for left in range(n):
        right = n - 1 - left
        multiplicity = comb(n - 1, left)
        for a, count_a in cost_counts(left).items():
            for b, count_b in cost_counts(right).items():
                out[n - 1 + a + b] += multiplicity * count_a * count_b
    assert sum(out.values()) == factorial(n)
    return out


def conditional_counts(n, j):
    """Unnormalised distribution at given first-pivot zero-based rank."""
    assert 0 <= j < n
    out = Counter()
    for a, count_a in cost_counts(j).items():
        for b, count_b in cost_counts(n - 1 - j).items():
            out[n - 1 + a + b] += comb(n - 1, j) * count_a * count_b
    assert sum(out.values()) == factorial(n - 1)
    return out


def difference_certificate(n, j):
    """(first cost, all cumulative differences, last cost), including zeros."""
    a, b = conditional_counts(n, j), conditional_counts(n, j + 1)
    lo = min(min(a), min(b))
    hi = max(max(a), max(b))
    cumul = 0
    vals = []
    for t in range(lo, hi + 1):
        cumul += b.get(t, 0) - a.get(t, 0)
        vals.append(cumul)
    assert cumul == 0
    return lo, vals


# Every adjacent pair toward the center, and every nonzero cumulative gap.
# These are an independent, human-inspectable certificate of the finite cutoff.
EXPECTED = {
    (3, 0): (2, [2]),
    (4, 0): (4, [6, 4]),
    (5, 0): (6, [8, 24, 12, 8]),
    (5, 1): (6, [16]),
    (6, 0): (9, [60, 80, 80, 48, 24, 16]),
    (6, 1): (8, [40, 60, 40]),
    (7, 0): (12, [240, 432, 496, 264, 320, 160, 96, 48, 32]),
    (7, 1): (11, [360, 240, 288, 144, 96]),
    (7, 2): (10, [80, 40, 240]),
    (8, 0): (15, [560, 2520, 2720, 2800, 2208, 1680, 1344, 912,
                   640, 320, 192, 96, 64]),
    (8, 1): (14, [1680, 2464, 1512, 1568, 1120, 672, 336, 224]),
    (8, 2): (13, [840, 1120, 896, 1008, 672]),
}


def direct_insertion_cost(order):
    """Computes total internal path length by inserting permutation into a BST."""
    keys = [order[0]]
    left, right = [-1], [-1]
    comparisons = 0
    for value in order[1:]:
        parent = 0
        while True:
            comparisons += 1
            children = left if value < keys[parent] else right
            if children[parent] == -1:
                children[parent] = len(keys)
                break
            parent = children[parent]
        keys.append(value)
        left.append(-1)
        right.append(-1)
    return comparisons


def main():
    nchecks = 0
    for (n, j), (expected_start, expected_positive) in EXPECTED.items():
        first, vals = difference_certificate(n, j)
        actual = [(first + i, val) for i, val in enumerate(vals) if val]
        expected = [(expected_start + i, val) for i, val
                    in enumerate(expected_positive)]
        assert actual == expected, ((n, j), actual, expected)
        assert all(x >= 0 for x in vals), (n, j)
        nchecks += len(vals) + 2
    # The recurrence covers all adjacent comparisons for n<=8.
    assert {(n, j) for n in range(2, 9)
            for j in range((n - 1)//2)} == set(EXPECTED)

    n = 9
    rank3, rank4 = conditional_counts(n, 3), conditional_counts(n, 4)
    denominator = factorial(8)
    cdf3 = lambda t: Fraction(sum(c for v, c in rank3.items() if v <= t), denominator)
    cdf4 = lambda t: Fraction(sum(c for v, c in rank4.items() if v <= t), denominator)
    expected = {
        (3, 16): Fraction(1, 9), (4, 16): Fraction(1, 4),
        (3, 17): Fraction(19, 45), (4, 17): Fraction(5, 12)
    }
    for (j, t), value in expected.items():
        assert (cdf3(t) if j == 3 else cdf4(t)) == value
        nchecks += 1
    assert cdf3(16) < cdf4(16)
    assert cdf3(17) > cdf4(17)
    assert Fraction(sum(v*c for v, c in rank3.items()), denominator) == Fraction(271, 15)
    assert Fraction(sum(v*c for v, c in rank4.items()), denominator) == Fraction(53, 3)
    nchecks += 4

    # Entire n=9 comparison landscape, for context (not needed for minimality proof).
    assert all(all(z >= 0 for z in difference_certificate(9, j)[1])
               for j in (0, 1, 2))
    nchecks += 3

    # Independent realization: exhaust all nine-key insertion orders with first
    # ranks 4 and 5. This does not share the recurrence's tree decomposition.
    direct = {3: Counter(), 4: Counter()}
    for permutation in permutations(range(1, 10)):
        j = permutation[0] - 1
        if j in direct:
            direct[j][direct_insertion_cost(permutation)] += 1
    assert direct[3] == rank3
    assert direct[4] == rank4
    nchecks += 2
    print('PASS: first failure at n=9, zero-based ranks 3 versus 4')
    print('cdf threshold 16:', str(cdf3(16)), str(cdf4(16)))
    print('cdf threshold 17:', str(cdf3(17)), str(cdf4(17)))
    print('conditional means: 271/15 and 53/3; exact checks:', nchecks)
    print('independent insertion permutations checked:', 2*factorial(8))


if __name__ == '__main__':
    main()
