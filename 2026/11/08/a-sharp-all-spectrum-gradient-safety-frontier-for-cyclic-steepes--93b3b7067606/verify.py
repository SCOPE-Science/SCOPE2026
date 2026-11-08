#!/usr/bin/env python3
"""Standalone exact-rational and deterministic numerical checks for cyclic steepest descent."""
from fractions import Fraction as Q
from math import isclose, log, exp

def two_mode(m, k, t):
    k, t = Q(k), Q(t)
    return (k - 1)**(2*m) * (t + t**(2*m)) / ((k*t+1)**(2*m)*(1+t))

def actual_cycle_ratio(m, k, t):
    k, t = Q(k), Q(t)
    alpha = (1+t)/(k*t+1)
    return (t * (1-alpha*k)**(2*m) + (1-alpha)**(2*m))/(1+t)

checks = 0
for m in range(2, 9):
    for k in (Q(3,2), Q(2), Q(5,2), Q(3), Q(4), Q(8)):
        for t in (Q(1,64), Q(1,5), Q(1,2), Q(1), Q(3), Q(12)):
            assert two_mode(m,k,t) == actual_cycle_ratio(m,k,t)
            checks += 1
assert two_mode(2,4,Q(1,16)) == Q(19521,10000)
checks += 1
# Chord domination for finite spectral distributions, exact arithmetic.
for m in (2,3,5,8):
    for lam in ((Q(1),Q(2),Q(3)), (Q(1),Q(5,3),Q(4)),
                (Q(1),Q(11,7),Q(3),Q(5))):
        a,b=min(lam),max(lam)
        for p in ((1,2,3,5), (7,2,1,1), (1,1,1,1), (2,9,3,6)):
            w=[Q(j,sum(p[:len(lam)])) for j in p[:len(lam)]]
            mu=sum(x*y for x,y in zip(w,lam))
            lhs=sum(x*(1-y/mu)**(2*m) for x,y in zip(w,lam))
            endpoint=sum(x*((b-y)/(b-a)*(1-a/mu)**(2*m)
                    +(y-a)/(b-a)*(1-b/mu)**(2*m)) for x,y in zip(w,lam))
            assert lhs<=endpoint
            checks += 1

def max_ratio(m,k):
    # Continuous one-dimensional maximization, used only for supplementary numeric illustrations.
    import math
    def plus(a,b):
        h=max(a,b)
        return h+math.log(math.exp(a-h)+math.exp(b-h))
    def log_ratio(u):
        return (2*m*math.log(k-1)+plus(u,2*m*u)
                -2*m*plus(0,math.log(k)+u)-plus(0,u))
    # coarse scan plus golden-section; endpoints sampled too
    vals=[]
    lo=-28.0; span=56.0; intervals=1600
    for i in range(intervals+1):
        u=lo+i*span/intervals
        vals.append((log_ratio(u),u))
    _,center=max(vals)
    left=max(lo,center-0.3); right=min(lo+span,center+0.3)
    phi=(5**0.5-1)/2
    c=right-phi*(right-left);d=left+phi*(right-left)
    for _ in range(110):
        if log_ratio(c)<log_ratio(d):left=c;c=d;d=left+phi*(right-left)
        else:right=d;d=c;c=right-phi*(right-left)
    return math.exp(log_ratio((left+right)/2))

def threshold(m):
    lo=2.0; hi=5.0
    while max_ratio(m,hi)<1:hi*=2
    for _ in range(45):
        mid=(lo+hi)/2
        if max_ratio(m,mid)>1:hi=mid
        else:lo=mid
    return (lo+hi)/2

ks=[threshold(m) for m in (2,3,4,8,16)]
assert all(ks[i]>ks[i+1] for i in range(len(ks)-1))
assert abs(ks[0]-3.44281586925707)<1e-8
checks+=2
# The finite checks do not establish global maxima, unique thresholds or asymptotics.
print('PASS',checks,'exact/supplementary assertions; numerical thresholds', ks)
