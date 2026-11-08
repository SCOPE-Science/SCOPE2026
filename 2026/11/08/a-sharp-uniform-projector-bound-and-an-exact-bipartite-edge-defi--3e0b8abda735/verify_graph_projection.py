#!/usr/bin/env python3
"""Exact rational checks for sharp graph-spline projector bounds.
Run: python verify_graph_projection.py
No external packages required.
"""
from fractions import Fraction as F
from random import Random
from collections import deque


def inverse(m):
    n = len(m)
    a = [[F(x) for x in row] + [F(i == j) for j in range(n)]
         for i, row in enumerate(m)]
    for i in range(n):
        pivot = next(j for j in range(i, n) if a[j][i])
        a[i], a[pivot] = a[pivot], a[i]
        v = a[i][i]
        a[i] = [x / v for x in a[i]]
        for j in range(n):
            if j == i:
                continue
            v = a[j][i]
            if v:
                a[j] = [x - v * y for x, y in zip(a[j], a[i])]
    return [row[n:] for row in a]


def mass(n, edges, atoms):
    m = [[F(0) for j in range(n)] for i in range(n)]
    for i, a in enumerate(atoms):
        m[i][i] += a
    for i, j, w in edges:
        m[i][i] += w / 3
        m[j][j] += w / 3
        m[i][j] += w / 6
        m[j][i] += w / 6
    return m


def bipartition(n, edges):
    adj = [[] for _ in range(n)]
    for i, j, w in edges:
        adj[i].append(j)
        adj[j].append(i)
    signs = [None] * n
    signs[0] = 1
    queue = deque([0])
    while queue:
        i = queue.popleft()
        for j in adj[i]:
            if signs[j] is None:
                signs[j] = -signs[i]
                queue.append(j)
            elif signs[j] == signs[i]:
                return None
    return signs


def edge_integral(a, b, w):
    if a * b >= 0:
        return w * (abs(a) + abs(b)) / 2
    u, v = abs(a), abs(b)
    return w * (u * u + v * v) / (2 * (u + v))


def projector_profile(n, edges, atoms):
    m = mass(n, edges, atoms)
    ainv = inverse(m)
    norms = []
    for v in range(n):
        row = ainv[v]
        norms.append(sum((atoms[j] * abs(row[j]) for j in range(n)), F(0))
                     + sum((edge_integral(row[i], row[j], w)
                            for i, j, w in edges), F(0)))
    return ainv, norms


def check(n, edges, atoms):
    a, norms = projector_profile(n, edges, atoms)
    assert max(norms) < 3, (n, edges, atoms, norms)
    sg = bipartition(n, edges)
    if sg is not None:
        for v in range(n):
            for j in range(n):
                assert a[v][j] * sg[v] * sg[j] > 0
            deficit = 2 * sum((atoms[j] * abs(a[v][j])
                               for j in range(n)), F(0))
            deficit += sum((w * abs(a[v][i]) * abs(a[v][j]) /
                            (abs(a[v][i]) + abs(a[v][j]))
                            for i, j, w in edges), F(0))
            assert norms[v] == 3 - deficit
        assert max(norms) == 3 - min(3 - x for x in norms)
    return sg is not None


def run():
    rng = Random(20261102)
    graphs = 0
    bipartite_graphs = 0
    for n in range(2, 9):
        for rep in range(80):
            # A random tree, augmented by optional extra edges.
            pairs = {(j, rng.randrange(j)) for j in range(1, n)}
            pairs = {(min(i, j), max(i, j)) for i, j in pairs}
            for i in range(n):
                for j in range(i + 1, n):
                    if rng.randrange(5) == 0:
                        pairs.add((i, j))
            edges = [(i, j, F(rng.randrange(1, 10), rng.randrange(1, 8)))
                     for i, j in sorted(pairs)]
            atoms = [F(0) if rng.randrange(3) else
                     F(rng.randrange(1, 5), rng.randrange(1, 7))
                     for _ in range(n)]
            bipartite_graphs += check(n, edges, atoms)
            graphs += 1
    print('RATIONAL_CONNECTED_GRAPH_PROFILES_OK', graphs, 'bipartite', bipartite_graphs)
    for n in range(3, 12):
        values = []
        for ratio in [F(10), F(100), F(1000)]:
            edges = [(i, i + 1, ratio ** i) for i in range(n - 1)]
            a, norms = projector_profile(n, edges, [F(0)] * n)
            target = F(3) - F(2 ** max(4 - n, 0), 3 * 2 ** max(n - 4, 0))
            assert norms[0] < target
            values.append(norms[0])
        assert values[0] < values[1] < values[2]
        assert target - values[-1] < F(1, 100)  # finite-r convergence
    print('GEOMETRIC_PATH_SHARPNESS_CHECKS_OK', 9, 3)
    # Exact endpoint on one edge: the familiar rank-two linear projection.
    edges = [(0, 1, F(1))]
    a, norms = projector_profile(2, edges, [F(0), F(0)])
    assert a == [[F(4), F(-2)], [F(-2), F(4)]]
    assert norms == [F(5, 3), F(5, 3)]
    print('SINGLE_EDGE_EXACT_PROFILE_OK', norms[0])
    # Verify the vertex-atom deficit is not silently omitted.
    edges = [(0, 1, F(1)), (1, 2, F(2))]
    atoms = [F(1, 2), F(0), F(3, 7)]
    assert check(3, edges, atoms)
    print('POSITIVE_VERTEX_ATOM_DEFICIT_OK')
    print('ALL_GRAPH_SPLINE_PROJECTION_CHECKS_OK')


if __name__ == '__main__':
    run()
