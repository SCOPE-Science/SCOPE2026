"""Finite checks for exact two-step tree-neighborhood shattering."""
from itertools import product, combinations
from collections import deque
from random import Random


def prufer_tree(code):
    n = len(code) + 2
    degree = [1] * n
    for x in code:
        degree[x] += 1
    edges = []
    for x in code:
        leaf = next(v for v in range(n) if degree[v] == 1)
        edges.append((leaf, x))
        degree[leaf] -= 1
        degree[x] -= 1
    a, b = (i for i in range(n) if degree[i] == 1)
    edges.append((a, b))
    return edges


def neighbors(n, edges):
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    return adj


def traces_at_two(adj, marked):
    # Directly enumerate length-two walks with different endpoints.
    out = set()
    for start in range(len(adj)):
        endpoints = set()
        for middle in adj[start]:
            endpoints.update(adj[middle])
        endpoints.discard(start)
        out.add(frozenset(v for v in marked if v in endpoints))
    return out


def counted_shattered_triples(adj):
    total = 0
    for u, nu in enumerate(adj):
        if len(nu) < 4:
            continue
        eligible = 0
        for a in nu:
            if any(len(adj[z]) >= 2 for z in adj[a] if z != u):
                eligible += 1
        if eligible >= 3:
            total += eligible * (eligible - 1) * (eligible - 2) // 6
    return total


def check(n, edges):
    a = neighbors(n, edges)
    observed = sum(len(traces_at_two(a, triple)) == 8
                   for triple in combinations(range(n), 3))
    predicted = counted_shattered_triples(a)
    assert observed == predicted, (n, edges, observed, predicted)
    if n <= 10:
        assert observed == 0
    return observed


def main():
    tests = 0
    for n in (1, 2):
        check(n, [] if n == 1 else [(0, 1)])
        tests += 1
    for n in range(3, 8):
        for code in product(range(n), repeat=n - 2):
            check(n, prufer_tree(code))
            tests += 1
    # Random labelled trees, including sizes above the sharp eleven-vertex threshold.
    rng = Random(22082026)
    for n, repeats in ((8, 120), (9, 120), (10, 120), (11, 120), (12, 100), (16, 40), (24, 15), (35, 5)):
        for _ in range(repeats):
            check(n, prufer_tree([rng.randrange(n) for _ in range(n - 2)]))
            tests += 1
    # Eleven-vertex realizing example.
    edges = [(0, 1), (0, 2), (0, 3), (0, 4),
             (1, 5), (5, 6), (2, 7), (7, 8), (3, 9), (9, 10)]
    a = neighbors(11, edges)
    assert traces_at_two(a, (1, 2, 3)) == {
        frozenset(subset) for r in range(4)
        for subset in combinations((1, 2, 3), r)
    }
    assert counted_shattered_triples(a) == 1
    print('VERIFY_OK', tests, 'trees; eleven-vertex witness and exact triple formula')


if __name__ == '__main__':
    main()
