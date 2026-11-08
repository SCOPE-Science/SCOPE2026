#!/usr/bin/env python3
"""Direct finite checks for the P3-convex-set stability theorem.

Graph vertices are 0,...,m-1 in the first shore and 0,...,n-1
in the second; missing cross edges are explicit pairs (i,j).
This checker uses only Python's standard library.
"""
from itertools import combinations
from random import Random


def convex(m, n, missing, x, y):
    """Independent, adjacency-based test: outside vertices have <=1 selected neighbor."""
    X = {i for i in range(m) if x >> i & 1}
    Y = {j for j in range(n) if y >> j & 1}
    for i in range(m):
        if i not in X and sum((i, j) not in missing for j in Y) > 1:
            return False
    for j in range(n):
        if j not in Y and sum((i, j) not in missing for i in X) > 1:
            return False
    return True


def expected(m, n, x, y):
    return ((x.bit_count() <= 1 and y.bit_count() <= 1) or
            (x == (1 << m) - 1 and y == (1 << n) - 1))


def check_instance(m, n, missing):
    for x in range(1 << m):
        for y in range(1 << n):
            assert convex(m, n, missing, x, y) == expected(m, n, x, y), (
                m, n, sorted(missing), x, y)


def partial_matchings(n):
    # Includes the empty matching, and every matching between two n-element shores.
    for t in range(n + 1):
        for asel in combinations(range(n), t):
            for bsel in combinations(range(n), t):
                # Do not enumerate permutations via a third-party package.
                from itertools import permutations
                for bperm in permutations(bsel):
                    yield frozenset(zip(asel, bperm))


def random_missing(m, n, d, rng):
    edges = [(i, j) for i in range(m) for j in range(n)]
    rng.shuffle(edges)
    miss = set()
    da, db = [0] * m, [0] * n
    for i, j in edges:
        if da[i] < d and db[j] < d and rng.randrange(4) != 0:
            miss.add((i, j))
            da[i] += 1
            db[j] += 1
    return frozenset(miss)


def sharp_example(d):
    m = n = 2 * d + 2
    # The four selected vertices are two in each shore.
    miss = set()
    for i in (0, 1):
        for j in range(2 + i * d, 2 + (i + 1) * d):
            miss.add((i, j))
    for j in (0, 1):
        for i in range(2 + j * d, 2 + (j + 1) * d):
            miss.add((i, j))
    assert max(sum((i, j) in miss for j in range(n)) for i in range(m)) <= d
    assert max(sum((i, j) in miss for i in range(m)) for j in range(n)) <= d
    assert convex(m, n, miss, 0b11, 0b11)
    assert not expected(m, n, 0b11, 0b11)
    return m


def main():
    matchings = 0
    for missing in partial_matchings(5):
        check_instance(5, 5, missing)
        matchings += 1
    print('ALL_PARTIAL_MATCHINGS_5X5_OK', matchings)

    rng = Random(23112026)
    for m, n, d, cases in ((5, 7, 1, 40), (7, 7, 2, 28), (8, 9, 2, 14)):
        for _ in range(cases):
            check_instance(m, n, random_missing(m, n, d, rng))
        print('BOUNDED_MISSING_DEGREE_OK', m, n, d, cases)

    for d in range(1, 25):
        sharp_example(d)
    print('SHARP_BOUNDARY_WITNESSES_OK', 'd=1..24')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
