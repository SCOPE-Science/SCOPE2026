"""Recompute square-switch adjacency and graph distances from the labeled table."""
from collections import Counter, deque
from itertools import combinations
from pathlib import Path

DATA = Path(__file__).resolve().parent / 'q4_flip_graph.tsv'
rows = DATA.read_text(encoding='utf-8').splitlines()
assert rows[0] == 'cycle_edges_hex\tneighbors_hex'
G = {}
for line in rows[1:]:
    x, tail = line.split('\t')
    key = int(x, 16)
    assert key not in G
    G[key] = set(int(s, 16) for s in tail.split(',')) if tail else set()
assert len(G) == 1344
edges = sorted(tuple(sorted((v, v ^ (1 << i)))) for v in range(16)
               for i in range(4) if v < (v ^ (1 << i)))
E = {e: i for i, e in enumerate(edges)}
assert len(edges) == 32
squares = set()
for a, b in combinations(range(4), 2):
    for v in range(16):
        S = {v, v ^ (1 << a), v ^ (1 << b), v ^ (1 << a) ^ (1 << b)}
        squares.add(sum(1 << i for i, e in enumerate(edges) if set(e) <= S))
assert len(squares) == 24

def is_cycle(m):
    adj = [[] for _ in range(16)]
    assert m.bit_count() == 16
    for i, (a, b) in enumerate(edges):
        if m >> i & 1:
            adj[a].append(b)
            adj[b].append(a)
    if any(len(a) != 2 for a in adj):
        return False
    seen = {0}
    q = [0]
    for v in q:
        for u in adj[v]:
            if u not in seen:
                seen.add(u)
                q.append(u)
    return len(seen) == 16

assert all(is_cycle(x) for x in G)
for x, neighbors in G.items():
    predicted = set()
    for face in squares:
        inter = face & x
        if inter.bit_count() != 2:
            continue
        selected = [edges[i] for i in range(32) if inter >> i & 1]
        if not set(selected[0]).isdisjoint(selected[1]):
            continue
        new = x ^ face
        if is_cycle(new):
            predicted.add(new)
    assert neighbors == predicted
    assert all(x in G[y] for y in neighbors)

degree = Counter(map(len, G.values()))
seen = set()
comp = Counter()
ecc = Counter()
rad = 100
Diam = 0
for x in G:
    if x in seen:continue
    group = {x}
    queue = [x]
    seen.add(x)
    for v in queue:
        for u in G[v]:
            if u not in seen:
                seen.add(u)
                group.add(u)
                queue.append(u)
    comp[len(group)] += 1
    if len(group) == 1:continue
    for v in group:
        dist = {v: 0}
        q = deque([v])
        while q:
            u = q.popleft()
            for w in G[u]:
                if w not in dist:
                    dist[w] = dist[u] + 1
                    q.append(w)
        assert len(dist) == len(group)
        e = max(dist.values())
        ecc[e] += 1
        rad = min(rad, e)
        Diam = max(Diam, e)
assert degree == {0: 240, 1: 384, 2: 192, 4: 288, 8: 240}
assert comp == {1: 240, 1104: 1}
assert ecc == {10: 96, 11: 192, 12: 816}
assert rad == 10 and Diam == 12
print('verified_cycle_masks', len(G))
print('verified_square_faces', len(squares))
print('verified_switch_edges', sum(map(len, G.values())) // 2)
print('verified_components', dict(sorted(comp.items())))
print('verified_radius_diameter', rad, Diam)
print('verified_eccentricities', dict(sorted(ecc.items())))
