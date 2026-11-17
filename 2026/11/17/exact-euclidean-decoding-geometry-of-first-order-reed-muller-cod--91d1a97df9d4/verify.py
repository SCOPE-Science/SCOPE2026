#!/usr/bin/env python3
"""Exact tests for Euclidean projection of binary truth tables onto affine-codeword polytopes."""
from fractions import Fraction
from collections import Counter
from math import isqrt


def fwht(a):
    a=list(a)
    h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):
                p,q=a[k],a[k+h]
                a[k],a[k+h]=p+q,p-q
        h*=2
    return a


def proj_data(W):
    """Euclidean l1 projection in UNNORMALIZED Walsh coordinates: sum |z| <= n."""
    n=len(W)
    magnitudes=sorted(map(abs,W),reverse=True)
    assert sum(w*w for w in W)==n*n
    if sum(magnitudes)==n:
        tau=Fraction(0)
    else:
        tau=None
        for k in range(1,n+1):
            candidate=Fraction(sum(magnitudes[:k])-n,k)
            if candidate>=0 and magnitudes[k-1]>=candidate and (k==n or candidate>=magnitudes[k]):
                tau=candidate
                break
        assert tau is not None
    z=[(1 if w>=0 else -1)*max(Fraction(abs(w))-tau,0) for w in W]
    assert sum(map(abs,z))<=n
    if tau>0:
        assert sum(map(abs,z))==n
    residual=[Fraction(w)-a for w,a in zip(W,z)]
    # KKT: residual equals threshold times the active facet sign,
    # or equals W when z is zero.
    assert all((r==(tau if z_i>0 else -tau) if z_i else abs(r)<=tau)
               for r,z_i in zip(residual,z))
    d2=sum(r*r for r in residual)/Fraction(4*n)
    return d2,z,tau


def bent_truth_table(m):
    assert m%2==0
    n=1<<m
    return [(-1 if sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(m//2))%2 else 1)
            for x in range(n)]


def run():
    for m in (2,3,4):
        n=1<<m
        counts=Counter(); bent_count=0
        for mask in range(1<<n):
            s=[1-2*((mask>>i)&1) for i in range(n)]
            W=fwht(s)
            d2,_,_=proj_data(W)
            counts[d2]+=1
            if m%2==0 and all(abs(w)==isqrt(n) for w in W):
                bent_count+=1
                assert d2==Fraction((isqrt(n)-1)**2,4)
        if m==2:
            assert counts=={Fraction(1,4):8,Fraction(0):8}
            assert bent_count==8
        if m==3:
            assert counts=={Fraction(9,16):128,Fraction(1,2):112,Fraction(0):16}
        if m==4:
            assert max(counts)==Fraction(9,4) and counts[Fraction(9,4)]==896
            assert bent_count==896
        print('EXHAUSTIVE m=',m,'truth_tables=',1<<n,
              'squared_distance_levels=',len(counts),'max=',max(counts),'max_count=',counts[max(counts)])
    for m in (2,4,6,8):
        n=1<<m
        s=bent_truth_table(m)
        W=fwht(s)
        assert all(abs(w)==isqrt(n) for w in W)
        d2,z,tau=proj_data(W)
        assert d2==Fraction((isqrt(n)-1)**2,4)
        assert tau==isqrt(n)-1
        assert all(abs(zi)==1 for zi in z)  # each facet coefficient is 1/n
        print('BENT_WITNESS m=',m,'dimension=',n,'squared_distance=',d2,'support=',sum(zi!=0 for zi in z))
    print('RM1_CODEWORD_PROJECTION_PASS')

if __name__=='__main__':
    run()
