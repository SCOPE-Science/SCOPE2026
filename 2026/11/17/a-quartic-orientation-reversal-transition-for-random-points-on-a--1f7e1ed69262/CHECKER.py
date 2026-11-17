#!/usr/bin/env python3
"""Reproduce numeric and elementary exact checks for the circular-helix orientation law."""
import math, random
from fractions import Fraction
import numpy as np

def det_direct(t):
    return float(np.linalg.det(np.array([[1.,x,math.cos(x),math.sin(x)] for x in t])))

def det_paired(t):
    m=(t[0]+t[1])/2; h=(t[1]-t[0])/2
    n=(t[2]+t[3])/2; k=(t[3]-t[2])/2; d=n-m
    H=(math.cos(k)-math.cos(h))*(h/math.sin(h)-k/math.sin(k))
    H+=(1-math.cos(d))*(h/math.tan(h)+k/math.tan(k))-d*math.sin(d)
    return 4*math.sin(h)*math.sin(k)*H

rng=random.Random(18451)
for _ in range(1000):
    t=sorted(rng.uniform(0,7) for j in range(4))
    a=det_direct(t); b=det_paired(t)
    assert abs(a-b)<1e-9*(1+abs(a)),(t,a,b)
for e in (0.1,0.03,0.01):
    x=(0.1,0.4,0.8,0.95)
    t=(e*x[0],e*x[1],2*math.pi+e*x[2],2*math.pi+e*x[3])
    exact=det_direct(t)
    lead=math.pi*e**3*(x[0]-x[1])*(x[2]-x[3])*(x[0]+x[1]-x[2]-x[3])
    assert abs(exact/lead-1)<0.03,(e,exact,lead)
# 4*(integral_0^1 a * integral_a^1 (1-b) db da) = 1/6.
a=Fraction(1,6)
assert 2*(Fraction(1,2)-2*Fraction(1,3)+Fraction(1,4))==a
# Independent Monte Carlo volume estimate in a finite box containing the polytope.
n=200000; hits=0
for _ in range(n):
    x1=rng.uniform(0,1); x2=rng.uniform(0,2)
    x3=rng.uniform(-1,1); x4=rng.uniform(0,1)
    hits+=(x1<x2 and x3<x4 and x3+x4>x1+x2)
volume=4*hits/n
assert abs(volume-1/6)<0.012,volume
print('HELIX_ORIENTATION_QUARTIC_CHECKS_OK',volume)
