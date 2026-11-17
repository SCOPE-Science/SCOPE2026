#!/usr/bin/env python3
"""Direct, finite magnitude-chain calculation for selected layered digraphs.

This executable checks a single source-to-sink shortcut against the full
bigraded magnitude chain complex over two finite fields; it is not an
infinite proof or an integral torsion certificate.
"""
from collections import defaultdict
from itertools import combinations, product


def directed_distances(vertices, edges):
    nbr = defaultdict(list)
    for u, v in edges:
        nbr[u].append(v)
    result = {}
    for start in vertices:
        d = {start: 0}
        queue = [start]
        for u in queue:
            for v in nbr[u]:
                if v not in d:
                    d[v] = d[u] + 1
                    queue.append(v)
        for target, value in d.items():
            if start != target:
                result[start, target] = value
    return result


def magnitude_betti(vertices, edges, prime):
    distances = directed_distances(vertices, edges)
    # Every positive-length chain in an acyclic digraph follows a strictly
    # increasing chain in its reachability partial order.
    groups = defaultdict(list)
    for k in range(1, len(vertices)):
        for seq in combinations(vertices, k + 1):
            if all((seq[i], seq[i+1]) in distances for i in range(k)):
                length = sum(distances[seq[i], seq[i+1]] for i in range(k))
                groups[k, length, seq[0], seq[-1]].append(seq)
    # C_0,0 has one vertex per generator.
    for v in vertices:
        groups[0, 0, v, v] = [(v,)]
    ranks = {}
    for (k, l, u, v), seqs in groups.items():
        if k <= 1:
            ranks[k, l, u, v] = 0
            continue
        rows = {f: i for i, f in enumerate(groups.get((k - 1, l, u, v), []))}
        # Sparse modular elimination: each boundary column is a vector.
        pivots = {}
        for seq in seqs:
            vec = {}
            for i in range(1, k):
                left = seq[:i] + seq[i+1:]
                delta = distances[seq[i-1], seq[i+1]]
                if delta != distances[seq[i-1], seq[i]] + distances[seq[i], seq[i+1]]:
                    continue
                j = rows[left]
                vec[j] = (vec.get(j, 0) + (1 if i % 2 == 0 else -1)) % prime
            vec = {r: a for r, a in vec.items() if a}
            while vec:
                p = min(vec)
                if p not in pivots:
                    inv = pow(vec[p], -1, prime)
                    pivots[p] = {r: a * inv % prime for r, a in vec.items()}
                    break
                scale = vec[p]
                pv = pivots[p]
                for r, a in pv.items():
                    vec[r] = (vec.get(r, 0) - scale * a) % prime
                    if not vec[r]:
                        vec.pop(r)
        ranks[k, l, u, v] = len(pivots)
    betti = defaultdict(int)
    for (k, l, u, v), seqs in groups.items():
        rank_out = ranks[k, l, u, v]
        rank_in = ranks.get((k+1, l, u, v), 0)
        betti[k, l] += len(seqs) - rank_out - rank_in
    return {key: value for key, value in betti.items() if value}


def graph(widths, absent=()):
    layers = []
    index = 0
    for width in widths:
        layers.append(list(range(index, index+width)))
        index += width
    edges = {(u, v) for left, right in zip(layers, layers[1:]) for u in left for v in right}
    edges.difference_update(absent)
    vertices = list(range(index))
    # Last layer vertex is final sink.
    s = layers[0][0]
    t = layers[-1][0]
    distances = directed_distances(vertices, edges)
    assert (s, t) in distances and distances[s,t] == len(layers)-1
    # All vertices must be on an s-t path, otherwise these are not st-DAGs.
    assert all(v in (s,t) or ((s,v) in distances and (v,t) in distances) for v in vertices)
    return vertices, edges, s, t


def main():
    candidates = []
    for widths in [(1,1,1), (1,2,1), (1,3,1), (1,1,1,1), (1,2,1,1),
                   (1,2,2,1), (1,2,3,1), (1,2,1,2,1), (1,1,2,2,1),
                   (1,2,2,2,1)]:
        vertices, edges, s, t = graph(widths)
        candidates.append((widths, edges, vertices, s, t))
    # Two disjoint paths in the open interval: an initially non-diagonal DAG.
    widths = (1,2,2,1)
    vertices, edges, s, t = graph(widths, ((1,4),(2,3)))
    candidates.append((widths, edges, vertices, s, t))
    # Noncomplete layered graphs that retain all vertices on an s-t path.
    for widths in [(1,2,2,1), (1,2,3,1), (1,2,2,2,1)]:
        vertices, edges, s, t = graph(widths)
        eligible = sorted((u,v) for u,v in edges if u not in (s,) and v not in (t,))
        for missing in eligible:
            try:
                vv, ee, ss, tt = graph(widths, (missing,))
                candidates.append((widths, ee, vv, ss, tt))
            except AssertionError:
                pass
    cases = 0
    for prime in [2, 3]:
        for widths, edges, vertices, s, t in candidates:
            before = magnitude_betti(vertices, edges, prime)
            after = magnitude_betti(vertices, edges | {(s,t)}, prime)
            keys = set(before) | set(after)
            expected = {(1,1): 1, (2,len(widths)-1): 1}
            actual = {key: after.get(key, 0) - before.get(key, 0) for key in keys}
            actual = {key: delta for key, delta in actual.items() if delta}
            assert actual == expected, (prime, widths, sorted(edges), actual, expected)
            cases += 1
    print('SHORTCUT_MAGNITUDE_CHAIN_CHECKS_PASS')
    print('Cases:', cases)
    print('Coefficient fields: F_2 and F_3')
    print('Independent enumeration: directed distances, all increasing magnitude tuples, signed boundary matrices')
    print('All changes: +1 at bidegree (1,1) and +1 at (2,L); other ranks unchanged')
    print('Scope: finite graphs only; no inference about integral torsion from modular ranks')

if __name__ == '__main__':
    main()
