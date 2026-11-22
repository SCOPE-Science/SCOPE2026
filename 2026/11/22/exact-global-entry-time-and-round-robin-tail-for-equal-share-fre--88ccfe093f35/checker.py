#!/usr/bin/env python3
"""Finite rational regression checks for the equal-share greedy map theorem.
The proof in RESULT.md, not testing, establishes all real initial points.
"""
from fractions import Fraction as F
from itertools import product
from math import floor
from random import Random

def step(heads):
    # Heads are relative scores a_i - number of allocations to candidate i;
    # the common +t/m part does not influence the winner.
    h=list(heads)
    i=max(range(len(h)),key=lambda j:h[j])
    h[i]-=1
    return tuple(h),i

def bound(a):
    lo=min(a)
    return sum(floor(v-lo) for v in a)

def verify(a):
    n=bound(a)
    h=tuple(a)
    lo=min(a)
    for t in range(n):
        if max(h)-min(h)<1:raise AssertionError(('early',a,t,n,h))
        if min(h)!=lo:raise AssertionError(('min moved',a,t,h))
        h,_=step(h)
    if h != tuple(v-floor(v-lo) for v in a):raise AssertionError(('wrong entry state',a,n,h))
    if max(h)-min(h)>=1:raise AssertionError(('not entered',a,n,h))
    for rep in range(4):
        before=h
        used=[]
        for _ in range(len(a)):
            h,i=step(h)
            used.append(i)
        if sorted(used)!=list(range(len(a))):raise AssertionError(('not permutation',a,n,used))
        if h!=tuple(v-1 for v in before):raise AssertionError(('not period',a,n,h,before))

rng=Random(251106)
checks=0
# exhaustive centered integer/half-integer points up to 5 agents
for m,levels in ((2,range(-9,10)),(3,range(-6,7)),(4,range(-3,4)),(5,range(-2,3))):
    for z in product(levels,repeat=m-1):
        a=tuple(F(v,2) for v in z)+(F(-sum(z),2),)
        verify(a);checks+=1
for m in range(2,10):
    for _ in range(250):
        v=[F(rng.randint(-20,20),rng.randint(1,9)) for _ in range(m)]
        a=tuple(x-sum(v)/m for x in v)
        verify(a);checks+=1
# Sharpness of the guarantee for a deterministic lowest-index tie policy.
for m in range(2,15):
    for N in range(1,20):
        a=tuple([F(N*(m-1),m)]+[F(-N,m)]*(m-1))
        n=bound(a)
        assert n==N
        h=tuple(a)
        for _ in range(n-1): h,_=step(h)
        at=h
        used=[]
        for _ in range(m): h,j=step(h);used.append(j)
        assert h!=tuple(v-1 for v in at), (m,N,used)
        checks+=1
print('PASS',checks,'finite tests: exact entry, strict pre-entry, m-step periodicity, and sharp examples')
