#!/usr/bin/env python3
"""Independent enumeration of ordered idempotent decompositions of square-zero matrices.

Fields are F2, F4=F2[t]/(t^2+t+1), F8=F2[t]/(t^3+t+1).
"""
from collections import Counter
from itertools import product

MODULUS = {2: 3, 4: 7, 8: 11}

def mul(x,y,q):
    p=0
    f=q.bit_length()-1
    for bit in range(f):
        if (y>>bit)&1:p ^= x<<bit
    for bit in range(2*f-2,f-1,-1):
        if p & (1<<bit):p ^= MODULUS[q] << (bit-f)
    return p

def matmul(a,b,n,q):
    c=[0]*(n*n)
    for i in range(n):
        for k in range(n):
            v=a[i*n+k]
            if v:
                for j in range(n):
                    c[i*n+j]^=mul(v,b[k*n+j],q)
    return tuple(c)

def rank(a,n,q):
    A=[list(a[i*n:(i+1)*n]) for i in range(n)]
    piv=0
    for j in range(n):
        k=next((k for k in range(piv,n) if A[k][j]),None)
        if k is None:continue
        A[piv],A[k]=A[k],A[piv]
        inv=next(t for t in range(1,q) if mul(t,A[piv][j],q)==1)
        for h in range(j,n):A[piv][h]=mul(inv,A[piv][h],q)
        for k in range(n):
            if k==piv:continue
            t=A[k][j]
            for h in range(j,n):A[k][h]^=mul(t,A[piv][h],q)
        piv+=1
        if piv==n:break
    return piv

def gauss(n,k,q):
    if k<0 or k>n:return 0
    ans=1
    for i in range(k):ans=ans*(q**(n-i)-1)//1
    # Exact integer numerator and denominator, separately.
    numerator=1;denominator=1
    for i in range(k):
        numerator*=q**(n-i)-1
        denominator*=q**(k-i)-1
    return numerator//denominator

def expected(n,r,q):
    s=n-2*r
    M=sum(gauss(r,a,q)*q**(r*r-a*(r-a)) for a in range(r+1))
    return {r+b:q**(r*s)*M*gauss(s,b,q)*q**(b*(s-b))
            for b in range(s+1)}

def verify(n,r,q):
    N=[0]*(n*n)
    for i in range(r):N[i*n+r+i]=1
    N=tuple(N)
    counts=Counter()
    total=0
    for a in product(range(q),repeat=n*n):
        if matmul(a,a,n,q)!=a:continue
        b=tuple(x^y for x,y in zip(a,N))
        if matmul(b,b,n,q)!=b:continue
        # Every solution is counted exactly once as its first summand.
        assert all((x^y)==z for x,y,z in zip(a,b,N))
        assert matmul(N,N,n,q)==(0,)*(n*n)
        counts[rank(a,n,q)]+=1
        assert rank(b,n,q)==rank(a,n,q)
        total+=1
    want=expected(n,r,q)
    assert dict(counts)==want,(n,r,q,dict(counts),want)
    print('PASS','n',n,'rank_N',r,'field',q,
          'rank_profile',sorted(counts.items()),'total',total)

if __name__=='__main__':
    for q in (2,4,8):
        for n,r in [(2,0),(2,1)]:verify(n,r,q)
    for q in (2,4):
        for n,r in [(3,0),(3,1)]:verify(n,r,q)
    for r in (0,1,2):verify(4,r,2)
    print('ALL_SQUAREZERO_IDEMPOTENT_SUM_FIBERS_PASS')
