#!/usr/bin/env python3
"""Standalone numerical checks for the one-particle binomial-adjusted tau leap.

No dependencies beyond the Python standard library. Analytical proof is in RESULT.md.
"""
import math

count=0

def near(a,b,atol=1.5e-12):
    global count
    assert abs(a-b)<=atol*(1+abs(a)+abs(b)),(a,b)
    count+=1


def law(theta,t):
    d=1-1/(2*theta)
    return math.exp(-t)+math.exp(-d*t)-math.exp(-theta*t)


def direct(theta,t):
    p0=(2*theta-1)/(2*theta**2)
    x=theta*t
    pois=math.exp(-x)
    acc=pois*math.exp(-(1-theta)*t)
    for n in range(1,150):
        pois*=x/n
        acc+=pois*(1-p0)**n
    return acc


def baseline(theta,t):
    return math.exp(-theta*t)*math.exp(-(1-theta)*t)

for theta in (0.5,0.5001,0.51,0.6,1/math.sqrt(2),0.8,0.99):
    c=2-theta-1/(2*theta)
    for t in (0.001,0.01,0.1,0.3,1,2*math.log(2),2,5,10):
        near(law(theta,t),direct(theta,t))
        near(baseline(theta,t),math.exp(-t))
        assert 0<=law(theta,t)<=1+2e-15
        count+=1
    for n in (32,128,1024,8192):
        physical=1.2
        approximate=law(theta,physical/n)**n
        expected=math.exp(-c*physical)
        assert abs(approximate-expected)<5/n
        count+=1
        # The old (uncorrected) method's survival is exact after n steps.
        near(baseline(theta,physical/n)**n,math.exp(-physical))
    for t in (0.001,0.003,0.005):
        rate=(1-law(theta,t))/t
        assert abs(rate-c)<5*t
        count+=1

for t in (0.001,0.05,0.3,1,2*math.log(2),3,5,10,40):
    u=math.exp(-t/2)
    near(law(0.5,t),0.75+(u-0.5)**2)
    assert law(0.5,t)>=0.75-1e-15
    count+=1
near(law(0.5,2*math.log(2)),0.75)
assert law(0.5,10)>law(0.5,2*math.log(2))
count+=1
print('VERIFY_OK',count,'assertions')
