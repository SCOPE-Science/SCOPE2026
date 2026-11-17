#!/usr/bin/env python3
"""Independent finite checks for color-incidence matching defects in clique-free complexes.
Only uses the Python standard library. The mathematical proof is independent of this code.
"""
from itertools import combinations, product
from collections import Counter


def graph_model(r, edges, extras=()):
    """Construct shore vertices and a matching of missing cross-shore edges."""
    incident = [[] for _ in range(r)]
    for index, (i, j) in enumerate(edges):
        assert 0 <= i < j < r
        incident[i].append(index)
        incident[j].append(index)
    shores = []
    endpoints = {}
    for i in range(r):
        count = max(1, len(incident[i])) + (i in extras)
        shore = []
        for _ in range(count):
            shore.append(sum(map(len, shores)) + len(shore))
        shores.append(shore)
        for index, vertex in zip(incident[i], shore):
            endpoints[(i, index)] = vertex
    missing = {
        frozenset((endpoints[(i, index)], endpoints[(j, index)]))
        for index, (i, j) in enumerate(edges)
    }
    assert len(set.union(*(set(sh) for sh in shores))) == sum(map(len, shores))
    assert len(set.union(*(set(pair) for pair in missing))) == 2 * len(missing) if missing else True
    return shores, missing


def complete_cliques(shores, missing):
    """Direct enumeration of all surviving full transversals."""
    return [sum(1 << v for v in trans)
            for trans in product(*shores)
            if all(frozenset(pair) not in missing for pair in combinations(trans, 2))]


def faces_of_complex(n, forbidden):
    faces = [[] for _ in range(n + 1)]
    for mask in range(1 << n):
        if all((mask & b) != b for b in forbidden):
            faces[mask.bit_count()].append(mask)
    return faces


def boundary_rank(domain, codomain, n):
    index = {f: i for i, f in enumerate(codomain)}
    basis = {}
    for sigma in domain:
        column = 0
        for i in range(n):
            if (sigma >> i) & 1:
                column ^= 1 << index[sigma ^ (1 << i)]
        while column:
            pivot = column.bit_length()
            if pivot not in basis:
                basis[pivot] = column
                break
            column ^= basis[pivot]
    return len(basis)


def reduced_betti(n, forbidden):
    faces = faces_of_complex(n, forbidden)
    ranks = [0] + [boundary_rank(faces[k], faces[k - 1], n)
                   for k in range(1, n + 1)] + [0]
    betti = {k - 1: len(faces[k]) - ranks[k] - ranks[k + 1]
             for k in range(n + 1)}
    return {dim: rank for dim, rank in betti.items() if dim >= 0 and rank},


def expected(r, edges):
    deg = [0] * r
    adj = [set() for _ in range(r)]
    for i, j in edges:
        adj[i].add(j); adj[j].add(i)
        deg[i] += 1; deg[j] += 1
    assert max(deg, default=0) <= 2
    active = set()
    cycles = []
    for i in range(r):
        if not deg[i] or i in active:
            continue
        component = set()
        stack = [i]
        while stack:
            v = stack.pop()
            if v in component: continue
            component.add(v);stack += list(adj[v] - component)
        active |= component
        if any(deg[v] == 1 for v in component):
            return {}
        cycles.append(len(component))
    return {r + sum(cycles) - len(cycles) - 2: 1} if cycles else {r - 2: 1}


def check_case(r, edges, extras=()):
    shores, missing = graph_model(r, edges, extras)
    transversals = complete_cliques(shores, missing)
    n = sum(map(len, shores))
    got = reduced_betti(n, transversals)[0]
    want = expected(r, edges)
    if got != want:
        raise AssertionError((r, edges, extras, n, got, want))
    return n, len(transversals), len(faces_of_complex(n, transversals)[-1]), got


def main():
    checked = 0
    # Exhaustive classification of every simple incidence graph on 3 and 4 colors.
    for r in (3, 4):
        links = list(combinations(range(r), 2))
        for bits in range(1 << len(links)):
            edges = [edge for i, edge in enumerate(links) if (bits >> i) & 1]
            if any(sum(v in e for e in edges) > 2 for v in range(r)):
                continue
            check_case(r, edges)
            checked += 1
    print('EXHAUSTIVE_COLOR_GRAPHS_R3_R4', checked, 'PASS')
    special = [
        (3, [(0, 1), (0, 2), (1, 2)], (0, 1)),
        (4, [(0, 1), (0, 2), (1, 2)], (0, 2, 3)),
        (4, [(0, 1), (1, 2), (2, 3), (0, 3)], (1,)),
        (5, [(0, 1), (1, 2), (2, 3), (3, 4), (0, 4)], ()),
        (5, [(0, 1), (0, 2), (1, 2)], ()),
        (5, [(0, 1), (1, 2), (2, 3)], ()),
        (6, [(0, 1), (0, 2), (1, 2), (3, 4), (3, 5), (4, 5)], ()),
        (6, [(0, 1), (0, 2), (1, 2), (3, 4)], ()),
    ]
    for r, e, extra in special:
        n, trans, _, got = check_case(r, e, extra)
        print('SPECIAL', 'r=',r,'color_edges=',len(e),'extra=',list(extra),'n=',n,
              'surviving_r_cliques=',trans,'reduced_betti=',got, 'PASS')
    print('COLOR_INCIDENCE_DEFECT_HOMOLOGY_CHECK_PASS')

if __name__ == '__main__': main()
