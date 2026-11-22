#!/usr/bin/env python3
"""Exact integer-arithmetic checks for the edge metric theorem on Hansen polytopes."""
from collections import Counter
from itertools import combinations
from math import comb


def vertices(p, q):
    masks = sorted(set(range(1 << p)) | {mask << p for mask in range(1 << q)})
    return [(sgn, mask) for sgn in (1, -1) for mask in masks]


def cliques(p, q):
    # Include the empty clique and all singletons and cross pairs.
    left = [1 << i for i in range(p)]
    right = [1 << (p + j) for j in range(q)]
    return [0] + left + right + [x | y for x in left for y in right]


def actual_edges(p, q):
    vv = vertices(p, q)
    facet_sets = []
    for clique in cliques(p, q):
        for facet_sign in (1, -1):
            support = 0
            for i, (vertex_sign, mask) in enumerate(vv):
                dot = vertex_sign * (-1 + 2 * (mask & clique).bit_count())
                if facet_sign * dot == 1:
                    support |= 1 << i
            assert support.bit_count() >= 2
            facet_sets.append(support)
    full = (1 << len(vv)) - 1
    incident = [[] for _ in vv]
    for k, support in enumerate(facet_sets):
        for i in range(len(vv)):
            if support & (1 << i):
                incident[i].append(k)
    counts = Counter()
    edge_pairs = []
    for i, j in combinations(range(len(vv)), 2):
        face = full
        for k in incident[i]:
            if facet_sets[k] & (1 << j):
                face &= facet_sets[k]
        if face.bit_count() == 2:
            a, b = vv[i], vv[j]
            distance_squared = (a[0] - b[0]) ** 2
            for idx in range(p + q):
                xa = a[0] * bool(a[1] & (1 << idx))
                xb = b[0] * bool(b[1] & (1 << idx))
                distance_squared += (xa - xb) ** 2
            counts[distance_squared] += 1
            edge_pairs.append((a, b, distance_squared))
    return counts, edge_pairs


def predicted_edges(p, q):
    out = Counter({1: p * 2**p + q * 2**q})
    out[p + 4] += 2**p
    out[q + 4] += 2**q
    for k in range(1, p + 1):
        for l in range(1, q + 1):
            count = 2 * comb(p, k) * comb(q, l)
            out[k + l] += count
            out[k + l + 4] += count
    return out


def predicted_adjacency(a, b, p, q):
    sa, ma = a
    sb, mb = b
    full_left = (1 << p) - 1
    full_right = ((1 << q) - 1) << p
    def which(mask):
        if mask == 0:
            return '0'
        if mask & full_left:
            return 'L'
        return 'R'
    xa, xb = which(ma), which(mb)
    if sa == sb:
        if xa == xb or xa == '0' or xb == '0':
            return (ma ^ mb).bit_count() == 1
        return True
    if xa == '0':
        return mb in (full_left, full_right)
    if xb == '0':
        return ma in (full_left, full_right)
    if xa != xb:
        return True
    return (ma & mb) == 0 and (ma | mb) in (full_left, full_right)


def verify(p, q):
    observed, pairs = actual_edges(p, q)
    expected = predicted_edges(p, q)
    assert observed == expected, (p, q, observed, expected)
    observed_pairs = {frozenset((a, b)) for a, b, _ in pairs}
    vv = vertices(p, q)
    for a, b in combinations(vv, 2):
        actual = frozenset((a, b)) in observed_pairs
        predicted = predicted_adjacency(a, b, p, q)
        assert actual == predicted, (p, q, a, b, actual, predicted)
    total = p * 2**p + q * 2**q + 4 * (2**p - 1) * (2**q - 1) + 2**p + 2**q
    assert sum(observed.values()) == total
    assert max(observed) == p + q + 4 and observed[p + q + 4] == 2
    return len(vv), total


if __name__ == '__main__':
    cases = 0
    total_pairs = 0
    for p in range(1, 6):
        for q in range(p, 6):
            n, edge_count = verify(p, q)
            cases += 1
            total_pairs += n * (n - 1) // 2
            print(f'CHECK p={p} q={q}: vertices={n}, edges={edge_count}')
    for p, q in ((2, 6), (3, 6), (4, 6), (5, 6), (6, 6)):
        n, edge_count = verify(p, q)
        cases += 1
        total_pairs += n * (n - 1) // 2
        print(f'CHECK p={p} q={q}: vertices={n}, edges={edge_count}')
    print(f'HANSEN_EDGE_METRIC_EXACT_PASS configurations={cases} tested_pairs={total_pairs}')
