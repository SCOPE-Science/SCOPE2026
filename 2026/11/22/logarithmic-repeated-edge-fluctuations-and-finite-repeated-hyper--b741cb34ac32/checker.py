from itertools import combinations, product
from fractions import Fraction
from math import comb,log
import random

def exhaustive_conditional_checks():
  checks=0
  p=Fraction(2,5)
  for k in (2,3,4):
    for N in range(k, k+4):
      choices=list(combinations(range(N),k))
      # Histories are multisets, with designated previously drawn hyperedges.
      for inds in product(range(min(4,len(choices))), repeat=3):
        old=[choices[j] for j in inds]
        exact=sum(p*0 +(1-p)*Fraction(tuple(e) in old,len(choices)) for e in choices)
        expected=(1-p)*Fraction(len(set(old)),comb(N,k))
        assert exact==expected
        checks+=1
  return checks

def simulate(p=.45,k=2,n=30000,seed=914):
  rng=random.Random(seed)
  N=k; old=set(); count=0
  for t in range(n):
    if rng.random()<p: N+=1
    else:
      e=tuple(sorted(rng.sample(range(N),k)))
      if e in old: count+=1
      else: old.add(e)
  return count, 2*(1-p)**2/p**2*log(n)

if __name__=='__main__':
 n=exhaustive_conditional_checks()
 print('conditional probability exact enumeration checks:',n)
 for k in (2,3,4):
  for i in range(3):
   v,c=simulate(k=k,seed=91+i*11,n=50000)
   print('k',k,'sample',i,'duplicate count',v,'k=2 asymptotic centering',round(c,3) if k==2 else 'n/a')
