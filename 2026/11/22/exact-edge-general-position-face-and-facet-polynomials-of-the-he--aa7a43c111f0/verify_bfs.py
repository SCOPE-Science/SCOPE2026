#!/usr/bin/env python3
"""Independent shortest-path and depth-first enumeration for the Fano Levi graph."""
from collections import Counter, deque
from itertools import combinations
from math import comb

LINES = [tuple(sorted({j % 7, (j+1) % 7, (j+3) % 7})) for j in range(7)]
EDGES = sorted((p, 7+j) for j in range(7) for p in LINES[j])
assert len(EDGES) == 21 and len(set(EDGES)) == 21
edge_id = {edge: i for i, edge in enumerate(EDGES)}
adj = [[] for _ in range(14)]
for u, v in EDGES:
    adj[u].append(v); adj[v].append(u)
# Construct the forbidden triples independently, from all shortest paths.
bad = set()
for source in range(14):
    dist = [-1] * 14
    dist[source] = 0
    queue = deque([source])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] < 0:
                dist[v] = dist[u] + 1; queue.append(v)
    assert max(dist) == 3
    def walk(v, path):
        if v == source:
            if len(path) >= 4:
                ids = [edge_id[tuple(sorted((a,b)))] for a,b in zip(path,path[1:])]
                for t in combinations(ids,3):
                    bad.add(tuple(sorted(t)))
            return
        for prev in adj[v]:
            if dist[prev] == dist[v]-1:
                walk(prev,path+[prev])
    for target in range(source+1,14):
        walk(target,[target])
assert len(bad) == 84, len(bad)

forbidden_containing = [[] for _ in range(21)]
for triple in bad:
    for x in triple:
        forbidden_containing[x].append(sum(1 << a for a in triple if a != x))

face_counts = Counter()
facet_counts = Counter()
visited = 0

def dfs(i, mask):
    global visited
    if i == 21:
        visited += 1
        size = mask.bit_count()
        face_counts[size] += 1
        maximal = True
        for x in range(21):
            if mask & (1 << x): continue
            if not any(mask & other == other for other in forbidden_containing[x]):
                maximal = False
                break
        if maximal: facet_counts[size] += 1
        return
    dfs(i+1,mask)
    if not any(mask & other == other for other in forbidden_containing[i]):
        dfs(i+1,mask | (1 << i))

dfs(0,0)
print('Shortest-path-derived forbidden triples:',len(bad))
print('All EGP sets:', sorted(face_counts.items()))
print('All maximal EGP sets:', sorted(facet_counts.items()))
print('Total sets:',visited)
assert [face_counts[i] for i in range(11)] == [1,21,210,1246,4725,11592,17962,16446,7875,1617,84]
assert dict(facet_counts) == {7:66,8:546,9:861,10:84}
print('PASS: exact independent BFS/DFS census')
