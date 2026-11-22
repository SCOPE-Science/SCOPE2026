#!/usr/bin/env python3
"""Supplementary finite algebra and numerical sanity tests for a Gaussian-quartic theorem.

This is NOT an exhaustive mathematical proof; the analytic proof is in RESULT.md.
Requires only Python 3 standard library.
"""
from fractions import Fraction as F
from itertools import product
import math
import random

checks = 0

def check(cond, message='failed'):
    global checks
    assert cond, message
    checks += 1

def lap(p):
    out={}
    for alpha,c in p.items():
        for j,n in enumerate(alpha):
            if n>=2:
                b=list(alpha); b[j]-=2; b=tuple(b)
                out[b]=out.get(b,F(0))+c*n*(n-1)
    return {k:v for k,v in out.items() if v}

def scaled(p,scalar):return {a:c*scalar for a,c in p.items() if c*scalar}

def add(*ps):
    o={}
    for p in ps:
        for a,c in p.items():o[a]=o.get(a,F(0))+c
    return {a:c for a,c in o.items() if c}

def evalp(p,x):return sum(float(c)*math.prod(t**k for t,k in zip(x,a)) for a,c in p.items())

def radial4(d):
    p={}
    for i in range(d):
        a=[0]*d;a[i]=4;p[tuple(a)]=F(1)
        for j in range(i+1,d):
            a=[0]*d;a[i]=a[j]=2;p[tuple(a)]=F(2)
    return p

def linear4(d,vec):
    from math import factorial
    p={}
    for a in product(range(5),repeat=d):
        if sum(a)==4:
            coef=F(factorial(4),math.prod(factorial(k) for k in a))*math.prod(v**k for v,k in zip(vec,a))
            if coef:p[a]=coef
    return p

# Exact Hermite-transform coefficient identities in every tested dimension.
# Fourier transform of homogeneous quartic P4 times e^-pi r²:
# P4 - (Delta P4)/(4 pi) + (Delta²P4)/(32 pi²).
# Fourier transform of degree-2 Q2 times e^-pi r²:
# -Q2 + (Delta Q2)/(4 pi).
for d in range(2,7):
    random.seed(d)
    for t in range(12):
        p=add(radial4(d),*(scaled(linear4(d,[random.randint(-2,2) for _ in range(d)]),F(random.randint(0,3),5)) for k in range(3)))
        dp=lap(p); ddp=lap(dp)
        q2=scaled(dp,F(-1,8))
        # Check Fourier fixed point, grading coefficients in powers of 1/pi.
        check(all(sum(a)==4 for a in p), 'homogeneous quartic coefficient')
        check(add(scaled(dp,F(-1,4)),scaled(q2,F(-1)))==q2,'quadratic Fourier coefficient')
        check(add(scaled(ddp,F(1,32)),scaled(lap(q2),F(1,4)))=={},'constant Fourier coefficient')
        for j in range(30):
            v=[random.uniform(-1,1) for _ in range(d)]
            # Laplacian of r^4 equals 4(d+2)r².
            check(abs(evalp(lap(radial4(d)),v)-4*(d+2)*sum(x*x for x in v))<1e-9,'radial Laplacian')

# d=2: the exact nonradial quartic A(theta)=1+e cos(4 theta).
# Q4=r^4 A and Delta Q4=16 r². The negative-set area is 2/sqrt(1-e²).
N=24000
for e in [0.,.05,.2,.5,.8,.95]:
    area=0.; mean_gradient=0.
    for j in range(N):
        theta=2*math.pi*(j+.5)/N
        c=math.cos(4*theta); s=math.sin(4*theta)
        A=1+e*c
        R2=2/(math.pi*A)
        area+=math.pi*R2/N
        mean_gradient+=(4*e*s/A)**2/N
    exact=2/math.sqrt(1-e*e)
    check(abs(area-exact)<3e-11,'nonradial exact volume')
    check(area>=(2-1e-10),'sharp volume')
    # The gradient-enhanced lower bound is an identity in dimension 2 for this family.
    check(abs(area-(2+mean_gradient/8))<4e-11,'gradient refinement')

# d=3: positive definite nonradial quartic and its geometric radial integration.
d=3
P=add(radial4(d),scaled(add(*[linear4(d,[int(i==j) for i in range(d)]) for j in range(d)]),F(1,3)))
DP=lap(P)
M=25000
area=0.; loggrad_energy=0.
phi=(1+5**.5)/2
for j in range(M):
    z=1-2*(j+.5)/M
    theta=2*math.pi*j/phi
    x=[math.sqrt(max(0,1-z*z))*math.cos(theta),math.sqrt(max(0,1-z*z))*math.sin(theta),z]
    A=evalp(P,x)
    b=evalp(DP,x)
    area+=((max(0,b/(8*math.pi*A)))**1.5)/M*(4*math.pi/3)
base=(4*math.pi/3)*(5/(2*math.pi))**1.5
check(area>base+0.005,'3D numerical strictness')
print('PASS',checks,'checks; d3-volume approximately',f'{area:.10f}','radial bound',f'{base:.10f}')
