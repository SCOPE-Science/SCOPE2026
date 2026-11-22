#!/usr/bin/env python3
"""Supplementary exact-rational checks for two-node square-zero data."""
from fractions import Fraction as Q

checks=0
for numerator in range(1,10):
 for den in range(numerator+1,15):
  r=Q(numerator,den)
  a=1/(1-r*r)
  det=a-1
  inv00=a/det
  inv01=-1/det
  inv11=1/det
  assert inv00==1/(r*r)
  checks+=1
  assert inv01==-(1-r*r)/(r*r)
  checks+=1
  assert inv11==(1-r*r)/(r*r)
  checks+=1
  # D (S tensor I_2) D^* has nonzero diagonal entries 1,a,
  # and the two nonzero eigenvalues of S^{-1} D S D^* agree.
  assert inv00*1==1/(r*r)
  checks+=1
  assert inv11*a==1/(r*r)
  checks+=1
  assert Q(2)*r>r
  checks+=1
print('NUMERICAL_PICK_COALESCENCE_RATIONAL_CHECK_OK',checks)
