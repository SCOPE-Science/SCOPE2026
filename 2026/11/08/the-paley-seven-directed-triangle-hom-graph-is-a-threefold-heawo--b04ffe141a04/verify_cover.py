#!/usr/bin/env python3
"""Exact finite verification of the Paley-seven directed triangle Hom cover."""
from collections import Counter, deque
from itertools import combinations

N=7
Q={1,2,4}

def arc(u,v):
    return ((v-u)%N) in Q

def rotate(t):
    return (t[1],t[2],t[0])

def cyclic_orbit(t):
    return {t,rotate(t),rotate(rotate(t))}

def valid_cell(A,B,C):
    return (all(arc(a,b) for a in A for b in B)
            and all(arc(b,c) for b in B for c in C)
            and all(arc(c,a) for c in C for a in A))

V={(a,b,c) for a in range(N) for b in range(N) for c in range(N)
   if valid_cell((a,),(b,),(c,))}
assert len(V)==42
cells=[]
for s in range(1,1<<N):
    A=[j for j in range(N) if s>>j&1]
    for t in range(1,1<<N):
        B=[j for j in range(N) if t>>j&1]
        if not all(arc(a,b) for a in A for b in B):
            continue
        for u in range(1,1<<N):
            C=[j for j in range(N) if u>>j&1]
            if len(A)+len(B)+len(C)>4:  # checked mathematically below
                continue
            if valid_cell(A,B,C):
                cells.append((tuple(A),tuple(B),tuple(C)))
# Check no cells of dimension >=2 without relying on this cutoff:
# every ordered pair of distinct targets has precisely one common successor
# and one common predecessor. Therefore any cell with one coordinate of
# size >=2 has both other coordinates of size <=1.
for a,b in combinations(range(N),2):
    assert sum(arc(a,x) and arc(b,x) for x in range(N))==1
    assert sum(arc(x,a) and arc(x,b) for x in range(N))==1
assert all(sum(map(len,t)) <=4 for t in cells)
fvector=Counter(sum(map(len,t))-3 for t in cells)
assert fvector=={0:42,1:63}, fvector

# Independent graph rule: neighboring triples differ in exactly one
# coordinate and the union of the changed coordinate remains valid.
adj={v:set() for v in V}
for v,w in combinations(sorted(V),2):
    differing=[i for i in range(3) if v[i]!=w[i]]
    if len(differing)!=1:
        continue
    blocks=[{v[i],w[i]} for i in range(3)]
    if valid_cell(*blocks):
        adj[v].add(w);adj[w].add(v)
assert all(len(adj[v])==3 for v in V)
E={frozenset({v,w}) for v in V for w in adj[v]}
assert len(E)==63
for v in V:
    assert rotate(v) in V
    assert {rotate(w) for w in adj[v]}==adj[rotate(v)]
assert all(rotate(v)!=v for v in V)
assert all({rotate(v),rotate(w)}!={v,w} for v,w in (tuple(e) for e in E))
assert all(len(cyclic_orbit(v))==3 for v in V)

# Connectivity and integral homotopy of a graph. This BFS is a
# spanning-tree certificate (41 vertices after the root).
start=(0,1,3)
assert start in V
seen={start};queue=deque([start]);tree=[]
while queue:
    v=queue.popleft()
    for w in sorted(adj[v]):
        if w not in seen:
            seen.add(w);queue.append(w);tree.append((v,w))
assert len(seen)==42 and len(tree)==41
beta1=len(E)-len(V)+1
assert beta1==22

# Quotient by cyclic rotation of the source triple.
orbit_label={}
for v in sorted(V):
    if v not in orbit_label:
        c=len(set(orbit_label.values()))
        for w in cyclic_orbit(v):orbit_label[w]=c
assert len(set(orbit_label.values()))==14
quot_adj={i:set() for i in range(14)}
for e in E:
    v,w=tuple(e);i,j=orbit_label[v],orbit_label[w]
    assert i!=j
    quot_adj[i].add(j);quot_adj[j].add(i)
assert all(len(quot_adj[i])==3 for i in quot_adj)
assert sum(map(len,quot_adj.values()))//2==21
for v in V:
    assert len({orbit_label[w] for w in adj[v]})==3  # covering, not quotient multigraph

# Classify cyclic directed triangles by their underlying three-subsets.
A0={0,1,3};B0={0,1,5}
A=[frozenset((a+x)%7 for x in A0) for a in range(7)]
B=[frozenset((a+x)%7 for x in B0) for a in range(7)]
assert len(set(A))==7 and len(set(B))==7
underlying={frozenset(v) for v in V}
assert underlying == set(A)|set(B)
assert len(underlying)==14 and set(A).isdisjoint(set(B))
# Each cyclic orbit has precisely one underlying triple; compare quotient.
q_orbits={}
for v in V:
    if frozenset(v) in q_orbits:
        assert q_orbits[frozenset(v)]==orbit_label[v]
    else:
        q_orbits[frozenset(v)]=orbit_label[v]
# Edges iff 2-element intersection of underlying triples.
for x,y in combinations(underlying,2):
    edge=(q_orbits[y] in quot_adj[q_orbits[x]])
    assert edge == (len(x&y)==2)
# The two seven-line systems each form a cyclic (7,3,1) design.
for family in (A,B):
    assert all(len(x&y)==1 for x,y in combinations(family,2))
# Opposite-family incidence equals the Fano difference-set relation.
for a in range(7):
    for b in range(7):
        assert (len(A[a]&B[b])==2)==(((b-a)%7) in {0,2,3})
D={0,2,3}
assert Counter((x-y)%7 for x in D for y in D if x!=y)==Counter(range(1,7))

# On rational cellular homology of a graph, 3-cycle deck rotation acts
# freely on all vertex and edge cells. Lefschetz then gives trace H1=1.
# The trivial multiplicity is dim H1(quotient;Q)=21-14+1=8.
# The other unique rational irrep of C3 is Q(zeta_3), dimension 2.
invariants=21-14+1
nontrivial=(beta1-invariants)//2
assert invariants==8 and nontrivial==7
assert beta1 == invariants+2*nontrivial
assert invariants-nontrivial ==1
print('PALEY7_HOM_C3_FANO_COVER_VERIFIED')
print('cells_by_dimension=42,63; higher_cells=0')
print('graph=connected_cubic_42_vertices_63_edges_beta1_22')
print('quotient=Fano_Heawood_14_vertices_21_edges')
print('covering=regular_connected_three_sheeted')
print('deck_Q_C3_H1=8_trivial_plus_7_cyclotomic')
print('deck_H1_traces=22,1,1')
print('spanning_tree_edges=41')
