#!/usr/bin/env python3
"""Exact integer sign and independent finite-spin checks for signed Ising C7."""
from math import comb
from fractions import Fraction
from itertools import product
A = (2,6,8)
B = (3,3,15,16)
EDGES = ((0,1,2),(1,2,6),(2,3,8),(3,4,16),(4,5,15),(5,6,3),(6,0,-3))

def mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b): c[i+j]+=x*y
 return c

def sub(a,b):
 c=[0]*max(len(a),len(b))
 for i,x in enumerate(a):c[i]+=x
 for i,x in enumerate(b):c[i]-=x
 return c

def pp(seq, parity):
 v=[1]
 for n in seq:
  f=[comb(n,k) if k%2==parity else 0 for k in range(n+1)]
  v=mul(v,f)
 return v

# Cross-multiplied numerator: Aprod - Bprod in tanh(beta)=x.
F=sub(mul(pp(A,1),pp(B,0)),mul(pp(B,1),pp(A,0)))
assert F[:3]==[0,0,0]
while F and F[-1]==0: F.pop()
G=F[3:]
assert G[-1]!=0
# Q(y)=(1+y)^deg G G(y/(1+y)), y>0, using exact binomial sums.
d=len(G)-1
Q=[0]*(d+1)
for i,c in enumerate(G):
 for j in range(d-i+1):Q[i+j]+=c*comb(d-i,j)
s=[1 if x>0 else -1 for x in Q if x]
variations=sum(s[i]!=s[i+1] for i in range(len(s)-1))
assert variations==3,variations

def tm(n,x):
 return sum(comb(n,k)*x**k for k in range(1,n+1,2))/sum(comb(n,k)*x**k for k in range(0,n+1,2))

def evalpoly(p,x):
 r=0
 for c in reversed(p):r=r*x+c
 return r

samples=(Fraction(1,20),Fraction(1,10),Fraction(1,6),Fraction(1,3))
expected=(1,-1,1,-1)
assert sum(J for _,_,J in EDGES)==47
for x,want in zip(samples,expected):
 u=Fraction(1)
 v=Fraction(1)
 for n in A:u*=tm(n,x)
 for n in B:v*=tm(n,x)
 C=(u-v)/(1-u*v)
 sign=1 if C>0 else -1
 assert sign==want and (evalpoly(F,x)>0)==(want>0)
 z=Fraction(0);zcor=Fraction(0)
 q=(1+x)/(1-x)
 for ss in product((-1,1),repeat=7):
  e=sum(J*ss[i]*ss[j] for i,j,J in EDGES)
  assert (e-47)%2==0
  weight=q**((e-47)//2)
  z+=weight
  zcor+=weight*ss[0]*ss[3]
 assert zcor/z==C, (x,zcor/z,C)
print('SEVEN_CYCLE_THREE_REVERSALS_CERTIFIED',variations,len(samples),'exact enumerations')
