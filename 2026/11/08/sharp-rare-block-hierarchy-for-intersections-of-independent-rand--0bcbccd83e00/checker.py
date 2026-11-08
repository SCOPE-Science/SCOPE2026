#!/usr/bin/env python3
"""Finite exact enumeration for intersections of uniform set partitions."""
from itertools import product, combinations
from math import comb
from fractions import Fraction


def set_partitions(n):
    labels = [0] * n
    def visit(i, maximum):
        if i == n:
            yield tuple(labels)
        else:
            for block in range(maximum + 2):
                labels[i] = block
                yield from visit(i + 1, max(maximum, block))
    if n == 0:
        yield ()
    else:
        labels[0] = 0
        yield from visit(1, 0)


def bell(n):
    return len(list(set_partitions(n)))


def large_block_indicator(partitions, subset):
    return all(all(p[x] == p[subset[0]] for x in subset[1:]) for p in partitions)


def exact_moments(n, r, m):
    partitions = list(set_partitions(n))
    subsets = tuple(combinations(range(n), m))
    count_0 = count_1 = count_2 = 0
    outcomes = 0
    for family in product(partitions, repeat=r):
        indicators = sum(large_block_indicator(family, ss) for ss in subsets)
        count_0 += int(indicators >= 1)
        count_1 += indicators
        count_2 += indicators * (indicators - 1)
        outcomes += 1
    return (Fraction(count_0, outcomes), Fraction(count_1, outcomes),
            Fraction(count_2, outcomes))


def predicted_moments(n, r, m):
    Bn = bell(n)
    mean = Fraction(comb(n, m) * bell(n - m + 1)**r, Bn**r)
    ordered = Fraction(0)
    for overlap in range(m):
        choices = comb(n, m) * comb(m, overlap) * comb(n-m, m-overlap)
        if not choices:
            continue
        if overlap == 0:
            numerator = bell(n - 2*m + 2)
        else:
            numerator = bell(n - 2*m + overlap + 1)
        ordered += Fraction(choices * numerator**r, Bn**r)
    return mean, ordered


def main():
    tests = [(n, r, m) for n in range(3, 6) for r in (2, 3)
             for m in range(2, min(4, n + 1))
             if bell(n)**r <= 150000]
    for n, r, m in tests:
        tail, mean, second = exact_moments(n, r, m)
        pmean, psecond = predicted_moments(n, r, m)
        assert mean == pmean, (n, r, m, mean, pmean)
        assert second == psecond, (n, r, m, second, psecond)
        assert mean-second/2 <= tail <= mean
        print(f'n={n},r={r},m={m}: tail={tail}, mean={mean}, factorial2={second}')
    print('ALL_FINITE_CHECKS_OK')

if __name__ == '__main__':
    main()
