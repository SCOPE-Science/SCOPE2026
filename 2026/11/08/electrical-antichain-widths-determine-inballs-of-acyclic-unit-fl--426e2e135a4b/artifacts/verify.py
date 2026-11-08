"""Exact resistance identities and independent numeric inball checks for DAG unit-flow polytopes.

Dependencies: sympy>=1.11, numpy>=1.24, scipy>=1.10. Run: python artifacts/verify.py
Finite tests support but do not replace the proof of the general theorem.
"""
from __future__ import annotations

import itertools
import random
from collections import defaultdict
from fractions import Fraction

import numpy as np
import sympy as sp
from scipy.optimize import linprog


def directed_paths(n, edges):
    out = defaultdict(list)
    for e in edges:
        out[e[0]].append(e)
    def visit(u, acc):
        if u == n - 1:
            yield tuple(acc)
        for e in out[u]:
            yield from visit(e[1], acc + [e])
    return list(visit(0, []))


def profile(n, edges, metric):
    assert all(0 <= u < v < n for u, v in edges)
    assert len(set(edges)) == len(edges)
    paths = directed_paths(n, edges)
    assert len(paths) >= 2
    assert set.union(*(set(p) for p in paths)) == set(edges)
    assert set(a for e in edges for a in e) == set(range(n))
    m = len(edges)
    incidence = sp.zeros(n - 1, m)
    for j, (u, v) in enumerate(edges):
        if u < n-1:
            incidence[u, j] = 1
        if v < n-1:
            incidence[v, j] = -1
    qinv = sp.diag(*[sp.Rational(1, d) for d in metric])
    lred = incidence * qinv * incidence.T
    assert lred.det() > 0
    pdual = qinv - qinv * incidence.T * lred.inv() * incidence * qinv
    squared = [sp.factor(pdual[i, i]) for i in range(m)]
    assert all(a >= 0 for a in squared)
    assert (incidence * pdual) == sp.zeros(n - 1, m)
    # Coordinates with zero tangent projection are affine constants, not metric facets.
    alpha = np.sqrt(np.array([float(a) for a in squared]))
    route_idx = [{edges.index(e) for e in p} for p in paths]
    antichains = []
    for mask in range(1, 1 << m):
        subset = [j for j in range(m) if (mask >> j) & 1]
        if all(len(set(subset) & r) <= 1 for r in route_idx):
            antichains.append((float(sum(alpha[j] for j in subset)), tuple(subset)))
    width, _ = max(antichains)
    assert width > 0
    # An entirely independent LP in the path-mixture coordinates and radius.
    pmat = np.zeros((m, len(paths)))
    for k, s in enumerate(route_idx):
        for j in s:
            pmat[j, k] = 1
    npaths = len(paths)
    obj = np.zeros(npaths + 1)
    obj[-1] = -1
    inequalities = np.column_stack([-pmat, alpha])
    equalities = np.zeros((1, npaths + 1))
    equalities[0, :npaths] = 1
    opt = linprog(obj, A_ub=inequalities, b_ub=np.zeros(m),
                  A_eq=equalities, b_eq=np.array([1.]),
                  bounds=[(0, None)] * (npaths + 1), method='highs')
    assert opt.success, opt.message
    radius = opt.x[-1]
    assert abs(radius * width - 1) <= 3e-8, (edges, metric, radius, width)
    center = pmat @ opt.x[:npaths]
    assert np.max(radius * alpha - center) < 3e-8
    for w, a in antichains:
        if abs(w-width) <= 1e-9:
            assert np.max(np.abs(center[list(a)]-radius*alpha[list(a)])) < 3e-8
    return len(paths), m, width, radius, squared


def run():
    rng = random.Random(270184)
    samples = [
        (4, [(0, 1), (0, 2), (1, 3), (2, 3)]),
        (6, [(0, 1), (0, 2), (1, 3), (2, 3), (1, 4), (4, 5), (3, 5)]),
        (7, [(0, 1), (1, 2), (0, 3), (3, 2), (2, 4), (2, 5), (4, 6), (5, 6)]),
    ]
    # Sort a topologically valid relabelling of the third example.
    samples[2] = (7, [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (3, 5), (4, 6), (5, 6)])
    for n in range(4, 8):
        for _ in range(100):
            cand = [(i, j) for i in range(n) for j in range(i + 1, n)]
            edges = [e for e in cand if rng.random() < 0.49]
            if len(edges) < n or len(edges) > 12:
                continue
            routes = directed_paths(n, edges)
            if len(routes) < 2:
                continue
            used = set().union(*(set(r) for r in routes))
            if used != set(edges) or set(v for e in edges for v in e) != set(range(n)):
                continue
            samples.append((n, edges))
    tests = 0
    matrix_entries = 0
    for n, edges in samples:
        for metric in ([1] * len(edges), [1+(i%3) for i in range(len(edges))]):
            result = profile(n, edges, metric)
            tests += 1
            matrix_entries += result[1]
    # Sharp geometry of k internally disjoint paths of given lengths.
    for lengths in [(2, 2), (2, 3), (2, 3, 4), (2, 2, 3, 5)]:
        edges = []
        cur = 1
        for length in lengths:
            prev = 0
            for step in range(length):
                nxt = cur if step < length-1 else sum(lengths)-len(lengths)+1
                if step < length-1:
                    cur += 1
                edges.append((prev, nxt))
                prev = nxt
        sink = sum(lengths)-len(lengths)+1
        # Relabel to make all arcs increasing.
        assert sink == cur
        harmonic = sum(1/x for x in lengths)
        predicted = 1 / sum((1/x - 1/(x*x*harmonic))**0.5 for x in lengths)
        measured = profile(sink+1, edges, [1]*len(edges))[3]
        assert abs(predicted-measured) < 1e-10
    print('DAG_FLOW_INRADIUS_ANTICHAIN_CHECKS_PASSED',
          'graph_metric_profiles='+str(tests),
          'checked_coordinate_norms='+str(matrix_entries),
          'parallel_path_profiles=4')

if __name__ == '__main__':
    run()
