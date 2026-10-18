#!/usr/bin/env python3
import itertools

P=[(x,y) for x in range(3) for y in range(3)]
idx={p:i for i,p in enumerate(P)}
# Four direction classes represented by normals, modulo nonzero scalars.
dirs=[(1,0),(0,1),(1,1),(1,2)]
lines=[]
for a,b in dirs:
    for c in range(3):
        L=frozenset(i for i,(x,y) in enumerate(P) if (a*x+b*y-c)%3==0)
        assert len(L)==3
        lines.append((a,b,c,L))
line_masks=frozenset(sum(1<<i for i in L) for *_,L in lines)
allmask=(1<<9)-1
blocks=[allmask ^ sum(1<<i for i in L) for *_,L in lines]
assert len(set(blocks))==12 and all(b.bit_count()==6 for b in blocks)
# point degrees in complement design
assert all(sum((b>>i)&1 for b in blocks)==8 for i in range(9))
# block-pair intersections: 12 pairs of size 3, 54 pairs of size 4.
c3=c4=0
adj=[set() for _ in range(12)]
for i in range(12):
    for j in range(i+1,12):
        s=(blocks[i]&blocks[j]).bit_count()
        if s==3:
            c3+=1; adj[i].add(j); adj[j].add(i)
        elif s==4:
            c4+=1
        else:
            raise AssertionError((i,j,s))
assert (c3,c4)==(12,54)
# size-3-intersection graph is 4 K3
seen=set(); comps=[]
for i in range(12):
    if i not in seen:
        st=[i]; comp=set()
        while st:
            u=st.pop()
            if u in comp: continue
            comp.add(u); seen.add(u); st.extend(adj[u]-comp)
        comps.append(comp)
assert sorted(map(len,comps))==[3,3,3,3]
assert all(sum(len(adj[u]&C) for u in C)==6 for C in comps)
# Exhaustive point-permutation automorphism count of the incidence design.
aut=[]
for perm in itertools.permutations(range(9)):
    ok=True
    for mask in line_masks:  # preserving complements iff preserving affine lines
        m=0
        for i in range(9):
            if (mask>>i)&1: m |= 1<<perm[i]
        if m not in line_masks:
            ok=False; break
    if ok: aut.append(perm)
assert len(aut)==432
# Generate all affine maps x -> A x + t; verify they are 432 distinct and equal to exhaustive set.
aff=set()
for a,b,c,d in itertools.product(range(3), repeat=4):
    if (a*d-b*c)%3==0: continue
    for u,v in P:
        perm=[]
        for x,y in P:
            q=((a*x+b*y+u)%3,(c*x+d*y+v)%3)
            perm.append(idx[q])
        aff.add(tuple(perm))
assert len(aff)==432
assert aff==set(aut)
assert 432//18==24 and 432%18==0
print('VERIFY_OK')
print('points=9 blocks=12 point_degree=8 block_size=6')
print('block_pair_intersections=size3:12,size4:54; size3_graph=4K3')
print('abstract_aut_order=432=|AGL(2,3)|')
print('projective_order_from_source=18; index=24')
