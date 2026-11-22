#!/usr/bin/env python3
"""Exact rational checks of rank-resolved 1D Euler curve / sample variance theorem.
All tests use the stated independent-Uniform(0,1) model and n-1 unbiased variance.
Only Python standard-library arithmetic is required.
"""
from fractions import Fraction as F
from math import comb

def Qcoeff(n):
    # Pairwise variance identity: S^2 = sum_{a<b}(U_(b)-U_(a))^2/[n(n-1)].
    Q = [[F(0) for _ in range(n-1)] for _ in range(n-1)]
    for a in range(1,n+1):
        for b in range(a+1,n+1):
            for i in range(a,b):
                for j in range(a,b):
                    Q[i-1][j-1] += F(1,n*(n-1))
    return Q

def via_conditional(n,k,t):
    # Affine-simplex memorylessness under D_k>t:
    # D'_k=t+(1-t)Z_k, D'_j=(1-t)Z_j (j!=k),
    # Z~Dirichlet(1,...,1), m=n+1 coordinates.
    m=n+1
    Q=Qcoeff(n)
    E=F(0)
    for i in range(n-1):
        for j in range(n-1):
            ezz= F(1+(i==j),m*(m+1))
            d= (1-t)**2 * ezz
            if i==k-1: d+=t*(1-t)*F(1,m)
            if j==k-1: d+=t*(1-t)*F(1,m)
            if i==k-1 and j==k-1: d+=t*t
            E += Q[i][j]*d
    return (1-t)**n * (E-F(1,12))

def formula(n,k,t):
    b=F(k*(n-k),n*(n-1))
    return (1-t)**n*t*( b*F(n, n+1)+b*t*F(1,n+1)+(t-2)*F(1,12))

def total(n,t):
    return (1-t)**n*t*(2+(n+1)*t)*F(1,12)

def signs(n,k):
    b=F(k*(n-k),n*(n-1))
    # sign profile bracket is strictly increasing with t
    lo=b*F(n,n+1)-F(1,6)
    hi=b-F(1,12)
    transition= F(2*(n+1)-12*n*b, 12*b+n+1)
    return lo,hi,transition

def check():
    checks=0
    for n in range(2,18):
        Q=Qcoeff(n)
        assert sum(Q[i][i] for i in range(n-1))==F(n+1,6); checks+=1
        assert sum(sum(row) for row in Q)==F(n*(n+1),12);checks+=1
        for k in range(1,n):
            b=F(k*(n-k),n*(n-1))
            assert Q[k-1][k-1]==b; checks+=1
            assert sum(Q[k-1])==F(k*(n-k),2*(n-1));checks+=1
            for t in (F(1,20),F(2,9),F(1,3),F(3,4),F(11,12)):
                assert via_conditional(n,k,t)==formula(n,k,t),(n,k,t);checks+=1
            lo,hi,trans=signs(n,k)
            if lo<0<hi:
                assert 0<trans<1 and formula(n,k,trans)==0;(checks:=checks+1)
        for t in (F(1,20),F(2,9),F(1,3),F(3,4),F(11,12)):
            assert sum(formula(n,k,t) for k in range(1,n))==total(n,t);checks+=1
            assert total(n,t)>0;checks+=1
    # The near-end, first interior gap is sign-changing exactly for 6<=n<=11.
    for n in range(2,31):
        lo,hi,tr=signs(n,1)
        if 6<=n<=11: assert lo<0<hi and 0<tr<1
        elif n==5: assert lo==0<hi
        elif n==12: assert lo<0 and hi==0
        elif n<5: assert lo>0 and hi>0
        else: assert lo<0 and hi<0
        checks+=1
    assert signs(6,1)[2]==F(2,9); checks+=1
    assert signs(11,1)[2]==F(11,12); checks+=1
    # An example of opposite signs within the same sample:
    assert formula(8,1,F(1,2))<0<formula(8,4,F(1,2)); checks+=1
    print('PASS EXACT ASSERTIONS',checks)
if __name__=='__main__': check()
