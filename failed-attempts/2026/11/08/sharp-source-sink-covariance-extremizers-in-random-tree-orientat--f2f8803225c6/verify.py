"""Exact source/sink covariance and tree-extremum checks.

Run: python verify.py
Uses only the Python standard library and exact integer/Fraction arithmetic.
Finite checks corroborate, but do not replace, the general proof.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from heapq import heapify, heappop, heappush


def edges_from_prufer(code, n):
    deg = [1] * n
    for v in code:
        deg[v] += 1
    leaves = [v for v in range(n) if deg[v] == 1]
    heapify(leaves)
    edges = []
    for v in code:
        leaf = heappop(leaves)
        edges.append((leaf, v))
        deg[v] -= 1
        deg[leaf] -= 1
        if deg[v] == 1:
            heappush(leaves, v)
    edges.append((leaves[0], leaves[1]))
    return edges


def covariance_local(edges, n):
    d = [0] * n
    for u, v in edges:
        d[u] += 1
        d[v] += 1
    return 2 * sum((Fraction(1, 2 ** (d[u] + d[v])) for u, v in edges), Fraction(0)) - sum(
        (Fraction(1, 4**dv) for dv in d), Fraction(0)
    )


def covariance_direct(edges, n):
    # Every possible direction choice for every edge, exactly equally weighted.
    count = 1 << (n - 1)
    ss = st = sst = 0
    for mask in range(count):
        in_deg = [0] * n
        out_deg = [0] * n
        for i, (u, v) in enumerate(edges):
            if mask & (1 << i):
                u, v = v, u
            out_deg[u] += 1
            in_deg[v] += 1
        sources = sum(z == 0 for z in in_deg)
        sinks = sum(z == 0 for z in out_deg)
        ss += sources
        st += sinks
        sst += sources * sinks
    return Fraction(sst, count) - Fraction(ss * st, count * count)


def path_bound(n):
    return Fraction(n - 4, 16)


def star_bound(n):
    return Fraction(n - 1, 2 ** (n - 1)) - Fraction(n - 1, 4) - Fraction(1, 4 ** (n - 1))


def run():
    total = 0
    for n in range(4, 9):
        low, high = None, None
        checked = 0
        for code in product(range(n), repeat=n - 2):
            edges = edges_from_prufer(code, n)
            got = covariance_local(edges, n)
            assert star_bound(n) <= got <= path_bound(n)
            deg = [0] * n
            for u, v in edges:
                deg[u] += 1
                deg[v] += 1
            assert (got == star_bound(n)) == (max(deg) == n - 1)
            assert (got == path_bound(n)) == (max(deg) <= 2)
            if n <= 6:
                assert got == covariance_direct(edges, n)
            low = got if low is None or got < low else low
            high = got if high is None or got > high else high
            checked += 1
        assert low == star_bound(n)
        assert high == path_bound(n)
        print(f'n={n} labeled_trees={checked} min={low} max={high} direct={n<=6}')
        total += checked
    assert total == sum(n ** (n - 2) for n in range(4, 9))
    print(f'PASS: {total} trees; exhaustive direct orientation moments for all labeled trees n=4,5,6')


if __name__ == '__main__':
    run()
