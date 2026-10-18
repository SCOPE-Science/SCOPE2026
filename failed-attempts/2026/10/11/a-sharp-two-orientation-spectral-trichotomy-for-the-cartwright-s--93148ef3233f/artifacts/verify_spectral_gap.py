#!/usr/bin/env python3
from math import sqrt

def a_plus(m):
    return 2 - 3*m*m - m*m*m

def a_minus(m):
    return 2 - 3*m*m + m*m*m

def rho(a):
    aa=abs(a)
    if aa <= 2:
        return 1.0
    return (aa + sqrt(aa*aa-4))/2

both_unit=[]
one_unit=[]
both_off=[]
for m in range(-1000,1001):
    u1=abs(a_plus(m)) <= 2
    u2=abs(a_minus(m)) <= 2
    if u1 and u2:
        both_unit.append(m)
    elif u1 or u2:
        one_unit.append(m)
    else:
        both_off.append(m)
assert both_unit == [-1,0,1]
assert one_unit == [-3,-2,2,3]
assert all(min(abs(a_plus(m)),abs(a_minus(m))) >= 18 for m in both_off)
assert min(abs(a_plus(-4)),abs(a_minus(-4))) == 18
assert min(abs(a_plus(4)),abs(a_minus(4))) == 18
assert abs(rho(18) - (9+4*sqrt(5))) < 1e-12
print('VERIFY_OK both_unit=-1,0,1 exactly_one=-3,-2,2,3 gap=9+4sqrt(5) equality=-4,4')
