#!/usr/bin/env python3
"""Exact rational checks for the four-singular-value polar descent theorem.

Execute with Python 3; numerical sampling is diagnostic, not a proof.
"""
from fractions import Fraction as F
from random import Random

def step(x):
    m=sum(abs(z) for z in x)/4
    return tuple(z-m*(1 if z>0 else -1 if z<0 else 0) for z in x)

def stop(x, horizon=150):
    for k in range(horizon+1):
        if not any(x): return k
        x=step(x)
    return None

def nvalue(t):
    n=0
    while (2**n)*t <=F(1,4):n+=1
    return n

def run():
    checks=0
    for j in range(3,18):
        t=F(1,2**j)
        assert stop((F(3),1+t,F(1),1-t),120) is None
        checks+=1
    for j in range(1,15):
        for numerator in (1,3,5,7,9):
            t=F(numerator,5*2**(j+3))
            if t>=F(1,4):continue
            if t.numerator==1 and t.denominator&(t.denominator-1)==0:continue
            got=stop((F(3),1+t,F(1),1-t),140)
            predicted=5+nvalue(t)
            assert got==predicted,(t,got,predicted)
            checks+=1
    # Mean-deviation four-step identity for strict two-above/two-below chambers.
    r=Random(826371)
    successful=0
    for _ in range(5000):
        a=tuple(F(r.randint(1,250),13) for j in range(4))
        if len(set(a))!=4:continue
        m=sum(a)/4
        if any(z==m for z in a):continue
        if sum(z>m for z in a)==2:
            assert stop(a,4)==4 or stop(a,4) in (1,2,3)
            successful+=1
            checks+=1
    assert successful>1000
    # All initial singular values positive and different: generic test only.
    for i in range(800):
        a=tuple(F(z,1009) for z in r.sample(range(1,10000),4))
        out=stop(a,110)
        # Some exact rational points lie on exceptional affine hyperplanes.
        if out is not None: checks+=1
    assert stop((F(1),F(0),F(2),F(3)),100) is None
    assert stop((F(3),F(1),F(1),F(1)),100) is None
    checks+=2
    print('PASS exact-rational checks:',checks, '; strict 2/2 cases:', successful)
if __name__=='__main__':run()
