#!/usr/bin/env python3
"""Reproducibility checks for the sharp two-frequency exterior leverage theorem.

Run with Python 3 standard library: python CHECK.py
Finite tests illustrate identities and bounds; the universal proof is in RESULT.md.
"""
import cmath
import math
import random
from fractions import Fraction as Q

checks = 0

def check(flag, label):
    global checks
    assert flag, label
    checks += 1

def leverage(d, x):
    s = math.sin(d) / d
    return (1 - s * math.cos(x*d)) / (1 - s*s)

def bound(x):
    return (1+3*x*x)/2

# Exact rational identity in the monotonicity certificate:
# u=1-d^2/6+d^4/120,
# 3(1-u^2)-d^2u=d^4(160-d^4)/4800.
def add(a,b):
    n = max(len(a),len(b))
    return [(a[i] if i<len(a) else Q(0))+(b[i] if i<len(b) else Q(0)) for i in range(n)]
def scale(a,t): return [x*t for x in a]
def mul(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):c[i+j]+=ai*bj
    return c
u=[Q(1),Q(0),-Q(1,6),Q(0),Q(1,120)]
expr=add(scale(add([Q(1)],scale(mul(u,u),-1)),Q(3)),scale([Q(0),Q(0)]+u,-1))
check(expr == [Q(0),Q(0),Q(0),Q(0),Q(1,30),Q(0),Q(0),Q(0),-Q(1,4800)], "sinc upper-bound polynomial identity")

rng=random.Random(20261106)
# Direct frequency-gram evaluation compared against an independent Simpson quadrature.
for _ in range(1500):
    d=10**rng.uniform(-1.5,1.7)
    c0=complex(rng.gauss(0,1),rng.gauss(0,1))
    c1=complex(rng.gauss(0,1),rng.gauss(0,1))
    s=math.sin(d)/d
    exact=2*(abs(c0)**2+abs(c1)**2+2*s*(c0.conjugate()*c1).real)
    n=500
    total=0.
    for j in range(n+1):
        t=-1+2*j/n
        value=abs(c0+c1*cmath.exp(1j*d*t))**2
        total+=(1 if j==0 or j==n else (4 if j%2 else 2))*value
    simpson=total*(2/n)/3
    check(abs(exact-simpson)<0.005*max(1,exact),"Gram vs independent integration")
    x=1+7*rng.random()
    val=abs(c0+c1*cmath.exp(1j*d*x))**2/exact
    check(val<=leverage(d,x)+3e-7,"Gram Cauchy Schwarz")

# Bound and strictness under many deterministic and random gaps/exterior points.
for d in [0.001,0.003,0.01,0.05,0.2,0.5,1.,1.5,1.99,2.,2.5,math.pi,4.,10.,50.]:
    for x in [1.,1.01,1.1,1.5,2.,3.,10.,100.]:
        check(leverage(d,x)<bound(x),"strict exterior bound")
for _ in range(10000):
    d=10**rng.uniform(-2.5,2.4)
    x=1+10**rng.uniform(-5,2.2)
    check(leverage(d,x) <= bound(x)+2e-6,"frequency uniform bound")

# Sharp confluent limit and its first gap-squared correction.
for x in [1.,1.2,2.,3.,8.]:
    c=(15*x**4+6*x*x-5)/120
    for d in [0.1,0.05,0.02]:
        deficit=bound(x)-leverage(d,x)
        check(abs(deficit/d**2-c)<0.3*d*d*max(1,x**6),"quadratic confluent deficit")
        check(deficit>0,"nonattainment at distinct frequencies")

# Explicit two-frequency sums converging to the affine representer K_x(t).
for x in [1.,1.5,2.5]:
    A=Q(1,2); B=3*x/2
    target=bound(x)
    for d in [0.1,0.05,0.02]:
        a=float(A)/2+B/(2j*d)
        b=float(A)/2-B/(2j*d)
        norm=2*(abs(a)**2+abs(b)**2+2*math.sin(2*d)/(2*d)*(a.conjugate()*b).real)
        evaluation=abs(a*cmath.exp(1j*d*x)+b*cmath.exp(-1j*d*x))**2
        check(abs(evaluation/norm-target)<3*x**4*d*d,"attaining sequence")

print('TWO_FREQUENCY_EXTERIOR_CHECKS_PASSED',checks)
