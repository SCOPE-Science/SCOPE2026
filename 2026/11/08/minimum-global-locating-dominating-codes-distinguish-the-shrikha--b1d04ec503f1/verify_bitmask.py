#!/usr/bin/env python3
"""Finite exact check of minimum global locating-domination and relocation graphs."""
from itertools import combinations
from collections import Counter, deque

VERTICES = [(r, c) for r in range(4) for c in range(4)]
INDEX = {p: i for i, p in enumerate(VERTICES)}
DIFFS = {(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1)}
ALL = (1 << 16) - 1


def adjacency(kind):
    result = []
    for r, c in VERTICES:
        if kind == 'Shrikhande':
            neighbors = [INDEX[((r + a) % 4, (c + b) % 4)] for a, b in DIFFS]
        elif kind == 'Rook':
            neighbors = [i for i, (u, v) in enumerate(VERTICES)
                         if (u == r) != (v == c)]
        else:
            raise ValueError(kind)
        result.append(sum(1 << i for i in neighbors))
    return result


def is_ld(bits, masks):
    seen = set()
    for v in range(16):
        if not (bits >> v) & 1:
            signature = bits & masks[v]
            if not signature or signature in seen:
                return False
            seen.add(signature)
    return True


def all_codes(masks, k):
    return {sum(1 << v for v in combo)
            for combo in combinations(range(16), k)
            if is_ld(sum(1 << v for v in combo), masks)}


def exchange_graph(codes, masks, sliding=False):
    edges = set()
    adj = {s: set() for s in codes}
    for s in codes:
        support = [v for v in range(16) if s >> v & 1]
        outside = [v for v in range(16) if not s >> v & 1]
        for v in support:
            for w in outside:
                if sliding and not (masks[v] >> w) & 1:
                    continue
                t = s ^ (1 << v) ^ (1 << w)
                if t in codes:
                    edges.add((min(s, t), max(s, t)))
                    adj[s].add(t)
    assert len(edges) * 2 == sum(len(q) for q in adj.values())
    return adj, edges


def radius_diameter_connected(adjacency_lists):
    vertices = list(adjacency_lists)
    ecc = []
    for root in vertices:
        dist = {root: 0}
        pending = deque([root])
        while pending:
            v = pending.popleft()
            for w in adjacency_lists[v]:
                if w not in dist:
                    dist[w] = dist[v] + 1
                    pending.append(w)
        assert len(dist) == len(vertices), 'Disconnected exchange graph'
        ecc.append(max(dist.values()))
    return min(ecc), max(ecc), Counter(ecc)


EXPECTED = {
    'Shrikhande': (1584, 1488, 18432, 8160),
    'Rook': (1968, 1872, 27072, 11520),
}

for graph_name in ('Shrikhande', 'Rook'):
    a = adjacency(graph_name)
    for v in range(16):
        assert a[v].bit_count() == 6 and not (a[v] & (1 << v))
        for w in range(v + 1, 16):
            assert bool(a[v] & (1 << w)) == bool(a[w] & (1 << v))
            assert (a[v] & a[w]).bit_count() == 2
    for k in range(5):
        assert not all_codes(a, k), f'{graph_name} smaller code k={k}'
    ld = all_codes(a, 5)
    ac = [ALL ^ (1 << v) ^ a[v] for v in range(16)]
    codes = {s for s in ld if is_ld(s, ac)}
    forbidden = ld - codes
    witnesses = {a[v] ^ (1 << w) for v in range(16)
                 for w in range(16) if (a[v] >> w) & 1}
    assert len(witnesses) == 96
    assert forbidden == witnesses
    J, J_edges = exchange_graph(codes, a)
    S, S_edges = exchange_graph(codes, a, sliding=True)
    jr, jd, _ = radius_diameter_connected(J)
    sr, sd, _ = radius_diameter_connected(S)
    assert (len(ld), len(codes), len(J_edges), len(S_edges)) == EXPECTED[graph_name]
    assert (jr, jd, sr, sd) == (5, 5, 6, 6)
    print(f'{graph_name}: parameters=(16,6,2,2), min_global=5, '
          f'LD5={len(ld)}, non_global_LD5={len(forbidden)}, '
          f'global_LD5={len(codes)}, J_edges={len(J_edges)}, '
          f'S_edges={len(S_edges)}, J_radius_diameter=({jr},{jd}), '
          f'S_radius_diameter=({sr},{sd})')
print('PASS verify_bitmask')
