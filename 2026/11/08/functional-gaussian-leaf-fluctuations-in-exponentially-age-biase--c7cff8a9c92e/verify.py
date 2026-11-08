#!/usr/bin/env python3
"""Standalone finite checks for the leaf-number fluctuation theorem.
Uses exact rational arithmetic on finite growth trees and separate infinite-volume
truncations. Numerical computations are diagnostics, not infinite proofs.
"""
from fractions import Fraction as Q
from itertools import product
from math import exp

checks=0

def ck(a,b,label):
 global checks
 checks+=1
 assert a==b,(label,a,b)

# Exact law for finite exponentially preferred recursive tree on 0..n.
def parent_options(n,r):
 return [(j,(1-r)*r**(n-1-j)/(1-r**n)) for j in range(n)]

def theoretical(n,r):
 opts={t:dict(parent_options(t,r)) for t in range(1,n+1)}
 one=[]
 for i in range(n+1):
  pr=Q(1)
  for t in range(i+1,n+1):pr*=1-opts[t][i]
  one.append(pr)
 two={}
 for i in range(n+1):
  for j in range(i+1,n+1):
   pr=Q(1)
   for t in range(i+1,n+1):
    pr*=1-opts[t][i]-(opts[t][j] if t>j else 0)
   two[i,j]=pr
 return one,two

for r in [Q(1,3),Q(1,2),Q(2,3)]:
 for n in range(1,7):
  P=parent_options
  ex=[Q(0)]*(n+1)
  pair={(i,j):Q(0) for i in range(n+1) for j in range(i+1,n+1)}
  total=Q(0)
  total2=Q(0)
  choices=[parent_options(t,r) for t in range(1,n+1)]
  for trial in product(*choices):
   parents=[p for p,_ in trial]
   prob=Q(1)
   for _,w in trial:prob*=w
   children=set(parents)
   leaves=[int(i not in children) for i in range(n+1)]
   k=sum(leaves)
   total+=prob*k
   total2+=prob*k*k
   for i in range(n+1):ex[i]+=prob*leaves[i]
   for i in range(n+1):
    for j in range(i+1,n+1):pair[i,j]+=prob*leaves[i]*leaves[j]
  one,two=theoretical(n,r)
  ck(sum(ex),total,'sum leaves')
  for i in range(n+1):ck(ex[i],one[i],f'leaf n={n} i={i}')
  for ij,v in pair.items():ck(v,two[ij],f'pair n={n} ij={ij}')
  ck(total2,sum(one)+2*sum(two.values()),f'second moment n={n}')

# Truncated stationary q-products and covariance, including strict negativity.
for r in [.08,.2,.5,.75,.93]:
 p=lambda h:(1-r)*r**(h-1)
 mu=1.
 for h in range(1,2200):mu*=1-p(h)
 var=mu*(1-mu)
 for d in range(1,700):
  ratio=1.
  for h in range(1,500):
   x=p(h); y=p(h+d)
   ratio*=1-x*y/((1-x)*(1-y))
  if p(1+d)>1e-13:
   ck(ratio < 1.0,True,'strict negative lag covariance')
  cov=mu*mu*(ratio-1)
  var+=2*cov
 ck(var>mu*(1-r)**2/(3*(1+r))-.000001,True,'positive lower bound')
 print('r,mu,var:',r,format(mu,'.9f'),format(var,'.9f'))

# Critical r -> 1 limit (bounded numerical confirmation, not proof).
for r in [.97,.99,.995]:
 p=lambda h:(1-r)*r**(h-1)
 mu=1.
 for h in range(1,5000):mu*=1-p(h)
 v=mu*(1-mu)
 for d in range(1,3500):
  ratio=1.
  for h in range(1,3500):
   x=p(h);y=p(h+d)
   ratio*=1-x*y/((1-x)*(1-y))
  v+=2*mu*mu*(ratio-1)
 target=exp(-1)-2*exp(-2)
 ck(abs(v-target)<.025,True,'r->1 variance diagnostic')
 print('r-limit',r,format(v,'.9f'),'target',format(target,'.9f'))
print('PASS exact/floating assertions',checks)
