"""Finite checks of vertex/edge separator containment for bipartite graphs.

Usage: python3 artifacts/verify.py
Uses only Python's standard library. The unrestricted result requires the written proof.
"""
from collections import Counter, deque
from itertools import combinations


def distance_matrix(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    out = []
    for source in range(n):
        ds = [n + 1] * n
        ds[source] = 0
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if ds[v] == n + 1:
                    ds[v] = ds[u] + 1
                    queue.append(v)
        out.append(ds)
    return out


def separating_masks(n, edges, distances):
    vertex = {(u, v): sum((distances[s][u] != distances[s][v]) << s
                         for s in range(n))
              for u, v in combinations(range(n), 2)}
    edge = {(i, j): sum((min(distances[s][edges[i][0]], distances[s][edges[i][1]])
                         != min(distances[s][edges[j][0]], distances[s][edges[j][1]])) << s
                        for s in range(n))
            for i, j in combinations(range(len(edges)), 2)}
    return vertex, edge


def verify_graph(a, b, edges):
    n = a + b
    d = distance_matrix(n, edges)
    diameter = max(map(max, d))
    if diameter > n:  # disconnected
        return None
    vmask, emask = separating_masks(n, edges, d)
    if diameter <= 3:
        full = (1 << n) - 1
        for x in range(a):
            for y in range(a, n):
                assert vmask[x, y] == full
        for u, v in combinations(range(n), 2):
            if (u < a) != (v < a):
                continue
            common = [z for z in range(n) if (u, z) in edges or (z, u) in edges
                      if (v, z) in edges or (z, v) in edges]
            assert common, ('missing shared neighbor', a, b, edges, u, v)
            z = common[0]
            e1 = tuple(sorted((u, z)))
            e2 = tuple(sorted((v, z)))
            i = edges.index(e1)
            j = edges.index(e2)
            assert vmask[u, v] == emask[min(i, j), max(i, j)]
        for (i, j), mask in emask.items():
            u, v = edges[i]
            x, y = edges[j]
            pair = (v, y) if v != y else (u, x)
            pair = tuple(sorted(pair))
            assert vmask[pair] & ~mask == 0
    return diameter


def main():
    hist = Counter()
    for a, b in [(2, 2), (2, 3), (3, 3), (3, 4), (4, 4)]:
        possible = [(i, a + j) for i in range(a) for j in range(b)]
        for mask in range(1 << (a * b)):
            edges = [e for k, e in enumerate(possible) if mask >> k & 1]
            d = verify_graph(a, b, edges)
            if d is not None and d <= 3:
                hist[(a, b, d)] += 1
    assert sum(hist.values()) == 8701, sum(hist.values())
    # C6 plus a leaf: diameter 4; {4,5} resolves its edges but not its vertices.
    edges = [(0, 4), (0, 5), (0, 6), (1, 3), (1, 5), (2, 3), (2, 4)]
    d = distance_matrix(7, edges)
    assert max(map(max, d)) == 4
    vm, em = separating_masks(7, edges, d)
    selected = (1 << 4) | (1 << 5)
    assert not all(mask & selected for mask in vm.values())
    assert all(mask & selected for mask in em.values())
    assert d[4][3] == d[4][6] and d[5][3] == d[5][6]
    print('PASS: 8701 connected labelled bipartite graphs of diameter <=3,')
    print('      all same-shore separator equalities and edge-mask inclusions')
    print('PASS: diameter-four sharpness witness C6 with pendant leaf')


if __name__ == '__main__':
    main()
