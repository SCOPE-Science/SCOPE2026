"""Exhaustive geodetic-set tests on triangular graphs; Python 3 stdlib."""
from collections import deque
from itertools import combinations
from math import comb, factorial


def expected_count(n):
    def match(k):
        return factorial(k) // (2 ** (k // 2) * factorial(k // 2))
    if n % 2 == 0:
        return match(n)
    return comb(n, 3) * match(n-3) + (60 * comb(n, 5) * match(n-5) if n >= 5 else 0)


def is_geodetic_by_shortest_paths(edges, selected, interval):
    covered = set(selected)
    for i, j in combinations(selected, 2):
        covered.update(interval[i][j])
    return len(covered) == len(edges)


def is_geodetic_by_leaf_criterion(n, chosen_edges):
    neighborhoods = [set() for _ in range(n)]
    for a, b in chosen_edges:
        neighborhoods[a].add(b)
        neighborhoods[b].add(a)
    return all(neighborhoods) and all(
        sum(len(neighborhoods[x]) == 1 for x in neighborhoods[v]) <= 1
        for v in range(n)
    )


def verify(n):
    edges = list(combinations(range(n), 2))
    N = len(edges)
    graph = [set() for _ in edges]
    for i, a in enumerate(edges):
        for j, b in enumerate(edges):
            if i != j and not set(a).isdisjoint(b):
                graph[i].add(j)
    dists = []
    for start in range(N):
        d = [-1] * N
        d[start] = 0
        todo = deque([start])
        while todo:
            x = todo.popleft()
            for y in graph[x]:
                if d[y] == -1:
                    d[y] = d[x] + 1
                    todo.append(y)
        assert all(i >= 0 for i in d)
        dists.append(d)
    interval = [[set() for _ in edges] for _ in edges]
    for a in range(N):
        for b in range(N):
            interval[a][b] = {x for x in range(N) if dists[a][x]+dists[x][b]==dists[a][b]}
    k = n // 2 if n % 2 == 0 else (n + 3) // 2
    for h in range(1, k):
        for s in combinations(range(N), h):
            assert not is_geodetic_by_shortest_paths(edges, s, interval)
    winners = 0
    for s in combinations(range(N), k):
        actual = is_geodetic_by_shortest_paths(edges, s, interval)
        criterion = is_geodetic_by_leaf_criterion(n, [edges[i] for i in s])
        assert actual == criterion, (n, s)
        winners += actual
    assert winners == expected_count(n), (n, winners, expected_count(n))
    print(f'n={n} minimum={k} bases={winners} direct_interval=PASS leaf_criterion=PASS')


if __name__ == '__main__':
    for n in range(3, 9):
        verify(n)
    print('DIRECT_CHECK_PASS')
