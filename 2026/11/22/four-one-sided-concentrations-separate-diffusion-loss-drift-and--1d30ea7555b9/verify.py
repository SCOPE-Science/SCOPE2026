#!/usr/bin/env python3
"""Numerical and exact-rational spot checks for the stated transport inversion.

The analytical proof, not these finite tests, establishes the theorem.
"""
import math
import random
from fractions import Fraction as F


def concentration(D, lam, w, Q, u, x):
    v = w + u
    s = math.sqrt(v*v + 4*D*lam)
    if x >= 0:
        k = (s-v)/(2*D)
        return Q/s * math.exp(-k*x)
    r = (s+v)/(2*D)
    return Q/s * math.exp(r*x)


def reconstruct(u1,u2,xa,xb,c1a,c1b,c2a,c2b):
    assert u1 > u2 and 0 < xa < xb
    assert min(c1a,c1b,c2a,c2b)>0
    k1=math.log(c1a/c1b)/(xb-xa)
    k2=math.log(c2a/c2b)/(xb-xa)
    A1=c1a*math.exp(k1*xa)
    A2=c2a*math.exp(k2*xa)
    R=A1/A2
    assert 0<k1<k2 and k1/k2 < R < k2/k1
    de=k2-k1
    V=u1-u2
    z=(R*k2-k1)/(1+R)
    D=V*z/(de*de)
    lam=k1*k2*(V/de-D)
    w=(u1*k1-u2*k2)/de-D*(k1+k2)
    Q=A1*(V*k2/de-D*de)
    assert D>0 and lam>0 and Q>0
    return D,lam,w,Q,k1,k2,A1,A2


def check_ratios():
    k1,k2,A1,A2,u1,u2=F(1),F(2),F(2),F(14,5),F(1),F(-1)
    V=u1-u2
    de=k2-k1
    R=A1/A2
    z=(R*k2-k1)/(1+R)
    D=V*z/de**2
    lam=k1*k2*(V/de-D)
    w=(u1*k1-u2*k2)/de-D*(k1+k2)
    Q=A1*(V*k2/de-D*de)
    assert (D,lam,w,Q)==(F(1,2),F(3),F(3,2),F(7))
    s1=V*k2/de-D*de
    s2=V*k1/de+D*de
    assert (s1,s2)==(F(7,2),F(5,2))
    assert A1==Q/s1 and A2==Q/s2
    assert k1/k2<R<k2/k1
    return 9


def close(x,y,tol=2e-10):
    return abs(x-y)<=tol*max(1.0,abs(x),abs(y))


def main():
    count=check_ratios()
    rng=random.Random(240312)
    u1,u2=1.,-1.
    xa,xb=.3,1.2
    for _ in range(12000):
        D=rng.uniform(.25,2.)
        lam=rng.uniform(.2,4.)
        w=rng.uniform(-2.,2.)
        Q=rng.uniform(.5,5.)
        samples=[concentration(D,lam,w,Q,u,x) for u in (u1,u2) for x in (xa,xb)]
        rec=reconstruct(u1,u2,xa,xb,*samples)
        for a,b in zip(rec[:4],(D,lam,w,Q)):
            assert close(a,b), (a,b,rec)
            count+=1
        for u in (u1,u2):
            v=w+u
            s=math.sqrt(v*v+4*D*lam)
            k=(s-v)/(2*D)
            r=(s+v)/(2*D)
            assert close(D*k*k+v*k-lam,0)
            assert close(D*r*r-v*r-lam,0)
            assert close(D*(k+r)*Q/s,Q)
            count+=3
    # Three observations can remain identical for distinct parameter quadruples.
    D,lam,w,Q=.5,3.,1.5,7.
    c1a=concentration(D,lam,w,Q,u1,xa)
    c1b=concentration(D,lam,w,Q,u1,xb)
    c2a=concentration(D,lam,w,Q,u2,xa)
    k2_new=2.01
    A2_new=c2a*math.exp(k2_new*xa)
    A1=2.0;k1=1.0
    ratio=A1/A2_new
    assert k1/k2_new < ratio < k2_new/k1
    c2b_new=A2_new*math.exp(-k2_new*xb)
    D2,lam2,w2,Q2,*_=reconstruct(u1,u2,xa,xb,c1a,c1b,c2a,c2b_new)
    assert abs(D2-D)>1e-3
    for u,x,observed in ((u1,xa,c1a),(u1,xb,c1b),(u2,xa,c2a)):
        assert close(concentration(D2,lam2,w2,Q2,u,x),observed)
        count+=1
    print(f'PASS: {count} assertions: exact-rational witness, 12,000 seeded forward/inverse cases, PDE and jump identities, and an explicit three-reading ambiguity.')

if __name__=='__main__':main()
