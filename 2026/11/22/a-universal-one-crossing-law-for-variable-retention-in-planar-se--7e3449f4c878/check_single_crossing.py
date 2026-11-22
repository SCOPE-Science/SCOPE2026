#!/usr/bin/env python3
"""Deterministic diagnostic checks for a planar stopped-diffusion comparison.

This tests examples of the analytic theorem, and is not a proof for all laws.
"""
import math
import random

COUNT = 0

def check(test, label):
    global COUNT
    COUNT += 1
    if not test:
        raise AssertionError(label)

def root(f, low, high):
    fl, fh = f(low), f(high)
    check(fl < 0 and fh > 0, 'bracket')
    for _ in range(90):
        mid = (low + high) / 2
        if f(mid) > 0:
            high = mid
        else:
            low = mid
    return (low + high) / 2

def family(values, weights):
    mean = sum(x*w for x,w in zip(values,weights))
    y = [1/mean-1/x for x in values]
    def F(s):
        return sum(w*math.expm1(s*z) for w,z in zip(weights,y))
    def J(s):
        return sum(w/x*math.exp(s*z) for w,x,z in zip(weights,values,y))-1/mean
    lo,hi=2*min(values),2*max(values)
    root_cross=root(F,lo,hi)
    check(lo<root_cross<hi,'support bound')
    check(F(root_cross*.6)<0,'cross lower')
    check(F(root_cross*1.1)>0,'cross upper')
    low_turn=root(lambda z: -J(z),0,root_cross)
    high_limit=max(10*max(values),2*root_cross)
    high_turn=root(J,root_cross,high_limit)
    check(0<low_turn<root_cross<high_turn,'turn ordering')
    check(J(low_turn*.5)>0,'first derivative negative')
    check(J((low_turn+root_cross)/2)<0,'middle derivative positive')
    check(J((root_cross+high_turn)/2)<0,'middle derivative positive')
    check(J(high_turn*1.2)>0,'last derivative negative')
    return root_cross,low_turn,high_turn

def run():
    rand=random.Random(192017)
    for n in range(2,9):
        for j in range(80):
            raw=[math.exp(rand.uniform(-1.25,1.25)) for _ in range(n)]
            weights0=[rand.uniform(.1,1) for _ in range(n)]
            weights=[w/sum(weights0) for w in weights0]
            a,b,c=family(raw,weights)
            check(a>0 and b>0 and c>0,'positive')
    # Fixed-mean two-point example: the unique root of z^3-z^2-z-1=0.
    z=root(lambda x:x*x*x-x*x-x-1,1.5,2)
    crossing=3*math.log(z)
    got,_,_=family([.5,1.5],[.5,.5])
    check(abs(got-crossing)<1e-11,'tribonacci example')
    # Weak-heterogeneity crossover and extrema: 2, 2-sqrt(2), 2+sqrt(2).
    for eps in (.07,.03,.01,.004):
        a,lower,upper=family([1-eps,1+eps],[.5,.5])
        check(abs(a-2)<4*eps,'weak crossover')
        check(abs(lower-(2-math.sqrt(2)))<3*eps,'weak trough')
        check(abs(upper-(2+math.sqrt(2)))<5*eps,'weak peak')
    # Nearly-zero retention time, testing that a finite inverse mean is not used.
    family([.00001,.95,2.05],[.01,.494,.496])
    print('PASS',COUNT,'deterministic assertions')

if __name__=='__main__':run()
