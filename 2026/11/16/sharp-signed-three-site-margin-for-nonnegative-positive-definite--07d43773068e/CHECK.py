#!/usr/bin/env python3
"""Exact rational algebra certificate for a three-site Fourier correlation margin."""
from fractions import Fraction as Q

def mul(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):c[i+j]+=u*v
    return c

def add(a,b):
    z=[Q(0)]*max(len(a),len(b))
    for i,v in enumerate(a):z[i]+=v
    for i,v in enumerate(b):z[i]+=v
    return z

u=[Q(0),Q(1)]
T2=[Q(-1),Q(0),Q(2)]
T3=[Q(0),Q(-3),Q(0),Q(4)]
left=add(add([Q(5,4)],[-2*v for v in u]),add(T2,[-v/Q(4) for v in T3]))
right=[v/Q(4) for v in mul([Q(1),Q(-1)],mul([Q(-1),Q(2)],[Q(-1),Q(2)]))]
assert left==right,(left,right)
f1=Q(3,4);f2=Q(1,4);f3=Q(0)
energy=3-4*f1+2*f2
assert energy==Q(1,2)
assert Q(5,4)-2*f1+f2-f3/Q(4)==0
mu0=Q(1,2);mu_plus=Q(1,4);mu_minus=Q(1,4)
assert mu0+mu_plus+mu_minus==1
assert mu0-(mu_plus+mu_minus)==0
assert energy-Q(1,2)==Q(0)
print('CHECK_OK polynomial_factorization=1 exact_extremizer=1 spectral_equal_mass=1')
