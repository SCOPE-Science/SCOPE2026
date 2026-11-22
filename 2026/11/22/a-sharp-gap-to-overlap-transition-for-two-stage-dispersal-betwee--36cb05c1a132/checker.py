#!/usr/bin/env python3
"""Reproduce exact phase-window benchmarks; no external dependencies."""
import math
import random


def F(z):
    if z <= 0.0: return 0.0
    return -math.expm1(-z)-z*math.exp(-z)

def G(z):
    if z <= 0.0: return 0.0
    return z - 2.0 + (z + 2.0)*math.exp(-z)

def density(z, x):
    if z <= 0.0: return 0.0
    return (F(z)-F(z-x))/x

def probability(d, x):
    return (G(d+x)-2*G(d)+G(d-x))/x

def root_bisect(fn,lo,hi,n=110):
    a=fn(lo); b=fn(hi)
    assert a*b<=0, (lo,hi,a,b)
    for _ in range(n):
        mid=(lo+hi)/2
        val=fn(mid)
        if val==0: return mid
        if val*a>0: lo,a=mid,val
        else: hi,b=mid,val
    return (lo+hi)/2

XCRIT=root_bisect(lambda x: math.expm1(x)-2*x, 1.,2.)
MEDIAN=root_bisect(lambda d: F(d)-.5, 1.,3.)

def opt2(x):
    assert x>0
    if x<=XCRIT:
        return x/math.tanh(x/2)-1
    return root_bisect(lambda d: F(d+x)-2*F(d),0.,x)

def opt1(x): return math.log(2-math.exp(-x))

assert abs(XCRIT-1.2564312086261697)<1.e-12
assert abs(MEDIAN-1.6783469900166605)<1.e-12

rng=random.Random(441123)
checks=0
prev=1.
for j in range(1,3000):
    x=0.03+0.007*j
    d=opt2(x)
    assert d > 1-1e-10 and d<MEDIAN+1e-10
    assert d>prev-1e-10 if j>1 else True
    prev=d
    assert (d>x)==(x<XCRIT) if abs(x-XCRIT)>1e-8 else True
    assert abs(density(d+x,x)-density(d,x))<2.e-9
    de=opt1(x)
    assert 0<de<min(x,math.log(2))
    checks+=5

for j in range(12000):
    x=0.18+14.82*rng.random()
    best=opt2(x)
    trial=-x + (best+5*x+12)*rng.random()
    if trial>0 and trial<best-1e-8:
        assert density(trial+x,x)-density(trial,x)>-3e-10
    if trial>best+1e-8:
        assert density(trial+x,x)-density(trial,x)<3e-10
    pbest=probability(best,x)
    pother=probability(trial,x)
    assert pbest >= pother-5e-10, (x,best,trial,pbest,pother)
    checks+=2

# Asymptotic convergence in a controlled finite regime (numerical, not a proof).
for x in (0.01, 0.015, 0.02, 0.03):
    assert abs(opt2(x)-1) < x*x/5
    assert abs(probability(0,x)/(x*x/6)-1)<0.025
    assert abs(probability(opt2(x),x)/(x/math.e)-1)<0.025
    checks+=3

print(f"PASS; {checks} assertions; threshold={XCRIT:.15f}; Erlang2 median={MEDIAN:.15f}")
for x in (0.2,1.0,XCRIT,2.,4.,10.):
    print(f"duration={x:.8f} optimum={opt2(x):.12f} gap={opt2(x)-x:+.12f} Popt={probability(opt2(x),x):.9f} Psync={probability(0,x):.9f}")
