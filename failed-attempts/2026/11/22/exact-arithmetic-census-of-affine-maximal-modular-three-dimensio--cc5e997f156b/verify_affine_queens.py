#!/usr/bin/env python3
"""Finite checks for an affine three-dimensional modular-queen census.

Python 3.9+; standard library only. Direct queen-attack tests are independent
of the slope-unit characterization used by the exact counting formula.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import gcd

DIRECTIONS = []
for vec in product((-1, 0, 1), repeat=3):
    if vec == (0, 0, 0):
        continue
    pivot = next(i for i, value in enumerate(vec) if value)
    if vec[pivot] == 1:
        DIRECTIONS.append(vec)
assert len(DIRECTIONS) == 13


def direct_nonattacking(n, a, b, c=0):
    """Independently test all 13 direction families on the full placement."""
    placed = [(x, y, (a*x + b*y + c) % n)
              for x in range(n) for y in range(n)]
    for vec in DIRECTIONS:
        pivot = next(i for i, value in enumerate(vec) if value)
        line_keys = set()
        for pos in placed:
            key = tuple((pos[j] - pos[pivot]*vec[j]) % n
                        for j in range(3))
            if key in line_keys:
                return False
            line_keys.add(key)
    return True


def unit_condition(n, a, b):
    return all(gcd(v - t, n) == 1
               for v in (a, b, a+b, a-b)
               for t in (-1, 0, 1))


def distinct_prime_factors(n):
    factors = []
    p = 2
    while p*p <= n:
        if n % p == 0:
            factors.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        factors.append(n)
    return factors


def predicted_slope_count(n):
    factors = distinct_prime_factors(n)
    if any(p < 11 for p in factors):
        return 0
    count = n*n
    for p in factors:
        count = (count // (p*p)) * (p-5) * (p-7)
    return count


def check_rational_arrangement():
    lines = [(u, v, t)
             for u, v in ((1, 0), (0, 1), (1, 1), (1, -1))
             for t in (-1, 0, 1)]
    points = set()
    for (a, b, c), (d, e, f) in combinations(lines, 2):
        det = a*e-b*d
        if det != 0:
            points.add((Fraction(c*e-b*f, det),
                        Fraction(a*f-c*d, det)))
    hist = Counter(sum(a*x+b*y == c for a, b, c in lines)
                   for x, y in points)
    assert len(points) == 21
    assert hist == Counter({2: 12, 3: 4, 4: 5}), hist
    assert sum((degree-1)*count for degree, count in hist.items()) == 35
    print('RATIONAL_ARRANGEMENT 12 lines 21 points 5x4 4x3 12x2 PASS')


def test():
    check_rational_arrangement()
    for n in (2, 3, 5, 7, 11, 13, 17, 19, 25, 49, 121, 143):
        good = {(a, b) for a in range(n) for b in range(n)
                if unit_condition(n, a, b)}
        expected = predicted_slope_count(n)
        assert len(good) == expected, (n, len(good), expected)
        if n <= 13:
            direct = {(a, b) for a in range(n) for b in range(n)
                      if direct_nonattacking(n, a, b)}
            assert direct == good, (n, len(direct), len(good))
        print('n', n, 'slopes', len(good),
              'affine_max_sets', n*len(good), 'PASS')
    print('VERIFY_OK')

if __name__ == '__main__':
    test()
