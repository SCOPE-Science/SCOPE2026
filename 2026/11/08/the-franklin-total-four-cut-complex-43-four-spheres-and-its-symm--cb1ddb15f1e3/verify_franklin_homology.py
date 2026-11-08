#!/usr/bin/env python3
"""Independent boundary-matrix homology check for the Franklin total 4-cut complex."""
from itertools import combinations
N=12
edges={tuple(sorted((i,(i+1)%N))) for i in range(N)}
edges|={tuple(sorted((i,(i+(5 if i%2==0 else -5))%N))) for i in range(N)}
adj=[0]*N
for i,j in edges:adj[i]|=1<<j;adj[j]|=1<<i
indeps=[sum(1<<i for i in c) for c in combinations(range(N),4)
        if all(not (adj[i]>>j & 1) for i,j in combinations(c,2))]
faces=[s for s in range(1,1<<N) if any(s&i==0 for i in indeps)]
bydim=[[s for s in faces if s.bit_count()==k+1] for k in range(8)]
assert tuple(len(x) for x in bydim)==(12,66,220,495,792,638,264,45)

def rank_gfp(dim,prime):
    if dim==0:return 0
    rowindex={s:i for i,s in enumerate(bydim[dim-1])}
    pivots={}
    for s in bydim[dim]:
        ordered=[i for i in range(N) if s>>i&1]
        col={rowindex[s^(1<<i)]: (1 if j%2==0 else prime-1)
             for j,i in enumerate(ordered)}
        while col:
            r=max(col)
            if r not in pivots:
                inv=pow(col[r],-1,prime)
                pivots[r]={j:(v*inv)%prime for j,v in col.items()}
                break
            scalar=col[r]
            for j,v in pivots[r].items():
                z=(col.get(j,0)-scalar*v)%prime
                if z:col[j]=z
                else:col.pop(j,None)
    return len(pivots)
for prime in (2,3,5):
    ranks=[0]+[rank_gfp(k,prime) for k in range(1,8)]+[0]
    betti=[len(bydim[k])-ranks[k]-ranks[k+1] for k in range(8)]
    assert betti == [1,0,0,0,43,0,0,0],(prime,ranks,betti)
    print('GF',prime,'boundary ranks',ranks[1:8],'betti',betti)
print('ALL_HOMOLOGY_OK')
