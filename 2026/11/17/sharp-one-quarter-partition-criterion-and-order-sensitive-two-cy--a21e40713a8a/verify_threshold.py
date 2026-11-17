#!/usr/bin/env python3
"""Exact rational witness checks for the residue-partition dynamical theorem.
This script is corroboration: the universal inequalities are proved in RESULT.md.
"""
from fractions import Fraction as F

def mass(k, residues, r):
    assert 0 < r < 1 and 0 in residues and set(residues) < set(range(k))
    return sum((r**j for j in residues), F(0))/sum((r**j for j in range(k)), F(0))

def delta(a,b,c):
    return 1+4*(b*b-b+c*(1-a))

k=14
low=(0,1,2,3)
high=(0,11,12,13)
a=mass(k, high, F(7,8))
b=mass(k, high, F(1,1000))
c=mass(k, high, F(1,2000))
assert a < F(6,25) and b>F(999,1000) and c>F(1999,2000)
assert F(1999,2000)*F(19,25)-F(1,1000)>F(3,4)
D=delta(a,b,c)
assert F(4)<D<F(5)
assert F(0)<5-D<F(1)
# Check all formulas on representative rational inputs (not an exhaustive proof).
for m,k in [(1,5),(2,9),(4,14),(3,12),(5,21)]:
    for r in [F(1,8),F(1,2),F(7,8),F(99,100)]:
        q=mass(k, tuple(range(m)), r)
        assert q==(1-r**m)/(1-r**k)
        assert F(m,k)<q<1
for r in [F(1,100),F(1,2),F(7,8),F(99,100),F(999,1000)]:
    assert mass(14,low,r)>F(2,7)
# Independently check numerical attracting two-cycle from one fixed-point-free seed.
x=1/3
def f(x): return a*x*x+2*b*x*(1-x)+c*(1-x)*(1-x)
for _ in range(1200): x=f(x)
y=f(x)
assert abs(float(x-y))>1e-3
assert abs(float(f(y)-x))<1e-12
print('RESIDUE_QUARTER_THRESHOLD_EXACT_OK')
print('a',float(a),'b',float(b),'c',float(c),'Delta',float(D),'Floquet',float(5-D))
