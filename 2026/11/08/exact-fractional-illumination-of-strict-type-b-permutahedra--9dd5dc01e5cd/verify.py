#!/usr/bin/env python3
"""Exact finite regressions for signed-permutahedron directional illumination.

This checks the rank-1 through rank-6 signed-permutation counts at generic
integer directions. Infinite-rank correctness is furnished by the proof and
Sparre Andersen's fluctuation identity, not by this enumeration.
"""
from itertools import permutations, product
from math import comb, factorial


def signed_permutations(vals):
    for p in permutations(vals):
        for signs in product((-1, 1), repeat=len(vals)):
            yield tuple(s * x for s, x in zip(signs, p))


def illuminated_by_prefix_cone(coords):
    s = 0
    for x in coords:
        s += x
        if s >= 0:
            return False
    return True


def count_illuminated(vals):
    return sum(illuminated_by_prefix_cone(v) for v in signed_permutations(vals))


def double_factorial_odd(n):
    out = 1
    for k in range(1, n + 1):
        out *= 2 * k - 1
    return out


def run():
    for n in range(1, 7):
        magnitudes = tuple(3**j for j in range(n))
        # No nonempty signed subset sum vanishes because each term exceeds
        # the sum of all lower powers of 3.
        for signed in product((-1, 0, 1), repeat=n):
            if any(signed):
                assert sum(c * x for c, x in zip(signed, magnitudes)) != 0
        actual = count_illuminated(magnitudes)
        N = (2**n) * factorial(n)
        expected = double_factorial_odd(n)
        assert actual == expected, (n, actual, expected)
        assert actual * (4**n) == N * comb(2*n, n)
        print('rank', n, 'vertices', N, 'illuminated-per-generic-direction', actual,
              'fractional-value', f'{N}/{actual}')
    # Two different generic directions have identical counts by the theorem;
    # these are independent exact-regression instances at rank four.
    for vals in [(1, 3, 9, 27), (2, 7, 23, 80), (1, 5, 35, 350)]:
        assert count_illuminated(vals) == 105
    # In rank three the full signed-permutation orbit of any generic direction
    # gives 48 directions. Every one of the 48 vertices occurs in exactly 15
    # illuminating direction sets, by the explicit signed-coordinate action.
    n = 3
    ds = tuple(signed_permutations((1, 3, 9)))
    vs = tuple(signed_permutations((3, 2, 1)))
    assert len(ds) == 48 and len(vs) == 48
    cover_counts = []
    for vertex in vs:
        order = sorted(range(n), key=lambda i: -abs(vertex[i]))
        active_prefixes_for_direction = []
        for d in ds:
            coords = tuple((1 if vertex[j] > 0 else -1) * d[j] for j in order)
            active_prefixes_for_direction.append(illuminated_by_prefix_cone(coords))
        cover_counts.append(sum(active_prefixes_for_direction))
    assert set(cover_counts) == {15}, set(cover_counts)
    print('rank-three balanced orbit incidence: all 48 vertices covered exactly 15 times')
    print('SIGNED_PERMUTAHEDRON_EXACT_OK')


if __name__ == '__main__':
    run()
