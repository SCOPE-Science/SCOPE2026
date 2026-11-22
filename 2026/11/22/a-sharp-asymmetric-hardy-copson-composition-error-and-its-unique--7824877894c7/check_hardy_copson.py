#!/usr/bin/env python3
"""Numerical diagnostics for a sharp Hardy–Copson BV approximation identity.

The infinite-dimensional theorem requires the analytic proof in RESULT.md;
these finite checks test its explicit formulas and selected signed-step examples.
Uses only the Python standard library.
"""
import math
import random


def dilog(x):
    assert 0 <= x < 1
    y, power = 0.0, 1.0
    for k in range(1, 5000):
        power *= x
        term = power/(k*k)
        y += term
        if abs(term) < 3e-17:
            return y
    raise AssertionError('series did not converge')


def a(s):
    return s+(1-s)*math.log1p(-s)


def error(s):
    return (1-s)*dilog(s)-a(s)*math.log(s)


def deriv(s):
    return -1-dilog(s)+math.log(s)*math.log1p(-s)-2*(1-s)/s*math.log1p(-s)


def mean_step(s,x):
    if x == 0:
        return 1-s
    if x <= s:
        return -(1-s)*math.log1p(-x)/x
    return 1-a(s)/x


def simpson(f,lo,hi,n=1000):
    if hi <= lo:
        return 0.0
    if n%2: n += 1
    step=(hi-lo)/n
    acc=f(lo)+f(hi)
    for k in range(1,n):
        acc += (4 if k%2 else 2)*f(lo+k*step)
    return acc*step/3


def direct_composition_step(s,x):
    if x == 0:
        return 1-s
    def reverse_step(u):
        return (1-s)/(1-u) if u<s else 1.0
    return (simpson(reverse_step,0,min(s,x),800)+max(x-s,0))/x


def direct_l1_error(s):
    return simpson(lambda x: mean_step(s,x),0,s,2500)+simpson(lambda x: 1-mean_step(s,x),s,1,2500)


def verify():
    lo,hi=.5,.7
    assert deriv(lo)>0 and deriv(hi)<0
    for _ in range(65):
        mid=(lo+hi)/2
        if deriv(mid)>0: lo=mid
        else: hi=mid
    s=(lo+hi)/2
    C=error(s)
    assert abs(s-0.58919541498742034)<3e-13
    assert abs(C-0.41050749871794369)<3e-13
    assert C>1/math.e and error(.5)>1/math.e
    grid=[.01,.01,.1,.2,.35,.5,.6,.78,.91,.99]
    comparisons=0
    for q in grid:
        assert abs(error(q)-direct_l1_error(q))<2e-10
        for x in [.02,.11,.29,.5,.79,.93]:
            if abs(x-q)<1e-10: continue
            assert abs(mean_step(q,x)-direct_composition_step(q,x))<1e-10
            comparisons+=1
    rng=random.Random(271828)
    signed_cases=0
    for _ in range(65):
        jumps=sorted((rng.uniform(.08,.92),rng.uniform(-1,1)) for j in range(rng.randrange(1,6)))
        V=sum(abs(v) for _,v in jumps)
        def defect(x):
            return sum(v*((1 if x>z else 0)-mean_step(z,x)) for z,v in jumps)
        edges=[0]+[z for z,v in jumps]+[1]
        def interior_abs(x,left,right):
            witness=(left+right)/2
            value=sum(v*((1 if witness>z else 0)-mean_step(z,x)) for z,v in jumps)
            return abs(value)
        err=sum(simpson(lambda x, left=left, right=right: interior_abs(x,left,right),left,right,1800)
                for left,right in zip(edges[:-1],edges[1:]))
        assert err <= C*V+1e-8,(err,C*V)
        signed_cases+=1
    print('PASS; unique-root diagnostic s*=%.15f, sharp error=%.15f' %(s,C))
    print('PASS; direct step-integral comparisons=%d, signed BV tests=%d' %(comparisons,signed_cases))
    print('PASS; sharp one-sided Hardy coefficient 1/e=%.15f is smaller' %(1/math.e))

if __name__=='__main__':
    verify()
