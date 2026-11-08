#!/usr/bin/env python3
"""Exhaustive class-relative C^2 split-graph cutoff; Python standard library only.

The enumerator exhausts every clique/independent-set partition and cross-edge matrix.
The common WL signatures are computed globally to make colors comparable.
"""
from collections import defaultdict


def split_graphs(n):
    for k in range(n + 1):
        l = n - k
        for b in range(1 << (k * l)):
            a = [(1 << k) - 1 - (1 << i) if i < k else 0 for i in range(n)]
            for i in range(k):
                for j in range(l):
                    if b & (1 << (i * l + j)):
                        a[i] |= 1 << (k + j)
                        a[k + j] |= 1 << i
            yield tuple(a)


def color_histograms(graphs, n):
    labels = [[0] * n for _ in graphs]
    for _ in range(n):
        sigs = []
        seen = set()
        for a, colors in zip(graphs, labels):
            row = []
            for i in range(n):
                m = a[i]
                neigh = []
                while m:
                    low = m & -m
                    neigh.append(colors[low.bit_length() - 1])
                    m -= low
                signature = (colors[i], tuple(sorted(neigh)))
                row.append(signature)
                seen.add(signature)
            sigs.append(row)
        global_ids = {s: j for j, s in enumerate(sorted(seen))}
        labels = [[global_ids[s] for s in row] for row in sigs]
    return [tuple(sorted(row)) for row in labels], labels


def isomorphism(a, b, ca, cb):
    n = len(a)
    classes = defaultdict(list)
    for j, c in enumerate(cb):
        classes[c].append(j)
    order = sorted(range(n), key=lambda x: (len(classes[ca[x]]), -a[x].bit_count()))
    mapping = [-1] * n

    def rec(depth, used):
        if depth == n:
            return True
        i = order[depth]
        for j in classes[ca[i]]:
            if used & (1 << j):
                continue
            if all(bool(a[i] & (1 << order[p])) == bool(b[j] & (1 << mapping[order[p]]))
                   for p in range(depth)):
                mapping[i] = j
                if rec(depth + 1, used | (1 << j)):
                    return True
                mapping[i] = -1
        return False
    return rec(0, 0)


def small_orders():
    expected_types = (1, 1, 2, 4, 9, 21, 56, 164)
    for n in range(0, 8):
        graphs = list(split_graphs(n))
        hist, colors = color_histograms(graphs, n)
        buckets = defaultdict(list)
        for i, h in enumerate(hist):
            buckets[h].append(i)
        for indices in buckets.values():
            i = indices[0]
            for j in indices[1:]:
                assert isomorphism(graphs[i], graphs[j], colors[i], colors[j]), (n, i, j)
        assert len(buckets) == expected_types[n], (n, len(buckets))
        print('order', n, 'generated', len(graphs), 'C2_groups', len(buckets), 'no_nonisomorphic_pair')


def witness():
    # Clique vertices 0,1,2,3; independent vertices 4,5,6,7.
    # Each independent vertex is adjacent to precisely two clique vertices.
    # For G, these pairs are 01,12,23,30: a single 8-cycle in the cut graph.
    # For H, they are 01,01,23,23: two disjoint 4-cycles in the cut graph.
    def make(pairs):
        a = [0] * 8
        for i in range(4):
            for j in range(4):
                if i != j:
                    a[i] |= 1 << j
        for t, (i, j) in enumerate(pairs):
            for v in (i, j):
                a[v] |= 1 << (4 + t)
                a[4 + t] |= 1 << v
        return tuple(a)

    g = make(((0, 1), (1, 2), (2, 3), (3, 0)))
    h = make(((0, 1), (0, 1), (2, 3), (2, 3)))
    hist, c = color_histograms((g, h), 8)
    assert hist[0] == hist[1]
    assert not isomorphism(g, h, c[0], c[1])
    for a in (g, h):
        assert sorted(x.bit_count() for x in a) == [2,2,2,2,5,5,5,5]
    print('order 8: two split graphs, jointly C2_equivalent, nonisomorphic')
    for t in range(1, 5):
        # Add the same t new universal vertices on both sides.
        def join_universal(a, t):
            n = len(a)
            return tuple(a[i] | (((1 << t) - 1) << n) for i in range(n)) + tuple(
                ((1 << (n + t)) - 1) ^ (1 << j) for j in range(n, n + t))
        g2, h2 = join_universal(g, t), join_universal(h, t)
        hk, cc = color_histograms((g2, h2), 8 + t)
        assert hk[0] == hk[1]
        assert not isomorphism(g2, h2, cc[0], cc[1])
        print('order', 8 + t, 'universal_join_pair_confirmed')
    print('result: PASS')


if __name__ == '__main__':
    small_orders()
    witness()
