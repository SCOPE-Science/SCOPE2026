"""Finite graph consistency tests for a graph Lipschitz-multiplier lower bound.

The infinite-dimensional theorem is proved analytically. These checks only
verify the graph metric, tent-profile and sharpness-witness identities.
Run with: python3 checker.py
"""
from collections import deque
from math import isqrt


def ladder(n):
    verts = [(i, j) for i in range(n) for j in (0, 1)]
    adjacency = {v: [] for v in verts}
    for i in range(n):
        adjacency[(i, 0)].append((i, 1))
        adjacency[(i, 1)].append((i, 0))
        for j in (0, 1):
            if i + 1 < n:
                adjacency[(i, j)].append((i + 1, j))
                adjacency[(i + 1, j)].append((i, j))
    return adjacency


def distances(adjacency, seeds):
    d = {v: 0 for v in seeds}
    q = deque(seeds)
    while q:
        u = q.popleft()
        for v in adjacency[u]:
            if v not in d:
                d[v] = d[u] + 1
                q.append(v)
    return d


def edge_lip(adjacency, f):
    return max(abs(f[u] - f[v]) for u in adjacency for v in adjacency[u])


def run():
    assertions = 0
    ratios = []
    for radius in (12, 30, 100, 300):
        graph = ladder(3 * radius + 10)
        u, v = (radius, 0), (radius + 1, 0)
        h = radius - isqrt(radius) - 1
        d = distances(graph, (u, v))
        root = (0, 0)
        tent = {z: max(0, h - d[z]) for z in graph}
        assert tent[root] == 0
        assert tent[u] == h == tent[v]
        assert edge_lip(graph, tent) == 1
        assertions += 4
        # The chosen edge is a constant-height plateau even in the presence
        # of many cycles.  Thus product differences measure only psi's jump.
        psi = {z: (-1)**z[0] / (z[0] + 1) for z in graph}
        product = {z: psi[z] * tent[z] for z in graph}
        jump = abs(product[u] - product[v])
        expected = h * abs(psi[u] - psi[v])
        assert abs(jump - expected) < 1e-10
        assert edge_lip(graph, product) + 1e-10 >= expected
        assertions += 2
        # All tent gradients disappear on the first floor(sqrt(radius))
        # graph-distance layers, the finite shadow of weak-null behavior.
        ball = distances(graph, (root,))
        cutoff = isqrt(radius)
        for z in graph:
            if ball[z] <= cutoff:
                assert tent[z] == 0
                assertions += 1
        ratio = jump / (radius * abs(psi[u] - psi[v]))
        assert abs(ratio - h / radius) < 1e-10
        assertions += 1
        ratios.append((radius, ratio, expected))
    assert ratios[-1][-1] > 1.7
    assertions += 1
    print(f"GRAPH_LIPSCHITZ_MULTIPLIER_TENT_CHECKS_OK {assertions}")
    for radius, ratio, lower_witness in ratios:
        print(f"radius={radius} height/radius={ratio:.7f} product_edge={lower_witness:.7f}")


if __name__ == '__main__':
    run()
