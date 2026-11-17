#!/usr/bin/env python3
"""Finite checks of fixed-sector structure and star cubical Euler characteristics."""
from itertools import combinations
from math import comb
from collections import defaultdict

def star_graph(arms, depth):
    # Vertex zero is the center; each arm has depth vertices.
    verts = {(i,j):1+i*depth+j for i in range(arms) for j in range(depth)}
    edges=[]
    for i in range(arms):
        edges.append((0,verts[(i,0)]))
        edges.extend((verts[(i,j)],verts[(i,j+1)]) for j in range(depth-1))
    return 1+arms*depth,edges

def cells(arms,particles,depth):
    V,edges=star_graph(arms,depth)
    counts=defaultdict(int)
    # Build matching sets recursively. For each choose remaining distinct vertices.
    def rec(mini, selected, occupied):
        ecount=len(selected)
        remaining=particles-ecount
        if remaining>=0:
            allowed=[v for v in range(V) if v not in occupied]
            if len(allowed)>=remaining:
                counts[ecount]+=comb(len(allowed),remaining)
        if ecount>=particles:return
        for t in range(mini,len(edges)):
            u,v=edges[t]
            if u in occupied or v in occupied:continue
            rec(t+1, selected+[t],occupied|{u,v})
    rec(0,[],set())
    return counts

def rank(m,b):
    if b==0:return 0
    return 1+(m-1)*comb(b+m-2,m-1)-comb(b+m-1,m-1)

def direct_fixed_orbit_counts(m,k):
    # Theta_m with each arm subdivided into 4 edges. The pole reversal
    # fixes the m middle vertices; all other vertices form 2-cycles.
    vertex_count=2+3*m
    def image(v):
        if v==0:return 1
        if v==1:return 0
        arm,step=divmod(v-2,3)
        return 2+arm*3+(2-step)
    if vertex_count>19:return None
    counts=defaultdict(int)
    for S in combinations(range(vertex_count),k):
        t=set(S)
        if {image(v) for v in t}!=t:continue
        a=sum(image(v)==v for v in t)
        counts[a]+=1
    return dict(counts)

nEuler=0; nFixed=0
for m in range(3,7):
    for b in range(0,5):
        depth=max(b+2,3)
        ncell=cells(m,b,depth)
        chi=sum((-1)**dim*cnt for dim,cnt in ncell.items())
        expected=1-rank(m,b)
        assert chi==expected,(m,b,chi,expected,ncell)
        nEuler+=1
    for k in range(0,7):
        actual=direct_fixed_orbit_counts(m,k)
        if actual is None:continue
        # An involution-invariant vertex set is a union of fixed points and two-cycles.
        expected={a:comb(m,a)*comb(1+m,(k-a)//2) for a in range(m+1) if (k-a)%2==0 and 0<=(k-a)//2<=1+m}
        assert actual==expected,(m,k,actual,expected)
        nFixed+=1
nPrimary=0
for m in range(3,15):
    for b in range(2,18):
        radial_rank=sum(comb(b+m-2,b-1)-comb(b+m-i-1,b-1) for i in range(2,m))
        assert radial_rank==rank(m,b),(m,b,radial_rank,rank(m,b))
        nPrimary+=1
print('STAR_CUBICAL_EULER_CHECKS',nEuler)
print('RADIAL_TREE_LITERATURE_RANK_CHECKS',nPrimary)
print('POLE_INVARIANT_DISCRETE_VERTEX_SECTORS',nFixed)
print('THETA_POLE_FIXED_SECTOR_CHECKS_PASS')
