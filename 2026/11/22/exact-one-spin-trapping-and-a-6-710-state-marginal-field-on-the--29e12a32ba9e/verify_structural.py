#!/usr/bin/env python3
"""Combinatorial certificates using face-dual matchings and constrained sets.
No full energy scan is used. Vertices are u_0..u_9,v_0..v_9.
"""
from collections import Counter
from functools import lru_cache
N=20
ALL=(1<<N)-1
edges=[]
for i in range(10):
    edges += [tuple(sorted((i,(i+1)%10))),
              tuple(sorted((i,10+i))),
              tuple(sorted((10+i,10+(i+2)%10)))]
edges=sorted(set(edges))
assert len(edges)==30
nbr=[0]*N
for i,j in edges:
    nbr[i]|=1<<j;nbr[j]|=1<<i
assert all(z.bit_count()==3 for z in nbr)
faces=[]
for i in range(10):
    faces.append([i,(i+1)%10,(i+2)%10,10+(i+2)%10,10+i])
faces += [[10+i for i in (0,2,4,6,8)],[10+i for i in (1,3,5,7,9)]]
assert len(faces)==12
edge_faces={e:[] for e in edges}
for k,face in enumerate(faces):
    assert len(set(face))==5
    for a,b in zip(face,face[1:]+face[:1]):
        e=tuple(sorted((a,b)))
        assert e in edge_faces
        edge_faces[e].append(k)
assert all(len(f)==2 for f in edge_faces.values())
dual_edges={tuple(sorted(v)):e for e,v in edge_faces.items()}
assert len(dual_edges)==30
D=[0]*12
for a,b in dual_edges:
    D[a]|=1<<b;D[b]|=1<<a
assert all(x.bit_count()==5 for x in D)

# Each matching of the face-dual graph labels one aligned primal edge per face.
# The resulting primal edge signs are consistent because every face has
# exactly four anti-aligned edges, giving even spin-change parity.
count=0
magn=Counter()
def matching(rem,chosen):
    global count
    if not rem:
        count+=1
        aligned={dual_edges[e] for e in chosen}
        spin=[0]*N;spin[0]=1
        stack=[0]
        while stack:
            i=stack.pop()
            for j in range(N):
                if nbr[i]>>j&1:
                    v=spin[i]*(1 if tuple(sorted((i,j))) in aligned else -1)
                    if not spin[j]:spin[j]=v;stack.append(j)
                    else:assert spin[j]==v
        assert all(spin)
        m=sum(spin)
        magn[m]+=1;magn[-m]+=1
        return
    low=rem&-rem;i=low.bit_length()-1
    nxt=D[i]&rem
    while nxt:
        jbit=nxt&-nxt;nxt-=jbit
        j=jbit.bit_length()-1
        matching(rem^low^jbit,chosen+(tuple(sorted((i,j))),))
matching((1<<12)-1,())
assert count==125
assert dict(magn)=={-4:5,0:240,4:5},magn

# Independent vertex sets of the primal graph, including empty set.
independence=Counter();maximal=Counter();max_at_h1=0

def indsets(rem,picked):
    global max_at_h1
    if not rem:
        k=picked.bit_count()
        independence[k]+=1
        dominated=picked
        for i in range(N):
            if picked>>i&1:dominated|=nbr[i]
        if dominated==ALL:
            maximal[k]+=1
            if all((picked&nbr[i]).bit_count()>=2 for i in range(N) if not (picked>>i&1)):
                max_at_h1+=1
        return
    bit=rem&-rem;i=bit.bit_length()-1
    indsets(rem^bit,picked)
    indsets(rem&~bit&~nbr[i],picked|bit)
indsets(ALL,0)
assert sum(independence.values())==5828, independence
assert dict(maximal)=={6:10,7:280,8:5}, maximal
assert max_at_h1==5

# At h/J=1 a weakly stable state has negative spins forming a dominating
# vertex set of induced maximum degree <=1. Generate such sets directly.
diss_count=0
def disssets(i,picked,degrees):
    global diss_count
    if i==N:
        dominated=picked
        for j in range(N):
            if picked>>j&1:dominated|=nbr[j]
        if dominated==ALL:diss_count+=1
        return
    disssets(i+1,picked,degrees)
    selected=[j for j in range(i) if (picked&nbr[i])>>j&1]
    if len(selected)>1 or any(degrees[j] for j in selected):return
    new=degrees.copy()
    new[i]=len(selected)
    for j in selected:new[j]+=1
    disssets(i+1,picked|(1<<i),new)
disssets(0,0,[0]*N)
assert diss_count==6710,diss_count
print('STRUCTURAL_PASS dual_matchings=125 zero_field_ground=250')
print('magnetization_distribution=',dict(sorted(magn.items())))
print('independent_sets=',dict(sorted(independence.items())))
print('maximal_independent_sets=',dict(sorted(maximal.items())))
print('h_equal_1_weak=',diss_count,'h_equal_1_strict=',max_at_h1)
