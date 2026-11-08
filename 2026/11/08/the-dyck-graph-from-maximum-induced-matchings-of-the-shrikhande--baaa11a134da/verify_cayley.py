#!/usr/bin/env python3
"""Exact finite certificate: maximum induced matchings on Shrikhande and Dyck correspondence.
Python standard library only. Run beside isomorphism.txt.
"""
from itertools import combinations
from collections import deque, Counter
from pathlib import Path

V = range(16)
S = ((1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3))
def xyz(u):
    return divmod(u, 4)

def vertex(x, y):
    return 4 * (x % 4) + y % 4

adj = [set() for _ in V]
for u in V:
    x,y = xyz(u)
    adj[u] = {vertex(x+a, y+b) for a,b in S}
assert all(len(t) == 6 for t in adj)
E = [(u,v) for u in V for v in sorted(adj[u]) if u < v]
assert len(E)==48

def is_induced_matching(indices):
    endpoints = [x for i in indices for x in E[i]]
    if len(set(endpoints)) != len(endpoints):
        return False
    # Among endpoints, exactly the chosen edges may be present.
    return sum(v in adj[u] for u,v in combinations(sorted(endpoints),2)) == len(indices)

M2 = [m for m in combinations(range(48),2) if is_induced_matching(m)]
M3 = [m for m in combinations(range(48),3) if is_induced_matching(m)]
M4 = [m for m in combinations(range(48),4) if is_induced_matching(m)]
assert len(M3) == 32 and len(M4) == 0
# There cannot be a larger induced matching without a size-four submatching.
assert not any(len(set(a)&set(b)) == 2 for a,b in combinations(M3,2))
T = [t for t in combinations(V,3) if all(v in adj[u] for u,v in combinations(t,2))]
assert len(T) == 32

move1 = {(i,j) for i,j in combinations(range(32),2) if len(set(M3[i]) & set(M3[j])) == 2}
move2 = {(i,j) for i,j in combinations(range(32),2) if len(set(M3[i]) & set(M3[j])) == 1}
triangle_edges = {(i,j) for i,j in combinations(range(32),2) if len(set(T[i]) & set(T[j])) == 2}
assert len(move1) == 0 and len(move2) == len(triangle_edges) == 48

pairs = [tuple(map(int,line.split())) for line in (Path(__file__).parent/'isomorphism.txt').read_text().splitlines()]
assert len(pairs) == 32 and sorted(i for i,j in pairs) == list(range(32))
phi = dict(pairs)
assert sorted(phi.values()) == list(range(32))
assert {tuple(sorted((phi[i],phi[j]))) for i,j in move2} == triangle_edges

neighbors=[set() for _ in M3]
for i,j in move2:
    neighbors[i].add(j);neighbors[j].add(i)
assert all(len(row)==3 for row in neighbors)
all_ecc=[]
for src in range(32):
    dist={src:0};q=deque([src])
    while q:
        u=q.popleft()
        for v in neighbors[u]:
            if v not in dist:
                dist[v]=dist[u]+1;q.append(v)
    assert len(dist)==32
    all_ecc.append(max(dist.values()))
assert set(all_ecc)=={5}

def cycle_girth(rows):
    best = len(rows) + 1
    for root in range(len(rows)):
        dist = {root: 0}; parent = {root: -1}; todo = deque([root])
        while todo:
            u = todo.popleft()
            for v in rows[u]:
                if v not in dist:
                    parent[v] = u; dist[v] = dist[u] + 1; todo.append(v)
                elif parent[u] != v:
                    best = min(best, dist[u] + dist[v] + 1)
    return best
assert cycle_girth(neighbors) == 6
# The Dyck model: triangles of Shrikhande, adjacent when sharing an edge.
print('VERIFY_OK Cayley graph: 16 vertices, 48 edges, maximal induced size 3; 32 optimum triples; no size 4')
print('VERIFY_OK 1-edge: 32 isolates; 2-edge: 32 vertices, 48 edges, cubic, connected, radius=diameter=5')
print('VERIFY_OK explicit bijection: all 32 vertices, all 48 Dyck adjacencies')
