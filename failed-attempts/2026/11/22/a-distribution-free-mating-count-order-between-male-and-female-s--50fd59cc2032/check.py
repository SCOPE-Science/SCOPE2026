from fractions import Fraction as F
from math import comb
import random
rng=random.Random(314159)
checks=0
for n in range(1,10):
 for case in range(200):
  atoms=sorted({F(rng.randrange(1,10),10) for _ in range(rng.randint(1,4))})
  weights=[rng.randint(1,7) for _ in atoms];Z=sum(weights)
  # atom u=e^{-alpha T} in (0,1], arbitrary finite trap lifetimes
  L=lambda j:sum((F(w,Z)*u**j for w,u in zip(weights,atoms)),F(0))
  q=L(n)
  pm=[F(comb(n,k))*sum((F((-1)**j*comb(k,j))*L(n-k+j)**n for j in range(k+1)),F(0)) for k in range(n+1)]
  pf=[F(comb(n,k))*(1-q)**k*q**(n-k) for k in range(n+1)]
  assert sum(pm)==sum(pf)==1
  assert pm[0]==pf[0]
  checks+=2
  for k in range(1,n+1):
   d=sum(pm[k:],F(0))-sum(pf[k:],F(0))
   assert d>=0
   if k>1 and len(atoms)>1:assert d>0
   else:
    if k==1:assert d==0
   checks+=1
  if n>1 and len(atoms)>1 and q<F(1):
   assert pm[1]<pf[1]
   checks+=1
print('EXACT ASSERTIONS:',checks)
