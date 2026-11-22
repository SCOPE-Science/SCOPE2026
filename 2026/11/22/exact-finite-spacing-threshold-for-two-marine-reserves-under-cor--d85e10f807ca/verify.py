#!/usr/bin/env python3
"""Checks for an exact two-reserve persistence-separation phase law.

Requires Python 3 standard library only. Finite tests supplement the analytic proof.
"""
import math
import random
from fractions import Fraction

COUNT = 0

def check(b):
    global COUNT
    assert b
    COUNT += 1

def entries(r, c, q):
    a = 1 - r * (1 + q) / 2
    return a * (1 - c), a * c, r * (1-q) * (1-c), 1-r+r*(1-q)*c

def radius(r,c,q):
    a,b,c1,d = entries(r,c,q)
    return (a+d+math.hypot(a-d,2*math.sqrt(b*c1)))/2

def comparison(r,c,q):
    return c*(2-r-(4-3*r)*q) - r*q

def H(k,r):
    if k <= 1: return 2-r
    return (2-r)/k * ((k-1)*(2-r)/(k*(4-3*r)))**(k-1)

def kcrit(r):
    lo,hi=1.0,2.0
    while H(hi,r)>r: hi*=2
    for _ in range(95):
        mid=(lo+hi)/2
        if H(mid,r)>r: lo=mid
        else: hi=mid
    return (lo+hi)/2

# Exact-rational identity and strict subdominant-eigenvalue inequality.
for rn in [1,2,3,5,7,9]:
    r=Fraction(rn,10)
    for cn in range(1,10):
        c=Fraction(cn,10)
        for qn in range(1,10):
            q=Fraction(qn,10)
            a,b,cc,d=entries(r,c,q)
            L=1-r/2
            check((L-a)*(L-d)-b*cc == r*(r*q-comparison(r,c,q)-r*q)/4)
            check(a<L)

# Independent direct-eigenvalue comparisons on the full interior, no false claims at near ties.
rng=random.Random(827315)
for _ in range(12000):
    r=rng.uniform(0.01,0.99)
    k=rng.uniform(0.05,10)
    d=rng.uniform(0.0001,20)
    q=math.exp(-d);c=q**k
    f=comparison(r,c,q)
    v=radius(r,c,q)-(1-r/2)
    if abs(f)>1e-9 and abs(v)>1e-9:
        check((f>0)==(v>0))

# All sharp regimes for the comparison function, using a broad bounded grid.
for r in [.01,.1,.25,.5,.9,.99]:
    kc=kcrit(r)
    check(kc>1)
    check(abs(H(kc,r)/r-1)<2e-12)
    for k in [0.25,0.99,1.0,(1+kc)/2,kc*1.08]:
        if k>1:
            q0=(k-1)*(2-r)/(k*(4-3*r))
            check(0<q0<1)
            if k<(1+kc)/2+1e-12: check(H(k,r)>r)
            if k>kc:check(H(k,r)<r)
        if k<=1:
            for q in [1e-6,1e-5,1e-4]:check(comparison(r,q**k,q)>0)

# Exact quadratic cutoff for k=2 and r=1/10, with the predicted bounded window.
r=0.1;k=2
A=2-r;B=4-3*r
D=A*A-4*B*r
qlo=(A-math.sqrt(D))/(2*B);qhi=(A+math.sqrt(D))/(2*B)
check(0<qlo<qhi<1)
check(abs(comparison(r,qlo**2,qlo))<1e-14)
check(abs(comparison(r,qhi**2,qhi))<1e-14)
for q in [qlo/2,(qlo+qhi)/2,(qhi+1)/2]:
    check((comparison(r,q*q,q)>0)==(qlo<q<qhi))
check(abs((10-4*math.sqrt(3))/13-0.23629205920957624)<1e-12)
print(f'{COUNT} checks passed')
