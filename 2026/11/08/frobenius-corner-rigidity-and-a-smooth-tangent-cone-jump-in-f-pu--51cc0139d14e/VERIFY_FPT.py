#!/usr/bin/env python3
"""Exact low-level polynomial Frobenius quotient checks (stdlib only)."""
from collections import defaultdict
from math import comb

def poly_mul(A,B,p,Q):
    C=defaultdict(int)
    for a,ca in A.items():
        for b,cb in B.items():
            ex=tuple(x+y for x,y in zip(a,b))
            if all(z<Q for z in ex):
                C[ex]=(C[ex]+ca*cb)%p
    return {ex:c for ex,c in C.items() if c}

def poly_pow(A,k,p,Q,n):
    R={(0,)*n:1}
    while k:
        if k&1:R=poly_mul(R,A,p,Q)
        k//=2
        if k:A=poly_mul(A,A,p,Q)
    return R

def cases(p,r,n,maxe):
    q=p**r;m=q-1
    for lam in (0,1):
        A={tuple((q+1 if j==i else 0) for j in range(n)):1 for i in range(n)}
        if lam:
            c=(m,)*n;A[c]=(A.get(c,0)+lam)%p
        for e in range(1,maxe+1):
            Q=p**e
            goal=((Q-1)//m if lam else (p**(e-r)-1 if e>=r else 0))
            v=poly_pow(A,goal,p,Q,n)
            w=poly_mul(v,A,p,Q)
            assert v, (p,r,n,lam,e,goal,'missing survivor')
            assert not w,(p,r,n,lam,e,goal,'unexpected next survivor',w)
            if lam:
                t=e%r
                expected=(Q-p**t,)*n
                assert v=={expected:1},(p,r,n,lam,e,'wrong exact corner',v)
            print(f'p={p} r={r} n={n} lambda={lam} e={e} nu={goal} checked')
for params in [(2,2,2,6),(2,2,3,4),(3,2,2,4),(5,1,2,3),(2,3,2,5)]:
    cases(*params)
print('CERTIFICATE_OK')
