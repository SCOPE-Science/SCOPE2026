#!/usr/bin/env python3
"""Exact checks for the alternating rank-at-most-four Fourier ball.
The computations are finite corroboration, not a substitute for the symbolic proof.
"""
from functools import lru_cache
from itertools import product
from math import comb

@lru_cache(None)
def gaussian(n,k,q):
    if k<0 or k>n:return 0
    if k==0 or k==n:return 1
    return gaussian(n-1,k,q)+q**(n-k)*gaussian(n-1,k-1,q)

def symplectic_isotropic(r,t,q):
    if t<0 or t>r:return 0
    z=gaussian(r,t,q)
    for i in range(t):z*=q**(r-i)+1
    return z

def isotropic(n,r,k,q):
    d=n-2*r
    return sum(gaussian(d,s,q)*q**((d-s)*(k-s))*symplectic_isotropic(r,k-s,q) for s in range(min(k,d)+1))

def rank_count(n,r,q):
    v=gaussian(n,2*r,q)*q**(r*(r-1))
    for j in range(1,r+1):v*=q**(2*j-1)-1
    return v

def transform_incidence(n,r,q):
    a=gaussian(n,2,q);b=gaussian(n-2,2,q);c=gaussian(n,4,q)
    return q**6*isotropic(n,r,4,q)+(1-b)*q*isotropic(n,r,2,q)+1-c-(1-b)*a

def transform_polynomial(n,r,q):
    h=q**n;z=q**(n-2*r);ss=sum(q**j for j in range(4))
    D=q**4*(q*q-1)**2*(q*q+1)
    num=h*h*(z*z-ss*z+q*ss)+h*q**5*((q*q+1)*z-ss)+q**10
    assert num%D==0
    return num//D

def ball_count(n,q):
    return sum(rank_count(n,r,q) for r in range(3))

def checks():
    total=0
    for q in (2,3,4,5,7,8):
        for n in range(6,13):
            a=[transform_incidence(n,r,q) for r in range(n//2+1)]
            b=[transform_polynomial(n,r,q) for r in range(n//2+1)]
            assert a==b,(q,n,'formula',a,b)
            N=[rank_count(n,r,q) for r in range(n//2+1)]
            M=q**comb(n,2);T=ball_count(n,q)
            assert sum(N)==M
            assert b[0]==T
            assert sum(x*y for x,y in zip(N,b))==M
            assert sum(x*y*y for x,y in zip(N,b))==M*T
            neg=[r for r,val in enumerate(b) if val<0]
            assert neg==[n//2-1],(q,n,'sign',neg)
            assert 0 not in b
            R=n//2-1; X=-b[R]
            if n%2==0:
                h=q**n; num=q*(h-q**4)*(h*(q**4-q**3-1)+q**5)
            else:
                h=q**n; num=q*(h-q**5)*(h*(q**4-q-1)+q**4)
            D=q**4*(q*q-1)**2*(q*q+1)
            assert num//D==X and num%D==0
            lhs=sum(t*abs(u) for t,u in zip(N,b))
            assert lhs==M+2*N[R]*X
            total+=1
    print('EXACT_SYMBOLIC_ORBIT_TESTS_PASS',total)

def bitrank(rows,n):
    R=0
    for i in range(n):
        pivot=max((j for j in range(R,n) if (rows[j]>>i)&1),default=None)
        if pivot is None:continue
        rows[R],rows[pivot]=rows[pivot],rows[R]
        for j in range(n):
            if j!=R and ((rows[j]>>i)&1):rows[j]^=rows[R]
        R+=1
    return R

def direct_binary(n):
    # Independent construction using upper-triangle bit strings and a full Walsh transform.
    import numpy as np
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    N=len(pairs);size=1<<N
    f=np.zeros(size,dtype=np.int64)
    ranks=np.zeros(size,dtype=np.uint8)
    for mask in range(size):
        rows=[0]*n
        for k,(i,j) in enumerate(pairs):
            if (mask>>k)&1:
                rows[i]^=1<<j
                rows[j]^=1<<i
        R=bitrank(rows,n)
        ranks[mask]=R//2
        f[mask]=int(R<=4)
    T=int(f.sum());assert T==ball_count(n,2)
    block=1
    while block<size:
        m=f.reshape(-1,2*block)
        left=m[:,:block].copy();right=m[:,block:].copy()
        m[:,:block]=left+right
        m[:,block:]=left-right
        block*=2
    for r in range(n//2+1):
        vals=f[ranks==r]
        assert vals.size==rank_count(n,r,2)
        assert np.all(vals==transform_polynomial(n,r,2)),(n,r,set(vals.tolist()))
    print('FULL_BINARY_FOURIER_CHECK_PASS',n,size,T)

if __name__=='__main__':
    checks()
    direct_binary(6)
    direct_binary(7)
    print('ALL_ALTERNATING_RANK_FOUR_CHECKS_PASS')
