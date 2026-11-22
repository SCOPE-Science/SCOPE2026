#!/usr/bin/env python3
"""Independent exact arithmetic checks for the finite-field arity threshold.
This program checks ranks of pure diagonal symmetric tensors and explicit
Frobenius counterexample identities. It does not replace the general proof.
"""
from itertools import product
from math import comb

def multi(n,m):
    if n==1:
        yield (m,)
    else:
        for k in range(m+1):
            for a in multi(n-1,m-k):yield (k,)+a

def rankmod(M,p):
    A=[list(map(lambda x:x%p,row)) for row in M]
    if not A:return 0
    h,w=len(A),len(A[0]); r=0
    for c in range(w):
        t=next((i for i in range(r,h) if A[i][c]),None)
        if t is None:continue
        A[r],A[t]=A[t],A[r]
        factor=pow(A[r][c],-1,p)
        A[r]=[(v*factor)%p for v in A[r]]
        for i in range(h):
            if i!=r and A[i][c]:
                factor=A[i][c]
                A[i]=[(x-factor*y)%p for x,y in zip(A[i],A[r])]
        r+=1
        if r==h:break
    return r

def check(p,n,m):
    B=list(multi(n,m)); N=len(B)
    pts=list(product(range(p),repeat=n))
    M=[[__import__('math').prod(pow(a[i],b[i],p) for i in range(n))%p for a in pts] for b in B]
    rr=rankmod(M,p)
    assert (rr==N)==(m<=p), ('span',p,n,m,N,rr)
    if m>p:
        for a in pts:
            lhs=(pow(a[0],m-1,p)*a[1] - pow(a[0],m-p,p)*pow(a[1],p,p))%p
            assert lhs==0,('Frobenius identity failed',p,n,m,a)
        b1=(m-1,1)+(0,)*(n-2)
        b2=(m-p,p)+(0,)*(n-2)
        assert b1!=b2 and b1 in B and b2 in B
    print('CHECK',p,n,m,rr,N)

if __name__=='__main__':
    for p in (2,3,5):
        for n in (2,3):
            for m in range(2,p+3):check(p,n,m)
    print('THRESHOLD_VERIFY_OK')
