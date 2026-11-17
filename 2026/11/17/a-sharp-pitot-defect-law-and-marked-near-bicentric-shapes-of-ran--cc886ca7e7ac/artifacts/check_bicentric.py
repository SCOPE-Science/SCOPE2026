#!/usr/bin/env python3
"""Deterministic numerical checks for the random cyclic-bicentric law.

All deductions of the theorem are analytic; these tests corroborate
trigonometric identities, the global inequalities, and the coefficient.
Requires only Python's standard library.
"""
import math
import random

pi=math.pi
rng=random.Random(17721)


def gap_sample():
    e=[rng.expovariate(1.0) for _ in range(4)]
    return [2*pi*x/sum(e) for x in e]


def coords(a,b,c,d):
    return (a+c)/2,(a-c)/2,(b-d)/2


def pitot_from_gaps(a,b,c,d):
    return 2*(math.sin(a/2)+math.sin(c/2)-math.sin(b/2)-math.sin(d/2))


def normal_form(u,v,w):
    A=math.cos(v/2)
    B=math.cos(w/2)
    H=math.hypot(A,B)
    u0=2*math.atan2(B,A)
    return 4*H*math.sin((u-u0)/2),u0,H


def diamond_integral(n):
    # Area preserving map (v,w)=(pi*s,pi*(1-s)*t) in one quadrant.
    accum=0.0
    for i in range(n):
        s=(i+0.5)/n
        cv=math.cos(pi*s/2)**2
        pref=4*pi*pi*(1-s)/(n*n)
        for j in range(n):
            t=(j+0.5)/n
            cw=math.cos(pi*(1-s)*t/2)**2
            accum+=pref/math.sqrt(cv+cw)
    return accum


def exact_small_t(t,n):
    # Integrate exact clipped arcsine window, rather than an asymptotic.
    accum=0.0
    for i in range(n):
        s=(i+0.5)/n
        v=pi*s
        for j in range(n):
            q=(j+0.5)/n
            w=(pi-v)*q
            A=math.cos(v/2); B=math.cos(w/2)
            H=math.hypot(A,B)
            u0=2*math.atan2(B,A)
            h=2*math.asin(min(1.0,t/(4*H)))
            lo=max(v,u0-h)
            hi=min(pi-w,u0+h)
            accum+=max(0.0,hi-lo)*4*pi*pi*(1-s)/(n*n)
    return accum*3/(2*pi**3)


for k in range(16000):
    a,b,c,d=gap_sample()
    u,v,w=coords(a,b,c,d)
    z,u0,H=normal_form(u,v,w)
    direct=pitot_from_gaps(a,b,c,d)
    assert abs(z-direct)<7e-14,(z,direct)
    assert abs(v)<u<pi-abs(w)
    assert abs(v)<u0<pi-abs(w)
    if abs(u-u0)>1e-10:
        ratio=abs(z)/abs(u-u0)
        assert 2-1e-11<=ratio<=2*math.sqrt(2)+1e-11,(ratio,a,b,c,d)
    assert z*(u-u0)>-1e-12

I=diamond_integral(700)
C=3*I/(2*pi**3)
assert abs(C-0.8185431011367532)<0.000004,(I,C)
for t in (0.02,0.1,0.4):
    p=exact_small_t(t,450)
    assert 0<p<1
    if t==0.02: assert abs(p/t-C)<0.04,(p/t,C)

# Empirical comparison with the independent exact clipped-arcsine integral.
sample=160000
for t in (0.1,0.4):
    hits=sum(abs(pitot_from_gaps(*gap_sample()))<t for _ in range(sample))
    p_mc=hits/sample
    p_formula=exact_small_t(t,360)
    assert abs(p_mc-p_formula)<0.012,(t,p_mc,p_formula)

print('CYCLIC_BICENTRIC_COORDINATE_AND_TAIL_CHECKS_OK')
print('coefficient',format(C,'.10f'))
print('I',format(I,'.10f'))
