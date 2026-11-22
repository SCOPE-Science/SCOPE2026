#!/usr/bin/env python3
"""Numerical diagnostics for Euclidean proximal norm flows. No third-party packages."""
from math import sqrt, copysign
import random


def prox_one(x,t):
    return tuple(copysign(max(abs(a)-t,0.0),a) for a in x)


def prox_two(x,t):
    r=sqrt(sum(a*a for a in x))
    fac=max(0.0,1.0-t/r) if r else 0.0
    return tuple(a*fac for a in x)


def prox_infty(x,t):
    mag=[abs(a) for a in x]; mass=sum(mag)
    if t>=mass:return tuple(0.0 for a in x)
    lo=0.0; hi=max(mag)
    for _ in range(70):
        mid=(hi+lo)/2
        if sum(max(a-mid,0.) for a in mag)>t:lo=mid
        else:hi=mid
    lam=(lo+hi)/2
    return tuple(copysign(min(abs(a),lam),a) for a in x)


def grad_pos(x,p):
    S=sum(a**p for a in x)
    return tuple(a**(p-1)*S**(1/p-1) for a in x)


def prox_small_pos(x,t,p):
    z=tuple(x)
    for _ in range(10000):
        gz=grad_pos(z,p)
        q=tuple(a-t*b for a,b in zip(x,gz))
        if min(q)<=0:raise AssertionError('unexpected active boundary')
        if max(abs(a-b) for a,b in zip(q,z))<2e-15:
            return q
        z=q
    raise AssertionError('no convergence')


def coefficient(n,p):
    S=(n-1)+2.**p
    return -(p-1)*S**(2/p-3)*(2**p-2**(2*p-2))


def run():
    rng=random.Random(20261115)
    num=0
    for n in range(2,19):
        for _ in range(120):
            x=tuple(rng.uniform(-4,4) for _ in range(n))
            for fun in [prox_one,prox_two,prox_infty]:
                s=rng.random()*15; t=rng.random()*15
                z=fun(fun(x,t),s); v=fun(x,t+s)
                assert max(abs(a-b) for a,b in zip(z,v))<5e-12,(n,fun.__name__,x,s,t,z,v)
                num+=1
    for n in [2,3,5,9,15]:
        x=(1.0,2.0)+(1.0,)*(n-2)
        for p in [1.25,1.5,1.9,3.0,4.0,6.0]:
            exact=coefficient(n,p)
            assert abs(exact)>1e-15
            prior=None
            for h in [0.002,0.001,0.0005,0.00025]:
                z=prox_small_pos(prox_small_pos(x,h,p),h,p)
                v=prox_small_pos(x,2*h,p)
                actual=(z[0]-v[0])/(h*h)
                assert exact*actual>0,(n,p,h,exact,actual)
                if h==0.00025:
                    assert abs(actual/exact-1.)<0.01,(n,p,h,exact,actual)
                assert max(abs(xi-zi-h*gi) for xi,zi,gi in zip(x,prox_small_pos(x,h,p),grad_pos(prox_small_pos(x,h,p),p)))<1e-12
                num+=2
    print(f'PASS {num} checks, including all three positive semigroup cases and nonzero signed second-order defects')

if __name__=='__main__':run()
