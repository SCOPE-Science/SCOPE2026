#!/usr/bin/env python3
"""Exact, standalone rational tests for the stated two-memory gap witness.

The universal convex-order assertion is proved in RESULT.md rather than by finite tests.
"""
from fractions import Fraction as Q

# All powers are exact: if J=log 2, exp(-s*k*J)=2**(-s*k).
def pow_two(k):
    return Q(2)**k

P={-1:Q(1,2),1:Q(1,2)}
R={-2:Q(1,8),0:Q(3,4),2:Q(1,8)}

def excess(distribution, rate):
    assert sum(distribution.values())==1
    return sum(prob*pow_two(-rate*k) for k,prob in distribution.items())-1

def moment(distribution, power):
    return sum(prob*k**power for k,prob in distribution.items())

for dist in (P,R):
    assert moment(dist,1)==0
    assert moment(dist,2)==1
    assert all(Q(5)>Q(2)**(-k) for k in dist)  # mu + k*J = log(5*2**k)>0

assert excess(P,1)==Q(1,4)
assert excess(P,2)==Q(9,8)
assert excess(R,1)==Q(9,32)
assert excess(R,2)==Q(225,128)

# v0=D=A=a=1, d=2, mu=log 5.
def change(dist, five):
    return excess(dist,2)/five**2-excess(dist,1)/five
assert change(P,Q(5)) == -Q(1,200)
assert change(R,Q(5)) == Q(9,640)
assert change(P,Q(4)) == Q(1,128)
assert change(P,Q(8)) == -Q(7,512)

# Unique crossover means are log(9/2) and log(25/4).
assert excess(P,2)/excess(P,1)==Q(9,2)
assert excess(R,2)/excess(R,1)==Q(25,4)
assert Q(9,2)<Q(5)<Q(25,4)
assert Q(5)>Q(4)   # all support points of R are strictly positive
print('PASS: exact first/second moments, support, four exponential moments, two opposite signs, and both thresholds')
