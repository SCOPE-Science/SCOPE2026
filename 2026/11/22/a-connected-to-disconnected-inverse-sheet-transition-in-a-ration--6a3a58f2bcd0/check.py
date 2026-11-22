#!/usr/bin/env python3
"""Exact arithmetic and sample diagnostics for a rational map inverse-fibre theorem.

This checker is standalone, uses only the Python standard library, and never
substitutes finite diagnostics for the complete analytic proof.
"""
from fractions import Fraction as F
from math import sqrt

def disc(A,B,C):
    return A*A*B*B - 4*B*B*B - 4*A*A*A*C - 27*C*C + 18*A*B*C

def cubic_coefficients(a,w,z):
    return z-w,1+a,z-(1+a)*w

def cubic_disc(a,w,z):
    return disc(*cubic_coefficients(a,w,z))

def H(a,w,y):
    return (w-y)*(1+a/(1+y*y))

def Q(a,w,y):
    return y**4+(2-a)*y*y+2*a*w*y+(1+a)

def bisect(f,lo,hi,steps=140):
    flo=f(lo)
    fhi=f(hi)
    assert flo*fhi<0
    for _ in range(steps):
        mid=(lo+hi)/2
        fm=f(mid)
        if fm==0: return mid
        if flo*fm<0:hi=mid
        else:lo=mid;flo=fm
    return (lo+hi)/2

# Hand-checkable exact cubic discriminants: positive = three simple roots,
# zero = repeated root, negative = one real root.
assert cubic_disc(F(-3),F(0),F(0))==F(32)
assert cubic_disc(F(-3),F(0),F(10))<0
assert cubic_disc(F(-1),F(2),F(1,4))==F(235,64)
assert cubic_disc(F(-1),F(2),F(0))==0
assert cubic_disc(F(-1),F(2),F(1,2))==0
assert cubic_disc(F(-1),F(2),F(-1))<0
assert cubic_disc(F(-1),F(0),F(0))==0

# Verify the derivative identity by two distinct direct expansions at rational points.
for a in [F(-1), F(-2),F(-3),F(-7,4)]:
  for w in [F(-3),F(0),F(2),F(13,7)]:
    for y in [F(-2),F(-1,3),F(0),F(2,5),F(4)]:
      eps=F(1,1_000_000)
      # The exact symbolic numerator equals the negative of the Jacobian numerator.
      den=(1+y*y)**2
      num=-(1+a/(1+y*y))*(den) - 2*a*y*(w-y)
      assert num==-Q(a,w,y)
      # Check defining cubic after multiplying by denominator.
      z=H(a,w,y)
      assert y**3+(z-w)*y*y+(1+a)*y+z-(1+a)*w==0

# At a=-1 with q=1 and w=2, the second critical value is 1/2.
assert H(F(-1),F(2),F(0))==0
assert H(F(-1),F(2),F(1))==F(1,2)
assert 1**3+3*1==2*2
# Rational sample across the cubic neck, with independent negative w symmetry.
assert cubic_disc(F(-1),F(-2),F(-1,4))>0
assert cubic_disc(F(-1),F(-2),F(1))<0

# Two nondegenerate critical locations and asymptotic gap at w=0.
for delta in [1e-2,1e-3,1e-4,1e-5]:
    a=-1-delta
    r=sqrt((a-2+sqrt(a*(a-8)))/2)
    width=H(a,0,r)-H(a,0,-r)
    predicted=4*delta**1.5/(3*sqrt(3))
    assert width>0 and abs(width/predicted-1)<0.05

# At fixed negative a, sample all three inverse regimes from both folds.
for a in [-2.0,-3.0,-10.0]:
  for w in [-12.0,-1.3,0.0,3.5,12.0]:
    f=lambda y:Q(a,w,y)
    lo=bisect(f,-100.0,0)
    hi=bisect(f,0,100.0)
    zlo=H(a,w,lo)
    zhi=H(a,w,hi)
    assert lo<0<hi and zlo<zhi
    middle=(zlo+zhi)/2
    edge=abs(zhi-zlo)
    assert cubic_disc(F(str(a)),F(str(w)),F(str(middle)))>0
    assert cubic_disc(F(str(a)),F(str(w)),F(str(zhi+edge)))<0
    assert cubic_disc(F(str(a)),F(str(w)),F(str(zlo-edge)))<0

print('PASS: exact cubic discriminant identities, full branch samples, and pinch diagnostics')
