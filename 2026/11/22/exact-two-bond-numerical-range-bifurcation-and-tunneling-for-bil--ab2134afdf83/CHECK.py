#!/usr/bin/env python3
"""Exact-polynomial and floating finite-difference checks for two bond weights.
Run: python3 CHECK.py. Standard library only. No infinite theorem is inferred from checks.
"""
from fractions import Fraction as F
from math import sqrt

checks=0

def ok(x):
    global checks
    assert x
    checks+=1

def h(r,d):
    return r*r*sum(r**j for j in range(d))/(1+r)

def roots(c,d):
    a=c*c-1
    lo,hi=0.,1.
    for _ in range(90):
        m=(lo+hi)/2
        if 1-c*c*m*m-a*m**(d+2)>0:lo=m
        else:hi=m
    rp=(lo+hi)/2
    rm=None
    if d*a>2:
        lo,hi=0.,1.
        for _ in range(90):
            m=(lo+hi)/2
            if a*h(m,d)<1:lo=m
            else:hi=m
        rm=(lo+hi)/2
    return rp,rm

def edge_eval(c,d,r,sgn):
    a=c*c-1
    return 1-c*c*r*r+sgn*a*r**(d+2)

def mode(c,d,r):
    a=c*c-1
    # u[0]=1, u[-j]=r^j, u[1..d+1] from exact two-tail matching
    denom=c*r*(1-r*r)
    u={n:r**(-n) for n in range(-18,1)}
    for n in range(1,d+2):
        u[n]=(a*r*r*r**(n-1)+(1-c*c*r*r)*r**(-(n-1)))/denom
    u[d+2]=c*r*u[d+1]
    for n in range(d+3,d+22):u[n]=u[d+2]*r**(n-d-2)
    return u

# Exact rational matching polynomial identity.
for d in range(1,10):
    for cc in [F(5,4), F(3,2), F(2), F(5,2)]:
        for rr in [F(1,3),F(2,5),F(3,4)]:
            a=cc*cc-1;r=rr
            P=a*r*r;Q=1-cc*cc*r*r
            ud=P*r**(d-1)+Q*r**(-(d-1))
            ud1=P*r**d+Q*r**(-d)
            match=ud-(r+1/r-cc*cc*r)*ud1
            identity=a*a*r**(2*d+4)-Q*Q
            ok(match*r**(d+1)==identity)
            ok(identity==-edge_eval(cc,d,r,+1)*edge_eval(cc,d,r,-1))

for c in (1.1,1.3,1.5,2.,3.):
    prev_plus=None;prev_minus=None
    for d in range(1,12):
        rp,rm=roots(c,d)
        ok(0<rp<1/c)
        ok(abs(edge_eval(c,d,rp,-1))<1e-11)
        ok((rm is not None)==(d*(c*c-1)>2))
        lam=lambda r:(r+1/r)/2
        if prev_plus is not None:ok(lam(rp)<prev_plus+1e-12)
        prev_plus=lam(rp)
        if rm is not None:
            ok(1/c<rm<1)
            ok(abs(edge_eval(c,d,rm,+1))<5e-10)
            if prev_minus is not None:ok(lam(rm)>prev_minus-1e-12)
            prev_minus=lam(rm)
        for r in (rp,rm):
            if r is None:continue
            u=mode(c,d,r)
            ll=lam(r)
            for n in range(-15,d+19):
                left=c if n-1 in (0,d+1) else 1
                right=c if n in (0,d+1) else 1
                err=ll*u[n]-(left*u[n-1]+right*u[n+1])/2
                ok(abs(err)<4e-7*max(1,abs(u[n])))

print('DOUBLE_BOND_TRANSFER_CHECK_OK',checks)
