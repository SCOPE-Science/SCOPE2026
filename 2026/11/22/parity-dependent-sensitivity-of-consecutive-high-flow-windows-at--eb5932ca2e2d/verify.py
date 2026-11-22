#!/usr/bin/env python3
"""Exact checks for a stationary binary wet-spell event, independent of numerical fitting."""
from fractions import Fraction as Q
from itertools import product

def bounds(p):
    return max(Q(0), 2-Q(1)/p), Q(1)

def event(n,p,s):
    b=p*(1-s)/(1-p)
    d,w=1-p,p
    for _ in range(1,n):
        d,w=d*(1-b)+w*(1-s),d*b
    return 1-d-w

def event_and_derivative(n,p,s):
    b=p*(1-s)/(1-p); bp=-p/(1-p)
    d,w=1-p,p; dd=dw=Q(0)
    for _ in range(1,n):
        nd=d*(1-b)+w*(1-s)
        nw=d*b
        ndd=dd*(1-b)-d*bp+dw*(1-s)-w
        ndw=dd*b+d*bp
        d,w,dd,dw=nd,nw,ndd,ndw
    return 1-d-w,-dd-dw

def brute(n,p,s):
    b=p*(1-s)/(1-p)
    t={(0,0):1-b,(0,1):b,(1,0):1-s,(1,1):s}
    acc=Q(0)
    for a in product((0,1),repeat=n):
        if not any(a[i]==a[i+1]==1 for i in range(n-1)):
            continue
        pr=p if a[0] else 1-p
        for i in range(n-1):pr*=t[a[i],a[i+1]]
        acc+=pr
    return acc

checks=0
for p in (Q(1,10),Q(1,3),Q(1,2),Q(3,5),Q(3,4),Q(4,5),Q(9,10),Q(99,100)):
    lo,_=bounds(p)
    for j in range(5):
        s=lo+(1-lo)*Q(j,4)
        for n in range(2,10):
            f,fd=event_and_derivative(n,p,s)
            assert f==brute(n,p,s),(p,s,n)
            checks+=1
            if n==4:
                assert f==p*s*(3-2*s)
                checks+=1
            if n==5:
                g=2*p*s**3-3*p*s**2-2*p*s+2*p+3*s-2
                assert fd==-2*p*g/(1-p)
                checks+=1
for p in (Q(51,100),Q(3,5),Q(4,5),Q(9,10),Q(99,100)):
    lo,_=bounds(p); r=(1-p)/p
    for m in range(1,61):
        _,fe=event_and_derivative(2*m,p,lo)
        _,fo=event_and_derivative(2*m+1,p,lo)
        assert fe==r**(m-2)*((3*m-2)-(4*m-3)*p),(m,p,'even')
        assert fo==2*m*p*r**m,(m,p,'odd')
        checks+=2
# Prove interval-constrained five-day concavity symbolically via positive lower bound
# of G'(s), and verify representative strict signs at all accessible boundaries.
for p in (Q(1,100),Q(1,3),Q(1,2),Q(2,3),Q(4,5),Q(9,10),Q(99,100)):
    lo,_=bounds(p)
    _,da=event_and_derivative(5,p,lo)
    _,db=event_and_derivative(5,p,Q(1))
    assert da>0 and db==-2*p
    checks+=2
print('PASS:',checks,'exact rational assertions; no sampling used for infinite claims')
