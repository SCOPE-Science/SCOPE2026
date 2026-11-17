#!/usr/bin/env python3
"""Independent finite-field boundary calculation for two graph complexes."""
from collections import defaultdict

def edges(kind):
    # Construct the 16-vertex graph without using an adjacency-mask generator.
    E=set()
    for x in range(4):
        for y in range(4):
            u=4*x+y
            if kind=='Shrikhande':
                diffs=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)]
                vv=[4*((x+a)%4)+(y+b)%4 for a,b in diffs]
            else:
                vv=[4*a+y for a in range(4) if a!=x]+[4*x+b for b in range(4) if b!=y]
            for v in vv:E.add(tuple(sorted((u,v))))
    assert len(E)==48
    return E

def simplices(E):
    adj=[set() for _ in range(16)]
    for u,v in E:adj[u].add(v);adj[v].add(u)
    ranks=defaultdict(list)
    for mask in range(1,1<<16):
        vs=[v for v in range(16) if mask & (1<<v)]
        if all(len(adj[v].intersection(vs))<=1 for v in vs):
            ranks[len(vs)-1].append(mask)
    return ranks

def rank_boundary(src,rows):
    loc={f:j for j,f in enumerate(rows)}
    basis={}
    for m in src:
        vec=0
        for b in range(16):
            bit=1<<b
            if m&bit:vec^=1<<loc[m^bit]
        while vec:
            piv=vec.bit_length()-1
            if piv in basis:vec^=basis[piv]
            else:
                basis[piv]=vec
                break
    return len(basis)

for name in ['Shrikhande','Rook']:
    F=simplices(edges(name))
    maxdim=max(F)
    b={0:0}
    for d in range(1,maxdim+1):b[d]=rank_boundary(F[d],F[d-1])
    betti={d:len(F[d])-b.get(d,0)-b.get(d+1,0) for d in range(maxdim+1)}
    print(name,'face_vector',[len(F[d]) for d in range(maxdim+1)],'boundary_ranks',[b[d] for d in range(1,maxdim+1)],'betti',[betti[d] for d in range(maxdim+1)])
    assert betti[0]==1
    assert {k:v for k,v in betti.items() if k>0 and v}=={3:57 if name=='Shrikhande' else 105}
print('INDEPENDENT_MOD2_HOMOLOGY_PASS')
