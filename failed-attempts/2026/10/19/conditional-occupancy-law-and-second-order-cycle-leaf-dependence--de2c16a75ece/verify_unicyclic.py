#!/usr/bin/env python3
"""Standalone exact finite verification for a uniform labelled unicyclic graph.

No third-party dependencies. Checks exact joint counts, occupancy factorial
moments, and strict conditional-mean monotonicity for all admissible sizes.
Finite checks support but do not establish the asymptotic theorem.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb, factorial


def predicted_joint(n, k, ell):
    h = n - k
    if h == 0:
        return factorial(n - 1) // 2 if ell == 0 else 0
    if ell < 0 or ell > h:
        return 0
    cycles = comb(n, k) * factorial(k - 1) // 2
    exact_forests = k * comb(h, ell) * sum(
        (-1)**j * comb(h - ell, j) * (n - ell - j)**(h - 1)
        for j in range(h - ell + 1)
    )
    return cycles * exact_forests


def graph_parameters(n, edges):
    parent = list(range(n))
    rank = [0]*n
    degrees = [0]*n
    adj = [[] for _ in range(n)]
    for a, b in edges:
        degrees[a] += 1
        degrees[b] += 1
        adj[a].append(b)
        adj[b].append(a)
        def root(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        ra, rb = root(a), root(b)
        if ra != rb:
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            rank[ra] += (rank[ra] == rank[rb])
    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    if len({root(i) for i in range(n)}) != 1:
        return None
    leaves = sum(d == 1 for d in degrees)
    deg = degrees[:]
    queue = [i for i, d in enumerate(deg) if d == 1]
    p = 0
    while p < len(queue):
        x = queue[p]
        p += 1
        for y in adj[x]:
            if deg[y] > 0:
                deg[y] -= 1
                if deg[y] == 1:
                    queue.append(y)
        deg[x] = 0
    cycle = sum(d > 0 for d in deg)
    assert cycle >= 3
    return cycle, leaves


def exact_checks():
    checked = 0
    for n in range(3, 8):
        all_edges = list(combinations(range(n), 2))
        actual = Counter()
        for edges in combinations(all_edges, n):
            param = graph_parameters(n, edges)
            if param is not None:
                actual[param] += 1
        assert sum(actual.values()) > 0
        for k in range(3, n + 1):
            h = n - k
            for ell in range(h + 1):
                expected = predicted_joint(n, k, ell)
                obtained = actual[(k, ell)]
                assert expected == obtained, (n, k, ell, expected, obtained)
                checked += 1
            count_k = sum(actual[(k, j)] for j in range(h + 1))
            assert count_k == factorial(n - 1)*n**h // (2*factorial(h))
            checked += 1
            if h >= 1:
                for r in range(h + 1):
                    falling = lambda x, r: factorial(x)//factorial(x-r)
                    actual_moment = sum(
                        falling(j, r)*actual[(k, j)] for j in range(r, h+1)
                    )
                    predicted_moment = Fraction(falling(h, r)*(n-r)**(h-1),n**(h-1))*count_k
                    assert actual_moment == predicted_moment
                    checked += 1
        for h in range(2, n-2):
            current = Fraction(h*(n-1)**(h-1),n**(h-1))
            previous = Fraction((h-1)*(n-1)**(h-2),n**(h-2))
            assert current > previous
            checked += 1
        print('n=',n,'unicyclic graphs=',sum(actual.values()),'joint categories=',len(actual))
    print('PASS:',checked,'exact joint/moment/monotonicity checks')


if __name__ == '__main__':
    exact_checks()
