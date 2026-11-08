#!/usr/bin/env python3
"""Finite-instance checks for the two-active-window cycle theorem.

Uses only the Python standard library. Each allowed length-n word is an edge of
its overlap digraph, and all matrix-tree cofactors are computed with exact integers.
"""
from collections import defaultdict, Counter
from itertools import combinations, product
from math import factorial


def det_bareiss(a):
    a = [list(map(int, r)) for r in a]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    denom = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            p = next((j for j in range(k + 1, n) if a[j][k] != 0), None)
            if p is None:
                return 0
            a[k], a[p] = a[p], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = a[i][j] * pivot - a[i][k] * a[k][j]
                assert num % denom == 0
                a[i][j] = num // denom
        for i in range(k + 1, n):
            a[i][k] = 0
        denom = pivot
    return sign * a[-1][-1]


def graph(q, n):
    parts = defaultdict(list)
    for ij in combinations(range(n), 2):
        d = min(ij[1] - ij[0], n - (ij[1] - ij[0]))
        for a, b in product(range(1, q), repeat=2):
            w = [0] * n
            w[ij[0]], w[ij[1]] = a, b
            w = tuple(w)
            parts[d].append((w[:-1], w[1:], w))
    return dict(parts)


def tree_cofactor(edges):
    vertices = sorted(set(x for e in edges for x in e[:2]))
    degrees = Counter(u for u, v, w in edges)
    branches = [v for v in vertices if degrees[v] > 1]
    root = branches[0] if branches else vertices[0]
    ix = {v: i for i, v in enumerate(vertices)}
    m = len(vertices)
    lap = [[0] * m for _ in range(m)]
    for u, v, _ in edges:
        lap[ix[u]][ix[u]] += 1
        lap[ix[u]][ix[v]] -= 1
    ridx = ix[root]
    minor = [[lap[i][j] for j in range(m) if j != ridx]
             for i in range(m) if i != ridx]
    count = det_bareiss(minor)
    fact = 1
    for v in vertices:
        fact *= factorial(degrees[v] - 1)
    return count, count * fact, len(branches), len(vertices)


def direct_tour_count(edges):
    """Naive edge-identity DFS with one fixed first edge; small instances only."""
    vertices = sorted(set(x for e in edges for x in e[:2]))
    outgoing = defaultdict(list)
    for i, (u, v, _) in enumerate(edges):
        outgoing[u].append((i, v))
    first = 0
    root, nxt, _ = edges[first]
    fullmask = (1 << len(edges)) - 1
    def dfs(v, used):
        if used == fullmask:
            return int(v == root)
        return sum(dfs(w, used | (1 << j)) for j, w in outgoing[v]
                   if not ((used >> j) & 1))
    return dfs(nxt, 1 << first)


def target(s, n, d):
    unequal = s ** (2 * s - 2) * factorial(s - 1) ** (2 * s)
    equal = (s ** (s - 2) if s > 1 else 1) * factorial(s - 1) ** s
    return (equal, n // 2 * s * s, s) if n % 2 == 0 and d == n // 2 else (unequal, n * s * s, 2 * s)


def verify():
    tested = []
    for q, ns in [(2, range(3, 9)), (3, range(3, 7)), (4, range(3, 6)), (5, range(3, 5))]:
        for n in ns:
            parts = graph(q, n)
            s = q - 1
            assert len(parts) == n // 2
            assert sum(len(e) for e in parts.values()) == n * (n - 1) // 2 * s * s
            for d, edges in sorted(parts.items()):
                expected, edge_count, branch_count = target(s, n, d)
                assert len(edges) == edge_count
                degin = Counter(v for u, v, w in edges)
                degout = Counter(u for u, v, w in edges)
                assert degin == degout
                tree, observed, branches, vertices = tree_cofactor(edges)
                assert branches == (branch_count if s > 1 else 0), (q, n, d, branches, branch_count)
                assert observed == expected, (q, n, d, observed, expected)
                if (q, n) in [(2, 3), (2, 4), (3, 3), (3, 4), (3, 5), (4, 3)]:
                    direct = direct_tour_count(edges)
                    assert direct == expected, (q, n, d, direct, expected)
                tested.append((q, n, d, len(edges), tree, observed))
    print('VERIFIED component instances:', len(tested))
    for row in tested:
        print('q={} n={} gap={} edges={} in_trees={} cycles={}'.format(*row))

if __name__ == '__main__':
    verify()
