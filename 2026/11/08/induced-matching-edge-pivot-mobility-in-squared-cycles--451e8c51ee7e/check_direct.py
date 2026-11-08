#!/usr/bin/env python3
"""Self-contained exact maximal-clique and pivot-component verification."""
from itertools import combinations
from collections import deque

def results(n):
    edges = sorted({tuple(sorted((i, (i + d) % n))) for i in range(n) for d in (1, 2)})
    def close(u, v):
        return (u-v) % n in (0, 1, 2, n-1, n-2)
    compatible = [set() for _ in edges]
    for i, j in combinations(range(len(edges)), 2):
        if not any(close(u,v) for u in edges[i] for v in edges[j]):
            compatible[i].add(j); compatible[j].add(i)

    best = 0
    maxima = set()
    def maximal_cliques(R, P, X):
        nonlocal best, maxima
        if len(R) + len(P) < best:
            return
        if not P and not X:
            if len(R) > best:
                best = len(R); maxima = set()
            if len(R) == best:
                maxima.add(frozenset(R))
            return
        pivot = max(P | X, key=lambda u: len(P & compatible[u]))
        for v in sorted(P - compatible[pivot]):
            maximal_cliques(R | {v}, P & compatible[v], X & compatible[v])
            P.remove(v); X.add(v)
    maximal_cliques(set(),set(range(len(edges))),set())
    remaining = set(maxima)
    sizes = []
    while remaining:
        origin = remaining.pop(); queue = deque([origin]); size = 0
        while queue:
            state = queue.popleft(); size += 1
            for old in state:
                for new in range(len(edges)):
                    if new not in state and len(set(edges[old]) & set(edges[new])) == 1:
                        candidate = (state - {old}) | {new}
                        if candidate in remaining:
                            remaining.remove(candidate); queue.append(candidate)
        sizes.append(size)
    return best, len(maxima), sorted(sizes)

def expected(n):
    k, r = divmod(n, 4)
    return (4, 2*n, 2*k*n, n*(4*k*k+2)//3)[r]

if __name__ == '__main__':
    for n in range(5, 24):
        size, count, components = results(n)
        assert size == n // 4
        assert count == expected(n), (n, count, expected(n))
        assert components == ([1] * 4 if n % 4 == 0 else [count])
        print(f'n={n}: size={size}; states={count}; components={len(components)}')
    print('DIRECT_EXHAUSTIVE_OK')
