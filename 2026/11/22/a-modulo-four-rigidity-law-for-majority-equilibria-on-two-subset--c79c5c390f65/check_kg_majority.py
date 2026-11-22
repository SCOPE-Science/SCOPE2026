#!/usr/bin/env python3
"""Independent integer checks for an exact majority-fixed-point classification.

Usage: python3 check_kg_majority.py
No external Python packages are needed.
"""
from itertools import combinations
from collections import Counter
from math import comb
import random

def graph(n):
    vertices = tuple(combinations(range(n), 2))
    nbr = [tuple(j for j, b in enumerate(vertices) if not (set(a) & set(b)))
           for a in vertices]
    assert all(len(row) == comb(n - 2, 2) for row in nbr)
    return vertices, nbr

def update(x, neighbors):
    # The direct adjacency implementation, without using graph edge degrees.
    y = 0
    for index, adjacent in enumerate(neighbors):
        ones = sum((x >> j) & 1 for j in adjacent)
        if 2 * ones > len(adjacent) or (2 * ones == len(adjacent) and ((x >> index) & 1)):
            y |= 1 << index
    return y

def degree_formula(x, n, vertices):
    degrees = [0] * n
    for j, (u, v) in enumerate(vertices):
        if (x >> j) & 1:
            degrees[u] += 1
            degrees[v] += 1
    total = x.bit_count()
    D = comb(n - 2, 2)
    y = 0
    for j, (u, v) in enumerate(vertices):
        local = total - degrees[u] - degrees[v] + ((x >> j) & 1)
        if 2 * local > D or (2 * local == D and (x >> j) & 1):
            y |= 1 << j
    return y

def cycle_balanced(n):
    # For n=4r+1 take all cyclic edges with step 1,...,r.
    r = (n - 1) // 4
    vertices, nbr = graph(n)
    x = 0
    for j, (u, v) in enumerate(vertices):
        diff = (v - u) % n
        if min(diff, n - diff) <= r:
            x |= 1 << j
    return x, vertices, nbr

def main():
    vertices, nbr = graph(5)
    fix = [x for x in range(1 << len(vertices)) if update(x, nbr) == x]
    assert len(fix) == 14
    assert Counter(x.bit_count() for x in fix) == {0: 1, 5: 12, 10: 1}
    print('n=5 exhaustive: 14 fixed states, exactly 12 nonunanimous, each 5-edge regular.')
    rng = random.Random(271828)
    for n in (5, 8, 9, 12, 13):
        vertices, nbr = graph(n)
        degree = comb(n - 2, 2)
        assert degree % 2 == 1
        m = len(vertices)
        for _ in range(1500):
            x = rng.getrandbits(m)
            assert update(x, nbr) == degree_formula(x, n, vertices)
            y = update(x, nbr)
            if y == x and x not in (0, (1 << m) - 1):
                assert n % 4 == 1
                ds = [sum((x >> j) & 1 for j, e in enumerate(vertices) if i in e)
                      for i in range(n)]
                assert all(v == (n - 1) // 2 for v in ds)
        if n % 4 == 1:
            x, _, _ = cycle_balanced(n)
            assert update(x, nbr) == x
            assert x.bit_count() == m // 2
            print(f'n={n}: constructed nonunanimous balanced fixed state with {x.bit_count()} active pairs')
        else:
            print(f'n={n}: majority/degree-count identity checked; regular half-degree is arithmetically impossible')
    print('All tests passed: 7,500 randomized direct-vs-identity comparisons.')

if __name__ == '__main__': main()
