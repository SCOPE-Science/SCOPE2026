#!/usr/bin/env python3
"""Exact rational reproducibility checks for trivariate Gaussian mixed moments."""
from fractions import Fraction as F
from itertools import product

def raw(a,b,c,s):
    v=1-a*a;w=1-b*b;u=c-a*b
    return (a*a*b*b*(1-s)*(3-s)+(1-s)*(a*a*w+b*b*v+4*a*b*u)+v*w+2*u*u)-1

def compact(a,b,c,s):
    return 2*c*c-s*(a*a+b*b+4*a*b*c-2*a*a*b*b)+s*s*a*a*b*b

def pd(a,b,c):
    return max(abs(a),abs(b),abs(c))<1 and 1+2*a*b*c-a*a-b*b-c*c>0

n=0
vals=[F(-2,5),F(-1,4),F(0),F(1,5),F(2,5),F(1,2)]
for a,b,c in product(vals,repeat=3):
    if not pd(a,b,c):
        continue
    for s in [F(1,5),F(1,3),F(1,2),F(3,4),F(9,10)]:
        assert raw(a,b,c,s)==compact(a,b,c,s)
        n+=1
for rho in [F(-2,5),F(-1,4),F(1,5),F(2,5),F(3,4)]:
    assert pd(rho,rho,rho)
    for s in [F(1,5),F(1,2),F(3,4),F(9,10)]:
        expected=rho*rho*(2*(1-s)-4*rho*s+2*rho*rho*s+rho*rho*s*s)
        assert raw(rho,rho,rho,s)==expected
        if rho<0: assert expected>0
assert compact(F(1,2),F(1,2),F(1,2),F(1,4))>0
assert compact(F(1,2),F(1,2),F(1,2),F(3,4))<0
print('VERIFY_OK',n,'exact rational comparisons plus sharp sign witnesses')
