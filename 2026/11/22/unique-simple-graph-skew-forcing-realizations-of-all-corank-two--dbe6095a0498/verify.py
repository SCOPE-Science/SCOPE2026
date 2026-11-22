#!/usr/bin/env python3
"""Reproducible finite checks of the corank-two skew-forcing realization theorem.
Run with Python 3.9 or later. Only standard-library modules are used.
"""
from itertools import combinations
from math import comb


def partitions(total, minimum=1):
    if total == 0:
        yield ()
    for first in range(minimum, total + 1):
        for suffix in partitions(total - first, first):
            yield (first,) + suffix


def layout(sizes, isolates):
    labels = []
    for i, size in enumerate(sizes):
        labels += [i] * size
    labels += [-1] * isolates
    return labels


def skew_closure(labels, starting):
    n = len(labels)
    universe = (1 << n) - 1
    neighborhoods = [sum(1 << j for j in range(n)
                         if labels[i] >= 0 and labels[j] >= 0
                         and labels[i] != labels[j]) for i in range(n)]
    filled = starting
    while True:
        white = universe & ~filled
        newly = 0
        for neighborhood in neighborhoods:
            unfilled = white & neighborhood
            if unfilled and not (unfilled & (unfilled - 1)):
                newly |= unfilled
        if not newly:
            return filled
        filled |= newly


def rank_dual(labels, subset):
    n = len(labels)
    complement = ((1 << n) - 1) ^ subset
    touched = {labels[i] for i in range(n)
               if complement & (1 << i) and labels[i] >= 0}
    return subset.bit_count() - 2 + min(2, len(touched))


def dual_closure(labels, starting):
    n = len(labels)
    base_rank = rank_dual(labels, starting)
    return starting | sum(1 << v for v in range(n)
                          if not (starting & (1 << v))
                          and rank_dual(labels, starting | (1 << v)) == base_rank)


def rank_primal(labels, subset):
    touched = {labels[i] for i in range(len(labels))
               if subset & (1 << i) and labels[i] >= 0}
    return min(2, len(touched))


def check_instance(sizes, isolates):
    labels = layout(sizes, isolates)
    n = len(labels)
    complete = (1 << n) - 1
    minsets = []
    for starting in range(1 << n):
        actual = skew_closure(labels, starting)
        expected = dual_closure(labels, starting)
        assert actual == expected, (sizes, isolates, starting, actual, expected)
        if actual == complete and starting.bit_count() == n - 2:
            minsets.append(starting)
    expected_pairs = sum(a * b for a, b in combinations(sizes, 2))
    assert len(minsets) == expected_pairs, (sizes, isolates, len(minsets))
    for initial in minsets:
        missing = [i for i in range(n) if not (initial & (1 << i))]
        assert all(labels[i] >= 0 for i in missing)
        assert labels[missing[0]] != labels[missing[1]]
    # Direct polynomial checks at several integer evaluation points.
    if n <= 8:
        for x, y in [(2, 2), (2, 3), (3, 2), (3, 3)]:
            direct = sum((x - 1) ** (n - 2 - rank_dual(labels, s))
                         * (y - 1) ** (s.bit_count() - rank_dual(labels, s))
                         for s in range(1 << n))
            N = n - isolates
            r = len(sizes)
            formula = x ** isolates * (
                (y - 1) ** 2
                + (y - 1) * sum((x ** m - 1) // (x - 1) for m in sizes)
                + (x ** N - sum(x ** m for m in sizes) + r - 1) // ((x - 1) ** 2)
            )
            assert direct == formula, (sizes, isolates, x, y, direct, formula)
    return 1 << n


def main():
    instances = 0
    checked_subsets = 0
    for N in range(2, 10):
        for sizes in partitions(N):
            if len(sizes) < 2:
                continue
            for isolates in range(3):
                if N + isolates > 10:
                    continue
                checked_subsets += check_instance(sizes, isolates)
                instances += 1
    print('GRAPH_INSTANCES', instances)
    print('INITIAL_SUBSETS_CHECKED', checked_subsets)
    print('DUAL_CLOSURE_MINIMUM_SET_AND_TUTTE_CHECKS_OK')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
