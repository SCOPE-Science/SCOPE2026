#!/usr/bin/env python3
"""Exact finite checks for the reflected-simplex mixed-volume formulas.
These tests supplement, and do not replace, the all-dimensional proof.
"""
from fractions import Fraction
from math import comb

def poly_mul(a,b):
 c=[Fraction(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):
   c[i+j]+=x*y
 return c

def poly_pow(a,n):
 v=[Fraction(1)]
 for _ in range(n):v=poly_mul(v,a)
 return v

def h(n,p):
 return sum((Fraction(comb(n,2*j)*comb(2*j,j))*p**j for j in range(n//2+1)),Fraction(0))

def f(n,a,b):
 return sum((Fraction(comb(n,j)**2)*a**(n-j)*b**j for j in range(n+1)),Fraction(0))

def coefficient_profile(n,p):
 # a+b=1 and ab=p, via the polynomial H identity.
 # polynomial for (s+u)^n H(p+(1-4p)su/(s+u)^2)
 out=[Fraction(0)]*(n+1)
 for j in range(n//2+1):
  cj=Fraction(comb(n,2*j)*comb(2*j,j))
  for l in range(j+1):
   weight=cj*comb(j,l)*p**(j-l)*(1-4*p)**l
   for k in range(l,n-l+1):
    out[k]+=weight*comb(n-2*l,k-l)
 den=h(n,p)
 return [v/den for v in out]

def direct_profile(n,t):
 a,b=1-t,t
 ans=[Fraction(0)]*(n+1)
 for j in range(n+1):
  # F(a*s+b*u,b*s+a*u)
  one=poly_pow([a,b],n-j)
  two=poly_pow([b,a],j)
  rr=poly_mul(one,two)
  for k,z in enumerate(rr):
   ans[k]+=comb(n,j)**2*z
 return [z/f(n,a,b) for z in ans]

checks=0
for n in range(2,17):
 for t in [Fraction(0),Fraction(1,20),Fraction(1,9),Fraction(1,4),Fraction(2,5),Fraction(1,2)]:
  p=t*(1-t)
  assert h(n,p)==f(n,t,1-t)
  A=coefficient_profile(n,p)
  B=direct_profile(n,t)
  assert A==B
  assert A[0]==1 and A[-1]==1
  for k in range(1,n):
   v=A[k]/comb(n,k)
   assert 1<=v<=comb(n,k)
   if t==0: assert v==comb(n,k)
   elif t==Fraction(1,2):assert v==1
   else:assert 1<v<comb(n,k)
   checks+=1
  checks+=3
 for ts in [[Fraction(0),Fraction(1,20),Fraction(1,9),Fraction(1,4),Fraction(2,5),Fraction(1,2)]]:
  for a,b in zip(ts,ts[1:]):
   P=coefficient_profile(n,a*(1-a))
   Q=coefficient_profile(n,b*(1-b))
   for k in range(1,n):
    assert P[k]>Q[k]
    checks+=1
 h0=h(n,Fraction(1,4))
 h1=sum((Fraction(j*comb(n,2*j)*comb(2*j,j))*Fraction(1,4)**(j-1) for j in range(1,n//2+1)),Fraction(0))
 assert h1/h0==Fraction(2*n*(n-1),2*n-1)
 checks+=1
print('PASS',checks)
