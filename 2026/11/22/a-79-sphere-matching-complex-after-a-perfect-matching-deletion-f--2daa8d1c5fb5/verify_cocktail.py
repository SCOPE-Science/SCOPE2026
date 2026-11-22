#!/usr/bin/env python3
"""Finite acyclic-matching certificate for matching complex of K_8 minus a perfect matching.
No dependencies outside Python's standard library; run: python3 verify_cocktail.py
"""
from itertools import combinations
from collections import deque

N = 8
# The removed perfect matching is (0,1),(2,3),(4,5),(6,7).
EDGES = [(a,b) for a in range(N) for b in range(a+1,N) if a//2 != b//2]
# A lexicographic sequence of legal toggles, chosen as an explicit certificate.
ORDER = [2,18,23,6,17,0,20,10,11,3,19,7,8,1,15,5,13,22,21,12,9,4,14,16]

assert len(EDGES) == 24 and sorted(ORDER) == list(range(24))
faces = {0}
for k in range(1,5):
    for inds in combinations(range(len(EDGES)),k):
        used = [v for j in inds for v in EDGES[j]]
        if len(set(used)) == 2*k:
            faces.add(sum(1<<j for j in inds))
face_list = sorted(faces, key=lambda f:(f.bit_count(),f))
assert len(face_list) == 513
index={f:i for i,f in enumerate(face_list)}
counts = [sum(f.bit_count()==k for f in faces) for k in range(5)]
assert counts == [1,24,156,272,60]

unpaired = set(faces)
pairs = []
for j in ORDER:
    b = 1<<j
    # Lexicographically scan all then-unpaired faces not containing this vertex.
    for f in sorted(unpaired):
        if f not in unpaired or f & b:
            continue
        top = f | b
        if top in unpaired:
            assert f in faces and top in faces and top.bit_count() == f.bit_count()+1
            unpaired.remove(f)
            unpaired.remove(top)
            pairs.append((f,top))
assert len(pairs) == 217
assert len(unpaired) == 79
assert all(f.bit_count() == 3 for f in unpaired)
assert len({f for pair in pairs for f in pair})==434

# Full face-poset Hasse orientation: downward except each matched edge upward.
# A Kahn topological sweep checks every directed edge, not just observed paths.
reverse={up:low for low,up in pairs}
deg=[0]*len(face_list)
adj=[[] for _ in face_list]
num_arcs=0
for up in face_list:
    for j in range(24):
        if not (up & (1<<j)):
            continue
        low=up ^ (1<<j)
        assert low in faces
        if reverse.get(up)==low:
            a,b=low,up
        else:
            a,b=up,low
        ai,bi=index[a],index[b]
        adj[ai].append(bi)
        deg[bi]+=1
        num_arcs+=1
queue=deque(i for i,d in enumerate(deg) if d==0)
visited=0
while queue:
    u=queue.popleft();visited+=1
    for v in adj[u]:
        deg[v]-=1
        if deg[v]==0:
            queue.append(v)
assert visited==len(faces), 'closed gradient path: Morse certificate invalid'
# The empty face is paired. Undoing that pair yields precisely one
# critical 0-simplex and 79 critical 2-simplices.
assert any(lo==0 and up.bit_count()==1 for lo,up in pairs)
# Euler cross-check: 24-156+272-60=80=1+79.
assert counts[1]-counts[2]+counts[3]-counts[4] == 80
print('graph_vertices=8 graph_edges=24 removed_edges=4')
print('face_counts_empty_through_tetrahedra=',counts)
print('Morse_pairs=',len(pairs))
print('critical_nonempty_without_empty_pair_restored= one_vertex_and_79_triangles')
print('directed_hasse_arcs=',num_arcs,'DAG_vertices_visited=',visited)
print('acyclic_morse_certificate=PASS')
print('homotopy_type= wedge_of_79_two_spheres')
