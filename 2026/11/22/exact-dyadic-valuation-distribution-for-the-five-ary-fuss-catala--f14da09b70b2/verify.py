#!/usr/bin/env python3
"""Exact integer-polynomial certificate for binary carry valuation distribution."""
import math
from collections import Counter
STATES=[(x,y,c) for x in (0,1) for y in (0,1) for c in (0,1)]
INDEX={s:i for i,s in enumerate(STATES)}
D_TERMS=[[4, 5, 1], [4, 4, -1], [3, 4, 1], [3, 3, -1], [2, 4, -1], [2, 3, 1], [1, 5, 1], [1, 4, 1], [1, 3, 1], [1, 1, -1], [0, 4, -1], [0, 3, -1], [0, 1, -1], [0, 0, 1]]
Q_TERMS=[[[2, 3, 1], [1, 4, -1], [1, 3, -2], [1, 2, -2], [1, 1, -1], [0, 3, 1], [0, 2, 2], [0, 1, 1], [0, 0, 1]], [[4, 4, -1], [4, 2, 1], [3, 4, 1], [3, 3, -1], [2, 3, 1], [2, 2, -1], [1, 4, -1], [1, 3, -1], [1, 2, -1], [0, 3, 1], [0, 2, 1], [0, 0, 1]], [[4, 4, -1], [4, 3, 1], [3, 3, -1], [3, 2, 1], [1, 2, -1], [1, 1, -1], [0, 1, 1], [0, 0, 1]], [[3, 4, -1], [3, 1, 1], [1, 1, -1], [0, 0, 1]], [[4, 4, -1], [4, 2, 1], [3, 4, 1], [3, 3, -1], [2, 3, 1], [2, 2, -1], [1, 4, -1], [1, 3, -1], [1, 2, -1], [0, 3, 1], [0, 2, 1], [0, 0, 1]], [[5, 4, -1], [5, 3, 1], [4, 3, -1], [4, 2, 1], [2, 2, -1], [2, 1, -1], [1, 1, 1], [1, 0, 1]], [[3, 4, -1], [3, 1, 1], [1, 1, -1], [0, 0, 1]], [[3, 3, 1], [3, 2, -1], [2, 4, -1], [2, 3, -1], [2, 2, 1], [2, 0, 1]]]
def poly(ts):
 p={}
 for a,b,c in ts:
  p[a,b]=p.get((a,b),0)+c
 return {k:v for k,v in p.items() if v}
def add(*ps):
 out={}
 for p in ps:
  for k,v in p.items():out[k]=out.get(k,0)+v
 return {k:v for k,v in out.items() if v}
def neg(p):return {k:-v for k,v in p.items()}
def mul(p,q):
 out={}
 for (a,b),v in p.items():
  for (c,d),w in q.items():out[a+c,b+d]=out.get((a+c,b+d),0)+v*w
 return {k:v for k,v in out.items() if v}
def U(p):return {(a+1,b):v for (a,b),v in p.items()}
def Z(p):return {(a,b+1):v for (a,b),v in p.items()}
D=poly(D_TERMS);Q=[poly(x) for x in Q_TERMS]
assert D.get((0,0))==1
assert len(Q)==8
# Exact certificate: (I-zM)Q = D*t, an identity of integer polynomials.
T=[]
for state in STATES:
 x,y,c=state; v=0
 for _ in range(4):
  cc=(x+c)//2;v+=cc;x,y,c=y,0,cc
 assert (x,y,c)==(0,0,0)
 T.append(v)
for i,(x,y,c) in enumerate(STATES):
 left=Q[i]
 for b in (0,1):
  cc=(b+x+c)//2
  q=Q[INDEX[y,b,cc]]
  if cc:q=U(q)
  left=add(left,neg(Z(q)))
 assert left=={(a+T[i],bb):coef for (a,bb),coef in D.items()}, (i,left)
# From the certificate the first component Q[0]/D is the exact GF.
# Check finite block histograms using three independently programmed methods.
hist=[1]
vec=[{0:1}]+[{} for i in range(7)]
for L in range(16):
 actual=Counter(2*n.bit_count()-(5*n).bit_count() for n in range(1<<L))
 predicted=Counter()
 for state,d in zip(STATES,vec):
  x,y,c=state;extra=0
  for _ in range(4):
   cc=(x+c)//2;extra+=cc;x,y,c=y,0,cc
  for v,count in d.items():predicted[v+extra]+=count
 assert actual==predicted,(L,actual,predicted)
 if L<=6:
  for n in range(1<<L):
   value=math.comb(5*n,n)//(4*n+1)
   v=0
   while value%2==0 and value>0:v+=1;value//=2
   assert v==2*n.bit_count()-(5*n).bit_count(),n
 nv=[{} for _ in STATES]
 for (x,y,c),d in zip(STATES,vec):
  for b in (0,1):
   cc=(b+x+c)//2; j=INDEX[y,b,cc]
   for v,cnt in d.items():nv[j][v+cc]=nv[j].get(v+cc,0)+cnt
 vec=nv
print('VERIFY_OK symbolic_polynomial_certificate=yes finite_histogram_lengths=16 factorial_checks=127')
