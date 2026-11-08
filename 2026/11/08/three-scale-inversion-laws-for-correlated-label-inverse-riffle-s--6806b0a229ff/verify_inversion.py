#!/usr/bin/env python3
"""Exact small-n checks and independent sample diagnostics for correlated binary-label inversions."""
from fractions import Fraction
from itertools import product
from math import sqrt, exp
from random import Random

EXACT=0
for n in range(2,11):
  for p in (Fraction(0),Fraction(1,3),Fraction(2,3),Fraction(9,10)):
    q=(1-p)/2
    mean=Fraction(0); pzero=Fraction(0); mass=Fraction(0)
    for labels in product((0,1),repeat=n):
      num_switch=sum(labels[i]!=labels[i-1] for i in range(1,n))
      prob=Fraction(1,2)*q**num_switch*(1-q)**(n-1-num_switch)
      spins=[2*z-1 for z in labels]
      inv=sum(labels[i]>labels[j] for i in range(n) for j in range(i+1,n))
      identity=Fraction(n*n,8)+Fraction(sum((n+1-2*(i+1))*spins[i] for i in range(n)),4)-Fraction(sum(spins)**2,8)
      assert inv==identity
      EXACT+=1
      mass+=prob;mean+=prob*inv
      if inv==0:pzero+=prob
    assert mass==1
    assert mean==Fraction(1,4)*sum((n-d)*(1-p**d) for d in range(1,n))
    assert pzero==(1-q)**(n-1)+Fraction(n-1,2)*q*(1-q)**(n-2)
    EXACT+=3
print('EXACT_ASSERTIONS',EXACT)

rng=Random(230193)
# Markov label construction: switch only between consecutive positions.
def sample(n,q):
 s=rng.randrange(2);ones_seen=0;inv=0
 for i in range(n):
  if i and rng.random()<q:s=1-s
  if s==0:inv+=ones_seen
  else:ones_seen+=1
 return inv

n=1000; p=Fraction(1,2);q=float((1-p)/2)
vals=[sample(n,q) for _ in range(1200)]
mu=sum((n-d)*(1-float(p)**d) for d in range(1,n))/4
sd=sqrt(n**3*(1+float(p))/(48*(1-float(p))))
z=[(v-mu)/sd for v in vals]
zm=sum(z)/len(z);zv=sum((x-zm)**2 for x in z)/len(z)
assert abs(zm)<.16 and abs(zv-1)<.20
print('CLT_DIAGNOSTIC',round(zm,3),round(zv,3),'n',n,'reps',len(vals))

n=1400; lam=2.4;q=lam/(2*n)
vals=[sample(n,q) for _ in range(3000)]
observed=sum(v==0 for v in vals)/len(vals)
pred=exp(-lam/2)*(1+lam/4)
assert abs(observed-pred)<.06
print('TELEGRAPH_ZERO_DIAGNOSTIC',round(observed,4),'theory',round(pred,4))

n=500; q=.00005
vals=[sample(n,q) for _ in range(15000)]
pnz=sum(v>0 for v in vals)/len(vals)
pred=n*q/2
assert abs(pnz-pred)<.012
print('RARE_NONZERO_DIAGNOSTIC',round(pnz,4),'firstorder',round(pred,4))
