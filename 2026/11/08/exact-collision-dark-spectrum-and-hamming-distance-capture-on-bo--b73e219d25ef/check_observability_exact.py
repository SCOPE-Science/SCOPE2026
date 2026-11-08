#!/usr/bin/env python3
"""Finite exact cross-check for a two-boson collision detector on Q_d.

Integer (not orthonormal) symmetric-coordinate Hamiltonian. The stacked
observability matrix [D; DH; ...; DH^(2d)] has the same rational rank as
the full observed subspace. Ranks modulo 1000000007 provide exact finite
checks; the general proof is independent of these examples.
"""
from math import comb

P=1000000007

def rank_mod(a):
    m=len(a)
    n=len(a[0])
    r=0
    for c in range(n):
        pivot=next((i for i in range(r,m) if a[i][c]%P),None)
        if pivot is None:
            continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=pow(a[r][c]%P,P-2,P)
        a[r]=[(x*inv)%P for x in a[r]]
        ar=a[r]
        for i in range(r+1,m):
            v=a[i][c]%P
            if v:
                ai=a[i]
                for j in range(c,n): ai[j]=(ai[j]-v*ar[j])%P
        r+=1
        if r==m:break
    return r

def check(d):
    n=1<<d
    pairs=[(i,j) for i in range(n) for j in range(i,n)]
    pos={p:k for k,p in enumerate(pairs)}
    N=len(pairs)
    # H_{(x,y),(i,j)} acts on symmetric coordinate amplitudes f(i,j).
    rows=[]
    for x,y in pairs:
        coeff={}
        for b in range(d):
            u,v=sorted((x^(1<<b),y))
            k=pos[u,v]; coeff[k]=coeff.get(k,0)+1
            u,v=sorted((x,y^(1<<b)))
            k=pos[u,v]; coeff[k]=coeff.get(k,0)+1
        rows.append(coeff)
    cols=[{} for _ in range(N)]
    for i,entries in enumerate(rows):
        for j,v in entries.items(): cols[j][i]=v
    R=[]
    for x in range(n):
        row=[0]*N
        row[pos[x,x]]=1
        R.append(row)
    stacked=[]
    for t in range(2*d+1):
        stacked.extend([r[:] for r in R])
        new=[]
        for row in R:
            nr=[0]*N
            for j,coeff in enumerate(cols):
                nr[j]=sum(row[k]*v for k,v in coeff.items())%P
            new.append(nr)
        R=new
    rank=rank_mod(stacked)
    bright=n*(d+2)//2
    dark=N-bright
    assert rank==bright, (d,N,rank,bright)
    assert dark==2**(d-1)*(2**d-d-1)
    print(f'EXACT_OBSERVABILITY_PASS d={d} N={N} rank={rank} dark={dark}')

for d in range(1,5):check(d)
