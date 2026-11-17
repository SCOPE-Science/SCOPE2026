#!/usr/bin/env python3
"""Finite independent arithmetic sanity checks, not an asymptotic certificate."""
from fractions import Fraction as Q
from math import sqrt, log

def add(p,q):
    r=[Q(0)]*max(len(p),len(q))
    for k,x in enumerate(p): r[k]+=x
    for k,x in enumerate(q): r[k]+=x
    return r

def mul(p,q):
    r=[Q(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): r[i+j]+=a*b
    return r

def scale(p,c): return [v*c for v in p]
def sub(p,q): return add(p,scale(q,-1))

def run():
    tests=0
    x=[Q(0),Q(1)]; one=[Q(1)]
    theta=mul(x,sub(one,x))
    for eps in [Q(1,n) for n in range(3,27)]:
        rho=Q(1)+2*eps-eps**3
        q=mul(sub(x,[eps*eps]),sub(x,[Q(1,2)]))
        a=scale(add(mul(x,x),scale(theta,eps)),rho)
        b=scale(theta,rho)
        c=add(scale(mul(sub(one,x),sub(one,x)),eps),scale(theta,1-eps*eps))
        lhs=sub(mul(a,c),mul(b,b)); rhs=scale(mul(theta,q),2*rho)
        assert add(lhs,scale(rhs,-1))==[Q(0)]*max(len(lhs),len(rhs)); tests+=1
        assert a[0]==0 and b[0]==0 and c[0]==eps; tests+=3
        assert a[1]==rho*eps and b[1]==rho; tests+=2
        assert q[0]==eps*eps/2; tests+=1
        assert rho>=1 and rho<=2; tests+=2
    r0=3+2*sqrt(2)
    assert abs(1/log(r0)-0.567296328553256)<1e-12; tests+=1
    # Distance of the origin from two fixed carrier intervals tends to the sharp constant.
    for n in [100,1000,10000]:
        de=1/n; aa=0.5+de; bb=1-de
        tt=-(aa+bb)/(bb-aa)
        modulus=abs(tt-sqrt(tt*tt-1))
        assert modulus>r0 and modulus<r0+40*de; tests+=2
    print(f'CHECK_OK: {tests} finite exact-arithmetic and geometric assertions')

if __name__=='__main__': run()
