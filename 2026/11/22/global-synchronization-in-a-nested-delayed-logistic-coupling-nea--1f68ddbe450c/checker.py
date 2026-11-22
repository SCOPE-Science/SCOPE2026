#!/usr/bin/env python3
"""Exact rational certificate for the delayed nested-logistic convergence theorem.
Run: python delayed_compositional_checker.py
"""
from fractions import Fraction as F
from random import Random

A = F(399, 100)
E = 4-A
D = 10**6

def g(x):
    u=x*(1-x)
    return u*(1-u)

def mag4(x):
    return 4*(2*x-1)*(1-2*x+2*x*x)

# Endpoint and scalar coercivity inequalities.
assert A*F(3,4)*F(13,16) > F(12,5)
assert A*F(39,256)==F(15561,25600)>F(3,5)
assert 4*g(F(1,2))==F(3,4)
assert g(F(1,4))==g(F(3,4))==F(39,256)

# Outward-rounded, exact-rational trapping intervals. The entries are
# numerator bounds with a fixed denominator of one million.
expected=[(607851,750000),
          (607851,726196),
          (635606,726196),
          (635606,711870),
          (650531,711870),
          (650531,702628)]
lo,hi = map(lambda n:F(n,D),expected[0])
for j in range(5):
    assert (lo,hi)==tuple(F(n,D) for n in expected[j])
    assert F(1,2)<lo<=hi<=F(3,4)
    ll=A*g(hi)
    uu=4*g(lo)
    newlo=F((ll.numerator*D)//ll.denominator,D)
    newhi=F(-((-uu.numerator*D)//uu.denominator),D)
    lo,hi=newlo,newhi
    assert (lo,hi)==tuple(F(n,D) for n in expected[j+1])
assert F(13,20)<lo<=hi<F(71,100)

# Invariance of the eventual four-dimensional trap.
left,right=F(13,20),F(71,100)
assert left < A*g(right)
assert 4*g(left) < right
assert F(1,2)<left<right<F(3,4)

# Universal (two-step) contraction of the full delayed state map.
assert mag4(right)==F(123522,125000) # 0.988176
assert E*F(3,16)==F(3,1600)
L=mag4(right)+E*F(3,16)
assert L==F(990051,10**6)<F(991,1000)<1

# The unique positive diagonal fixed point is bracketed uniformly.
def fixed_diff(x,a):
    return (a+(4-a)*x)*g(x)-x
assert fixed_diff(left,A)>0
assert fixed_diff(left,4)>0
assert fixed_diff(right,A)<0
assert fixed_diff(right,4)<0

def step(a,oldx,x,oldy,y):
    nx=(a+(4-a)*min(oldx,x))*g(y)
    ny=(a+(4-a)*min(oldy,y))*g(x)
    return x,nx,y,ny

# Supplementary approximate dynamical sanity tests (not the proof).
rng=Random(195701)
for a in (F(399,100),F(799,200),F(4,1)):
    for _ in range(120):
        s=[F(rng.randrange(1,10000),10000) for j in range(4)]
        for i in range(80):
            s=step(float(a),*map(float,s))
        assert abs(s[1]-s[3])<0.00001, (a,s)
        assert 0.65<s[1]<0.71
print('PASS: 5 exact interval transitions, invariance, quantitative two-step contraction, and 360 orbit checks')
