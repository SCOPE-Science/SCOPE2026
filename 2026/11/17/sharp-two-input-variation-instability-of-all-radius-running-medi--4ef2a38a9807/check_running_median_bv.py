#!/usr/bin/env python3
"""Exact integer witnesses for the sharp two-input path-variation median bound."""
import random

def med(x,r):
 n=len(x)
 return [sorted(x[max(0,min(n-1,i+d))] for d in range(-r,r+1))[r] for i in range(n)]

def var(x):
 return sum(abs(b-a) for a,b in zip(x,x[1:]))

def test():
 for r in range(1,41):
  k=r+1
  x=[2*i for i in range(k)]+[2*i+1 for i in range(k)]
  h=[0]*k+[1]*k
  z=[100*u+v for u,v in zip(x,h)]
  assert med(x,r)==list(range(2*k)),(r,med(x,r))
  d=[b-100*a for a,b in zip(med(x,r),med(z,r))]
  assert d==[i%2 for i in range(2*k)],(r,d)
  assert var(d)==2*r+1
  for ext in (1,r+1):
   xe=x+[x[-1]]*ext;he=h+[1]*ext
   ze=[100*u+v for u,v in zip(xe,he)]
   dd=[b-100*a for a,b in zip(med(xe,r),med(ze,r))]
   assert var(dd)==2*r+1,(r,ext,dd)
 print('EXPLICIT_SHARP_ALL_RADII_1_TO_40_PASS')
 rng=random.Random(50317)
 for r in range(1,7):
  for n in range(2*r+2,2*r+12):
   for _ in range(150):
    x=[rng.uniform(-10,10) for i in range(n)]
    y=[rng.uniform(-10,10) for i in range(n)]
    assert var([a-b for a,b in zip(med(x,r),med(y,r))])<= (2*r+1)*var([a-b for a,b in zip(x,y)])+1e-8
 print('RANDOM_TWO_INPUT_PATH_VARIATION_STRESS_PASS')
 print('ALL_MEDIAN_VARIATION_TESTS_PASS')
if __name__=='__main__':test()
