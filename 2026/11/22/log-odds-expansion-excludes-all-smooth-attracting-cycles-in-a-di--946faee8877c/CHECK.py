#!/usr/bin/env python3
"""Exact arithmetic checks for the stated multiplier identity and nonvacuous two-cycle.

The mathematical proof is algebraic; this finite checker tests the identity and example.
"""
from fractions import Fraction as Q

def step(x, p):
    return x + (2*p - 1)*x*(1-x)

def slope(x, p):
    return 1 + (2*p - 1)*(1-2*x)

case_count=0
for i in range(1,20):
    x=Q(i,20)
    for k in range(21):
        p=Q(k,20)
        y=step(x,p)
        assert 0<y<1
        assert x*(1-x)*slope(x,p) == y*(1-y)+(y-x)**2
        assert slope(x,p)*x*(1-x)/(y*(1-y)) == 1+(y-x)**2/(y*(1-y))
        case_count+=1
x0=Q(1,5)
x1=Q(17,50)
a=Q(15,16)
b=Q(211,1122)
c=Q(1,2)
assert 0<x0<Q(1,3)<x1<Q(2,3)<1
assert 0<=a<=1 and 0<=b<=1 and 0<=c<=1
assert step(x0,a)==x1
assert step(x1,b)==x0
actual=slope(x0,a)*slope(x1,b)
pred=(1+(x1-x0)**2/(x1*(1-x1)))*(1+(x0-x1)**2/(x0*(1-x0)))
assert actual==pred==Q(27389,22440)>1
assert slope(Q(3,4),Q(1,1))==Q(1,2)
print('PASS:',case_count,'exact branch identities; exact two-cycle and multiplier',actual)
