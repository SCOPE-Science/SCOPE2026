#!/usr/bin/env python3
"""Exact finite-field spot checks for the characteristic-two Markoff pencil."""
from itertools import product

IRRED={1:0b11,2:0b111,3:0b1011,4:0b10011,5:0b100101,6:0b1000011}

def gf(m):
 q=1<<m; poly=IRRED[m];
 def mul(a,b):
  s=0
  while b:
   if b&1:s^=a
   a<<=1
   if a&q:a^=poly
   b>>=1
  return s&(q-1)
 t=[[mul(a,b) for b in range(q)] for a in range(q)]
 def trace(a):
  x=a;s=0
  for _ in range(m):
   s^=x;x=t[x][x]
  assert s in (0,1)
  return s
 return q,t,trace

def count(q,t,k):
 return sum((t[x][x]^t[y][y]^t[z][z]^t[t[x][y]][z])==k for x,y,z in product(range(q),repeat=3))

for m in range(1,7):
 q,t,tr=gf(m)
 sqrts={t[x][x]:x for x in range(q)}
 inv={0:None}
 for a in range(1,q):inv[a]=next(b for b in range(1,q) if t[a][b]==1)
 for k in range(q):
  if k==0: pred=q*q+1
  else: pred=q*q+1+q*(1 if tr(inv[sqrts[k]])==0 else -1)
  actual=count(q,t,k)
  assert actual==pred,(m,k,actual,pred)
 print(f'GF(2^{m}) all {q} levels exact verified; zero={q*q+1}; nonzero-level point-count classes={sorted(set(q*q+1+q*(1 if tr(inv[sqrts[k]])==0 else -1) for k in range(1,q)))}')
print('VERIFY_OK')
