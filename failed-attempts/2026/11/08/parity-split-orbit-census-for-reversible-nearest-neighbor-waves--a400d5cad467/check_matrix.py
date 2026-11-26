#!/usr/bin/env python3
"""Exact binary matrix checks for cyclic second-order nearest-neighbor waves.

Rows are stored as arbitrary-precision Python integers. No third-party packages.
"""
from math import gcd


def step(x, n):
    mask = (1 << n) - 1
    u, v = x & mask, x >> n
    left = ((u << 1) & mask) | (u >> (n - 1))
    right = (u >> 1) | ((u & 1) << (n - 1))
    return ((left ^ right ^ v) & mask) | (u << n)


def rank_gf2(columns):
    pivots = {}
    for value in columns:
        while value:
            index = value.bit_length() - 1
            if index in pivots:
                value ^= pivots[index]
            else:
                pivots[index] = value
                break
    return len(pivots)


def fixed_dimension(n, t):
    columns = []
    for j in range(2 * n):
        x = 1 << j
        for _ in range(t):
            x = step(x, n)
        columns.append(x ^ (1 << j))
    return 2 * n - rank_gf2(columns)


def expected(n, t):
    return 2 * gcd(n, t) - (int(n % 2 == 1 and t % 2 == 1))


def run():
    comparisons = 0
    for n in range(3, 36):
        for t in range(1, 2 * n + 1):
            found = fixed_dimension(n, t)
            want = expected(n, t)
            assert found == want, (n, t, found, want)
            comparisons += 1
    print('matrix/nullity comparisons:', comparisons)
    print('n range: 3..35; t range: 1..2n inclusive')
    print('all predicted fixed-space dimensions agree: PASS')


if __name__ == '__main__':
    run()
