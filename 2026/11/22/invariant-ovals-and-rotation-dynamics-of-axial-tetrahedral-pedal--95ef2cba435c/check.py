#!/usr/bin/env python3
"""Exact-rational cross-checks for a fixed-center tetrahedral face-pedal map.

Finite checks complement, but do not replace, the written algebraic proof.
Requires only Python's standard library.
"""
from fractions import Fraction as F
from random import Random


def step(p, q):
    s = p + q
    h = s*s + F(1,4)
    return F(1,2)/s, 2*p*h/(q*s)


def T(u,v):
    return v,(u+2*v)/(2*u*v-1)


def I(u,v):
    return (2*u*v-1)/((1+u*u)*(1+v*v))


def dot(x,y):
    return sum(a*b for a,b in zip(x,y))


def sub(x,y):
    return tuple(a-b for a,b in zip(x,y))


def cross(x,y):
    return (x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0])


def foot(triple):
    a,b,c=triple
    n=cross(sub(b,a),sub(c,a))
    t=dot(n,a)/dot(n,n)
    return tuple(t*x for x in n)


def test():
    rng=Random(20261118)
    count=0
    for _ in range(512):
        p=F(rng.randint(1,35),rng.randint(1,20))
        q=F(rng.randint(1,35),rng.randint(1,20))
        u,v=F(1,2)/p,p+q
        pn,qn=step(p,q)
        uu,vv=T(u,v)
        assert (uu,vv)==(F(1,2)/pn,pn+qn)
        assert I(uu,vv)==I(u,v)
        assert F(1,3)-I(u,v)==((u*v-2)**2+(u-v)**2)/(3*(1+u*u)*(1+v*v))
        w=vv
        J=(1+4*v*v)/(2*u*v-1)**2
        assert J==(1+w*w)/(1+u*u)
        assert J/((1+v*v)*(1+w*w))==1/((1+u*u)*(1+v*v))
        assert 0<I(u,v)<=F(1,3)
        count+=6
    for _ in range(128):
        # The axis is (1,1,1); the base lies on the negative side of 0.
        a=F(rng.randint(1,30))
        b=-F(rng.randint(25,70))
        c=F(rng.randint(1,30))
        assert a+2*b<0 and a-b>0
        v0=(a,b,b);v1=(b,a,b);v2=(b,b,a);ap=(c,c,c)
        lateral=[foot((ap,v0,v1)),foot((ap,v1,v2)),foot((ap,v2,v0))]
        basefoot=foot((v0,v1,v2))
        h=lateral[0]
        assert all(sum(x)==sum(h) for x in lateral)
        # Source's exact 3-fold symmetric facet-projection formula.
        diff=3*c-a-2*b
        D=(diff*diff + (a-b)**2/F(2,1))/3
        r2=F(2,3)*(a-b)**2
        assert sum(h)==(a-b)**2*c/(2*D)
        assert sum(basefoot)==a+2*b
        newr2=dot(h,h)-sum(h)**2/3
        assert newr2==r2*c*c*diff*diff/(4*D*D)
        pn2=sum(h)**2/(3*newr2)
        assert pn2==(a-b)**2/(2*diff*diff)
        qn2=sum(basefoot)**2/(3*newr2)
        assert qn2==(a+2*b)**2/(3*newr2)
        count+=5
    print('PASS:',count,'exact Fraction identities/cross-checks')

if __name__=='__main__':
    test()
