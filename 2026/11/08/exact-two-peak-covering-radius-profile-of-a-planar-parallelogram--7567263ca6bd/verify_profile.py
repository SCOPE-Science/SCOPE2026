#!/usr/bin/env python3
"""Exact-rational checks for the planar covering-radius phase profile.
All mathematical proof is given separately; finite tests are corroboration.
No third-party packages required.
"""
from fractions import Fraction as F
from itertools import product
from random import Random

zero=F(0);one=F(1);half=F(1,2)

def const(t):
 return (F(2+t,4),F(7-3*t,4),F(3-t,4),F(4+3*t,4))

def critical(t):
 s=min(t,1-t)
 return max(F(14,14+s),F(6,7-3*s))

def interval(t,r,y):
 A,B,C,D=const(t)
 if abs(y)>r*A:return None
 return max(3*y-r*B,y-r*C,(y-r*D)/2),min(3*y+r*B,y+r*C,(y+r*D)/2)

def inside(x,y,t,r):
 A,B,C,D=const(t)
 return abs(y)<=r*A and abs(x-3*y)<=r*B and abs(x-y)<=r*C and abs(2*x-y)<=r*D

def covered(x,y,t,r):
 return any(inside(x-i,y-j,t,r) for i,j in product(range(-2,3),repeat=2))

def assert_slice_certificate(t):
 assert zero<=t<=half
 r=critical(t); A,B,C,D=const(t)
 y0=one-r*A
 yL=r*(B-C)/2
 assert half<=r*A<one
 assert zero<=y0<=half and zero<=yL<=half
 assert one<=r*D
 assert y0>=r*(D-2*C)
 assert yL>=r*(D-2*C)
 assert half>=r*(2*B-D)/5
 assert r*B>=F(3,2)
 # Every horizontal slice has a concave, symmetric width W(y).
 i0=interval(t,r,y0); iL=interval(t,r,yL)
 assert i0 and iL
 assert i0[1]-i0[0]>=1 and iL[1]-iL[0]>=1
 assert iL[1]-iL[0]==r*(1+t/4)
 for j in range(101):
  y=F(j,200)
  a=interval(t,r,y)
  assert a
  if y<=max(y0,yL):assert a[1]-a[0]>=1
  else:
   b=interval(t,r,y-1)
   assert b
   assert a[1]-b[0]>=1
   assert b[1]-a[0]>=0
  for k in range(101):
   x=F(k,100)
   assert covered(x,y,t,r)

samples=[F(0),F(1,48),F(1,24),F(1,12),F(1,6),F(1,4),F(7,24),F(3,10),F(1,3),F(2,5),F(9,20),F(1,2)]
for t in samples:
 assert_slice_certificate(t)
 r=critical(t)
 assert critical(1-t)==r
 if t==0:
  assert not covered(F(1,3),half,t,r-F(1,100000))
 elif t<=F(7,24):
  less=r-F(1,1000000)
  A,B,C,D=const(t)
  y0=1-less*A
  # Near a newly appearing row, row zero has a gap.
  y=y0-F(1,100000000)
  assert 0<y<half
  ii=interval(t,less,y)
  assert ii and ii[1]-ii[0]<1
  assert interval(t,less,y-1) is None
 else:
  assert not covered(zero,half,t,r-F(1,1000000))

# Symbolic algebra of the two sharp branches using exact rational sampling.
for t in [F(j,240) for j in range(121)]:
 r=critical(t)
 A,B,C,D=const(t)
 ra=F(14,14+t);rb=F(6,7-3*t)
 assert r==max(ra,rb)
 assert (ra>=rb)==(t<=F(7,24))
 assert F(1,1)/r==min(F(1)+t/14,F(7,6)-t/2)

# Independent randomly sampled lattice cover checks, with purely rational arithmetic.
rng=Random(20261101)
for i in range(15000):
 t=F(rng.randrange(1001),1000)
 x=F(rng.randrange(1001),1000)
 y=F(rng.randrange(1001),1000)
 assert covered(x,y,t,critical(t))
print('EXACT_RATIONAL_OK: 12 analytical-branch samples, 120,000 slice point checks, 15,000 independent rational torus points')
