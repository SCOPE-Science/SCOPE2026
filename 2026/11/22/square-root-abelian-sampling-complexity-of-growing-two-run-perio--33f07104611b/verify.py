#!/usr/bin/env python3
"""Independent finite checks of cyclic-window bounds and construction."""
from math import isqrt
from itertools import combinations

def complexity(c,h):
    q=len(c)
    return len({sum(c[(i+j)%q] for j in range(h)) for i in range(q)})

def witness(h,k,q):
    t=isqrt(2*h*k)
    r=t-h+1
    assert k>=h and q>=t+1 and r>=1
    c=[0]*q
    for i in range(t): c[i]=i//h
    c[t]+=k-sum(c)
    return c,r

num=0
for h in range(1,10):
 for k in range(h,190):
  t=isqrt(2*h*k)
  for q in (t+1,t+2,t+7):
   c,r=witness(h,k,q)
   assert min(c)>=0 and sum(c)==k
   sums=[sum(c[i+j] for j in range(h)) for i in range(r)]
   assert sums==list(range(r)),(h,k,q,sums)
   P=complexity(c,h)
   upper=(1+isqrt(1+8*h*k))//2
   assert r<=P<=upper and P<=q and P<=k+1
   num+=1
print('constructive_cases',num)

# Exhaustive independent small-case maximum over all residue-multiplicity vectors.
count=0
for q in range(2,8):
 for h in range(1,q):
  for k in range(1,9):
   best=0
   for separators in combinations(range(k+q-1),q-1):
    c=[separators[0]]+[separators[i]-separators[i-1]-1 for i in range(1,q-1)]+[k+q-2-separators[-1]]
    best=max(best,complexity(c,h))
   upper=(1+isqrt(1+8*h*k))//2
   assert best<=min(q,k+1,upper),(q,h,k,best)
   t=isqrt(2*h*k)
   if k>=h and q>=t+1:
    c,r=witness(h,k,q)
    assert best>=r,(q,h,k,best,r)
   count+=1
print('exhaustive_maxima',count)
