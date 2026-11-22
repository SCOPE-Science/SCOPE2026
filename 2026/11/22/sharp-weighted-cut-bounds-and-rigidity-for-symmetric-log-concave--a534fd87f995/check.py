#!/usr/bin/env python3
"""Exact rational consistency checks for weighted line-cut identities.

Finite checks supplement, but do not replace, the analytic proofs.
"""
from fractions import Fraction as F

def absdiff_uniform(a,b):
    if a < b: a,b=b,a
    return a/F(2) + b*b/(F(6)*a)

checks=0
for p in range(101):
    I1=F(1,p+2)
    I2=F(1,2*p+3)
    L=2*I1-I2
    fraction=I1/L
    assert fraction==F(2*p+3,3*p+4)
    assert F(2,3)<fraction<=F(3,4)
    assert F(3,2)*I1-L==I2-I1/F(2)
    checks+=4

# Laplace and uniform endpoint integrals.
assert F(1)/(2*F(1)-F(1,2)) == F(2,3)
assert F(1,2)/(2*F(1,2)-F(1,3)) == F(3,4)
checks+=2

# Two-uniform-radius identity with exact convolution integration.
for ia in range(1,20):
 for ib in range(1,20):
    a,b=F(ia,7),F(ib,11)
    diff=absdiff_uniform(a,b)
    assert diff - F(1,3)*(a+b) == (a-b)**2/(F(6)*max(a,b))
    checks+=1

# An independent radius mixture with 2 atoms, weights 2/5 and 3/5.
probs=[F(2,5),F(3,5)]
radii=[F(1),F(3)]
I1=sum((p*a/F(2) for p,a in zip(probs,radii)),F(0))
L=sum((probs[i]*probs[j]*absdiff_uniform(radii[i],radii[j]) for i in range(2) for j in range(2)),F(0))
deficit=sum((probs[i]*probs[j]*(radii[i]-radii[j])**2/(F(6)*max(radii[i],radii[j])) for i in range(2) for j in range(2)),F(0))
assert L-F(4,3)*I1==deficit
checks+=1
print('Exact rational consistency checks passed:',checks)
