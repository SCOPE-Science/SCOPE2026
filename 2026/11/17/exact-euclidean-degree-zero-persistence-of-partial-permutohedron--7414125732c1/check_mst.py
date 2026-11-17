#!/usr/bin/env python3
"""Exact Euclidean MST death-spectrum checks for partial permutohedron vertices.

Run: python3 check_mst.py
This enumerates every pair in each tested finite vertex set and applies
Kruskal's algorithm to the complete Euclidean graph using integer squares.
The all-parameter proof is mathematical, not computational.
"""

from collections import Counter
from itertools import permutations
from math import comb, factorial


def falling(m, k):
    return factorial(m) // factorial(m-k)


def formula(m, n):
    assert m >= 1 and n >= 1
    p = min(m, n)
    if n >= m + 1:
        result = {2: sum(falling(m, k)-comb(m, k) for k in range(1, m+1))}
        for k in range(m):
            result[(n-k)**2] = comb(m, k)
    else:
        result = {1: falling(m, p),
                  2: falling(m, p-1)-1+sum(falling(m, k)-comb(m,k)
                                               for k in range(1, p-1))}
        for k in range(p-1):
            result[(n-k)**2] = comb(m, k)
    return {key: val for key, val in result.items() if val > 0}


def vertices(m, n):
    points = [(0,) * m]
    for k in range(1, min(m, n) + 1):
        for positions in permutations(range(m), k):
            x = [0] * m
            for i, position in enumerate(positions):
                x[position] = n-i
            points.append(tuple(x))
    assert len(set(points)) == len(points)
    return points


def exact_kruskal(points):
    N = len(points)
    edges = []
    for i in range(N):
        for j in range(i+1, N):
            sq = sum((a-b)**2 for a, b in zip(points[i], points[j]))
            edges.append((sq, i, j))
    edges.sort()
    parent = list(range(N))
    def root(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    picked = Counter()
    used = 0
    for sq, i, j in edges:
        a, b = root(i), root(j)
        if a != b:
            parent[a] = b
            picked[sq] += 1
            used += 1
    assert used == N-1
    return dict(picked), len(edges)


def main():
    profiles = pairs = vertex_total = 0
    examples = []
    for m in range(1, 7):
        for n in range(1, 13):
            v = vertices(m, n)
            if len(v) > 210:
                continue
            predicted = formula(m, n)
            actual, count_pairs = exact_kruskal(v)
            assert actual == predicted, (m, n, predicted, actual)
            assert sum(predicted.values()) == len(v)-1
            pairs += count_pairs
            vertex_total += len(v)
            profiles += 1
            if (m, n) in [(3, 4), (4, 2), (4, 5), (5, 3)]:
                examples.append((m, n, sorted(actual.items())))
    print('PARTIAL_PERMUTOHEDRON_MST_CHECKS_PASSED',
          f'parameter_profiles={profiles}', f'exact_pairs={pairs}',
          f'cumulative_vertices={vertex_total}', f'examples={examples}')

if __name__ == '__main__':
    main()
