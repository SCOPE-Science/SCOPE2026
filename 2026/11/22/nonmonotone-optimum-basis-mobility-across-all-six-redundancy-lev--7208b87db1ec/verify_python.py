#!/usr/bin/env python3
"""Complete finite verifier: k-metric bases and optimum moves of the Frucht graph.
No third-party modules are required. Run: python3 verify_python.py
"""
from collections import deque, Counter
from itertools import combinations

N = 12
LCF = (-5, -2, -4, 2, 5, -2, 2, 5, -2, -5, 4, 2)
g = [set() for _ in range(N)]
for i, offset in enumerate(LCF):
    for j in ((i + 1) % N, (i + offset) % N):
        g[i].add(j)
        g[j].add(i)
assert all(len(neighbors) == 3 for neighbors in g)
assert sum(map(len, g)) == 36

dist = []
for start in range(N):
    row = [-1] * N
    row[start] = 0
    q = deque([start])
    while q:
        u = q.popleft()
        for v in g[u]:
            if row[v] == -1:
                row[v] = row[u] + 1
                q.append(v)
    assert -1 not in row
    dist.append(row)

separators = []
for a, b in combinations(range(N), 2):
    separators.append(sum(1 << v for v in range(N)
                          if dist[a][v] != dist[b][v]))
assert len(separators) == 66
assert min(mask.bit_count() for mask in separators) == 6


def mobility(bases, sliding):
    bases = set(bases)
    graph = {s: set() for s in bases}
    for s in bases:
        for u in range(N):
            if not s & (1 << u):
                continue
            for v in (g[u] if sliding else range(N)):
                if s & (1 << v):
                    continue
                t = s ^ (1 << u) ^ (1 << v)
                if t in bases:
                    graph[s].add(t)
    assert all(s in graph[t] for s in bases for t in graph[s])
    remaining = bases.copy()
    components = []
    while remaining:
        root = min(remaining)
        q = [root]
        remaining.remove(root)
        for s in q:
            for t in sorted(graph[s]):
                if t in remaining:
                    remaining.remove(t)
                    q.append(t)
        eccentricities = []
        for source in q:
            d = {source: 0}
            front = deque([source])
            while front:
                s = front.popleft()
                for t in graph[s]:
                    if t not in d:
                        d[t] = d[s] + 1
                        front.append(t)
            assert len(d) == len(q)
            eccentricities.append(max(d.values()))
        components.append((len(q), min(eccentricities), max(eccentricities)))
    return sum(map(len, graph.values())) // 2, sorted(components, reverse=True)

for k in range(1, 7):
    qualifying = [s for s in range(1 << N)
                  if all((s & r).bit_count() >= k for r in separators)]
    minimum = min(s.bit_count() for s in qualifying)
    bases = [s for s in qualifying if s.bit_count() == minimum]
    je, jc = mobility(bases, False)
    se, sc = mobility(bases, True)
    print(f'k={k} min={minimum} bases={len(bases)} jump_edges={je} '
          f'jump_components={jc} slide_edges={se} slide_components={sc}')
