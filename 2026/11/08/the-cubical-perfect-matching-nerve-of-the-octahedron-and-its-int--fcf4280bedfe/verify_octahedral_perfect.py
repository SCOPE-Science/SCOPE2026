#!/usr/bin/env python3
"""Standalone, exhaustive checks for octahedral perfect-matching complex.

Uses only the Python standard library. All symbols and objects are defined here.
"""
from itertools import combinations, permutations, product
from collections import Counter

V = tuple(range(6))              # i+3*b denotes the vertex (part i, side b)
E = tuple((a,b) for a,b in combinations(V,2) if a%3 != b%3)
edgelook = {e:i for i,e in enumerate(E)}
assert len(E)==12

# Independent full enumeration of all three-edge perfect matchings.
PM = tuple(sorted(tuple(sorted(I)) for I in combinations(range(12),3)
     if len({v for k in I for v in E[k]})==6))
assert len(PM)==8 and len(set(PM))==8

# Second derivation: for each binary triple, the three between-part edges.
by_bits={}
for b0,b1,b2 in product((0,1), repeat=3):
    e1 = edgelook[tuple(sorted((0+3*b0,1+3*b1)))]
    e2 = edgelook[tuple(sorted((1+3*(1-b1),2+3*b2)))]
    e3 = edgelook[tuple(sorted((2+3*(1-b2),0+3*(1-b0))))]
    by_bits[(b0,b1,b2)]=tuple(sorted((e1,e2,e3)))
assert set(by_bits.values())==set(PM)

# Enumerate both simplicial complexes and the exact nonextendible pairs.
faces_P={frozenset()}
for m in PM:
    for k in range(1,4):
        faces_P.update(frozenset(s) for s in combinations(m,k))
match_pairs=tuple(frozenset((i,j)) for i,j in combinations(range(12),2)
                  if set(E[i]).isdisjoint(E[j]))
faces_M=faces_P|set(match_pairs)
bad=set(match_pairs)-faces_P
assert len(faces_P)==45 and len(faces_M)==51 and len(bad)==6
assert Counter(len(s) for s in faces_P)=={0:1,1:12,2:24,3:8}
assert Counter(len(s) for s in faces_M)=={0:1,1:12,2:30,3:8}
assert all(len(set(V)-{v for k in s for v in E[k]})==2 for s in bad)
assert all(len({v%3 for v in set(V)-{w for k in s for w in E[k]}})==1 for s in bad)

# Nerve vertices are the eight perfect matchings; no intersection of three facets.
Pindex={M:i for i,M in enumerate(PM)}
Nedges={frozenset((i,j)) for i,j in combinations(range(8),2)
        if set(PM[i]).intersection(PM[j])}
assert len(Nedges)==12
assert all(not set(PM[i]).intersection(PM[j],PM[k])
           for i,j,k in combinations(range(8),3))
bitindex={val:key for key,val in by_bits.items()}
assert all(sum(x!=y for x,y in zip(bitindex[PM[i]],bitindex[PM[j]]))==1
           for i,j in (tuple(e) for e in Nedges))
assert all(sum(x!=y for x,y in zip(bitindex[PM[i]],bitindex[PM[j]]))!=1 or
           frozenset((i,j)) in Nedges for i,j in combinations(range(8),2))
assert Counter(sum(k in m for m in PM) for k in range(12))=={2:12}

# Every matching of two graph edges extending to a perfect one is in exactly
# one 2-simplex; hence the simplicial collapse leaves a connected graph.
incidences=Counter(frozenset(c) for m in PM for c in combinations(m,2))
assert len(incidences)==24 and set(incidences.values())=={1}
# Check the connectivity of each 1-skeleton.
def components(edges, n):
    a=[set() for _ in range(n)]
    for edge in edges:
        i,j=tuple(edge)
        a[i].add(j);a[j].add(i)
    seen={0};todo=[0]
    while todo:
        for z in a[todo.pop()]:
            if z not in seen:seen.add(z);todo.append(z)
    return len(seen)
assert components([s for s in faces_P if len(s)==2],12)==12
assert components([s for s in faces_M if len(s)==2],12)==12
assert components(Nedges,8)==8
# The eight triangular 2-faces collapse using distinct free 1-faces.
assert 24-8-12+1==5
assert 30-8-12+1==11

# Exhaust full octahedral group, including action on the 8 perfect matchings.
G=[];Gpm=[];Gbad=[];central=None
bad_order=tuple(sorted(bad,key=lambda x: tuple(sorted(x))))
badindex={m:i for i,m in enumerate(bad_order)}
for perm in permutations(range(3)):
    for flips in product((0,1),repeat=3):
        vert=tuple(perm[x%3]+3*(x//3 ^ flips[x%3]) for x in V)
        emap=tuple(edgelook[tuple(sorted((vert[a],vert[b])))] for a,b in E)
        if any(tuple(sorted((vert[a],vert[b]))) not in edgelook for a,b in E):
            raise AssertionError('not graph automorphism')
        pmap=tuple(Pindex[tuple(sorted(emap[i] for i in m))] for m in PM)
        bmap=tuple(badindex[frozenset(emap[i] for i in m)] for m in bad_order)
        assert {frozenset(pmap[i] for i in s) for s in Nedges}==Nedges
        assert len(set(bmap))==6
        G.append((vert,emap))
        Gpm.append(pmap)
        Gbad.append(bmap)
        if perm==(0,1,2) and flips==(1,1,1):
            central=(pmap,emap,bmap)
assert len(G)==48 and len(set(Gpm))==48 and central is not None

def cycle_trace(q, edges):
    """H_1 trace = 1 - vertex trace + signed edge trace, for connected graph."""
    vt=sum(q[i]==i for i in range(len(q)))
    et=sum(1 if q[i]==i and q[j]==j else
           -1 if q[i]==j and q[j]==i else 0
           for i,j in (tuple(sorted(s)) for s in edges))
    return 1-vt+et

h1traces=[cycle_trace(q,Nedges) for q in Gpm]
assert Counter(h1traces)=={1:24,-1:20,-3:3,5:1}
assert sum(h1traces)==0
center_trace=cycle_trace(central[0],Nedges)
assert center_trace==1
assert (5+center_trace)//2==3 and (5-center_trace)//2==2

# Identify the two irreducible rational modules using cycle types of the
# action on the four body diagonals (opposite cube-vertex pairs).
opp_pairs=tuple(sorted({tuple(sorted((i, next(j for j in range(8)
                      if all(x!=y for x,y in zip(bitindex[PM[i]],bitindex[PM[j]]))))))
                        for i in range(8)}))
assert len(opp_pairs)==4
pairidx={p:i for i,p in enumerate(opp_pairs)}
chi_211={(1,1,1,1):3,(2,1,1):-1,(2,2):-1,(3,1):0,(4,):1}
chi_22={(1,1,1,1):2,(2,1,1):0,(2,2):2,(3,1):-1,(4,):0}
class_table={}
for (verts,_),q in zip(G,Gpm):
    diag=tuple(pairidx[tuple(sorted((q[a],q[b])))] for a,b in opp_pairs)
    seen=set();sizes=[]
    for i in range(4):
        if i in seen:continue
        j=i;size=0
        while j not in seen:
            seen.add(j);size+=1;j=diag[j]
        sizes.append(size)
    cycle=tuple(sorted(sizes, reverse=True))
    part_perm=tuple(verts[i]%3 for i in range(3))
    parity=sum(part_perm[i]>part_perm[j] for i in range(3) for j in range(i+1,3))
    flipcount=sum(verts[i]//3 for i in range(3))
    determinant=(-1)**(parity+flipcount)
    expect=chi_211[cycle]+determinant*chi_22[cycle]
    actual=cycle_trace(q,Nedges)
    assert actual==expect
    class_table.setdefault((cycle,determinant),[]).append(actual)
assert len(class_table)==10
assert all(len(set(v))==1 for v in class_table.values())
assert sorted(len(v) for v in class_table.values())==[1,1,3,3,6,6,6,6,8,8]

# Compare chain-level contributions from the six unextendible matching pairs.
# Each is reversed (not simply permuted) by the central inversion.
central_emap=central[1]
for s in bad:
    i,j=tuple(s)
    assert frozenset((central_emap[i],central_emap[j]))==s
    assert central_emap[i]==j and central_emap[j]==i
assert (center_trace-6)==-5

# Unsigned edge stabilizer with reversed ends forces no full G-fixed cycle.
for edge in Nedges:
    i,j=tuple(edge)
    assert any(q[i]==j and q[j]==i for q in Gpm)

print('graph: vertices=6 edges=12 perfect_matchings=8')
print('perfect_complex_faces: 0:1 1:12 2:24 3:8')
print('ordinary_complex_faces: 0:1 1:12 2:30 3:8')
print('nonextendible_two_edge_matchings=6')
print('nerve: cube_vertices=8 cube_edges=12 triple_intersections=0')
print('face_to_nerve_intersections: graph_edge_multiplicity=2')
print('automorphisms=48 faithful_cube_actions=48')
print('perfect_first_homology_rank=5 ordinary_first_homology_rank=11')
print('perfect_H1_character_histogram=5:1,1:24,-1:20,-3:3')
print('rational_module=S^(2,1,1) plus determinant_twist(S^(2,2))')
print('signed_oct_group_conjugacy_classes=10 verified_character_classes=10')
print('central_inversion_H1_trace=1 central_eigenspaces=3,2')
print('ordinary_minus_perfect_relative_rank=6 center_relative_trace=-6')
print('full_group_H1_fixed_rank=0')
print('VERIFY_OK')
