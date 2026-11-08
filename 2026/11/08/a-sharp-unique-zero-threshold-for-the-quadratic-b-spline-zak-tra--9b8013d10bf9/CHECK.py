#!/usr/bin/env python3
"""Supplementary exact-rational tests for the two-variable Zak-zero theorem.

The proof's global inequalities are analytical. These tests sample rational grids
and are neither an exhaustive real-domain search nor an infinite proof.
"""
from fractions import Fraction as Q

def b3(t):
    t = abs(t)
    if t <= Q(1, 2):
        return Q(3, 4) - t*t
    if t <= Q(3, 2):
        return (Q(3, 2)-t)**2 / 2
    return Q(0)

def term(b, x, k):
    return b3((x-k)/b)

def R(b, x):
    return sum((1 if k % 2 == 0 else -1)*term(b,x,k)
               for k in range(-5,6))

def D(b, x):
    return (term(b,x,1)-term(b,x,-1)
            -2*(term(b,x,2)-term(b,x,-2)))

checks=0
for b in (Q(1),Q(9,8),Q(5,4),Q(4,3),Q(7,5),Q(3,2),Q(8,5),Q(5,3)):
    for j in range(101):
        x=Q(j,200)
        assert (R(b,x)>0)==(j<100)
        if j>0:
            assert D(b,x)>0
        checks+=1
for b in (Q(7,4),Q(15,8),Q(2)):
    d=2-b
    for j in range(41):
        x=Q(3,2)*d+(1-3*d)*Q(j,40)
        assert R(b,x)==0
        checks+=1
print('CHECK_OK exact-rational-configurations='+str(checks))
