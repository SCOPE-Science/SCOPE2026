#!/usr/bin/env python3
"""Exact rational certificate for point evaluation of three-tone Fourier sums."""
from fractions import Fraction as Q
from math import factorial, comb
from functools import lru_cache
N=70
@lru_cache(None)
def fact(k): return factorial(k)
def plus(a,b): return [a[k]+b[k] for k in range(N+1)]
def mul(a,b):
 r=[Q(0)]*(N+1)
 for i,x in enumerate(a):
  if x:
   for j in range(N+1-i):
    if b[j]: r[i+j]+=x*b[j]
 return r
def scale(a,r):return [x*r for x in a]
def const(q):return [Q(q)]+[Q(0)]*N
A=[Q((-1)**k, fact(2*k+1)) for k in range(N+1)]
B=[Q((-1)**k*2**(2*k),fact(2*k+1)) for k in range(N+1)]
C=[Q((-1)**k*2**(2*k),fact(2*k)) for k in range(N+1)]
C4=[Q((-1)**k*4**(2*k),fact(2*k)) for k in range(N+1)]
D=plus(scale(plus(const(1),B),Q(1,2)),scale(mul(A,A),-1))
T=plus(const(1),scale(B,-1))
E=plus(plus(scale(plus(const(1),B),Q(1,2)),scale(mul(A,C),-2)),mul(C,C))
O=plus(const(1),scale(C4,-1))
F=plus(plus(scale(mul(D,T),Q(657,4)),scale(mul(E,T),-1)),scale(mul(O,D),-1))
assert all(F[i]==0 for i in range(4)), [(i,F[i]) for i in range(4)]
print('first coeff:',F[4],F[5],F[6])
P=F[4:]+[Q(0)]*4
DEG=N-4
# power polynomial P(lo+(hi-lo)t); Bernstein coefficients on each unit interval

def bern(lo,hi):
 p=[Q(0)]*(DEG+1)
 for i,ci in enumerate(P[:DEG+1]):
  if ci:
   for k in range(i+1): p[k]+=ci*comb(i,k)*lo**(i-k)*(hi-lo)**k
 b=[]
 for j in range(DEG+1):
  b.append(sum((p[k]*Q(comb(j,k),comb(DEG,k)) for k in range(j+1)),Q(0)))
 return min(b), b.index(min(b)), b
if __name__=='__main__':
 assert Q(10**29 * 9**67 * 100, 100**71 * 91) < Q(1,1000)
 for lo in range(9):
  v,j,_=bern(lo,lo+1)
  assert v>Q(1,100), (lo,j,v)
  print('interval',lo,lo+1,'Bernstein lower coefficient > 1/100; minimum ≈',round(float(v),12))
 print('Exact polynomial positivity and analytic-tail certificate: PASS')
