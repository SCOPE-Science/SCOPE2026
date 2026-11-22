#!/usr/bin/env python3
"""Independent exact cut enumeration of Euclidean widths for cycle-star graphs.

Graph: a cycle of m vertices, plus t leaves incident to vertex 0.
Uses rational arithmetic and exhaustive finite enumeration; it does not prove
claims for unbounded m,t. Run: python3 bunched_cycle_width_checker.py
"""
from fractions import Fraction


def predicted(m, t):
    n = m + t
    h = min(m - 1, n // 2)
    star = Fraction(n, n - 1)
    arc = Fraction(4 * n, h * (n - h))
    best = min(star, arc)
    normal_sets = set()
    if star == best:
        for v in range(m, n):
            normal_sets.add(1 << v)
    if arc == best:
        best_q = h * (n - h)
        # Every contiguous non-hub cycle arc is an interval of 1,...,m-1.
        for i in range(1, m):
            for j in range(i, m):
                s = j - i + 1
                if s * (n - s) == best_q:
                    normal_sets.add(sum(1 << v for v in range(i, j + 1)))
    return best, normal_sets


def exhaustive(m, t):
    n = m + t
    edges = [(i, (i + 1) % m) for i in range(m)]
    edges += [(0, m + j) for j in range(t)]
    min_value, winners = None, set()
    for subset in range(1, 1 << n):
        # A cut equals its complement, so keep the side avoiding hub 0.
        if subset & 1:
            continue
        s = subset.bit_count()
        q = sum(((subset >> a) & 1) != ((subset >> b) & 1)
                for a, b in edges)
        width_squared = Fraction(n * q * q, s * (n - s))
        if min_value is None or width_squared < min_value:
            min_value, winners = width_squared, {subset}
        elif width_squared == min_value:
            winners.add(subset)
    return min_value, winners


def phase(m, t):
    n = m + t
    h = min(m - 1, n // 2)
    difference = h * (n - h) - 4 * (n - 1)
    return 'arc' if difference > 0 else ('tie' if difference == 0 else 'leaf')


def expected_phase(m, t):
    if m <= 5:
        return 'leaf'
    if m == 6:
        critical = 15
    elif m == 7:
        critical = 9
    elif m <= 14:
        critical = 15 - m
    else:
        return 'arc'
    return 'leaf' if t < critical else ('tie' if t == critical else 'arc')


def main():
    cases = 0
    # Independently compare all minimizing cuts, not merely their width values.
    for m in range(3, 11):
        for t in range(1, 9):
            if m + t > 17:
                continue
            theory = predicted(m, t)
            direct = exhaustive(m, t)
            assert theory == direct, (m, t, theory, direct)
            cases += 1
    for m in range(3, 101):
        for t in range(1, 101):
            assert phase(m, t) == expected_phase(m, t), (m, t)
    print('BUNCHED_CYCLE_WIDTH_EXACT_PASS enumerated_cases=%d phase_checks=9800' % cases)


if __name__ == '__main__':
    main()
