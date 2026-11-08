#!/usr/bin/env python3
"""Independent finite checks for shattering by matching-covered vertex sets.
Run: python matching_shatter_check.py
"""
from itertools import combinations, product
from collections import Counter


def all_matchings(edge_list):
    ans = [()]
    for edge in edge_list:
        old = list(ans)
        for matching in old:
            if all(not (set(edge) & set(other)) for other in matching):
                ans.append(matching + (edge,))
    return ans


def matches_to_complement(edges, n, query_mask):
    # Unlike direct trace enumeration, this checks a transversal matching
    # of selected vertices to vertices outside the query support.
    selected = [v for v in range(n) if (query_mask >> v) & 1]
    neighbors = [[y for a, b in edges for y in
                  ((b,) if a == v else ((a,) if b == v else ()))
                  if not (query_mask >> y) & 1] for v in selected]
    order = sorted(range(len(selected)), key=lambda i: len(neighbors[i]))
    def search(depth, used):
        if depth == len(order):
            return True
        return any(not (used >> y) & 1 and search(depth + 1, used | (1 << y))
                   for y in neighbors[order[depth]])
    return search(0, 0)


def directly_shattered(matchings, n, query_mask):
    selected = [v for v in range(n) if (query_mask >> v) & 1]
    traces = set()
    for matching in matchings:
        covered = set(v for edge in matching for v in edge)
        traces.add(sum(1 << j for j, v in enumerate(selected) if v in covered))
    return len(traces) == (1 << len(selected))


def check_graph(m, n, edges):
    matchings = all_matchings(edges)
    rank = max(map(len, matchings))
    supported = []
    for mask in range(1 << (m + n)):
        a = matches_to_complement(edges, m + n, mask)
        b = directly_shattered(matchings, m + n, mask)
        assert a == b, (m, n, edges, mask, a, b)
        if b:
            supported.append(mask)
    assert max(map(int.bit_count, supported)) == rank
    return len(supported)


def main():
    graphs = 0
    support_checks = 0
    for m, n in ((1, 1), (1, 2), (2, 2), (2, 3), (3, 3)):
        universe = list(product(range(m), range(m, m + n)))
        for flags in range(1 << len(universe)):
            edges = [e for i, e in enumerate(universe) if flags >> i & 1]
            support_checks += 1 << (m + n)
            check_graph(m, n, edges)
            graphs += 1
    paths = 0
    facet_checks = 0
    for n in range(2, 18):
        edges = [(i, i + 1) for i in range(n - 1)]
        supported = [matches_to_complement(edges, n, s) for s in range(1 << n)]
        assert max(s.bit_count() for s in range(1 << n) if supported[s]) == n // 2
        if n % 5 == 1 and n >= 6:
            t = (n - 1) // 5
            s = sum((1 << (5 * j + 2)) | (1 << (5 * j + 3)) for j in range(t))
            assert supported[s]
            assert not any(supported[s | (1 << i)] for i in range(n) if not (s >> i & 1))
            assert n // 2 - s.bit_count() == (t + 1) // 2
            facet_checks += 1
        paths += 1
    for a, b in ((1, 2), (2, 3), (3, 4), (4, 4)):
        edges = list(product(range(a), range(a, a+b)))
        for s in range(1 << (a+b)):
            assert matches_to_complement(edges, a+b, s) == (s.bit_count() <= min(a, b))
    # Nonbipartite boundary: triangle has VC dimension two, matching number one.
    edges = [(0, 1), (1, 2), (0, 2)]
    assert directly_shattered(all_matchings(edges), 3, 0b011)
    assert max(map(len, all_matchings(edges))) == 1
    print('MATCHING_SATURATION_SHATTERING_PASS', graphs, support_checks, paths, facet_checks)


if __name__ == '__main__':
    main()
