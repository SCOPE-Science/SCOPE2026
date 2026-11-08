"""Independent finite checks for rooted-tree order-polytope surface areas.

Requirements: Python 3, networkx, numpy, scipy. Run: python checker.py
All computations here are finite; the proof of the theorem is analytical.
"""
import itertools
import math
from fractions import Fraction

import networkx as nx
import numpy as np
from scipy.spatial import ConvexHull


def rooted_parent(graph, root):
    parent = {root: None}
    order = [root]
    for u in order:
        for v in graph.neighbors(u):
            if v not in parent:
                parent[v] = u
                order.append(v)
    return parent, order


def hook_volume(graph, root):
    parent, order = rooted_parent(graph, root)
    hooks = {u: 1 for u in order}
    for u in reversed(order[1:]):
        hooks[parent[u]] += hooks[u]
    product = math.prod(hooks.values())
    return Fraction(1, product)


def facet_area_pair(graph, root):
    """Exact area in the basis (1, sqrt(2)) from all facet classes."""
    parent, order = rooted_parent(graph, root)
    volume = hook_volume(graph, root)
    rational = len(graph) * volume  # root lower facet
    radical = Fraction(0)
    for u in order:
        if len(graph[u]) == 1 and u != root:
            reduced = graph.copy()
            reduced.remove_node(u)
            rational += hook_volume(reduced, root)
    for u in order[1:]:
        contracted = nx.contracted_nodes(graph, parent[u], u, self_loops=False)
        radical += hook_volume(contracted, root)
    return rational, radical


def upper_ideals_vertices(graph, root):
    parent, order = rooted_parent(graph, root)
    verts = []
    for bits in itertools.product((0, 1), repeat=len(order)):
        values = dict(zip(order, bits))
        if all(values[parent[u]] <= values[u] for u in order[1:]):
            verts.append([values[u] for u in order])
    return np.asarray(verts, dtype=float)


def predicted_extrema(n):
    f = math.factorial(n-1)
    chain = (Fraction(2, f), Fraction(n-1, f))
    fork = (Fraction(4, f), Fraction(2*(n-2), f))
    broom = (Fraction(1), Fraction(n+1, 2*(n-1)))
    star = (Fraction(2), Fraction(1))
    return (chain, fork, broom, star)


def near(a, b):
    return abs(a-b) <= 1.0e-8 * max(1.0, abs(b))


def evaluate_pair(pair):
    return float(pair[0]) + math.sqrt(2.0)*float(pair[1])


def verify():
    hull_count = 0
    rooted_count = 0
    second_rank_count = 0
    for n in range(4, 11):
        profiles = []
        for tree in nx.nonisomorphic_trees(n):
            for root in tree.nodes():
                parent, order = rooted_parent(tree, root)
                pair = facet_area_pair(tree, root)
                val = evaluate_pair(pair)
                profiles.append((val, pair, tree, root))
                rooted_count += 1
                if n <= 6:
                    verts = upper_ideals_vertices(tree, root)
                    area = ConvexHull(verts).area
                    assert near(val, area), (n, root, val, area)
                    hull_count += 1
        chain, fork, broom, star = predicted_extrema(n)
        levels = sorted({p[1] for p in profiles}, key=evaluate_pair)
        assert levels[0] == chain, ('chain', n)
        assert levels[1] == fork, ('fork', n)
        assert levels[-2] == broom, ('broom', n)
        assert levels[-1] == star, ('star', n)
        second_rank_count += 4
        # Equality profiles have the asserted rooted-tree structures.
        for val, pair, tree, root in profiles:
            parent, order = rooted_parent(tree, root)
            ch = {u:0 for u in order}
            for v in order[1:]: ch[parent[v]] += 1
            leaves = sum(ch[u] == 0 for u in order)
            if pair == chain:
                assert leaves == 1
            if pair == fork:
                assert leaves == 2 and sum(ch[u] == 2 for u in order) == 1 and max(ch.values()) == 2 and ch[root] == 1
            if pair == star:
                assert ch[root] == n-1
            if pair == broom:
                assert ch[root] == n-2 and max(ch.values()) == n-2 and sorted(ch.values(),reverse=True)[1] == 1
    print('ROOTED_TREE_ORDER_POLYTOPE_CHECKS_PASSED', rooted_count, hull_count, second_rank_count)


if __name__ == '__main__':
    verify()
