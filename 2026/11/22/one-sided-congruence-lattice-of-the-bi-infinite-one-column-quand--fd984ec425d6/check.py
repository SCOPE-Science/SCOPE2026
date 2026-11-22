#!/usr/bin/env python3
"""Finite-window sanity checks for a shift-quandle congruence classification.

These checks illustrate the infinite proof; they do not certify its universal quantifiers.
"""
from math import gcd, lcm
from itertools import product

RANGE = range(-16, 17)
SHIFT = range(-16, 16)


def equivalent(a, b, cutoff=None, period=None):
    # None,None: equality; cutoff == float('-inf'): periodic everywhere.
    if cutoff is None:
        return a == b
    if cutoff == float('-inf'):
        return (a-b) % period == 0
    return a == b or (a >= cutoff and b >= cutoff and (a-b) % period == 0)


def and_relation(x, y, a, b):
    return equivalent(x, y, *a) and equivalent(x, y, *b)


def or_relation(x, y, a, b):
    # use transitive union find for exact finite sampled set only
    return equivalent(x, y, *a) or equivalent(x, y, *b)


def verify():
    count = 0
    cuts = range(-3, 4)
    periods = range(1, 6)
    parameters = [(c, d) for c, d in product(cuts, periods)] + [(float('-inf'), d) for d in periods]
    for p in parameters:
        c, d = p
        # Reflexivity, symmetry, transitivity from normalized closed forms.
        for i in RANGE:
            assert equivalent(i, i, c, d)
            for j in RANGE:
                assert equivalent(i, j, c, d) == equivalent(j, i, c, d)
                if i < 16 and j < 16 and equivalent(i, j, c, d):
                    assert equivalent(i + 1, j + 1, c, d)
        if c != float('-inf'):
            assert equivalent(c, c + d, c, d)
            assert not equivalent(c - 1, c + d - 1, c, d)
        else:
            for i in SHIFT:
                for j in SHIFT:
                    if equivalent(i, j, c, d):
                        assert equivalent(i - 1, j - 1, c, d)
        count += 1

    # Check gcd/lcm lattice formulas for every tested pair.
    for a, b in product(parameters, repeat=2):
        c1, d1 = a
        c2, d2 = b
        mn = min(c1, c2)
        mx = max(c1, c2)
        meeting = (mx, lcm(d1, d2))
        joining = (mn, gcd(d1, d2))
        for i in RANGE:
            for j in RANGE:
                assert and_relation(i, j, a, b) == equivalent(i, j, *meeting)
        # Generated union is checked on a bounded universe, not in infinite generality.
        lo, hi = -30, 90
        parent = list(range(hi - lo + 1))
        def root(x):
            a = x - lo
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a
        def union(x, y):
            parent[root(x)] = root(y)
        for i in range(lo, hi+1):
            for j in range(i+1, hi+1):
                if or_relation(i, j, a, b):
                    union(i, j)
        for i in range(-8, 17):
            for j in range(-8, 17):
                assert (root(i) == root(j)) == equivalent(i, j, *joining), (a, b, i, j)
        count += 1
    print('SHIFT_QUANDLE_LATTICE_CHECKS_PASSED', count, 'parameter_or_pair_cases')

if __name__ == '__main__':
    verify()
