#!/usr/bin/env python3
"""Independent finite verification of paired domination and single-token slides.

Enumerates vertex subsets of the line graph of a complete graph, tests the
ordinary domination and perfect-matching requirements directly, then constructs
the token-slide graph with no use of the structural encoding in the theorem.
"""
from collections import deque
from itertools import combinations
from math import factorial


def test(n):
    ground_edges = tuple(combinations(range(n), 2))
    q = len(ground_edges)
    neighbors = [sum((1 << j) for j in range(q)
                     if j != i and set(e).intersection(ground_edges[j]))
                 for i, e in enumerate(ground_edges)]
    closed = [neighbors[i] | (1 << i) for i in range(q)]
    m = (n - 1) // 3
    target = 2 * m
    def dominates(chosen):
        covered = 0
        for x in chosen: covered |= closed[x]
        return covered == (1 << q) - 1
    def paired(chosen):
        # Explicit search for a perfect matching in the selected-vertex graph.
        def go(remaining):
            if not remaining:return True
            a = remaining[0]
            for i in range(1, len(remaining)):
                b = remaining[i]
                if neighbors[a] & (1 << b) and go(remaining[1:i] + remaining[i+1:]):
                    return True
            return False
        return go(chosen)
    if n == 7:
        assert not any(dominates(s) and paired(s) for s in combinations(range(q), 2))
    states = {frozenset(c) for c in combinations(range(q), target)
              if dominates(c) and paired(c)}
    N = factorial(n) // (2 ** m * factorial(m))
    assert len(states) == N, (n, len(states), N)
    adj = {}
    for s in states:
        seen = set()
        for e in s:
            for f in range(q):
                if f in s or not (neighbors[e] & (1 << f)):
                    continue
                t = s - {e} | {f}
                if t in states:
                    seen.add(t)
        assert len(seen) == 4 * m
        adj[s] = seen
    assert all(s in adj[t] for s, ns in adj.items() for t in ns)
    first = next(iter(states)); visited = {first}; stack = [first]
    while stack:
        for t in adj[stack.pop()]:
            if t not in visited:
                visited.add(t); stack.append(t)
    assert len(visited) == N
    triangles = sum(len(adj[s] & adj[t]) for s, neighbors_s in adj.items()
                    for t in neighbors_s) // 6
    assert triangles == (2 * m * N) // 3
    print(f'n={n}: optimal_size={target}, states={N}, degree={4*m}, '
          f'edges={2*m*N}, triangles={triangles}, components=1: PASS')


if __name__ == '__main__':
    for n in (4, 7):test(n)
