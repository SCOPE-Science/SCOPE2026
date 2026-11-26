#!/usr/bin/env python3
"""Independent, standard-library finite checks for an elementary graph construction.

Usage: python3 verify.py
The checks verify stated finite instances only; structural assertions for all
finite graphs follow from the separate combinatorial proof.
"""
from collections import Counter


def new_graph():
    return {}


def add_vertex(g):
    v = len(g)
    g[v] = set()
    return v


def add_edge(g, a, b):
    assert a != b
    g[a].add(b)
    g[b].add(a)


def make_graph(core_edges, k):
    # A core is a tree on k vertices with maximum degree at most three.
    assert k >= 1
    r = [set() for _ in range(k)]
    for a, b in core_edges:
        r[a].add(b)
        r[b].add(a)
    assert all(len(x) <= 3 for x in r)
    assert len(core_edges) == k - 1
    # Complete the degrees of core vertices to three by adding leaves.
    t = new_graph()
    for _ in range(k):
        add_vertex(t)
    for a, b in core_edges:
        add_edge(t, a, b)
    for a in range(k):
        for _ in range(3 - len(r[a])):
            b = add_vertex(t)
            add_edge(t, a, b)
    return graph_from_tree(t), t


def graph_from_tree(t):
    g = {a: set() for a in t}
    for a in t:
        for b in t[a]:
            if a < b:
                u, v = add_vertex(g), add_vertex(g)
                add_edge(g, a, u)
                add_edge(g, u, v)
                add_edge(g, v, b)
    for a in t:
        if len(t[a]) == 1:
            u, v = add_vertex(g), add_vertex(g)
            add_edge(g, a, u)
            add_edge(g, u, v)
            add_edge(g, v, a)
    return g


def inverse_tree(g):
    h = {v for v in g if len(g[v]) == 3}
    ell = set(g) - h
    assert len(ell) == 3 * len(h)
    assert all(len(g[v]) == 2 for v in ell)
    assert all(g[v] <= ell for v in h)
    t = {v: set() for v in h}
    loops = Counter()
    visited = set()
    for v in ell:
        assert len(g[v] & h) == 1 and len(g[v] & ell) == 1
        if v in visited:
            continue
        w = next(iter(g[v] & ell))
        assert w not in visited
        visited.update([v, w])
        a = next(iter(g[v] & h))
        b = next(iter(g[w] & h))
        if a == b:
            loops[a] += 1
        else:
            assert b not in t[a]  # Parallel edges impossible in this construction.
            add_edge(t, a, b)
    assert len(visited) == len(ell)
    assert all(len(t[v]) + 2 * loops[v] == 3 for v in h)
    return t, loops


def stable_colors(g):
    colors = {v: 0 for v in g}
    for step in range(len(g) + 1):
        sig = {v: (colors[v], tuple(sorted(Counter(colors[u] for u in g[v]).items())))
               for v in g}
        ids = {x: i for i, x in enumerate(sorted(set(sig.values())))}
        new = {v: ids[sig[v]] for v in g}
        if len(set(new.values())) == len(set(colors.values())):
            return new, step + 1
        colors = new
    raise AssertionError('color refinement did not stabilize')


def blocks(g):
    # Edge-stack Tarjan biconnected-component algorithm.
    discovery, low, stack, answer = {}, {}, [], []

    def dfs(u, parent):
        discovery[u] = low[u] = len(discovery)
        for v in sorted(g[u]):
            if v == parent:
                continue
            if v not in discovery:
                stack.append((u, v))
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] >= discovery[u]:
                    component = set()
                    while True:
                        e = stack.pop()
                        component.update(e)
                        if e == (u, v):
                            break
                    answer.append(component)
            elif discovery[v] < discovery[u]:
                low[u] = min(low[u], discovery[v])
                stack.append((u, v))

    dfs(min(g), None)
    assert len(discovery) == len(g)
    assert not stack
    return answer


def check(g, t, k):
    assert len(t) == 2 * k + 2
    assert len(g) == 8 * k + 8
    assert Counter(map(len, g.values())) == Counter({2: 6 * k + 6, 3: 2 * k + 2})
    assert sum(map(len, g.values())) // 2 == 9 * (k + 1)
    reconstructed, loops = inverse_tree(g)
    assert reconstructed == t
    assert sum(loops.values()) == k + 2
    for block in blocks(g):
        assert all((block - {v}) <= g[v] for v in block), 'block not clique'
    colors, iterations = stable_colors(g)
    assert len(set(colors.values())) == 2
    h = [v for v in g if len(g[v]) == 3]
    assert len({colors[v] for v in h}) == 1
    return len(g), iterations


def disjoint_union(a, b):
    size = len(a)
    g = {v: set(neighbors) for v, neighbors in a.items()}
    for v, neighbors in b.items():
        g[size + v] = {size + u for u in neighbors}
    return g


def run():
    # The unique core shapes of orders 1, 2, 3 and the two shapes of order 4.
    small = {
        1: [[]],
        2: [[(0, 1)]],
        3: [[(0, 1), (1, 2)]],
        4: [[(0, 1), (1, 2), (2, 3)],
            [(0, 1), (0, 2), (0, 3)]],
    }
    for k, families in small.items():
        for edges in families:
            g, t = make_graph(edges, k)
            n, _ = check(g, t, k)
            print('core', k, 'order', n, 'block graph: yes; two stable colors: yes')

    a, ta = make_graph(small[4][0], 4)
    b, tb = make_graph(small[4][1], 4)
    # Isomorphisms preserve the degree-3 vertices and hence the inverse tree.
    # The induced subgraph on degree-three vertices of each inverse tree
    # has, respectively, maximum degree 2 and maximum degree 3.
    assert max(len(ta[v] & set(range(4))) for v in range(4)) == 2
    assert max(len(tb[v] & set(range(4))) for v in range(4)) == 3
    both = disjoint_union(a, b)
    colors, _ = stable_colors(both)
    assert Counter(colors[v] for v in range(len(a))) == Counter(
        colors[v] for v in range(len(a), len(a) + len(b)))
    assert len(set(colors.values())) == 2
    print('40-vertex nonisomorphic pair: joint color refinement indistinguishable')

    for k in range(1, 31):
        edges = [(i, i + 1) for i in range(k - 1)]
        g, t = make_graph(edges, k)
        check(g, t, k)
    print('30 additional path-core instances checked; all checks passed')


if __name__ == '__main__':
    run()
