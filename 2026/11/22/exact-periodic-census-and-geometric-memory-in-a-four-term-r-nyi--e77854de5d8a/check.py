#!/usr/bin/env python3
"""Exact rational checks for a multiple-fractional-part dynamical system.

This checks the explicitly stated finite identities and sample periodic lifts.
The all-period assertions are established in the mathematical proof, not by enumeration.
"""
from fractions import Fraction as Q
from math import gcd

SLOPES=(1,10,100,1000)
A=sum(SLOPES)

def frac(t):
    return t-t.numerator//t.denominator

def H(t,slopes=SLOPES):
    return sum((frac(a*t) for a in slopes),Q(0))

def G(t,slopes=SLOPES):
    return frac(sum(slopes)*t)

def F(x,slopes=SLOPES):
    return H(x,slopes)

def paired_cov(a,b):
    return Q(gcd(a,b)**2,12*a*b)

# Independent integration via exact affine pieces [j/1000,(j+1)/1000).
# H(t)=A*t-C on each such piece, so integration is polynomial and exact.
m1=m2=Q(0)
for j in range(1000):
    lo,hi=Q(j,1000),Q(j+1,1000)
    C=sum(a*j//1000 for a in SLOPES)
    m1+=A*(hi**2-lo**2)/2-C*(hi-lo)
    m2+=A*A*(hi**3-lo**3)/3-A*C*(hi**2-lo**2)+C*C*(hi-lo)
assert m1==2,(m1,'mean')
var=m2-m1*m1
assert var==Q(2321,6000),(var,'variance')
assert sum((paired_cov(a,b) for a in SLOPES for b in SLOPES),Q(0))==var

# Independent checks of a Fourier-gcd covariance identity by exact piecewise integration.
def exact_pair_cov(a,b):
    from math import lcm
    den=lcm(a,b)
    out=Q(0)
    for j in range(den):
        l,r=Q(j,den),Q(j+1,den)
        A0=(a*l).numerator//(a*l).denominator
        B0=(b*l).numerator//(b*l).denominator
        # integral (a*t-A0-1/2)*(b*t-B0-1/2) dt
        u,v=-Q(A0)-Q(1,2),-Q(B0)-Q(1,2)
        out+=Q(a*b,3)*(r**3-l**3)+Q(a*v+b*u,2)*(r**2-l**2)+u*v*(r-l)
    return out
for a,b in [(1,10),(10,100),(1,1000),(3,7),(2,6),(5,12)]:
    assert exact_pair_cov(a,b)==paired_cov(a,b),(a,b)
for h in range(7):
    assert sum((paired_cov(a,b*A**h) for a in SLOPES for b in SLOPES),Q(0))==var/Q(A**h)

# Periodic lifting and semiconjugacy, including all base period-1 points.
checks=0
for small in [(1,2,4),(1,3,4),(1,10,100,1000)]:
    N=sum(small)
    for n in ([1,2,3] if N<10 else [1]):
        den=N**n-1
        pts=set()
        for k in range(den):
            t=Q(k,den)
            assert frac(H(t,small))==G(t,small)
            x=H(frac(N**(n-1)*t),small)
            assert frac(x)==t
            y=x
            for _ in range(n):y=F(y,small)
            assert y==x
            pts.add(x)
            checks+=1
        assert len(pts)==den,(small,n,len(pts),den)

# Period-2 examples for published coefficients without enumerating 1.2M points.
for k in (0,1,2,3,10,1110,12000,1234320):
    den=A*A-1
    k%=den
    t=Q(k,den)
    x=H(frac(A*t))
    assert F(F(x))==x and frac(x)==t
    checks+=1
print('PASS: 1000 rational integration cells; 6 exact covariance integrations; 7 all-lag arithmetic identities; %d rational periodic lifts'%checks)
print('A=%d; mean=%s; variance=%s; lag-1 covariance=%s'%(A,m1,var,var/A))
