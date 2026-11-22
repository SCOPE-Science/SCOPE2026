#!/usr/bin/env python3
"""Exact small-model checks for graph-quandle retraction rank spectra.

No external packages or network resources.  Python 3.9 or newer.
"""
from collections import Counter
from itertools import combinations, product
from math import comb


def adjacency(n, edges):
    a = [[0] * n for _ in range(n)]
    for u, v in edges:
        if u == v or a[u][v]:
            raise ValueError('expected a simple graph')
        a[u][v] = a[v][u] = 1
    return a


def predicted(a):
    n = len(a)
    rows = {}
    for v in range(n):
        rows.setdefault(tuple(a[v]), []).append(v)
    rank_count = Counter()
    for bits in range(1, 1 << n):
        vertices = [v for v in range(n) if bits & (1 << v)]
        if any(a[u][v] for u in vertices for v in vertices):
            continue
        j = len(vertices)
        rank_count[j] += (2 ** j) * (j ** (n - j))
    product_count = Counter({0: 1})
    for vertices in rows.values():
        m = len(vertices)
        new_count = Counter()
        for r in range(1, m + 1):
            for current_rank, number in product_count.items():
                new_count[current_rank + 2 * r] += number * comb(m, r) * ((2 * r) ** (m - r))
        product_count = new_count
    rank_count.update(product_count)
    return rank_count


def operation(a):
    n = len(a)
    return [[2 * (y // 2) + ((y % 2) ^ a[x // 2][y // 2])
             for y in range(2 * n)] for x in range(2 * n)]


def valid_retraction(f, table):
    d = len(f)
    if any(f[f[x]] != f[x] for x in range(d)):
        return False
    return all(f[table[x][y]] == table[f[x]][f[y]]
               for x in range(d) for y in range(d))


def all_maps_census(a):
    """Fully enumerate ALL functions of the 2n-point set, without normal forms."""
    d = 2 * len(a)
    op = operation(a)
    counts = Counter()
    for f in product(range(d), repeat=d):
        if valid_retraction(f, op):
            counts[len(set(f))] += 1
    return counts


def fiber_maps_census(a):
    """Independently test ALL fiber maps with vertex/bit functions by quandle law."""
    n = len(a)
    table = operation(a)
    counts = Counter()
    for h in product(range(n), repeat=n):
        for eps in product((0, 1), repeat=n):
            for b in product((0, 1), repeat=n):
                f = tuple(2 * h[v] + (eps[v] * bit ^ b[v])
                          for v in range(n) for bit in (0, 1))
                if valid_retraction(f, table):
                    counts[len(set(f))] += 1
    return counts


def main():
    cases = {
        'K2': (2, [(0, 1)]),
        'P3': (3, [(0, 1), (1, 2)]),
        'K3': (3, [(0, 1), (1, 2), (0, 2)]),
        'P4': (4, [(0, 1), (1, 2), (2, 3)]),
        'C4': (4, [(0, 1), (1, 2), (2, 3), (3, 0)]),
        'K4': (4, list(combinations(range(4), 2))),
        'paw': (4, [(0, 1), (1, 2), (2, 0), (0, 3)]),
        'K1,3': (4, [(0, 1), (0, 2), (0, 3)]),
    }
    for name, (n, edges) in cases.items():
        a = adjacency(n, edges)
        expected = predicted(a)
        observed = all_maps_census(a) if n <= 3 else fiber_maps_census(a)
        assert expected == observed, (name, expected, observed)
        print(name, sorted(observed.items()), 'PASS')
    print('GRAPH_QUANDLE_RETRACTION_RANK_VERIFIED')


if __name__ == '__main__':
    main()
