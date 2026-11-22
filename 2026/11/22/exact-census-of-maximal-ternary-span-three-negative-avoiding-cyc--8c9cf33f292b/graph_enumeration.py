#!/usr/bin/env python3
"""Exact Euler-tour count for maximal ternary span-three negative-avoiding cycles."""
from collections import Counter
from itertools import product
from math import factorial

ALPHABET = range(3)
VERTICES = list(product(ALPHABET, repeat=2))
VID = {v: i for i, v in enumerate(VERTICES)}


def complement(e):
    return tuple((-v) % 3 for v in e)


def pair_orbits():
    seen = set()
    pairs = []
    for e in product(ALPHABET, repeat=3):
        if e in seen:
            continue
        mate = complement(e)
        seen.add(e)
        seen.add(mate)
        if e != mate:
            pairs.append((e, mate))
    return pairs


def determinant_integer(a):
    """Exact fraction-free elimination; a is square with integer entries."""
    n = len(a)
    if n == 0:
        return 1
    b = [list(map(int, row)) for row in a]
    last = 1
    sign = 1
    for k in range(n - 1):
        if b[k][k] == 0:
            pivot = next((j for j in range(k + 1, n) if b[j][k]), None)
            if pivot is None:
                return 0
            b[k], b[pivot] = b[pivot], b[k]
            sign = -sign
        d = b[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = b[i][j] * d - b[i][k] * b[k][j]
                assert numerator % last == 0
                b[i][j] = numerator // last
            b[i][k] = 0
        last = d
    return sign * b[n - 1][n - 1]


def graph_data(edges):
    incoming = [0] * 9
    outgoing = [0] * 9
    neighbors = [set() for _ in range(9)]
    adjacent = [[0] * 9 for _ in range(9)]
    for a, b, c in edges:
        u = VID[(a, b)]
        v = VID[(b, c)]
        outgoing[u] += 1
        incoming[v] += 1
        adjacent[u][v] += 1
        neighbors[u].add(v)
        neighbors[v].add(u)
    if incoming != outgoing:
        return 'unbalanced', 0, None
    active = [u for u in range(9) if outgoing[u]]
    visited = {active[0]}
    stack = [active[0]]
    while stack:
        u = stack.pop()
        for v in neighbors[u]:
            if v not in visited:
                visited.add(v)
                stack.append(v)
    if len(visited) != len(active):
        return 'disconnected', 0, None
    # Directed matrix tree theorem: in-arborescences toward first active root.
    laplacian = [[(outgoing[u] if u == v else 0) - adjacent[u][v]
                  for v in active] for u in active]
    minor = [row[1:] for row in laplacian[1:]]
    trees = determinant_integer(minor)
    assert trees >= 1
    # BEST theorem: distinct Eulerian circuits modulo cyclic edge rotation.
    tours = trees
    for u in active:
        tours *= factorial(outgoing[u] - 1)
    spectrum = tuple(sorted(outgoing))
    return 'connected', tours, spectrum


def main():
    pairs = pair_orbits()
    assert len(pairs) == 13
    status = Counter()
    distribution = Counter()
    degrees = Counter()
    total = 0
    for bits in range(1 << len(pairs)):
        chosen = [pair[(bits >> j) & 1] for j, pair in enumerate(pairs)]
        kind, tours, spectrum = graph_data(chosen)
        status[kind] += 1
        if tours:
            distribution[tours] += 1
            degrees[spectrum] += 1
            total += tours
    print('orientation_choices', 1 << len(pairs))
    print('status', dict(sorted(status.items())))
    print('tour_distribution', dict(sorted(distribution.items())))
    print('degree_patterns', {str(k): v for k, v in sorted(degrees.items())})
    print('maximal_rotation_classes', total)
    assert status == Counter({'unbalanced': 8120, 'disconnected': 12, 'connected': 60})
    assert distribution == Counter({1: 16, 2: 16, 4: 8, 6: 8, 8: 8, 24: 4})
    assert total == 288


if __name__ == '__main__':
    main()
