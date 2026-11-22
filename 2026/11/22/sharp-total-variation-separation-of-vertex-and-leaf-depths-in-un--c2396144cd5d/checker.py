#!/usr/bin/env python3
"""Finite enumeration and rational-law verification for recursive-tree leaf depths."""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product
from math import factorial, sqrt, log, pi

checks=0

def ck(condition, message):
 global checks
 checks+=1
 if not condition: raise AssertionError(message)

def conv(a, b):
 c=[F(0) for _ in range(len(a)+len(b)-1)]
 for i,x in enumerate(a):
  for j,y in enumerate(b): c[i+j]+=x*y
 return c

def law_S(n):
 p=[F(1)]
 for j in range(3,n+1):p=conv(p,[F(j-1,j),F(1,j)])
 return p

def all_trees(n):
 for parents in product(*(range(1,j) for j in range(2,n+1))):
  pa=[0,0]+list(parents); depths=[0]*(n+1); children=[0]*(n+1)
  for j in range(2,n+1):
   depths[j]=depths[pa[j]]+1; children[pa[j]]+=1
  leaves=[j for j in range(1,n+1) if children[j]==0]
  yield depths,leaves

for n in range(2,9):
 p=law_S(n); depth_vertex=conv(p,[F(1,2),F(1,2)]); depth_bias=[F(0)]+p
 times=factorial(n-1)
 en_v=defaultdict(F); en_leaf=defaultdict(F); en_true=defaultdict(F)
 el=F(0); ell=F(0); ell2=F(0)
 for depths,leaves in all_trees(n):
  el+=F(len(leaves),times)
  ell+=F(len(leaves),times);ell2+=F(len(leaves)**2,times)
  for j in range(1,n+1):en_v[depths[j]]+=F(1,n*times)
  for j in leaves:
   en_leaf[depths[j]]+=F(2,n*times)
   en_true[depths[j]]+=F(1,len(leaves)*times)
 ck(el==F(n,2),f'expected leaves n={n}')
 if n>=3:ck(ell2-ell**2==F(n,12),f'variance leaves n={n}')
 for k in range(n):
  ck(en_v[k]==(depth_vertex[k] if k<len(depth_vertex) else 0),f'vertex pgf n={n},k={k}')
  ck(en_leaf[k]==(depth_bias[k] if k<len(depth_bias) else 0),f'leaf pgf n={n},k={k}')
 tv=sum(abs(en_v[k]-en_leaf[k]) for k in range(n))/2
 ck(tv==max(p)/2,f'TV identity n={n}')
 tvtrue=sum(abs(en_v[k]-en_true[k]) for k in range(n))/2
 if n>=3:ck(abs(tvtrue-tv)**2<=F(1,12*n),f'TV comparison n={n}')
 print('n',n,'trees',times,'exact-TV',tv,'real-leaf-TV',tvtrue)

for n in (100,1000,10000):
 p=[1.]
 for j in range(3,n+1):
  q=1/j; z=[0.]* (len(p)+1)
  for k,v in enumerate(p): z[k]+=v*(1-q);z[k+1]+=v*q
  p=z
 v=sum((1/j)*(1-1/j) for j in range(3,n+1))
 ratio=max(p)*sqrt(2*pi*v)
 ck(.80<ratio<1.25,f'local CLT n={n}')
 print('n',n,'mode/local-CLT ratio',round(ratio,8))
print('PASS',checks,'assertions')
