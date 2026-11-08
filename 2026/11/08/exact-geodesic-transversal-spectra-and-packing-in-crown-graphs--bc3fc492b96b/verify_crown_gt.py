#!/usr/bin/env python3
"""Independent small-order check of crown-graph maximal-geodesic transversals.

Runs on Python 3 with no third-party packages. Directly enumerates shortest paths,
checks geodesic maximality by endpoint extension, and tests every vertex subset.
"""
from collections import Counter, deque
from math import comb


def crown_graph(n):
    adj = [set() for _ in range(2 * n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                adj[i].add(n + j)
                adj[n + j].add(i)
    return adj


def distances(adj):
    result = []
    for root in range(len(adj)):
        dist = [-1] * len(adj)
        dist[root] = 0
        q = deque([root])
        while q:
            v = q.popleft()
            for w in adj[v]:
                if dist[w] < 0:
                    dist[w] = dist[v] + 1
                    q.append(w)
        result.append(dist)
    return result


def maximal_geodesics(adj):
    dist = distances(adj)
    assert max(max(row) for row in dist) == 3
    paths = set()
    for first in range(len(adj)):
        stack = [(first,)]
        while stack:
            p = stack.pop()
            if len(p) >= 2 and dist[p[0]][p[-1]] == len(p) - 1:
                extend_left = any(dist[x][p[-1]] == len(p) for x in adj[p[0]] if x not in p)
                extend_right = any(dist[p[0]][x] == len(p) for x in adj[p[-1]] if x not in p)
                if not extend_left and not extend_right:
                    paths.add(min(p, p[::-1]))
            if len(p) < 4:
                stack.extend(p + (x,) for x in adj[p[-1]] if x not in p)
    return paths


def classification(n, mask):
    a_missing = {i for i in range(n) if not (mask & (1 << i))}
    b_missing = {i for i in range(n) if not (mask & (1 << (n + i)))}
    common = a_missing & b_missing
    return (not common or len(a_missing) == 1 or len(b_missing) == 1
            or (a_missing == b_missing and len(a_missing) == 2))


def expected_all(n):
    c = Counter()
    for j in range(n + 1):
        c[n + j] += comb(n, j) * 2 ** (n - j)
    for j in range(n):
        c[n - 1 + j] += 2 * n * comb(n - 1, j)
    c[2 * n - 2] -= n
    c[2 * n - 4] += comb(n, 2)
    return +c


def expected_minimal(n):
    c = Counter()
    c[n - 1] += 2 * n
    c[n] += 2 ** n - 2 * n - 2
    c[2 * n - 4] += comb(n, 2)
    return +c


def run_one(n):
    adj = crown_graph(n)
    paths = maximal_geodesics(adj)
    assert len(paths) == n * (n - 1) * (n - 2), (n, len(paths))
    masks = [sum(1 << v for v in path) for path in paths]
    totals, minima = Counter(), Counter()
    for s in range(1 << (2 * n)):
        hits = all(s & m for m in masks)
        assert hits == classification(n, s), (n, s, hits)
        if hits:
            totals[s.bit_count()] += 1
            if all(not all((s ^ (1 << v)) & m for m in masks)
                   for v in range(2 * n) if s & (1 << v)):
                minima[s.bit_count()] += 1
    assert totals == expected_all(n), (n, totals, expected_all(n))
    assert minima == expected_minimal(n), (n, minima, expected_minimal(n))
    p = n // 2
    unused = list(range(p, 2 * p))
    packing = [(i, n + unused[i], unused[(i + 1) % p], n + i) for i in range(p)]
    assert len(set(sum((list(x) for x in packing), []))) == 4 * p
    assert all(min(path, path[::-1]) in paths for path in packing)
    assert p == (2 * n) // 4
    return len(paths), 1 << (2 * n), sum(totals.values()), sum(minima.values())


def main():
    results = [run_one(n) for n in range(4, 9)]
    accum = [sum(case[i] for case in results) for i in range(4)]
    print("VERIFY_OK orders=4..8 maximal_geodesics=%d all_subsets=%d "
          "transversals=%d inclusion_minimal=%d independent_BFS=PASS "
          "all_polynomials=PASS minimal_families=PASS packing_construction=PASS"
          % tuple(accum))


if __name__ == '__main__':
    main()
