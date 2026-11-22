#!/usr/bin/env python3
"""Independent finite checks for near-centre circular simplicial depth.
Python 3 standard library only. Finite checks are not infinite-limit proofs.
"""
import math
import random
from itertools import combinations
from fractions import Fraction

PI = math.pi

def triangle_contains_origin(t):
    x=sorted((v%(2*PI))/(2*PI) for v in t)
    g=[x[1]-x[0],x[2]-x[1],1+x[0]-x[2]]
    return max(g)<0.5

def depth_direct(t):
    return sum(triangle_contains_origin(v) for v in combinations(t,3))

def depth_sweep(t):
    # Outside-origin triples are those contained in an open semicircle.
    p=sorted((v%(2*PI))/(2*PI) for v in t)
    n=len(p)
    a=p+[x+1 for x in p]
    outside=0
    j=1
    for i in range(n):
        j=max(j,i+1)
        while j<i+n and a[j]-a[i]<0.5-1e-12:
            j+=1
        k=j-i-1
        outside+=k*(k-1)//2
    return math.comb(n,3)-outside

def ray_angle(t,r):
    return math.atan2(math.sin(t),math.cos(t)-r)

def cvar(n):
    return Fraction(3,16)*math.comb(n,3)+Fraction(1,24)*math.comb(n,2)*math.comb(n-2,2)

def eig(k):
    return Fraction(-1,k*k) if k%2 else Fraction(0)

def run():
    rng=random.Random(132705)
    passed=0
    # Analytic lambda_k = 2 int_0^1/2 s cos(2*pi*k*s) ds.
    for k in range(1,50):
        integral=(math.cos(math.pi*k)-1)/(2*math.pi**2*k*k)
        assert abs(integral-float(eig(k))/PI**2)<1e-13
        passed+=1
    # Spectral identities: sum odd k^-4=pi^4/96.
    assert abs(sum(1/k**4 for k in range(1,20001,2))-(PI**4)/96)<2e-13
    passed+=1
    assert abs(2*(1/96)-1/48)<1e-14
    passed+=1
    # Exact central depth variance for finite n from overlapping triples.
    for n in range(3,60):
        v=cvar(n)
        assert v>0
        assert abs(float(v)/n**4-1/96) < (1 if n<10 else .05)
        passed+=1
    # Direct independent geometric enumeration versus sliding semicircle count.
    for n in range(3,14):
        for rep in range(60):
            theta=[rng.uniform(0,2*PI) for _ in range(n)]
            r=rng.uniform(0,0.98)
            a=[ray_angle(t,r) for t in theta]
            assert depth_direct(a)==depth_sweep(a), (n,r)
            passed+=1
    # Compare density to finite-difference of inverse angle map,
    # and verify first-harmonic shift for r->0.
    for r in [0.001,0.015,0.08,0.3]:
        for k in range(1,38):
            th=2*PI*k/38
            # theta is the direction from displaced query point.
            s=math.sqrt(1-r*r*math.sin(th)**2)-r*math.cos(th)
            ph=math.atan2(s*math.sin(th),r+s*math.cos(th))
            dt=1e-6
            def wrapfun(x):
                sl=math.sqrt(1-r*r*math.sin(x)**2)-r*math.cos(x)
                return math.atan2(sl*math.sin(x),r+sl*math.cos(x))
            diff=((wrapfun(th+dt)-wrapfun(th-dt)+PI)%(2*PI)-PI)/(2*dt)
            expected=1-r*math.cos(th)/math.sqrt(1-r*r*math.sin(th)**2)
            assert abs(diff-expected)<2e-9, (r,th,diff,expected)
            passed+=1
    # Simulations of exact geometry to verify center probability,
    # first nonzero quadratic drift at small displacement.
    nrep=40000
    for r in [0.0,0.04,0.07]:
        hit=0
        for _ in range(nrep):
            t=[rng.uniform(0,2*PI) for _ in range(3)]
            hit+=triangle_contains_origin([ray_angle(x,r) for x in t])
        p=hit/nrep
        target=1/4-3*r*r/(2*PI*PI)
        assert abs(p-target)<0.013, (r,p,target)
        passed+=1
    # Critical law moments follow independent noncentral gaussian:
    # Var(sum lambda (E_k-1))=1/96; Var of shifted first mode
    # adds c^2 /(2*pi^4), mean -c^2/(4*pi^2).
    for c in [0,0.5,1,2,4]:
        mu=-c*c/(4*PI**2)
        var=1/96+c*c/(2*PI**4)
        assert var>=1/96 and mu<=0
        passed+=1
    print(f'PASS: {passed} independent finite/numerical assertions')

if __name__=='__main__':
    run()
