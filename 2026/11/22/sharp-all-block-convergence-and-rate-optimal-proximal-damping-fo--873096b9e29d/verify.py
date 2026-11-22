#!/usr/bin/env python3
"""Exact finite checks for the homogeneous parallel proximal-Jacobi quadratic benchmark."""
from fractions import Fraction as Q
from math import sqrt, isclose
import cmath

def core(m,s):
    D=s+2
    beta=(s+1)/D
    a=(s+1-m)/D
    M=((a,-Q(m)/D),(a,(s+2-m)/D))
    t=M[0][0]+M[1][1]
    q=M[0][0]*M[1][1]-M[0][1]*M[1][0]
    return D,beta,M,t,q

def rho(m,s):
    s=float(s)
    D=s+2
    b=(s+1)/D
    t=(2*s+3-2*m)/D
    q=(s+1-m)/D
    r=cmath.sqrt(t*t-4*q)
    return max(b,abs((t+r)/2),abs((t-r)/2))

cases=0
for m in list(range(2,26))+[40,75,100]:
    for s in [Q(0),Q(1,7),Q(1),Q(m-1),Q(m),Q(2*m+1,3)]:
        D,b,M,t,q=core(m,s)
        assert t==Q(2*s+3-2*m,D)
        assert q==Q(s+1-m,D)
        assert 1-q==Q(m+1,D)
        assert 1-t+q==Q(m,D)
        assert 1+t+q==Q(4*s+6-3*m,D)
        assert b*b-t*b+q==Q(m*s,D*D)
        assert b*b+t*b+q==Q(4*s*s+(10-3*m)*s+6-4*m,D*D)
        assert b*b-q==Q((m-1)*s+2*m-1,D*D)
        # Check independent simultaneous block updates and dual sum directly.
        x=[Q((i+1)*(i%3-1),i+2) for i in range(m)]
        lam=Q(5,11)
        S=sum(x)
        new=[((s+1)*z-S-lam)/D for z in x]
        for z0,z1 in zip(x,new):
            old_other=S-z0
            derivative=(1+s+1)*z1+lam+old_other-s*z0
            assert derivative==0
        Sp=sum(new)
        lp=lam+Sp
        assert Sp==M[0][0]*S+M[0][1]*lam
        assert lp==M[1][0]*S+M[1][1]*lam
        for i in range(m):
            assert new[i]-Sp/m==b*(x[i]-S/m)
        cases+=1
    optimal=(3*m-10+sqrt(9*m*m+4*m+4))/8
    left=(3*m-6)/4
    assert left < optimal < m-1
    rstar=(optimal+1)/(optimal+2)
    assert abs(rho(m,optimal)-rstar)<1.e-11
    assert abs(rho(m,left)-1)<1.e-10
    assert rho(m,left-0.05)>1 if left>0.05 else True
    assert rho(m,optimal*0.85)>rstar+1.e-8
    assert rho(m,optimal*1.15)>rstar+1.e-8
    assert rstar < m/(m+1)
# Independent numerical decay/growth in full matrix for a representative case.
m=5
for s,expected in [(0,'unstable'),(Q(2),'unstable'),(Q(9,4),'neutral'),(Q(4),'stable')]:
    spectral=rho(m,s)
    if expected=='unstable': assert spectral>1
    if expected=='neutral': assert abs(spectral-1)<1e-12
    if expected=='stable': assert spectral<1
for m in [1000,10000,100000]:
    opt=(3*m-10+sqrt(9*m*m+4*m+4))/8
    assert abs((m-opt)/m-.25) < .002
    assert abs(m*(1-rho(m,opt))-4/3) < .004
print(f'PASS: {cases} rational instances; exact characteristic/Schur/polynomial identities, mode decomposition, finite spectral and asymptotic tests')
