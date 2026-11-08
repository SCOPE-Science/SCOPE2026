#!/usr/bin/env python3
"""Exact finite-deck and renewal moment checks for independent cut-and-reverse packets."""
from fractions import Fraction as Q
from itertools import product

def summarize(n, rates):
    assert len(rates)==n-1
    M=EF=EI=EFF=EII=EFI=Q(0)
    for cuts in product((0,1), repeat=n-1):
        mass=Q(1)
        for b,p in zip(cuts,rates): mass*=p if b else 1-p
        lengths=[]; last=0
        for j,b in enumerate(cuts,1):
            if b: lengths.append(j-last);last=j
        lengths.append(n-last)
        fixed=sum(ell&1 for ell in lengths)
        inv=sum(ell*(ell-1)//2 for ell in lengths)
        M+=mass;EF+=mass*fixed;EI+=mass*inv
        EFF+=mass*fixed*fixed;EII+=mass*inv*inv;EFI+=mass*fixed*inv
    assert M==1
    return EF,EI,EFF-EF*EF,EII-EI*EI,EFI-EF*EI

def exact_limit(p):
    q=1-p
    T=1/p
    T2=(1+q)/p**2
    T3=(1+4*q+q*q)/p**3
    T4=(1+11*q+11*q*q+q**3)/p**4
    R=1/(1+q)
    TR=(1+q*q)/(p*(1+q)**2)
    T2R=(1+6*q*q+q**4)/(p*p*(1+q)**3)
    U=q/p**2
    TU=(T3-T2)/2
    U2=(T4-2*T3+T2)/4
    u=R/T;v=U/T
    A=(R-2*u*TR+u*u*T2)/T
    B=(U2-2*v*TU+v*v*T2)/T
    C=((T2R-TR)/2-u*TU-v*TR+u*v*T2)/T
    assert u==p/(2-p)
    assert v==q/p
    assert A==4*p*q/(2-p)**3
    assert B==q*(2-p)/p**3
    assert C==-2*q*(1+q*q)/(p*(2-p)**3)
    assert C*C < A*B
    assert C*C/(A*B)==(1+q*q)**2/(1+q)**4
    return A,B,C

checks=0
for n in range(2,11):
    for p in [Q(1,4),Q(1,2),Q(3,4)]:
        f,i,vf,vi,c=summarize(n,[p]*(n-1));checks+=1
        assert c<0 and vf>0 and vi>0
        assert i==n*(1-p)/p-(1-p)*(1-(1-p)**n)/p**2
        assert f.numerator>=0 and f<=n
    if n<=8:
        rates=[Q(j+1,n+3) for j in range(1,n)]
        f,i,vf,vi,c=summarize(n,rates);checks+=1
        assert c<0
for p in [Q(1,50),Q(1,10),Q(1,4),Q(1,3),Q(1,2),Q(2,3),Q(3,4),Q(9,10),Q(49,50)]:
    exact_limit(p);checks+=1
print('PASS',checks,'independent exact-deck and rational moment sets')
