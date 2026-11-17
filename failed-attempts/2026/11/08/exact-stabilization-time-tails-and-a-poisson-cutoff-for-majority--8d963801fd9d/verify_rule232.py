#!/usr/bin/env python3
"""Exact finite-ring majority absorption-time and forbidden-run transfer checks."""
from itertools import product
from collections import Counter

def majority(x):
 n=len(x)
 return tuple(int(x[(i-1)%n]+x[i]+x[(i+1)%n]>=2) for i in range(n))

def alt_at(x,i,t):
 n=len(x); r=t+1
 return all(x[(i+j)%n]!=x[(i+j+1)%n] for j in range(-r,r))

def exact_T(x):
 seen={};y=x;t=0
 while y not in seen:
  seen[y]=t;z=majority(y)
  if y==z or (majority(z)==y and y!=z):return t
  y=z;t+=1
 raise AssertionError('unexpected')

def tr_power(n,m,sign):
 # m=2t+3, transfer states h=0..m-2
 d=m-1;V=[[int(i==j) for j in range(d)] for i in range(d)]
 for _ in range(n):
  W=[[0]*d for _ in range(d)]
  for i in range(d):
   for k in range(d):
    v=V[i][k]
    if v:
     W[i][0]+=v
     if k<d-1:W[i][k+1]+=sign*v
  V=W
 return sum(V[i][i] for i in range(d))
for n in range(3,15):
 c=Counter()
 for x in product(range(2),repeat=n):
  T=exact_T(x);c[T]+=1
  y=x
  for t in range(min(n,5)):
   z=majority(y)
   assert all((y[i]!=z[i])==alt_at(x,i,t) for i in range(n)),(n,x,t)
   y=z
 for t in range(0,6):
  got=sum(v for k,v in c.items() if k<=t)
  m=2*t+3
  form=tr_power(n,m,1)+tr_power(n,m,-1)+(2 if n%2==0 else 0)
  assert got==form,(n,t,got,form)
 print(f'n={n:2d} states={2**n:6d} T_counts='+str(dict(sorted(c.items()))))
print('PASS exhaustive entry-time identities, flip rule, and parity transfer matrix for n=3..14, t=0..5')
