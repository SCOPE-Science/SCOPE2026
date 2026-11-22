#!/usr/bin/env python3
"""Standalone finite checks for the power bounded-density shift theorem.

These calculations check finite examples; the all-length theorem is proved
by the analytic packing argument in RESULT.md.
"""
from fractions import Fraction
from math import comb
from random import Random


def ceil_power(k, numerator, denominator):
    """Exact ceiling of k**(numerator/denominator) for integers."""
    target = k ** numerator
    low, high = 0, k + 1
    while high - low > 1:
        mid = (low + high) // 2
        if mid ** denominator >= target:
            high = mid
        else:
            low = mid
    return high


def admissible_positions(pos, numerator, denominator):
    # It suffices to inspect shortest intervals spanning consecutive markers.
    for i, left in enumerate(pos):
        for j in range(i, len(pos)):
            length = pos[j] - left + 1
            if j - i + 1 > ceil_power(length, numerator, denominator):
                return False
    return True


def brute_word_count(n, numerator, denominator):
    return sum(
        admissible_positions([i for i in range(n) if mask & (1 << i)], numerator, denominator)
        for mask in range(1 << n)
    )


def cell_family(n, numerator, denominator, delta_num, delta_den, seed):
    rng = Random(seed)
    alpha = numerator / denominator
    m = int((1 - delta_num / delta_den) * (n ** alpha))
    if m < 1:
        return ()
    L = n // m
    lo, hi = L // 4, 3 * L // 4
    pos = [i*L + rng.randint(lo, hi - 1) for i in range(m)]
    return pos


def main():
    count = 0
    for a, b in [(1, 2), (2, 3), (3, 4)]:
        previous = 0
        for n in range(1, 13):
            p = brute_word_count(n, a, b)
            assert previous <= p <= sum(comb(n, j) for j in range(ceil_power(n, a, b)+1))
            previous = p
            count += 1
    # Every randomly chosen representative from the central-half construction
    # is checked against every possible interval spanned by its markers.
    for n, a, b in [(250000, 1, 2), (1000000, 1, 2), (40000, 2, 3), (120000, 2, 3)]:
        for seed in range(8):
            positions = cell_family(n, a, b, 1, 4, seed)
            assert admissible_positions(positions, a, b), (n, a, b, seed)
            count += 1
    # Local checks on monotonicity in the exponent, used in the nested family.
    for k in range(1, 401):
        assert ceil_power(k, 1, 2) <= ceil_power(k, 2, 3)
        count += 1
    print(f"PASS: {count} finite combinatorial cases; exact integer powers used")


if __name__ == '__main__':
    main()
