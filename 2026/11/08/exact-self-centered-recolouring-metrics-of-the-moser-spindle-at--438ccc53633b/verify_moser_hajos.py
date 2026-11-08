#!/usr/bin/env python3
"""Exhaustive check for named-colour one-vertex recolouring on the 7-vertex Hajós graph.
Uses two K4-minus-edge diamonds; no external Python packages are needed.
"""
from collections import Counter, deque
from itertools import permutations


def graph():
    # On each diamond {u,t,a,b}, the only missing edge is ut.
    edges = set()
    for u, t, a, b in ((0, 1, 2, 3), (0, 4, 5, 6)):
        for x, y in ((u, a), (u, b), (t, a), (t, b), (a, b)):
            edges.add(tuple(sorted((x, y))))
    edges.add((1, 4))
    return sorted(edges)


def canonical(c):
    encountered = {}
    return tuple(encountered.setdefault(x, len(encountered)) for x in c)


def run(k):
    edges = graph()
    assert len(edges) == 11
    lower_neighbors = [set() for _ in range(7)]
    for a, b in edges:
        lower_neighbors[b].add(a)
    colors = [-1] * 7
    states = []

    def rec(pos):
        if pos == 7:
            states.append(tuple(colors))
            return
        for col in range(k):
            if all(colors[v] != col for v in lower_neighbors[pos]):
                colors[pos] = col
                rec(pos + 1)
        colors[pos] = -1

    rec(0)
    states.sort()
    ix = {c: i for i, c in enumerate(states)}
    assert len(ix) == len(states)
    adj = []
    for c in states:
        neighbors = []
        for at in range(7):
            for new in range(k):
                if new != c[at]:
                    candidate = c[:at] + (new,) + c[at+1:]
                    if candidate in ix:
                        neighbors.append(ix[candidate])
        adj.append(sorted(neighbors))
    assert all(i in adj[j] for i, neighbors in enumerate(adj) for j in neighbors)
    n = len(states)
    counts = Counter(map(len, adj))
    m = sum(map(len, adj)) // 2
    distance_hist = Counter()
    ecc = Counter()
    for source in range(n):
        dist = [-1] * n
        dist[source] = 0
        frontier = deque([source])
        while frontier:
            v = frontier.popleft()
            for w in adj[v]:
                if dist[w] == -1:
                    dist[w] = dist[v] + 1
                    frontier.append(w)
        assert all(d >= 0 for d in dist), 'disconnected'
        ecc[max(dist)] += 1
        distance_hist.update(d for t, d in enumerate(dist) if t > source)
    assert sum(distance_hist.values()) == n * (n - 1) // 2
    unlabeled = {canonical(c) for c in states}
    output = {
        'k': k, 'states': n, 'edges': m,
        'unlabeled_partitions': len(unlabeled),
        'degree_hist': dict(sorted(counts.items())),
        'ecc_hist': dict(sorted(ecc.items())),
        'radius': min(ecc), 'diameter': max(ecc),
        'pair_distance_hist': dict(sorted(distance_hist.items()))
    }
    print(output, flush=True)
    return output


if __name__ == '__main__':
    a, b = run(4), run(5)
    assert (a['states'], a['edges'], a['unlabeled_partitions'], a['radius'], a['diameter']) == (384, 528, 16, 13, 13)
    assert (b['states'], b['edges'], b['unlabeled_partitions'], b['radius'], b['diameter']) == (5040, 22560, 42, 10, 10)
    print('PYTHON_EXHAUSTIVE_BOTH_PALETTES_PASS')
