#!/usr/bin/env python3
"""Finite combinatorial verification of the icosahedral graph GP-complex proof.
Uses only the Python standard library; all 4096 vertex subsets are examined.
"""
from collections import Counter, deque
from itertools import combinations

N = 12
adj = [set() for _ in range(N)]

def add(u, v):
    assert u != v
    adj[u].add(v)
    adj[v].add(u)

# Two staggered pentagonal belts, with a north and a south pole.
for j in range(5):
    u, v = 1 + j, 6 + j
    add(0, u)
    add(11, v)
    add(u, 1 + (j + 1) % 5)
    add(v, 6 + (j + 1) % 5)
    add(u, v)
    add(u, 6 + (j - 1) % 5)

assert all(len(adj[u]) == 5 for u in range(N))
assert sum(map(len, adj)) // 2 == 30
D = [[None] * N for _ in range(N)]
for u in range(N):
    D[u][u] = 0
    q = deque([u])
    while q:
        x = q.popleft()
        for y in sorted(adj[x]):
            if D[u][y] is None:
                D[u][y] = D[u][x] + 1
                q.append(y)
assert max(max(row) for row in D) == 3
assert all(sum(D[u][v] == 3 for v in range(N)) == 1 for u in range(N))

all_triples = list(combinations(range(N), 3))

def gp_triple(t):
    a, b, c = t
    return (D[a][b] + D[b][c] > D[a][c]
            and D[a][c] + D[c][b] > D[a][b]
            and D[b][a] + D[a][c] > D[b][c])

bad = [t for t in all_triples if not gp_triple(t)]
bad_masks = [sum(1 << v for v in t) for t in bad]
faces = [mask for mask in range(1, 1 << N)
         if not any(mask & t == t for t in bad_masks)]
by_size = Counter(mask.bit_count() for mask in faces)
assert by_size == {1: 12, 2: 66, 3: 100, 4: 30}, by_size
assert len(bad) == 120

# Six antipodal pairs are isolated edges in the 2-dimensional incidence structure.
antipodal = [(u, v) for u in range(N) for v in range(u + 1, N) if D[u][v] == 3]
assert len(antipodal) == 6
for u, v in antipodal:
    assert all(not gp_triple(tuple(sorted((u, v, w))))
               for w in range(N) if w not in (u, v))

# Distance-two core: a 12-vertex connected closed combinatorial 2-manifold.
core_edges = [tuple(e) for e in combinations(range(N), 2) if D[e[0]][e[1]] == 2]
core_tris = [t for t in all_triples if all(D[a][b] == 2 for a, b in combinations(t, 2))]
assert len(core_edges) == 30 and len(core_tris) == 20
assert all(gp_triple(t) for t in core_tris)
edge_inc = Counter(tuple(sorted(e)) for t in core_tris for e in combinations(t, 2))
assert all(edge_inc[e] == 2 for e in core_edges)
for v in range(N):
    link_edges = [tuple(w for w in t if w != v) for t in core_tris if v in t]
    link_vertices = set(x for e in link_edges for x in e)
    link_adj = {x: set() for x in link_vertices}
    for a, b in link_edges:
        link_adj[a].add(b)
        link_adj[b].add(a)
    seen, todo = set(), [next(iter(link_vertices))]
    while todo:
        x = todo.pop()
        if x in seen:
            continue
        seen.add(x)
        todo.extend(link_adj[x] - seen)
    assert len(link_vertices) == len(link_edges) == 5
    assert seen == link_vertices and all(len(link_adj[x]) == 2 for x in link_vertices)
seen, todo = set(), [0]
core_adj = {u: {v for v in range(N) if D[u][v] == 2} for u in range(N)}
while todo:
    x = todo.pop()
    if x in seen:
        continue
    seen.add(x)
    todo.extend(core_adj[x] - seen)
assert len(seen) == N and N - len(core_edges) + len(core_tris) == 2

# Every original graph edge can be eliminated from pi_1 using a GP triangle
# with two edges of the simply-connected distance-two surface.
edges = [(u, v) for u in range(N) for v in range(u+1, N) if D[u][v] == 1]
witness = {}
for u, v in edges:
    possibilities = [w for w in range(N) if D[u][w] == D[v][w] == 2]
    assert possibilities and all(gp_triple(tuple(sorted((u, v, w)))) for w in possibilities)
    witness[(u, v)] = min(possibilities)
assert len(witness) == 30

# Every tetrahedron has two free triangular faces. Their choices are distinct
# across tetrahedra, allowing all tetrahedra to be collapsed independently.
tetra = [f for f in faces if f.bit_count() == 4]
counts = Counter(f ^ (1 << u) for f in tetra for u in range(N) if f & (1 << u))
choices = []
for f in sorted(tetra):
    free = sorted(f ^ (1 << u) for u in range(N)
                  if f & (1 << u) and counts[f ^ (1 << u)] == 1)
    assert len(free) == 2
    choices.append((f, free[0]))
assert len(set(t for f, t in choices)) == 30

# GP without six isolated edges has Euler characteristic 22 and collapses
# to a simply-connected two-complex; hence it is a wedge of 21 two-spheres.
chi_rest = by_size[1] - (by_size[2] - 6) + by_size[3] - by_size[4]
assert chi_rest == 22
print('PASS: icosahedral 12 vertices, 30 graph edges; distance-2 core is S^2')
print('PASS: GP face vector 12, 66, 100, 30; forbidden triples 120')
print('PASS: six isolated antipodal GP edges; 30 edge-to-core triangle witnesses')
print('PASS: 30 tetrahedral free-face collapse certificates')
print('CONCLUSION: GP(I) homotopy type wedge 6 S^1 and 21 S^2')
