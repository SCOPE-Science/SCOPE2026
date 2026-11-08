"""Exact finite tests of the Euclidean diameter-coloring theorem.

Run: python3 verify.py. Python standard library only.
These tests corroborate, but do not replace, the general proof.
"""
from itertools import combinations

TESTS = 0


def check(ok):
    global TESTS
    TESTS += 1
    if not ok:
        raise AssertionError('failed at assertion {}'.format(TESTS))


def source(n, edges):
    # Vector data: (edge index, type, tuple of length n+m).
    out = []
    for k, (u, v) in enumerate(edges):
        for typ, su, sv, se in (('t', 1, 1, -1), ('u', 1, -1, 1), ('v', -1, 1, 1)):
            a = [0] * (n + len(edges))
            a[u] = su
            a[v] = sv
            a[n + k] = se
            out.append((k, typ, tuple(a)))
    return out


def graph_connected(n, edges):
    if not edges:
        return False
    reached = {0}
    while True:
        expanded = reached | {v for u, v in edges if u in reached} | {u for u, v in edges if v in reached}
        if expanded == reached:
            break
        reached = expanded
    return len(reached) == n


def diameter_edges(n, edges):
    vs = source(n, edges)
    pairs = set()
    for i, j in combinations(range(len(vs)), 2):
        u, v = vs[i][2], vs[j][2]
        dist2 = sum((a - b) ** 2 for a, b in zip(u, v))
        check(dist2 in (4, 6, 8))
        if dist2 == 8:
            pairs.add((i, j))
        k, l = vs[i][0], vs[j][0]
        if k == l:
            expected = True
        else:
            # Each edge's node signs at the common endpoint determine distance.
            eu, ev = edges[k], edges[l]
            common = set(eu) & set(ev)
            expected = bool(common) and vs[i][2][next(iter(common))] != vs[j][2][next(iter(common))]
        check((dist2 == 8) == expected)
    return vs, pairs


def count_colorings(n, edge_pairs):
    neighbors = [set() for _ in range(n)]
    for u, v in edge_pairs:
        neighbors[u].add(v)
        neighbors[v].add(u)
    order = sorted(range(n), key=lambda i: -len(neighbors[i]))
    colors = [-1] * n

    def dfs(k):
        if k == n:
            return 1
        node = order[k]
        prohibited = {colors[v] for v in neighbors[node] if colors[v] != -1}
        total = 0
        for color in range(3):
            if color not in prohibited:
                colors[node] = color
                total += dfs(k + 1)
        colors[node] = -1
        return total
    return dfs(0)


def check_instance(n, edges, check_colors):
    m = len(edges)
    vs, pairs = diameter_edges(n, edges)
    check(len(vs) == 3 * m)
    degrees = [sum(v in e for e in edges) for v in range(n)]
    check(len(pairs) == 3 * m + 4 * sum(d * (d - 1) // 2 for d in degrees))
    # No four selected vertices have every pair diametral.
    for quad in combinations(range(len(vs)), 4):
        check(not all((min(i, j), max(i, j)) in pairs for i, j in combinations(quad, 2)))
    if check_colors:
        check(count_colorings(n, edges) == count_colorings(len(vs), pairs))


def main():
    instances = 0
    for n in range(2, 6):
        possible_edges = list(combinations(range(n), 2))
        for mask in range(1, 1 << len(possible_edges)):
            edges = [e for j, e in enumerate(possible_edges) if (mask >> j) & 1]
            if not graph_connected(n, edges):
                continue
            # Coloring comparison for all connected labeled graphs through 4 nodes.
            check_instance(n, edges, n <= 4)
            instances += 1
    print('PASS: {} assertions for {} connected labeled graphs, 2 <= n <= 5.'.format(TESTS, instances))


if __name__ == '__main__':
    main()
