#!/usr/bin/env python3
"""Exact independent finite-checking script for the rooted-forest variance phase boundary."""
from fractions import Fraction as F
from math import acosh, cosh, exp, sqrt

checks=0

def measure(a,b,q):
    # Enumerate edge subsets and count admissible root positions in each tree.
    # No edges: 3 singleton roots; one edge: 2 root choices; two edges: 3.
    weights={1:3*a*b*q,2:2*(a+b)*q*q,3:q*q*q}
    total=sum(weights.values(),F(0))
    return {k:w/total for k,w in weights.items()}

def variance_direct(a,b,q):
    dist=measure(a,b,q)
    m=sum(k*p for k,p in dist.items())
    return sum((k-m)**2*p for k,p in dist.items())

def variance_from_log_partition(a,b,q):
    s=a+b; product=3*a*b
    d=q*q+2*s*q+product
    num=3*q*q+4*s*q+product
    return q*((6*q+4*s)*d-num*(2*q+2*s))/d**2

for a in range(1,24):
    for b in range(1,24):
        A,B=F(a),F(b)
        for k in range(1,31):
            Q=F(k,7)
            vd=variance_direct(A,B,Q)
            vf=variance_from_log_partition(A,B,Q)
            assert vd==vf,(a,b,k,vd,vf)
            assert vd==variance_direct(A,B,3*A*B/Q)
            checks+=2
# Critical-shape identity, independent numerical evaluation of the spectral formula.
for a,b in [(1,1),(2,3),(1,9),(1,10),(1,100),(33,2),(5,49)]:
    c=sqrt(3*a*b)
    v=(a+b)/c
    for t in [-5,-3,-1,-0.1,0,0.1,1,3,5]:
        u=cosh(t)
        q=c*exp(t)
        s=a+b
        delta=sqrt(a*a-a*b+b*b)
        lam1=s-delta;lam2=s+delta
        direct=q*lam1/(q+lam1)**2+q*lam2/(q+lam2)**2
        elegant=(1+v*u)/(v+u)**2
        assert abs(direct-elegant)<2e-13,(a,b,t,direct,elegant)
        checks+=1
    if v>2:
        peak_u=v-2/v
        peak_t=acosh(peak_u)
        peak=(1+v*peak_u)/(v+peak_u)**2
        assert abs(peak-v*v/(4*(v*v-1)))<1e-13
        assert peak>1/(1+v)
        assert peak> (1+v*cosh(peak_t+0.2))/(v+cosh(peak_t+0.2))**2
        checks+=3
    else:
        assert 1/(v+1)>(1+v*cosh(0.2))/(v+cosh(0.2))**2
        checks+=1
print('VERIFY_OK',checks,'exact rational and independent numerical checks')
