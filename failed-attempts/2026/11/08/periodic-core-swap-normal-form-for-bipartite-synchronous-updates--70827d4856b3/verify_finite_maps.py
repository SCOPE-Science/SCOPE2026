#!/usr/bin/env python3
"""Exhaustive identity verification for finite off-diagonal maps."""
from itertools import product
from math import gcd

def iterate(fn, z, t):
    for _ in range(t): z=fn(z)
    return z

cases=0; identities=0
for nx in range(1,4):
 for ny in range(1,4):
  for f in product(range(nx), repeat=ny):
   for g in product(range(ny), repeat=nx):
    h=lambda x:f[g[x]]
    F=lambda xy:(f[xy[1]],g[xy[0]])
    for n in range(1,13):
     directly=sum(iterate(F,(x,y),n)==(x,y) for x in range(nx) for y in range(ny))
     if n%2:
      predicted=sum(iterate(h,x,n)==x for x in range(nx))
     else:
      predicted=sum(iterate(h,x,n//2)==x for x in range(nx))**2
     assert directly==predicted, (nx,ny,f,g,n,directly,predicted)
     identities+=1
    cases+=1
print(f'FINITE_MAPS_OK cases={cases} iterate_identities={identities} size_bounds_XY=1..3 iterates=1..12')
