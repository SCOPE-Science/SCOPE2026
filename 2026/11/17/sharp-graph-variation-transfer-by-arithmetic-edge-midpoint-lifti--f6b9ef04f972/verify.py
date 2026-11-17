#!/usr/bin/env python3
"""Exact independent checks for midpoint-lift graph variation formulas."""
from fractions import Fraction
from itertools import combinations
from collections import deque


def connected(n, edges):
    reached = {0}
    while True:
        new = reached | {v for u, v in edges if u in reached} | {u for u, v in edges if v in reached}
        if new == reached:
            return len(new) == n
        reached = new


def cut_data(n, edges, mask):
    neighbours = [[] for _ in range(n)]
    for u, v in edges:
        neighbours[u].append(v)
        neighbours[v].append(u)
    bd = sum(((mask >> u) & 1) != ((mask >> v) & 1) for u, v in edges)
    if bd == 0:
        return Fraction(0), False
    wedge = sum(sum((mask >> v) & 1 for v in neighbours[u]) *
                (len(neighbours[u]) - sum((mask >> v) & 1 for v in neighbours[u]))
                for u in range(n))
    ratio = Fraction(wedge, 2 * bd)
    boundary = [u for u in range(n) if any(((mask >> u) & 1) != ((mask >> v) & 1)
                   for v in neighbours[u])]
    equality = all(all(v == u or v in neighbours[u]
                       for v in range(n) if ((mask >> v) & 1) == ((mask >> u) & 1))
                   for u in boundary)
    return ratio, equality


def direct_midpoint_ratio(n, edges, mask):
    values = [(mask >> i) & 1 for i in range(n)]
    midpoint = [Fraction(values[u] + values[v], 2) for u, v in edges]
    out = sum(abs(midpoint[i] - midpoint[j])
              for i in range(len(edges)) for j in range(i + 1, len(edges))
              if len(set(edges[i]) & set(edges[j])) == 1)
    den = sum(abs(values[u] - values[v]) for u, v in edges)
    return out / den if den else Fraction(0)


def check():
    total_graphs = total_cuts = total_trees = 0
    for n in range(2, 6):
        possible = list(combinations(range(n), 2))
        for encoded in range(1, 1 << len(possible)):
            edges = [edge for idx, edge in enumerate(possible) if encoded & (1 << idx)]
            if not connected(n, edges):
                continue
            total_graphs += 1
            degrees = [sum(i in e for e in edges) for i in range(n)]
            vals = []
            eq_conditions = []
            for mask in range(1, 1 << (n - 1)):
                ratio, eq_condition = cut_data(n, edges, mask)
                assert ratio == direct_midpoint_ratio(n, edges, mask)
                assert (ratio == Fraction(n - 2, 2)) == eq_condition
                vals.append(ratio)
                eq_conditions.append(eq_condition)
                total_cuts += 1
            gain = max(vals)
            assert gain <= Fraction(n - 2, 2)
            assert (gain == Fraction(n - 2, 2)) == any(eq_conditions)
            if len(edges) == n - 1:
                total_trees += 1
                edge_degree = max(degrees[u] + degrees[v] - 2 for u, v in edges)
                assert gain == Fraction(edge_degree, 2)
                assert (gain <= 1) == (max(degrees[u] + degrees[v] for u, v in edges) <= 4)
        print('CONNECTED_GRAPHS_N', n, 'PASS', flush=True)
    print('EXACT_CUT_WEDGE_AND_RIGIDITY_PASS', total_graphs, total_cuts, flush=True)
    print('TREE_DEGREE_FORMULA_PASS', total_trees, flush=True)
    for n in range(2, 13):
        path = [(i, i + 1) for i in range(n - 1)]
        star = [(0, i) for i in range(1, n)]
        complete = list(combinations(range(n), 2))
        cycle = path + ([(n-1, 0)] if n >= 3 else [])
        def exact(edges):
            return max(cut_data(n, edges, mask)[0]
                       for mask in range(1, 1 << (n - 1)))
        assert exact(star) == Fraction(n - 2, 2)
        assert exact(complete) == Fraction(n - 2, 2)
        assert exact(path) == (Fraction(0) if n == 2 else
                               Fraction(1, 2) if n == 3 else Fraction(1))
        if n >= 3:
            assert exact(cycle) == (Fraction(1, 2) if n == 3 else Fraction(1))
    print('PATH_STAR_COMPLETE_CYCLE_CROSSCHECK_PASS', flush=True)
    print('ALL_MIDPOINT_LIFT_EXACT_CHECKS_PASS', flush=True)

if __name__ == '__main__':
    check()
