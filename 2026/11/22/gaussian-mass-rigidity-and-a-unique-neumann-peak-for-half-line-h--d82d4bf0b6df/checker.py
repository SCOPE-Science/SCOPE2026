#!/usr/bin/env python3
"""Reproducible numerical checks for half-line heat commutator identities.

All analytic identities and monotonicity assertions have independent proofs
in the accompanying result; this script checks their normalizations.
"""
import math
import random
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import erf, erfc, erfinv

PI = math.pi
W = math.sqrt(PI / 2)

def A(c):
    return W * erf(c / math.sqrt(2))

def Q(c):
    return W * erfc(c / math.sqrt(2))

def F(c, sign):
    base = 1 - math.exp(-2*c*c) + 2*c*Q(2*c)
    return (base + sign*2*A(c)*Q(c))/(2*PI)

def Fprime(c, sign):
    return (Q(2*c)+sign*math.exp(-c*c/2)*(Q(c)-A(c)))/PI

def direct_integral(intervals, sign, t):
    # Symmetric Hilbert-Schmidt norm squared = 2 times cross-cut energy.
    boundaries = [0.0]
    for l,r in intervals:
        boundaries += [l,r]
    boundaries.append(math.inf)
    outside = []
    start=0.0
    for l,r in intervals:
        if l>start:
            outside.append((start,l))
        start=r
    outside.append((start, math.inf))
    def kernel(x,y):
        return (math.exp(-(x-y)**2/(4*t)) + sign*math.exp(-(x+y)**2/(4*t))) / math.sqrt(4*PI*t)
    total=0.
    for l,r in intervals:
        for a,b in outside:
            def inner(x):
                return quad(lambda y: kernel(x,y)**2, a,b,epsabs=2e-11,epsrel=2e-11)[0]
            total += quad(inner,l,r,epsabs=2e-11,epsrel=2e-11)[0]
    return 2*total

def predicted_gap(intervals,t):
    mass=sum(math.sqrt(PI*t/2)*(erf(r/math.sqrt(2*t))-erf(l/math.sqrt(2*t))) for l,r in intervals)
    w=math.sqrt(PI*t/2)
    return (2/(PI*t))*mass*(w-mass)

def main():
    tests=0
    for t in (0.25, 0.9, 2.3):
        for c in (0.2, 0.7, 1.4, 3.0):
            ints=[(0.0,c*math.sqrt(t))]
            n=direct_integral(ints,+1,t)
            d=direct_integral(ints,-1,t)
            assert abs(n-F(c,+1)) < 1e-9, (t,c,n,F(c,+1))
            assert abs(d-F(c,-1)) < 1e-9, (t,c,d,F(c,-1))
            assert abs(n-d-erf(c/math.sqrt(2))*erfc(c/math.sqrt(2))) < 1e-9
            tests+=3
    for t in (0.6,1.8):
        for intervals in ([(0.2,1.0)],[(0.,0.2),(0.8,1.4)],[(0.1,0.3),(0.5,0.8),(1.2,1.5)]):
            n=direct_integral(intervals,+1,t)
            d=direct_integral(intervals,-1,t)
            assert abs(n-d-predicted_gap(intervals,t))<1e-9
            tests+=1
    cm=math.sqrt(2)*erfinv(0.5)
    assert abs(F(cm,+1)-F(cm,-1)-0.25)<2e-14
    tests+=1
    peak=brentq(lambda x:Fprime(x,+1),0.6,1.5,xtol=1e-14)
    assert abs(peak-0.7990017881788918)<1e-12
    assert abs(F(peak,+1)-0.2719729564300915)<1e-12
    tests+=2
    grid=[0.002*i for i in range(1,5001)]
    for c in grid:
        assert Fprime(c,-1)>0
        assert (Fprime(c,+1)>0)==(c<peak)
        tests+=2
    for c in (0.001,0.003,0.005,0.01):
        assert abs(F(c,+1)/c-math.sqrt(2/PI))<0.03
        assert abs(F(c,-1)/c**3-1/(6*math.sqrt(2*PI)))<0.001
        tests+=2
    print(f"PASS: {tests} normalization, direct-kernel, mask, and sign checks")
    print(f"Neumann peak c={peak:.15f}, HS-square={F(peak,+1):.15f}")
    print(f"Gaussian-half-mass interval c={cm:.15f}")

if __name__=='__main__':
    main()
