#!/usr/bin/env python3
"""Finite corroboration of exact affine identities and selected attracting cycles."""
from fractions import Fraction as Q
import math

def B(x,l,u): return 1+l-u*x

def C(x,l,u): return 1+l+l*l-l*u*x

def formal(l,u,k):
    U=u**(2*k);h=1+l;star=h/(1+u)
    return (U*(1+l+l*l)+(1-U)*star)/(1+l*u*U)

checks=0
for ell in (Q(1,10),Q(1,4),Q(2,5)):
 for k in range(1,9):
  for u in (Q(11,10),Q(6,5),Q(5,4)):
   x=formal(ell,u,k);z=C(x,ell,u)
   for _ in range(2*k):z=B(z,ell,u)
   assert z==x
   U=u**(2*k)
   assert B(x,ell,u)==(1+ell-u*U*(u-ell))/((1+u)*(1+ell*u*U))
   checks+=2

def bisection(ell,k):
    n=2*k+1
    lo,hi=1.,3.
    for _ in range(130):
        mid=(lo+hi)/2
        if mid**n*(mid-ell)<1+ell: lo=mid
        else: hi=mid
    return (lo+hi)/2

for ell in (.12,.3,.4,math.sqrt(2)-1,.5,.7):
 for k in (1,2,4,8,16):
  n=2*k+1;ub=ell**(-1/n);root=bisection(ell,k)
  criterion=ub>2*ell+ell*ell
  if criterion:
    assert root<ub
    u=root+min((ub-root)*.001,1e-5)
    x=formal(ell,u,k)
    inputs=[C(x,ell,u)]
    for _ in range(2*k-1): inputs.append(B(inputs[-1],ell,u))
    assert x>0 and min(inputs)>0 and B(x,ell,u)<0
    r=-2/min([x]+inputs); d=ell*r+u
    curx,cury=x,0.
    marks=[]
    for _ in range(4*k+3):
      if curx>0:
        marks.append('R');curx,cury=r*curx+cury+1,-d*curx
      else:
        marks.append('L');curx,cury=ell*curx+cury+1,0.
    assert ''.join(marks)=='RLL'+'RL'*(2*k)
    assert abs(curx-x)<1e-6 and abs(cury)<1e-6
    assert 0<ell*u**n<1
    checks+=6
  else: assert root>=ub-1e-12
  checks+=1
print('PASS:',checks,'finite supporting assertions')
