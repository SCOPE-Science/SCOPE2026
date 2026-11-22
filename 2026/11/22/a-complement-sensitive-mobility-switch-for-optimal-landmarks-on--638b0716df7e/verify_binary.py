#!/usr/bin/env python3
"""Exhaustive vertex-metric-basis and exchange/slide verification for the Clebsch graph."""
from itertools import combinations
from collections import Counter, deque

N = 16
GENERATORS = (1, 2, 4, 8, 15)
vertices = range(N)
adj = [frozenset(x ^ d for d in GENERATORS) for x in vertices]
assert all(len(a) == 5 for a in adj)
assert all(x not in adj[x] for x in vertices)
assert all((len(adj[u] & adj[v]) == (0 if v in adj[u] else 2))
           for u in vertices for v in range(u + 1, N))

def distances(g):
    out = []
    for a in vertices:
        d = [-1] * N
        d[a] = 0
        q = deque([a])
        while q:
            u = q.popleft()
            for v in g[u]:
                if d[v] == -1:
                    d[v] = d[u] + 1
                    q.append(v)
        assert all(t >= 0 for t in d)
        out.append(d)
    return out

D = distances(adj)
complement = [frozenset(set(vertices) - {x} - adj[x]) for x in vertices]
Dc = distances(complement)
assert all(D[u][v] + Dc[u][v] == 3 for u in vertices for v in vertices if u != v)

def resolving(S, mat):
    return len({tuple(mat[u][s] for s in S) for u in vertices}) == N

for k in range(4):
    assert not any(resolving(S, D) for S in combinations(vertices, k))
bases = {frozenset(S) for S in combinations(vertices, 4) if resolving(S, D)}
assert len(bases) == 80
assert bases == {frozenset(adj[x] - {y}) for x in vertices for y in adj[x]}
assert all(resolving(S, Dc) for S in bases)
assert sum(resolving(S, Dc) for S in combinations(vertices, 4)) == 80

independent = [S for S in combinations(vertices, 4)
               if all(v not in adj[u] for u, v in combinations(S, 2))]
assert len(independent) == 120
assert sum(frozenset(S) in bases for S in independent) == 80

bases = sorted(bases, key=lambda s:tuple(sorted(s)))
basis_id = {S: i for i, S in enumerate(bases)}
J = [set() for _ in bases]
T = [set() for _ in bases]
Tc = [set() for _ in bases]
for i, A in enumerate(bases):
    for u in A:
        for v in vertices:
            if v not in A:
                B = (A - {u}) | {v}
                if B in basis_id:
                    j = basis_id[B]
                    J[i].add(j)
                    if v in adj[u]: T[i].add(j)
                    if v in complement[u]: Tc[i].add(j)
assert all(len(a) == 4 for a in J)
assert sum(map(len, J)) // 2 == 160
assert all(not a for a in T)
assert all(Tc[i] == J[i] for i in range(len(bases)))

seen = set()
components = []
for s in range(len(bases)):
    if s in seen: continue
    group = {s}
    stack = [s]
    seen.add(s)
    while stack:
        for y in J[stack.pop()]:
            if y not in seen:
                seen.add(y)
                group.add(y)
                stack.append(y)
    components.append(group)
assert len(components) == 16
assert all(len(group) == 5 and all(J[i] == group - {i} for i in group)
           for group in components)
print('binary_graph: 16 vertices; strongly_regular=(16,5,0,2)')
print('metric_dimension=4; minimum_bases=80; independent_four_sets=120')
print('exchange=16*K5; exchange_edges=160; base_slide_edges=0; complement_slide_edges=160')
print('verification=PASS')
