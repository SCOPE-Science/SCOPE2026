"""Exact checks of a universal graph-metric numerical-index bound and its sharp triangle."""
from fractions import Fraction as Q
from itertools import combinations, product


def connected(n, edges):
    reached = {0}
    changed = True
    while changed:
        old = len(reached)
        for u, v in edges:
            if u in reached:
                reached.add(v)
            if v in reached:
                reached.add(u)
        changed = len(reached) != old
    return len(reached) == n


def distances(n, edges, weights):
    big = Q(10**6)
    d = [[Q(0) if i == j else big for j in range(n)] for i in range(n)]
    for (u, v), w in zip(edges, weights):
        d[u][v] = min(d[u][v], w)
        d[v][u] = min(d[v][u], w)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


def extreme_heights(n, edges):
    diam = int(max(distances(n, edges, [Q(1)] * len(edges))[0]))
    for values in product(range(-diam, diam + 1), repeat=n - 1):
        h = (0,) + values
        if any(abs(h[u] - h[v]) > 1 for u, v in edges):
            continue
        tight = [(u, v) for u, v in edges if abs(h[u] - h[v]) == 1]
        if connected(n, tight):
            yield h


def verify_graph(n, edges):
    assert connected(n, edges)
    checked = 0
    for h in extreme_heights(n, edges):
        assert all(isinstance(x, int) for x in h)
        weights = [Q(1) - Q(abs(h[u] - h[v]), 2) for u, v in edges]
        for u, v in edges:
            if h[u] != h[v]:
                assert abs(h[u] - h[v]) == 1
                continue
            d = distances(n, edges, weights)
            assert d[u][v] == 1
            k = [d[v][z] - d[v][0] for z in range(n)]
            plus = [k[z] + Q(h[z], 2) for z in range(n)]
            minus = [k[z] - Q(h[z], 2) for z in range(n)]
            assert plus[0] == minus[0] == 0
            assert plus[u] - plus[v] == 1
            assert minus[u] - minus[v] == 1
            assert all(plus[z] - minus[z] == h[z] for z in range(n))
            assert all(abs(plus[a] - plus[b]) <= 1 and abs(minus[a] - minus[b]) <= 1
                       for a, b in edges)
            checked += 1
    return checked


def triangle_sharpness():
    hverts = list(extreme_heights(3, [(0, 1), (0, 2), (1, 2)]))
    assert set(hverts) == {(0, 1, 0), (0, 0, 1), (0, 1, 1),
                           (0, -1, 0), (0, 0, -1), (0, -1, -1)}
    m = [(Q(1), Q(0)), (Q(0), Q(1)), (Q(1), Q(-1))]
    def T(x):
        a, b = x
        return (Q(-1, 2) * a, a + Q(1, 2) * b)
    def f(h, x):
        return h[1] * x[0] + h[2] * x[1]
    operator_norm = max(abs(f(h, T(x))) for h in hverts for x in m)
    numerical_radius = max(abs(f(h, T(x))) for h in hverts for x in m if f(h, x) == 1)
    assert operator_norm == 1 and numerical_radius == Q(1, 2)


def main():
    total_graphs = 0
    total_checks = 0
    for n in range(2, 5):
        possible_edges = list(combinations(range(n), 2))
        for mask in range(1, 1 << len(possible_edges)):
            edges = [e for i, e in enumerate(possible_edges) if mask & (1 << i)]
            if connected(n, edges):
                total_graphs += 1
                total_checks += verify_graph(n, edges)
    for n, edges in [
        (5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]),
        (5, [(0, i) for i in range(1, 5)] + [(1, 2), (2, 3), (3, 4), (4, 1)]),
        (5, list(combinations(range(5), 2))),
        (5, [(0, 1), (1, 2), (2, 3), (3, 4)]),
        (5, [(u, v) for u in range(2) for v in range(2, 5)])
    ]:
        total_graphs += 1
        total_checks += verify_graph(n, edges)
    triangle_sharpness()
    print(f"VERIFY_OK graphs={total_graphs} zero-edge_face_checks={total_checks} triangle_norm=1 triangle_radius=1/2")

if __name__ == '__main__':
    main()
