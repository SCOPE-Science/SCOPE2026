#!/usr/bin/env python3
"""Independent adjacency-list/BFS verification for odd complete-graph matching flips."""
from itertools import combinations
from collections import Counter, deque
from math import comb, factorial


def all_states(n):
    def pairings(vertices):
        if not vertices:
            yield ()
            return
        a = vertices[0]
        for i in range(1, len(vertices)):
            b = vertices[i]
            for tail in pairings(vertices[1:i] + vertices[i + 1:]):
                yield ((a, b),) + tail
    for free in range(n):
        for matching in pairings(tuple(v for v in range(n) if v != free)):
            yield (free, tuple(sorted(matching)))


def successors(state):
    free, matching = state
    for index, (a, b) in enumerate(matching):
        for newfree, other in ((a, b), (b, a)):
            edge = tuple(sorted((free, other)))
            yield newfree, tuple(sorted(matching[:index] + matching[index+1:] + (edge,)))


def profile(k):
    n = 2*k + 1
    states = set(all_states(n))
    start = (n - 1, tuple((i, i+1) for i in range(0, n-1, 2)))
    d = {start: 0}
    queue = deque([start])
    while queue:
        state = queue.popleft()
        for nxt in successors(state):
            assert nxt in states
            if nxt not in d:
                d[nxt] = d[state] + 1
                queue.append(nxt)
    assert len(d) == len(states)
    return tuple(Counter(d.values())[i] for i in range(max(d.values())+1))


def direct_domination(n):
    edges = tuple(combinations(range(n), 2))
    k = (n - 1)//2
    def dominant(selection):
        covered = set()
        for e in selection:
            covered.update(e)
        # Every edge with both endpoints outside covered is undominated.
        return len(covered) >= n-1
    for size in range(k):
        assert not any(dominant(s) for s in combinations(edges, size))
    count = sum(dominant(s) for s in combinations(edges, k))
    assert count == factorial(n)//(2**k*factorial(k))
    return count

if __name__ == '__main__':
    expected = {
      1: (1, 2),
      2: (1, 4, 8, 2),
      3: (1, 6, 24, 54, 20),
      4: (1, 8, 48, 204, 464, 208, 12),
      5: (1, 10, 80, 500, 2120, 4880, 2524, 280),
    }
    for k in range(1, 6):
        got = profile(k)
        assert got == expected[k], (k, got)
        print('k=', k, 'vertices=', sum(got), 'distance-profile=', list(got), 'PASS')
    for n in (3, 5, 7, 9):
        print('n=', n, 'minimum dominating sets=', direct_domination(n), 'PASS')
    print('GRAPH_BFS_PASS')
