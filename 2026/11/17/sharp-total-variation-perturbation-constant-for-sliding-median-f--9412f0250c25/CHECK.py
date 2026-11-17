#!/usr/bin/env python3
"""Exact rational tests for the sharp cyclic running-median BV perturbation theorem.

Run: python3 CHECK.py. Requires only Python's standard library.
"""
from fractions import Fraction
from random import Random


def median_filter(f, radius):
    n = len(f)
    assert n >= 2 * radius + 1
    return [sorted(f[(i + j) % n] for j in range(-radius, radius + 1))[radius]
            for i in range(n)]


def tv(f):
    return sum(abs(f[(i + 1) % len(f)] - f[i]) for i in range(len(f)))


def left_template(radius):
    r = radius
    ordered_labels = [('L', i) for i in range(r)]
    for i in range(r):
        ordered_labels.extend([('R', i), ('L', r + i)])
    ordered_labels.extend([('R', i) for i in range(r, 2 * r)])
    rank = dict((label, value) for value, label in enumerate(ordered_labels))
    return ({i - 2 * r: rank[('L', i)] for i in range(2 * r)} |
            {i: rank[('R', i)] for i in range(2 * r)})


def sharp_witness(radius, n):
    r = radius
    assert n >= 8 * r
    left = left_template(r)
    base = [0] * n
    for s, val in left.items():
        base[s % n] = val
    for s in range(-2 * r, 2 * r):
        base[(4 * r + s) % n] = left[-1 - s]
    perturbation = [int(i < 4 * r) for i in range(n)]
    return base, perturbation


def verify_witnesses():
    count = 0
    for r in range(1, 17):
        for n in (8 * r, 8 * r + 1, 10 * r + 3):
            f, h = sharp_witness(r, n)
            for eps in (Fraction(1, 4), Fraction(2, 3)):
                g = [x + eps * dx for x, dx in zip(f, h)]
                F, G = median_filter(f, r), median_filter(g, r)
                delta = [y - x for x, y in zip(F, G)]
                assert tv(h) == 2
                assert tv(delta) == 2 * (2 * r + 1) * eps, (r, n, eps)
                assert tv(delta) == (2 * r + 1) * tv([eps * z for z in h])
                count += 1
    return count


def verify_random_upper_bound():
    rng = Random(19943)
    count = 0
    for radius in range(1, 6):
        for n in range(2 * radius + 1, 2 * radius + 17):
            for _ in range(30):
                f = [Fraction(rng.randrange(-9, 10), 3) for i in range(n)]
                g = [Fraction(rng.randrange(-9, 10), 4) for i in range(n)]
                d = [x - y for x, y in zip(f, g)]
                D = [x - y for x, y in zip(median_filter(f, radius), median_filter(g, radius))]
                assert tv(D) <= (2 * radius + 1) * tv(d)
                count += 1
    return count


if __name__ == '__main__':
    w = verify_witnesses()
    b = verify_random_upper_bound()
    print('EXACT_SHARP_MEDIAN_WITNESSES_PASSED', w)
    print('RATIONAL_BV_PERTURBATION_UPPER_CHECKS_PASSED', b)
    print('ALL_RUNNING_MEDIAN_BV_CHECKS_PASSED')
