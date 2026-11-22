#!/usr/bin/env python3
"""Exact finite checks for a one-point disagreement spectrum in two orders.
No external packages; computes type labels by direct order comparisons.
"""
from collections import Counter
from itertools import permutations
from math import comb


def distribution_direct(perm):
    n = len(perm)
    coeff = [0] * (n + 1)
    for gap_a in range(n + 1):
        for gap_b in range(n + 1):
            disagreement = sum(
                (old_pos < gap_a) != (rank <= gap_b)
                for old_pos, rank in enumerate(perm)
            )
            coeff[disagreement] += 1
    return tuple(coeff)


def match_count_if_bandwidth_one(perm):
    n = len(perm)
    k = 0
    j = 0
    while j < n:
        if perm[j] == j + 1:
            j += 1
        elif (j + 1 < n and perm[j] == j + 2
              and perm[j + 1] == j + 1):
            k += 1
            j += 2
        else:
            return None
    return k


def theoretical(n, k):
    arr = [n + 1] + [2 * (n + 1 - j) for j in range(1, n + 1)]
    arr[0] -= k
    arr[2] += k
    return tuple(arr)


def run():
    total = 0
    matching_total = 0
    for n in range(2, 9):
        category = Counter()
        seen_profiles = {}
        for perm in permutations(range(1, n + 1)):
            poly = distribution_direct(perm)
            total += 1
            assert sum(poly) == (n + 1) ** 2
            assert poly[1] <= 2 * n
            k = match_count_if_bandwidth_one(perm)
            assert (poly[1] == 2 * n) == (k is not None)
            if k is not None:
                matching_total += 1
                assert poly == theoretical(n, k)
                category[k] += 1
                seen_profiles.setdefault(k, poly)
                assert seen_profiles[k] == poly
        for k in range(n // 2 + 1):
            assert category[k] == comb(n - k, k)
        print('n=%d tested=%d matching_extremizers=%d classes=%s' %
              (n, __import__('math').factorial(n), sum(category.values()),
               sorted(category.items())))
    assert distribution_direct((1, 3, 2, 4)) == distribution_direct((1, 2, 4, 3))
    assert distribution_direct((1, 3, 2, 4)) == (4, 8, 7, 4, 2)
    print('TOTAL_PERMUTATIONS_CHECKED=%d' % total)
    print('TOTAL_MATCHING_EXTREMIZERS=%d' % matching_total)
    print('ALL_EXHAUSTIVE_INSERTION_CHECKS_PASS')


if __name__ == '__main__':
    run()
