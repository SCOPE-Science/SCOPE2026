#!/usr/bin/env python3
"""Independent priority-permutation cross-check on all subcubic graphs <= 6 vertices."""
from itertools import permutations
from collections import Counter
from fractions import Fraction
from verify_census import extend

def priority_law(a):
 n=len(a);closed=[a[v]|(1<<v) for v in range(n)]
 freq=Counter()
 for order in permutations(range(n)):
  blocked=0;k=0
  for v in order:
   if not (blocked>>v&1):k+=1;blocked|=closed[v]
  freq[k]+=1
 return {k:Fraction(t,sum(freq.values())) for k,t in freq.items()}

def recurrence_law(a):
 n=len(a)
 from functools import lru_cache
 @lru_cache(None)
 def f(mask):
  if mask==0:return {0:Fraction(1)}
  result=Counter()
  c=mask.bit_count()
  for v in range(n):
   if (mask>>v)&1:
    for k,p in f(mask & ~(a[v]|(1<<v))).items():result[k+1]+=p/c
  return dict(result)
 return f((1<<n)-1)

def main():
 graphs=[(0,)];tested=0
 for n in range(1,7):
  if n>1:graphs,_=extend(graphs)
  for g in graphs:
   assert priority_law(g)==recurrence_law(g),(n,g)
   tested+=1
  print(f'n={n}, graphs={len(graphs)}, direct-order comparison passed')
 print('total graph checks',tested)
if __name__=='__main__':main()
