"""Exact rational checks for centered-Hilbert stability of cyclic maximum filters."""
from fractions import Fraction
from itertools import permutations
import random

def variance_num(z):
    n=len(z);return n*sum(t*t for t in z)-sum(z)**2

def windows(n,w):return [tuple((i+j)%n for j in range(w)) for i in range(n)]

def filt(z,W):return [max(z[j] for j in B) for B in W]

def selection(z,W):return [max(B,key=lambda j:z[j]) for B in W]

def bound(n,w):return Fraction(w if 2*w<=n else 2*w*(n-w),1 if 2*w<=n else n)

c_perm=0
for n in range(2,8):
 for w in range(1,n+1):
  W=windows(n,w);target=bound(n,w)
  for xs in permutations(range(n)):
   s=selection(xs,W)
   counts=[s.count(i) for i in range(n)]
   assert max(counts)==w
   for p in range(n):
    for q in range(p+1,n):
     h=[0]*n;h[p]=1;h[q]=-1
     z=[h[j] for j in s]
     assert variance_num(z)<=target*variance_num(h),(n,w,xs,p,q,variance_num(z),target)
     c_perm+=1
print('EXACT_CHAMBER_TWO_SITE_DIRECTION_TESTS',c_perm)

rng=random.Random(20261109)
c_pair=0;c_attain=0
for n in range(2,20):
 for w in range(1,n+1):
  W=windows(n,w);C=bound(n,w)
  for _ in range(28):
   x=[Fraction(rng.randint(-15,15),rng.randint(1,5)) for _ in range(n)]
   y=[Fraction(rng.randint(-15,15),rng.randint(1,5)) for _ in range(n)]
   h=[u-v for u,v in zip(x,y)]
   z=[u-v for u,v in zip(filt(x,W),filt(y,W))]
   assert variance_num(z)<=C*variance_num(h),(n,w,x,y)
   c_pair+=1
  if w==n:continue
  p=0;q=w if 2*w<=n else n-w
  x=[Fraction(i,10*n+1) for i in range(n)]
  x[p]=Fraction(4);x[q]=Fraction(2)
  h=[Fraction(0)]*n;h[p]=1;h[q]=-1
  y=[u+v*Fraction(1,4) for u,v in zip(x,h)]
  z=[u-v for u,v in zip(filt(y,W),filt(x,W))]
  assert variance_num(z)==C*variance_num([u-v for u,v in zip(y,x)]),(n,w,p,q,z,C)
  c_attain+=1
print('EXACT_ARBITRARY_INPUT_PAIR_TESTS',c_pair)
print('EXACT_ATTAINED_TWO_PEAK_WITNESSES',c_attain)
print('ALL_CYCLIC_MAX_CENTERED_HILBERT_CHECKS_PASSED')
