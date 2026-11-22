#!/usr/bin/env python3
"""Exact finite checks for higher-tolerance complexes of unfilled graphs.

The infinite-family theorem is proved separately; these GF(2) ranks test its
face enumeration and differential formula, not integral torsion or homotopy.
"""
from itertools import combinations
from math import comb
from random import Random


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def binary_rank(vectors):
    pivots = {}
    for value in vectors:
        while value:
            p = value.bit_length() - 1
            if p in pivots:
                value ^= pivots[p]
            else:
                pivots[p] = value
                break
    return len(pivots)


def invariants(n, edges, tolerance):
    edge_set = {frozenset(e) for e in edges}
    vertices = tuple(range(n))
    parent = list(range(n))

    def root(i):
        while parent[i] != i:
            i = parent[i]
        return i

    for u, v in edges:
        parent[root(u)] = root(v)
    components = len({root(v) for v in vertices})
    k = tolerance
    lower = list(combinations(vertices, k + 1))
    upper = [a for a in combinations(vertices, k + 2)
             if any(frozenset(e) in edge_set for e in combinations(a, 2))]
    index = {f: i for i, f in enumerate(lower)}
    columns = []
    for face in upper:
        # Mod-two simplicial boundary; signs are immaterial in this check.
        col = 0
        for i in range(k + 2):
            facelet = face[:i] + face[i + 1:]
            col ^= 1 << index[facelet]
        columns.append(col)
    rank = binary_rank(columns)
    predicted_rank = choose(n - 1, k + 1) - choose(components - 1, k + 1)
    assert rank == predicted_rank, (n, k, edges, rank, predicted_rank)
    b_low = choose(n - 1, k + 1) - rank
    b_high = len(upper) - rank
    assert b_low == choose(components - 1, k + 1)
    assert b_high == len(upper) - choose(n - 1, k + 1) + choose(components - 1, k + 1)
    return len(upper), b_low, b_high


def main():
    cases = 0
    for n in range(4, 7):
        pairs = list(combinations(range(n), 2))
        for mask in range(1 << len(pairs)):
            edges = [e for i, e in enumerate(pairs) if mask & (1 << i)]
            for t in range(2, n - 1):
                invariants(n, edges, t)
                cases += 1
    print('Exhaustive graphs of orders 4,5,6: 32,960 graphs; %d (graph,t) cases PASS' % cases)
    n = 7
    pairs = list(combinations(range(n), 2))
    for mask in Random(20261118).sample(range(1 << len(pairs)), 1000):
        edges = [e for i, e in enumerate(pairs) if mask & (1 << i)]
        for t in range(2, n - 1):
            invariants(n, edges, t)
            cases += 1
    print('Plus 1,000 seven-vertex graphs at all allowed t=2..5: %d cases total PASS' % cases)
    for n in (6, 7, 8):
        edges = [(i, (i + 1) % n) for i in range(n)]
        print('cycle', n, 't=2', invariants(n, edges, 2))
    print('disjoint edges plus isolates', invariants(6, [(0, 1), (2, 3)], 2))


if __name__ == '__main__':
    main()
