#!/usr/bin/env python3
"""Exact census of left/right multiplication ranks for binary Alexander quandle algebras.

Uses the original multiplication table and ordinary finite-field Gaussian elimination.
Does not use Fourier coordinates in the observed-rank calculation.
"""
import itertools, math
from collections import defaultdict

def apply(cols,x):
    y=0
    for i,c in enumerate(cols):
        if x&(1<<i): y ^= c
    return y

def rank2(vals):
    pivot={}
    for x in vals:
        y=x
        while y:
            j=y.bit_length()-1
            if j in pivot: y ^= pivot[j]
            else: pivot[j]=y;break
    return len(pivot)

def rankmod(M,p):
    n=len(M); m=len(M[0]); A=[row[:] for row in M]
    r=0
    for c in range(m):
        k=next((i for i in range(r,n) if A[i][c]%p),None)
        if k is None: continue
        A[r],A[k]=A[k],A[r]
        inv=pow(A[r][c],-1,p)
        for j in range(c,m): A[r][j]=A[r][j]*inv%p
        for i in range(r+1,n):
            a=A[i][c]
            if a:
                for j in range(c,m): A[i][j]=(A[i][j]-a*A[r][j])%p
        r+=1
        if r==n:break
    return r

def poly_theorem(m,h,d,q):
    t=2**(m-h);j=2**d; c=2**(h-d)
    P={(0,0):1}
    def mul(factor):
        nonlocal P
        Z=defaultdict(int)
        for (a,b),v in P.items():
            for (u,w),z in factor.items(): Z[(a+u,b+w)]+=v*z
        P=dict(Z)
    for _ in range(2**h-c):mul({(0,0):1,(0,1):q**t-1})
    F={(0,0):1,(0,1):q**(t-j)-1}
    for s in range(1,j+1): F[(s,1)]=q**(t-j)*math.comb(j,s)*(q-1)**s
    for _ in range(c):mul(F)
    return {k:v for k,v in P.items() if v}

def check(name,m,phi,q=3):
    N=2**m
    B=[(1<<i)^phi[i] for i in range(m)]
    h=rank2(B)
    im={apply(B,x) for x in range(N)}
    ker={x for x in range(N) if apply(B,x)==0}
    d=rank2([x for x in im if x in ker]);t=len(ker)
    assert 2**d == len(im.intersection(ker))
    mult=[[apply(phi,x)^apply(B,y) for y in range(N)] for x in range(N)]
    observed=defaultdict(int)
    for v in itertools.product(range(q),repeat=N):
        R=[[0]*N for _ in range(N)]
        L=[[0]*N for _ in range(N)]
        for j in range(N):
            for a in range(N):
                R[mult[a][j]][a]=(R[mult[a][j]][a]+v[j])%q
                L[mult[j][a]][a]=(L[mult[j][a]][a]+v[j])%q
        rr=rankmod(R,q);ll=rankmod(L,q)
        assert rr%t==0,(name,rr,t)
        observed[(rr//t,ll)]+=1
    predicted=poly_theorem(m,h,d,q)
    assert dict(observed)==predicted,(name,dict(observed),predicted)
    print(f'{name}: m={m} h={h} d={d} kernel={t} q={q} elements={q**N} strata={len(observed)} xy_coefficient={observed.get((1,1),0)} MATCH')
    return q**N

cases=[('trivial2',2,[1,2]),('jordan2',2,[1,3]),('order3',2,[2,3]),
       ('jordan3',3,[1,3,6]),('one_plus_order3',3,[1,4,6]),('jordan2_plus1',3,[1,3,4]),
       ('trivial3',3,[1,2,4]),('order7',3,[2,4,3])]
tot=0
for args in cases:tot+=check(*args)
print('VERIFY_OK',f'cases={len(cases)}',f'original_basis_elements_tested={tot}',f'operator_rank_calculations={2*tot}')
