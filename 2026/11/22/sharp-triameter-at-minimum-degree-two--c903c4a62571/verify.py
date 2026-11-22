#!/usr/bin/env python3
"""Exact small graph census and infinite-family witness checks.

Requires only the Python standard library. Not a replacement for the proof.
"""
from itertools import combinations
from collections import deque


def distances(graph):
    n = len(graph)
    ds = []
    for s in range(n):
        d = [-1] * n
        d[s] = 0
        todo = deque([s])
        while todo:
            u = todo.popleft()
            for v in graph[u]:
                if d[v] == -1:
                    d[v] = d[u] + 1
                    todo.append(v)
        if -1 in d:
            return None
        ds.append(d)
    return ds


def triameter(graph):
    ds = distances(graph)
    if ds is None:
        return None
    return max(ds[a][b] + ds[b][c] + ds[a][c]
               for a, b, c in combinations(range(len(graph)), 3))


def expected(n):
    return {3: 3, 4: 4, 5: 6}.get(n, 2 * n - 5)


def all_graphs(n):
    pairs = list(combinations(range(n), 2))
    for mask in range(1 << len(pairs)):
        deg = [0] * n
        for bit, (u, v) in enumerate(pairs):
            if mask >> bit & 1:
                deg[u] += 1
                deg[v] += 1
        if min(deg) < 2:
            continue
        graph = [[] for _ in range(n)]
        for bit, (u, v) in enumerate(pairs):
            if mask >> bit & 1:
                graph[u].append(v)
                graph[v].append(u)
        if distances(graph) is not None:
            yield graph


def barbell(n):
    length = n - 5
    edges = [(0, 1), (1, 2), (2, 0),
             (n - 3, n - 2), (n - 2, n - 1), (n - 1, n - 3)]
    # Joining 0 to n-3 by an edge path of length n-5.
    chain = [0] + list(range(3, n - 3)) + [n - 3]
    assert len(chain) - 1 == length
    edges.extend(zip(chain, chain[1:]))
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph


def main():
    for n in range(3, 7):
        tested = 0
        observed = 0
        for graph in all_graphs(n):
            tested += 1
            observed = max(observed, triameter(graph))
        assert observed == expected(n), (n, observed, expected(n))
        print(f'ALL_LABELLED n={n} qualifying={tested} maximum={observed} PASS')
    for n in range(6, 21):
        graph = barbell(n)
        assert min(map(len, graph)) >= 2
        assert triameter(graph) == expected(n), n
    print('BARBELL_WITNESSES n=6..20 PASS')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
