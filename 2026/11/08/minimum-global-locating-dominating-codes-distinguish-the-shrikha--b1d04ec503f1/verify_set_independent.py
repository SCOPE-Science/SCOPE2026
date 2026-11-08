#!/usr/bin/env python3
"""Independent vertex-set enumeration using independently constructed edge sets."""
from itertools import combinations, product
from collections import defaultdict

POSITIONS = list(product(range(4), repeat=2))


def graph_edges(graph_name):
    e = set()
    for a, b in combinations(POSITIONS, 2):
        if graph_name == 'Rook':
            adjacent = (a[0] == b[0] or a[1] == b[1])
        elif graph_name == 'Shrikhande':
            d = tuple((x - y) % 4 for x, y in zip(a, b))
            adjacent = (d in ((1, 0), (0, 1), (1, 1),
                              (3, 0), (0, 3), (3, 3)))
        else:
            raise ValueError(graph_name)
        if adjacent:
            e.add(frozenset((a, b)))
    return e


def neighbor_map(E, complement=False):
    N = {v: set() for v in POSITIONS}
    for v, w in combinations(POSITIONS, 2):
        edge = frozenset((v, w)) in E
        if edge != complement:
            N[v].add(w)
            N[w].add(v)
    return N


def passes(code, neighbors):
    other = set(POSITIONS) - code
    patterns = [frozenset(neighbors[v] & code) for v in other]
    return all(patterns) and len(patterns) == len(set(patterns))


def one_exchange_components(codes, edges, slide=False):
    graph = {frozenset(c): set() for c in codes}
    for c in graph:
        for u in c:
            for v in set(POSITIONS) - c:
                if slide and frozenset((u, v)) not in edges:
                    continue
                t = (c - {u}) | {v}
                tt = frozenset(t)
                if tt in graph:
                    graph[c].add(tt)
    links = sum(len(ns) for ns in graph.values()) // 2
    discovered = set()
    sizes = []
    for v in graph:
        if v in discovered:
            continue
        stack = [v]
        discovered.add(v)
        count = 0
        while stack:
            u = stack.pop()
            count += 1
            for w in graph[u]:
                if w not in discovered:
                    discovered.add(w)
                    stack.append(w)
        sizes.append(count)
    return links, sorted(sizes)


expect = {'Shrikhande': (1584, 1488, 18432, 8160),
          'Rook': (1968, 1872, 27072, 11520)}
for graph_name in expect:
    edges = graph_edges(graph_name)
    neighbor = neighbor_map(edges)
    cneighbor = neighbor_map(edges, complement=True)
    assert len(edges) == 48
    for size in range(0, 6):
        local = []
        global_codes = []
        for group in combinations(POSITIONS, size):
            c = frozenset(group)
            if passes(c, neighbor):
                local.append(c)
                if passes(c, cneighbor):
                    global_codes.append(c)
        if size < 5:
            assert not local
        else:
            nJ, jcomp = one_exchange_components(global_codes, edges)
            nS, scomp = one_exchange_components(global_codes, edges, True)
            assert (len(local), len(global_codes), nJ, nS) == expect[graph_name]
            assert jcomp == scomp == [len(global_codes)]
            print(f'{graph_name}: LD5={len(local)}, global_LD5={len(global_codes)}, '
                  f'J_edges={nJ}, S_edges={nS}, components=1')
print('PASS verify_set_independent')
