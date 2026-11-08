#!/usr/bin/env python3
"""Exact verification of four-arrival root selection on two-hub trees.

Run: python checker.py. Dependencies: networkx>=3.6,<3.7; sympy>=1.14,<1.15.
"""
from itertools import product
from math import comb
import networkx as nx
from sympy import symbols, ff, expand, factor

A, B = symbols('a b', integer=True)


def two_hub_tree(a, b):
    """Central junction 0, hubs 1,2, central leaf 3; a,b outer leaves."""
    assert a >= 1 and b >= 1
    g = nx.Graph()
    g.add_edges_from([(0, 1), (0, 2), (0, 3)])
    for j in range(a):
        g.add_edge(1, 4 + j)
    for j in range(b):
        g.add_edge(2, 4 + a + j)
    return g


def tree_parents(g, root):
    parents = {root: None}
    queue = [root]
    for v in queue:
        for w in g[v]:
            if w not in parents:
                parents[w] = v
                queue.append(w)
    assert len(parents) == len(g)
    return parents, queue


def direct_success(parents, preferences):
    occupied = set()
    for start in preferences:
        v = start
        while v is not None and v in occupied:
            v = parents[v]
        if v is None:
            return False
        occupied.add(v)
    return True


def parking_count(g, root, m):
    """Coefficient DP in the binomial (labeled-sequence) basis, all integers."""
    parents, order = tree_parents(g, root)
    state = {}
    for v in reversed(order):
        current = {(0, 0): 1}
        for child in g[v]:
            if parents[child] != v:
                continue
            next_state = {}
            for (overflow, k), a in current.items():
                for (child_overflow, ell), b in state[child].items():
                    if k + ell > m:
                        continue
                    key = (overflow + child_overflow, k + ell)
                    next_state[key] = next_state.get(key, 0) + a*b*comb(k + ell, k)
            current = next_state
        next_state = {}
        for (overflow, k), count in current.items():
            for cars_at_vertex in range(m - k + 1):
                key = (max(0, overflow + cars_at_vertex - 1), k + cars_at_vertex)
                next_state[key] = next_state.get(key, 0) + count*comb(k + cars_at_vertex, cars_at_vertex)
        state[v] = next_state
    return state[root].get((0, m), 0)


def orbit_key(tup, core, group_a, group_b):
    group_a, group_b = set(group_a), set(group_b)
    maps = [{}, {}]
    key = []
    for vertex in tup:
        if vertex in group_a:
            m = maps[0]
            if vertex not in m: m[vertex] = len(m)
            key.append(('A', m[vertex]))
        elif vertex in group_b:
            m = maps[1]
            if vertex not in m: m[vertex] = len(m)
            key.append(('B', m[vertex]))
        else:
            assert vertex in core
            key.append(('C', vertex))
    return tuple(key), len(maps[0]), len(maps[1])


def root_class_polynomial(which):
    """Orbit enumeration: each successful pattern gets falling-factorial multiplicity."""
    g = two_hub_tree(5, 5)
    roots = {'center': 0, 'hub_a': 1, 'hub_b': 2,
             'central_leaf': 3, 'outer_a': 4, 'outer_b': 9}
    root = roots[which]
    core = {0, 1, 2, 3}
    group_a = list(range(4, 9))
    group_b = list(range(9, 14))
    da = db = 0
    if which == 'outer_a':
        core.add(4); group_a.remove(4); da = 1
    if which == 'outer_b':
        core.add(9); group_b.remove(9); db = 1
    parent, _ = tree_parents(g, root)
    patterns = {}
    for tup in product(g.nodes, repeat=4):
        key, ka, kb = orbit_key(tup, core, group_a, group_b)
        if key not in patterns:
            patterns[key] = (ka, kb, direct_success(parent, tup))
    polynomial = 0
    for ka, kb, ok in patterns.values():
        if ok:
            polynomial += ff(A-da, ka)*ff(B-db, kb)
    return expand(polynomial)


def verify():
    # Independent exhaustive probability enumeration for the ten-vertex witness.
    witness = two_hub_tree(3, 3)
    expected = {
        4: {'center':8898, 'hub_a':8855, 'central_leaf':9290, 'outer_a':9263},
        5: {'center':76140, 'hub_a':76650, 'central_leaf':85500, 'outer_a':85378}
    }
    class_roots = {'center':0,'hub_a':1,'central_leaf':3,'outer_a':4}
    for m in (4, 5):
        for cls, root in class_roots.items():
            parent, _ = tree_parents(witness, root)
            direct = sum(direct_success(parent, t) for t in product(range(10), repeat=m))
            assert direct == expected[m][cls]
            assert parking_count(witness, root, m) == direct
    print('PASS: independent direct enumeration of 10^4 and 10^5 preference tuples per rooted orbit')

    # All unlabelled tree shapes through ten vertices and every admissible load.
    tree_type_counts = [1,1,1,2,3,6,11,23,47,106]
    counterexamples = []
    comparisons = 0
    for n in range(1,11):
        count = 0
        for g in nx.nonisomorphic_trees(n) if n >= 2 else [nx.path_graph(1)]:
            count += 1
            diameter = nx.diameter(g)
            ecc = nx.eccentricity(g)
            endpoints = {v for v in g if ecc[v] == diameter}
            for m in range(1, n+1):
                values = {root:parking_count(g, root, m) for root in g}
                comparisons += len(g)
                if max(values[v] for v in endpoints) < max(values.values()):
                    counterexamples.append((n, m, g))
        assert count == tree_type_counts[n-1], (n, count)
    assert [(n,m) for n,m,g in counterexamples] == [(10,4),(10,5)]
    assert all(nx.is_isomorphic(g,witness) for _,_,g in counterexamples)
    print('PASS: 201 isomorphism types of trees on 1..10 vertices, all loads 1..n')
    print('PASS: only failure is B(3,3) at m=4 or m=5; rooted comparisons',comparisons)

    # A separate exact orbit polynomial computation, valid for ALL a,b >= 1.
    polynomials = {cls:root_class_polynomial(cls) for cls in
                   ('center','hub_a','hub_b','central_leaf','outer_a','outer_b')}
    central = polynomials['central_leaf']
    expected_deltas = {
        'center': 59*(A+B)+38,
        'hub_a': A*(19*A+16*B+40),
        'hub_b': B*(16*A+19*B+40),
        'outer_a': 27*(A-2),
        'outer_b': 27*(B-2),
    }
    for cls, val in expected_deltas.items():
        assert expand(central - polynomials[cls] - val) == 0, cls
    for a,b in ((1,1),(2,3),(3,3),(4,7),(7,4)):
        g=two_hub_tree(a,b)
        roots={'center':0,'hub_a':1,'hub_b':2,
               'central_leaf':3,'outer_a':4,'outer_b':4+a}
        for cls,root in roots.items():
            assert int(polynomials[cls].subs({A:a,B:b})) == parking_count(g,root,4)
    print('PASS: five exact four-car root-gap identities for every integer a,b >= 1')
    print('PASS: unique optimal central pendant root when a,b >= 3')
    print('ALL CHECKS PASSED')

if __name__ == '__main__':
    verify()
