#!/usr/bin/env python3
"""Exact Picard-pairing verification of the twenty-two negative curves."""
from itertools import combinations
from collections import Counter
pairs = list(combinations(range(6), 2))
# coordinates [H,E0,...,E5]; H^2=1, E_i^2=-1
C=[]
for i in range(6):C.append((0,)+tuple(int(k==i) for k in range(6)))
for i,j in pairs:C.append((1,)+tuple(-int(k in (i,j)) for k in range(6)))
C.append((2,)+(-1,)*6)
def dot(a,b):return a[0]*b[0]-sum(a[i]*b[i] for i in range(1,7))
assert [dot(c,c) for c in C] == [-1]*21+[-2]
for i in range(22):
 for j in range(i+1,22):
  d=dot(C[i],C[j])
  if i<6 and j<6: want=0
  elif i<6 and j<21: want=int(i in pairs[j-6])
  elif i<6 and j==21: want=1
  elif i<21 and j<21: want=int(not set(pairs[i-6]) & set(pairs[j-6]))
  else: want=0
  assert d==want,(i,j,d,want)
# A necessary condition for a principal submatrix to be negative definite:
# all of its 2x2 principal minors must be positive. For (-1) curves it
# excludes any positive intersection. For the conic root, the Schur
# complement against k selected exceptional curves is exactly -2+k.
assert dot(C[21],C[0])==1
print('PICARD_PAIRINGS_OK: 22 negative curves; 6 exceptionals, 15 secants, 1 conic root')
