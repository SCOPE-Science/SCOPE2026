"""Direct enumeration of isolating sets and their reconfiguration graph.

Only Python standard library required.  The test of isolation uses the original
Kneser-graph adjacency, not an edge-shape characterization.
"""
from collections import Counter, deque
from itertools import combinations
from math import comb


def edge_shape(edges, chosen):
    degree = Counter(v for index in chosen for v in edges[index])
    return tuple(sorted(degree.values(), reverse=True))


def check(n):
    edges = tuple(combinations(range(n), 2))
    m = len(edges)
    # Closed neighborhood of each vertex of the Kneser graph.
    closed = []
    for e in edges:
        covered = 0
        for j, f in enumerate(edges):
            if e == f or (e[0] not in f and e[1] not in f):
                covered |= 1 << j
        closed.append(covered)
    # Independent remainder iff no pair of remaining vertices is disjoint.
    adjacent = []
    for e in edges:
        mask = 0
        for j, f in enumerate(edges):
            if e[0] not in f and e[1] not in f:
                mask |= 1 << j
        adjacent.append(mask)
    universe = (1 << m) - 1

    def isolating(chosen):
        remaining = universe
        for index in chosen:
            remaining &= ~closed[index]
        for i in range(m):
            if (remaining >> i) & 1 and remaining & adjacent[i]:
                return False
        return True

    for k in range(3):
        assert all(not isolating(s) for s in combinations(range(m), k)), (n, k)

    solutions = {tuple(s) for s in combinations(range(m), 3) if isolating(s)}
    expected = comb(m, 3) - 12 * comb(n, 4)
    assert len(solutions) == expected, (n, len(solutions), expected)

    # The path of three edges has degree multiset (2,2,1,1).
    type_counts = Counter()
    degree_profile = Counter()
    graph = {}
    for s in solutions:
        shape = edge_shape(edges, s)
        assert shape in {(3, 1, 1, 1), (2, 2, 2), (2, 1, 1, 1, 1), (1, 1, 1, 1, 1, 1)}
        type_counts[shape] += 1
        S = set(s)
        neighbors = set()
        for old in s:
            for new in range(m):
                if new not in S:
                    nxt = tuple(sorted((S - {old}) | {new}))
                    if nxt in solutions:
                        neighbors.add(nxt)
        graph[s] = neighbors
        degree_profile[(shape, len(neighbors))] += 1

    desired_counts = {
        (3, 1, 1, 1): n * comb(n - 1, 3),
        (2, 2, 2): comb(n, 3),
        (2, 1, 1, 1, 1): n * comb(n - 1, 2) * comb(n - 3, 2),
        (1, 1, 1, 1, 1, 1): 15 * comb(n, 6) if n >= 6 else 0,
    }
    assert all(type_counts[t] == count for t, count in desired_counts.items())
    expected_degree = {
        (3, 1, 1, 1): 3 * comb(n - 2, 2),
        (2, 2, 2): 3 * comb(n - 2, 2),
        (2, 1, 1, 1, 1): (3 * n * n - 7 * n - 22) // 2,
        (1, 1, 1, 1, 1, 1): (3 * n * n - 3 * n - 42) // 2,
    }
    assert all(degree_profile[(t, expected_degree[t])] == count
               for t, count in desired_counts.items())
    assert sum(len(v) for v in graph.values()) % 2 == 0
    # Full distance census up to n=7; a whole-graph connectivity check at n=8.
    diameter = 0
    sources = solutions if n <= 7 else {next(iter(solutions))}
    for s in sources:
        dist = {s: 0}
        q = deque([s])
        while q:
            v = q.popleft()
            for w in graph[v]:
                if w not in dist:
                    dist[w] = dist[v] + 1
                    q.append(w)
        assert len(dist) == len(solutions), (n, s, len(dist))
        diameter = max(diameter, max(dist.values()))
    if n <= 7:
        assert diameter == 3
    else:
        assert diameter >= 3  # The all-n upper bound is checked separately.
    print('n={} minimum=3 configurations={} edges={} connected=1 {}={} types={}'.format(
        n, len(solutions), sum(map(len, graph.values())) // 2,
        'full_diameter' if n <= 7 else 'one_source_eccentricity', diameter,
        [(str(t), type_counts[t]) for t in sorted(type_counts)]))


if __name__ == '__main__':
    for n in range(5, 9):
        check(n)
    print('PASS: all subsets, transitions, n<=7 distance census, n=8 connectivity')
