#!/usr/bin/env python3
"""Exhaustive verifier of the chromatic-plus-one forced-colouring profile.
Colors are integers 0,...,r; -1 is initially blank.
"""
from itertools import product
from math import factorial, comb
from collections import Counter

def mul(a,b):
 c=Counter()
 for i,ai in a.items():
  for j,bj in b.items(): c[i+j]+=ai*bj
 return c

def formula(profile):
 r=len(profile);n=sum(profile);lf=factorial(r+1);p=Counter({n:lf})
 for j,nj in enumerate(profile):
  if nj<2:continue
  others=[i for i in range(r) if i!=j]
  for skipped in [None]+others:
   q=Counter({nj:lf//2*((2**nj)-2)})
   for i in others:
    if i!=skipped:
     q=mul(q,Counter({k:comb(profile[i],k) for k in range(1,profile[i]+1)}))
   for degree,coeff in q.items():p[degree]+=coeff
 return +p

def brute(profile):
 r=len(profile);n=sum(profile);palette=r+1
 parts=tuple(k for k,s in enumerate(profile) for _ in range(s))
 neigh=tuple(tuple(w for w in range(n) if parts[w]!=parts[v]) for v in range(n))
 res=Counter()
 for initial in product(range(-1,palette),repeat=n):
  if any(initial[v]==initial[w]>=0 for v in range(n) for w in neigh[v]): continue
  state=list(initial)
  while True:
   todo=[]
   for v in range(n):
    if state[v]>=0:continue
    used={state[w] for w in neigh[v] if state[w]>=0}
    if len(used)==palette-1:
     todo.append((v,next(c for c in range(palette) if c not in used)))
   if not todo:break
   for v,c in todo:state[v]=c
  if all(c>=0 for c in state) and all(state[v]!=state[w] for v in range(n) for w in neigh[v]):
   res[sum(c>=0 for c in initial)]+=1
 return +res

def main():
 profiles=[(1,1,1),(2,1,1),(2,2,1),(3,1,1),(2,2,2),(3,2,1),(4,1,1),
           (2,2,3),(3,3,1),(1,1,1,1),(2,1,1,1),(2,2,1,1),(3,1,1,1),(1,1,1,1,1)]
 for p in profiles:
  a,b=brute(p),formula(p)
  if a!=b:raise AssertionError((p,a,b))
  print('PROFILE_OK',p,dict(sorted(a.items())))
 print('ALL_PROFILES_OK',len(profiles))
if __name__=='__main__':main()
