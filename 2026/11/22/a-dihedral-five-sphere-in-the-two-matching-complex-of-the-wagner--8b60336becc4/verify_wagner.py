#!/usr/bin/env python3
"""Exact finite certificate for the two-matching complex of the Wagner graph.

No third-party modules. All faces, matching pairs, Hasse incidences, and signed
simplicial Lefschetz traces are generated from the given graph definition.
"""
from collections import Counter, deque

V = tuple(range(8))
E = tuple(sorted({tuple(sorted((i, (i+1)%8))) for i in V}
                 | {tuple(sorted((i, (i+4)%8))) for i in range(4)}))
m = len(E)
assert m == 12 and len(set(E)) == 12
stars = tuple(sum(1<<j for j,edge in enumerate(E) if v in edge) for v in V)
assert all(s.bit_count()==3 for s in stars)

# A selected edge subset belongs to M_2 if it contains no entire 3-star.
faces = {mask for mask in range(1<<m)
         if all((mask & star) != star for star in stars)}
assert 0 in faces
face_vector = Counter(mask.bit_count()-1 for mask in faces if mask)
assert dict(sorted(face_vector.items())) == {
    0:12, 1:66, 2:212, 3:423, 4:516, 5:352, 6:108, 7:7}
assert len(faces) == 1697

# Repeated ordered toggles: remove every available lower/upper pair, advancing
# through edge positions in lexicographic order. This is a finite matching.
unmatched = set(faces)
augmented_pairs = []
for i in range(m):
    bit = 1<<i
    for low in sorted(x for x in unmatched if not x&bit and (x|bit) in unmatched):
        high = low|bit
        if low in unmatched and high in unmatched:
            augmented_pairs.append((low,high))
            unmatched.remove(low)
            unmatched.remove(high)
assert len(augmented_pairs) == 848 and unmatched == {2646}
assert sum(low == 0 for low,high in augmented_pairs) == 1

# Standard unaugmented face poset: do not match the empty simplex.
matching = {(low,high) for low,high in augmented_pairs if low != 0}
assert len(matching) == 847
critical_vertex = next(high for low,high in augmented_pairs if low == 0)
assert critical_vertex == 1
critical = unmatched | {critical_vertex}
assert {x.bit_count()-1 for x in critical} == {0,5}
assert len(critical) == 2

# Verify each matched incidence and disjointness independently.
seen=set()
for low,high in matching:
    assert low in faces and high in faces and low != 0
    assert high.bit_count() == low.bit_count()+1 and (low & high) == low
    assert low not in seen and high not in seen
    seen.add(low); seen.add(high)
assert seen == (faces-{0})-critical

# Directed Hasse graph, with all unmatched arrows downward and matched
# arrows reversed (lower -> upper). Topological sort proves no directed cycle.
nonempty = faces-{0}
out = {x:[] for x in nonempty}
indeg = {x:0 for x in nonempty}
for upper in nonempty:
    rem = upper
    while rem:
        bit = rem & -rem
        rem -= bit
        lower = upper ^ bit
        if not lower: continue
        src,dst = (lower,upper) if (lower,upper) in matching else (upper,lower)
        out[src].append(dst)
        indeg[dst] += 1
queue = deque(x for x in nonempty if indeg[x] == 0)
visited=0
while queue:
    x=queue.popleft(); visited+=1
    for y in out[x]:
        indeg[y]-=1
        if indeg[y] == 0: queue.append(y)
assert visited == len(nonempty), (visited,len(nonempty))

# Full automorphism group: each cycle edge lies in exactly one 4-cycle and
# every diameter edge in exactly two; hence all automorphisms preserve the
# 8-cycle, and are the 16 rotations/reflections below.
cycles=set()
for a in V:
    for b in V:
        if b==a or tuple(sorted((a,b))) not in E: continue
        for c in V:
            if c in (a,b) or tuple(sorted((b,c))) not in E: continue
            for d in V:
                if d in (a,b,c): continue
                cc = tuple(sorted(tuple(sorted(edge)) for edge in
                         ((a,b),(b,c),(c,d),(d,a))))
                if tuple(sorted((c,d))) in E and tuple(sorted((d,a))) in E:
                    cycles.add(cc)
assert len(cycles)==4
for j,edge in enumerate(E):
    expected = 2 if abs(edge[0]-edge[1])==4 else 1
    assert sum(edge in cycle for cycle in cycles)==expected

# For an automorphism f, sum the signed traces on all nonempty chain groups,
# then subtract the augmentation trace to obtain the reduced Lefschetz number.
# With only reduced H_5=Z, reduced Lefschetz = -Tr(f|H_5).
def sign_of_permutation(image):
    return -1 if sum(image[i]>image[j] for i in range(len(image))
                     for j in range(i+1,len(image)))%2 else 1

def homology_trace(perm):
    edgemap=tuple(E.index(tuple(sorted((perm[a],perm[b])))) for a,b in E)
    assert len(set(edgemap))==m
    assert all(sum(1<<edgemap[i] for i in range(m) if x>>i & 1) in faces
               for x in faces)
    reduced_lefschetz = -1   # augmented empty face contributes -1
    contributions=Counter()
    for mask in nonempty:
        positions = [i for i in range(m) if mask>>i&1]
        p = [edgemap[i] for i in positions]
        if set(p) == set(positions):
            contribution=(-1)**(len(positions)-1) * sign_of_permutation(p)
            reduced_lefschetz += contribution
            contributions[len(positions)-1] += contribution
    return -reduced_lefschetz, dict(sorted(contributions.items()))

for k in range(8):
    r=[(v+k)%8 for v in V]
    s=[(k-v)%8 for v in V]
    tr,_=homology_trace(r)
    ts,_=homology_trace(s)
    assert tr == (-1)**k and ts == (-1)**(k+1)
rot_trace,rot_contributions = homology_trace([(v+1)%8 for v in V])
ref_trace,ref_contributions = homology_trace([(-v)%8 for v in V])
assert rot_trace==ref_trace==-1

print('PASS')
print('graph_edges:',E)
print('nonempty_faces:',len(nonempty),'f_vector:',dict(sorted(face_vector.items())))
print('matching_pairs:',len(matching),'critical_vertex_mask:',critical_vertex,
      'critical_5_face_mask:',list(unmatched)[0],
      'critical_5_graph_edges:',tuple(E[j] for j in range(m) if 2646>>j&1))
print('directed_hasse_graph_acyclic:',visited,'vertices')
print('full_graph_automorphism_group_order: 16 (D8)')
print('homology_rotation_trace:',rot_trace,'chain_trace_by_dim:',rot_contributions)
print('homology_reflection_trace:',ref_trace,'chain_trace_by_dim:',ref_contributions)
print('r^k_traces:',[(-1)**k for k in range(8)])
print('sr^k_traces:',[(-1)**(k+1) for k in range(8)])
print('rational_dihedral_quotient_reduced_homology: 0 in all dimensions')
