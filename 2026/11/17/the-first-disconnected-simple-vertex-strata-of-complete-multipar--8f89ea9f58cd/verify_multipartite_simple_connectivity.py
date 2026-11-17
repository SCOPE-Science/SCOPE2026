#!/usr/bin/env python3
"""Exact small-order census of the simple-vertex induced graph of graphic zonotopes.

All operations are finite integer combinatorics. No numerical approximation or
external libraries. Run: python3 verify_multipartite_simple_connectivity.py
"""
from itertools import permutations
from collections import Counter


def integer_partitions(total, bound=None):
    if bound is None:
        bound = total
    for k in range(min(bound, total), 0, -1):
        if k == total:
            yield (k,)
        else:
            for tail in integer_partitions(total-k, k):
                yield (k,) + tail


def edges_of(parts):
    colors = [c for c, size in enumerate(parts) for _ in range(size)]
    edges = [(i, j) for i in range(len(colors))
             for j in range(i + 1, len(colors)) if colors[i] != colors[j]]
    return colors, edges


def orientation_masks_from_orders(parts):
    colors, edges = edges_of(parts)
    n = len(colors)
    masks = set()
    for order in permutations(range(n)):
        pos = [0] * n
        for i, v in enumerate(order):
            pos[v] = i
        masks.add(sum((pos[a] < pos[b]) << k
                      for k, (a, b) in enumerate(edges)))
    return masks, edges


def direct_acyclic_masks(parts):
    # Independent exhaustive oracle: examine all edge-direction assignments,
    # detecting DAGs by iterative source removal (not via permutations).
    colors, edges = edges_of(parts)
    n = len(colors)
    all_masks = set()
    for mask in range(1 << len(edges)):
        indeg = [0] * n
        adj = [[] for _ in range(n)]
        for bit, (a, b) in enumerate(edges):
            if (mask >> bit) & 1:
                adj[a].append(b)
                indeg[b] += 1
            else:
                adj[b].append(a)
                indeg[a] += 1
        sources = [i for i in range(n) if indeg[i] == 0]
        removed = 0
        while sources:
            v = sources.pop()
            removed += 1
            for w in adj[v]:
                indeg[w] -= 1
                if indeg[w] == 0:
                    sources.append(w)
        if removed == n:
            all_masks.add(mask)
    return all_masks


def induced_components(states, edge_count, n):
    simple = set()
    degrees = Counter()
    for state in states:
        degree = sum((state ^ (1 << bit)) in states
                     for bit in range(edge_count))
        degrees[degree] += 1
        if degree == n-1:
            simple.add(state)
    pending = set(simple)
    components = []
    while pending:
        v = pending.pop()
        queue = [v]
        count = 1
        while queue:
            u = queue.pop()
            for bit in range(edge_count):
                w = u ^ (1 << bit)
                if w in pending:
                    pending.remove(w)
                    queue.append(w)
                    count += 1
        components.append(count)
    components.sort(reverse=True)
    return simple, components, degrees


def inspect(parts, independently=False):
    states, edges = orientation_masks_from_orders(parts)
    if independently:
        oracle = direct_acyclic_masks(parts)
        assert states == oracle, (parts, 'orientation representations disagree')
    simple, components, degrees = induced_components(states, len(edges), sum(parts))
    assert sum(degrees.values()) == len(states)
    assert sum(components) == len(simple)
    assert all(k >= sum(parts)-1 for k in degrees)
    return len(states), len(simple), components


def main():
    profiles = 0
    disconnected = []
    summary = {}
    for n in range(3, 8):
        for parts in integer_partitions(n):
            if len(parts) < 3:
                continue
            independent = (parts in ((3, 3, 1), (3, 2, 2), (2, 2, 2)))
            count, simple_count, components = inspect(parts, independently=independent)
            summary[parts] = (count, simple_count, components)
            profiles += 1
            if len(components) > 1:
                disconnected.append((parts, components))
            print('partition=', parts, 'vertices=', count,
                  'simple=', simple_count, 'components=', components)
    assert profiles == 25
    assert len(disconnected) == 2
    assert disconnected[0] == ((3, 3, 1), [430, 430])
    assert disconnected[1] == ((3, 2, 2), [1192] + [1]*48)
    assert summary[(2, 2, 2)] == (426, 288, [288])
    assert summary[(3, 3, 1)][0:2] == (1902, 860)
    assert summary[(3, 2, 2)][0:2] == (2286, 1240)
    # Independent local certificate for the explicitly isolated orientation:
    # class sequence C,A,C,A,B,A,B of K_{3,2,2}.
    parts = (3, 2, 2)
    colors, edges = edges_of(parts)
    order = (5, 0, 6, 1, 3, 2, 4)
    assert [colors[v] for v in order] == [2, 0, 2, 0, 1, 0, 1]
    pos = [0]*7
    for i, v in enumerate(order):pos[v] = i
    m = sum((pos[a] < pos[b]) << bit for bit, (a, b) in enumerate(edges))
    states, _ = orientation_masks_from_orders(parts)
    simple, comps, degs = induced_components(states, len(edges), 7)
    assert m in simple
    assert sum((m ^ (1 << bit)) in simple for bit in range(len(edges))) == 0
    assert sum((m ^ (1 << bit)) in states for bit in range(len(edges))) == 6
    print('MULTIPARTITE_SIMPLE_STRATUM_PASS profiles=25 independent_direct_DAGs=3 '
          'exceptional_types=2 component_counts=(2,49) isolated_witness=1')


if __name__ == '__main__':
    main()
