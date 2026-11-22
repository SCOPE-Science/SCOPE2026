#!/usr/bin/env python3
"""Exact cellular-chain calculations for geodesic general-position prism complexes.
Run: python3 verify.py. Python standard library only.
"""
from itertools import combinations
from collections import Counter

def vertex_dist(a,b,n):
    i,x=divmod(a,2); j,y=divmod(b,2)
    h=abs(i-j)
    return min(h,n-h)+abs(x-y)

def complex_faces(n):
    N=2*n
    bad=[]
    for a,b,c in combinations(range(N),3):
        if any(vertex_dist(x,z,n)==vertex_dist(x,y,n)+vertex_dist(y,z,n)
               for x,y,z in ((a,b,c),(a,c,b),(b,a,c))):
            bad.append((1<<a)|(1<<b)|(1<<c))
    faces={k:[] for k in range(4)}
    for mask in range(1,1<<N):
        if any(mask&b==b for b in bad):continue
        k=mask.bit_count()-1
        if k>3:raise AssertionError((n,mask,'unexpected dimension'))
        faces[k].append(tuple(i for i in range(N) if mask & (1<<i)))
    for k in faces:faces[k].sort()
    return bad,faces

def chain_boundary(faces,k):
    codom={f:i for i,f in enumerate(faces[k-1])};
    rows=[{} for _ in faces[k-1]]
    for j,s in enumerate(faces[k]):
        for t in range(k+1):
            r=codom[s[:t]+s[t+1:]]
            rows[r][j]= (-1)**t
    return rows,len(faces[k])

def primitive_rank(rows,ncols):
    """Exact integer unimodular elimination using only +/-1 pivots.
    An all-zero final matrix certifies that every nonzero Smith factor is 1.
    """
    rows=[r.copy() for r in rows]
    rank=0
    while True:
        # Find a unit pivot with low Schur-complement fill.
        cols=Counter(c for r in rows for c in r)
        best=None
        for i,row in enumerate(rows):
            for c,v in row.items():
                if abs(v)==1:
                    key=((len(row)-1)*(cols[c]-1),len(row)+cols[c],i,c)
                    if best is None or key<best[0]:best=(key,i,c,v)
        if best is None:break
        _,i,c,p=best
        pivot=rows[i]
        for j,row in enumerate(rows):
            if j==i or c not in row:continue
            mult=row.pop(c)//p
            for t,pv in pivot.items():
                if t==c:continue
                nv=row.get(t,0)-mult*pv
                if nv:row[t]=nv
                else:row.pop(t,None)
        rows.pop(i)
        rank+=1
    remaining=sum(len(row) for row in rows)
    assert remaining==0,('non-unit residual',rank,remaining)
    return rank

EXPECTED={
 3: ((6,15,8,0),(3,1,0)),
 4: ((8,28,8,2),(15,0,0)),
 5: ((10,45,50,10),(5,9,0)),
 6: ((12,66,52,18),(24,3,0)),
 7: ((14,91,154,56),(7,27,0)),
 8: ((16,120,160,76),(32,15,4)),
}
def verify():
    for n,(fv,betti) in EXPECTED.items():
        bad,faces=complex_faces(n)
        counts=tuple(len(faces[k]) for k in range(4))
        assert counts==fv,(n,counts,fv)
        ranks={0:0,4:0}
        for k in range(1,4):
            rows,ncols=chain_boundary(faces,k)
            ranks[k]=primitive_rank(rows,ncols)
        actual=tuple(counts[k]-ranks[k]-ranks[k+1] for k in range(1,4))
        assert actual==betti,(n,actual,betti)
        assert counts[0]-ranks[1]==1
        print(f'n={n}, bad_triples={len(bad)}, faces={counts}, boundary_ranks={(ranks[1],ranks[2],ranks[3])}, reduced_Betti={actual}, all_nonzero_Smith_factors=1')
    print('PASS: complete face enumeration and primitive integer ranks for n=3..8')
if __name__=='__main__':verify()
