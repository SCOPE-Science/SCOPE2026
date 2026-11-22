#!/usr/bin/env python3
"""Deterministic numerical consistency checks for the spectral-band envelope.
These checks supplement, but do not replace, the Hilbert-space proof.
"""
import math
import random

def profile(r,t):
    return math.sqrt(r*r+(1-r*r)*t)+(1-r)*math.sqrt(t*(1-t))

def critical_t(r):
    if not 0<=r<1: raise ValueError('r must lie in [0,1)')
    lo,hi=.5,1.
    for _ in range(100):
        t=(lo+hi)*.5
        lhs=(1+r)*math.sqrt(t*(1-t))
        rhs=(2*t-1)*math.sqrt(r*r+(1-r*r)*t)
        if lhs>rhs: lo=t
        else: hi=t
    return (lo+hi)*.5

def constant(r):
    return 1. if r==1 else profile(r,critical_t(r))

def numerical_radius_2x2_rankone(a,b):
    # rank-one column a and source b, both two-coordinate real vectors
    dot=a[0]*b[0]+a[1]*b[1]
    return (math.hypot(*a)*math.hypot(*b)+abs(dot))/2

def main():
    assert abs(critical_t(0)-.75)<1e-12
    assert abs(constant(0)-3*math.sqrt(3)/4)<1e-12
    assert constant(1)==1
    rng=random.Random(713)
    tests=0
    for r in (0.,.03,.1,.25,.5,.75,.9,.99,1.):
        c=constant(r)
        if r<1:
            t=critical_t(r)
            assert .5<t<1
            assert all(c+1e-12>=profile(r,j/400) for j in range(401))
            # A=diag(r,1), u=(sqrt(1-t),sqrt(t)), v a perpendicular unit
            u=(math.sqrt(1-t),math.sqrt(t))
            au=(r*u[0],u[1]); s=r*u[0]**2+u[1]**2
            z=(au[0]-s*u[0],au[1]-s*u[1]); q=math.hypot(*z)
            v=(z[0]/q,z[1]/q)
            # B=uv^T, w(B)=1/2, w(AB)/w(B)=c
            assert abs(2*numerical_radius_2x2_rankone(au,v)-c)<2e-12
        for _ in range(1000):
            t=rng.random()
            theta=rng.random()*2*math.pi
            # sampling an arbitrary positive 2x2 diagonal with spectrum within [r,1]
            a=r+(1-r)*rng.random();b=r+(1-r)*rng.random()
            u=(math.cos(theta),math.sin(theta))
            au=(a*u[0],b*u[1]);s=a*u[0]**2+b*u[1]**2
            z=(au[0]-s*u[0],au[1]-s*u[1]);q=math.hypot(*z)
            ratio=math.hypot(*au)+q
            assert ratio<=c+1e-12,(r,a,b,ratio,c)
            tests+=1
    print('PASS',tests,'spectral-band samples; endpoint constants')
    for r in (0,.1,.5,.9,.99,1): print(r,constant(r))
if __name__=='__main__':main()
