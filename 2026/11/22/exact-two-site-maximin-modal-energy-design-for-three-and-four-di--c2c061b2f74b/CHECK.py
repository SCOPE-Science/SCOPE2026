#!/usr/bin/env python3
"""Standalone numerical cross-checks for a closed-form modal-energy theorem.
Run: python3 CHECK.py. The analytic upper bound is proved separately.
"""
import math
import random

TOL = 4e-12

def E(x, y, m):
    return min(math.sin(math.pi*k*x)**2 + math.sin(math.pi*k*y)**2
               for k in range(1,m+1))

# All four unordered equality pairs: one in {1/5,4/5}, other in {2/5,3/5}.
for m in (3,4):
    for x in (1/5,4/5):
        for y in (2/5,3/5):
            assert abs(E(x,y,m)-1.25)<TOL
            for k in range(1,m+1):
                assert abs(math.sin(math.pi*k*x)**2+math.sin(math.pi*k*y)**2-1.25)<TOL

# Exact algebraic extremizer tests in the Chebyshev coordinates.
a = (math.sqrt(5)-1)/4
b = -(math.sqrt(5)+1)/4
s,p = a+b,a*b
assert abs(s+0.5)<TOL and abs(p+0.25)<TOL
for k in range(1,5):
    assert abs(math.cos(2*math.pi*k/5)+math.cos(4*math.pi*k/5)+0.5)<TOL

# Check the rational factorization leading to the strict upper-bound certificate.
for num in range(-99,-50):
    s0 = num/100
    lo = (s0*s0-0.75)/2
    hi = (0.5+4*s0**3-3*s0)/(12*s0)
    assert hi<lo
    assert abs(24*s0*(hi-lo)-(1-s0)*(2*s0+1)**2)<TOL

# Paired-sensor exhaustive modest grid and seeded random probes (non-proof).
N = 251
for i in range(N):
    x=i/(N-1)
    for j in range(i,N):
        y=j/(N-1)
        assert E(x,y,3)<=1.25+TOL
        assert E(x,y,4)<=1.25+TOL
rng=random.Random(931521)
for _ in range(18000):
    x,y=rng.random(),rng.random()
    assert E(x,y,3)<=1.25+TOL
    assert E(x,y,4)<=1.25+TOL

# Repeating one site cannot exceed 1 for the three-mode problem.
for i in range(5001):
    x=i/5000
    assert E(x,x,3)<=1+TOL
assert abs(E(0.25,0.25,3)-1)<TOL
print('MODAL_ENERGY_CHECKS_PASS',2*4*4+49+2*31626+18000*2+5001)
