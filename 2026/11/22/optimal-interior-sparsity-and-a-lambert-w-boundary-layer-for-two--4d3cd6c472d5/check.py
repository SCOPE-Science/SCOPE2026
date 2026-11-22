#!/usr/bin/env python3
"""Independent finite checks for the two-column sparse-sign sketch theorem.
Run: python3 check.py (Python 3.9+, standard library only).
All analytic all-m results are proved separately; this script only checks finite cases.
"""
from fractions import Fraction as Q
from itertools import product
from math import exp, log

STATES = [(x,y) for x in (-1,0,1) for y in (-1,0,1)]

def point_probability(point,p):
    q=1-p
    result=Q(1)
    for x in point:
        result *= q if x==0 else p/2
    return result

def is_rank_deficient(rows):
    for x,y in rows:
        for u,v in rows:
            if x*v-y*u !=0:
                return False
    return True

def closed_failure(m,p):
    a=1-p
    b=1-2*p+Q(3,2)*p*p
    return 2*a**m+2*b**m-3*a**(2*m)

def exhaustive_failure(m,p):
    probs={state:point_probability(state,p) for state in STATES}
    out=Q(0)
    for rows in product(STATES,repeat=m):
        if is_rank_deficient(rows):
            weight=Q(1)
            for state in rows:weight*=probs[state]
            out+=weight
    return out

checks=0
for m in (2,3,4):
    for p in (Q(1,4),Q(1,2),Q(2,3),Q(3,4),Q(1)):
        actual=exhaustive_failure(m,p)
        expected=closed_failure(m,p)
        assert actual==expected,(m,p,actual,expected)
        checks+=1

# Derivative equation and unique optimizer: numerical localization only.
# Existence and uniqueness, as well as asymptotics, are proven analytically.
def deriv_core(m,p):
    a=1-p
    b=1-2*p+1.5*p*p
    return -a**(m-1)+(3*p-2)*b**(m-1)+3*a**(2*m-1)

def optimum(m):
    left=2/3
    right=1-1e-12
    assert deriv_core(m,left)<0 and deriv_core(m,right)>0
    for _ in range(90):
        mid=(left+right)/2
        if deriv_core(m,mid)>0:right=mid
        else:left=mid
    return (left+right)/2

for m in range(2,161):
    p=optimum(m)
    assert 2/3 < p <1
    assert deriv_core(m,p-1e-5)<0
    assert deriv_core(m,p+1e-5)>0
    checks+=3

assert abs(optimum(2)-(2/3)**.5)<1e-11
checks+=1
for m in (20,50,100,160):
    p=optimum(m)
    # W(m) is uniquely solved by w e^w=m.
    lo,hi=0.,log(m)+1
    for _ in range(100):
        w=(lo+hi)/2
        if w*exp(w)>m:hi=w
        else:lo=w
    w=(lo+hi)/2
    assert abs(3*m*(p-2/3)-w) < 0.20
    checks+=1
print('PASS',checks,'exact-enumeration/numeric checks; sample p_2=',optimum(2))
