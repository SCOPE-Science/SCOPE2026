#!/usr/bin/env python3
"""Exact enumeration for seven-point, seven-triple, three-regular coupon designs.

Requires only Python's standard library. Run `python verify.py`.
An alternative full unpruned combination traversal is available with --full.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import comb
import sys

TRIPLES = tuple(sum(1 << i for i in tup) for tup in combinations(range(7), 3))
TARGET = Counter({
    (-6, 21, -21, 0, 7): 30,
    (-4, 15, -15, -2, 7): 630,
    (-3, 12, -12, -3, 7): 1680,
    (-2, 9, -9, -4, 7): 3780,
    (-1, 6, -6, -5, 7): 3360,
    (1, 0, 0, -7, 7): 360,
    (0, 4, -6, -3, 6): 1260,
    (0, 5, -9, 0, 5): 105,
})
FANO = (7, 25, 97, 42, 82, 76, 52)


def coefficients(blocks):
    c = [0] * 5
    for subset in range(1, 128):
        d = sum((block & subset) == 0 for block in blocks)
        assert 0 <= d <= 4
        c[d] += 1 if subset.bit_count() % 2 else -1
    return tuple(c)


def census():
    histogram = Counter()
    maximizers = set()

    def visit(start, blocks, degrees):
        if len(blocks) == 7:
            if degrees != (3,) * 7:
                return
            key = coefficients(blocks)
            histogram[key] += 1
            if key == (-6, 21, -21, 0, 7):
                maximizers.add(tuple(sorted(blocks)))
            return
        remaining = 7 - len(blocks)
        for j in range(start, len(TRIPLES) - remaining + 1):
            block = TRIPLES[j]
            newdeg = tuple(degrees[i] + ((block >> i) & 1) for i in range(7))
            if max(newdeg) > 3 or min(newdeg) + remaining - 1 < 3:
                continue
            visit(j + 1, blocks + (block,), newdeg)

    visit(0, (), (0,) * 7)
    return histogram, maximizers


def full_census():
    histogram = Counter()
    # Traverse all C(35,7) possibilities, avoiding the pruning used by census.
    assert comb(35, 7) == 6724520
    for ids in combinations(range(35), 7):
        blocks = tuple(TRIPLES[i] for i in ids)
        packed = sum(sum(1 << (3 * i) for i in range(7) if b & (1 << i)) for b in blocks)
        if packed == sum(3 << (3 * i) for i in range(7)):
            histogram[coefficients(blocks)] += 1
    return histogram


def orbit(blocks):
    seen = set()
    for p in permutations(range(7)):
        transformed = []
        for block in blocks:
            transformed.append(sum(1 << p[i] for i in range(7) if block & (1 << i)))
        seen.add(tuple(sorted(transformed)))
    return seen


def mean(c):
    return sum((Fraction(7 * c[k], 7 - k) for k in range(5)), Fraction(0))


def survival_numerator(c, t):
    assert t >= 1
    return sum(c[k] * k ** t for k in range(1, 5))


def main():
    hist, maximizers = census()
    assert hist == TARGET, (hist, TARGET)
    assert sum(hist.values()) == 11205
    assert coefficients(FANO) == (-6, 21, -21, 0, 7)
    assert all(sum((b >> i) & 1 for b in FANO) == 3 for i in range(7))
    assert orbit(FANO) == maximizers and len(maximizers) == 30
    f = (-6, 21, -21, 0, 7)
    assert mean(f) == Fraction(163, 30)
    assert max(mean(k) for k in TARGET if k != f) == Fraction(16, 3)
    assert mean(f) - max(mean(k) for k in TARGET if k != f) == Fraction(1, 10)
    for c in TARGET:
        assert survival_numerator(c, 1) == 7
        assert survival_numerator(c, 2) == 49
        for t in range(3, 25):
            if c != f:
                assert survival_numerator(f, t) > survival_numerator(c, t)
        assert mean(c) == sum((Fraction(7 * c[k], 7 - k) for k in range(5)), Fraction(0))
    if '--full' in sys.argv:
        assert full_census() == hist
        print('FULL_UNPRUNED_CENSUS_OK: 6724520 combinations')
    print('EXACT_CENSUS_OK: 11205 admissible families, eight profiles, 30 Fano relabelings')
    for c, count in sorted(hist.items(), key=lambda pair: -mean(pair[0])):
        print('profile', c, 'count', count, 'mean', mean(c))
    print('SYMBOLIC_COMPARISON: D_t=b(3^t-3*2^t+3) for c4=7; '
          'D_t=4^t+3*3^t-15*2^t+17 for c4=6; '
          'D_t=2(2^t-2)(2^t-4) for c4=5; inequalities proved in RESULT.md')


if __name__ == '__main__':
    main()
