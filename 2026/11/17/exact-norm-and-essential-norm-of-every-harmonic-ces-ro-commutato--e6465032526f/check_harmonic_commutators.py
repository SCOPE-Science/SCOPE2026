#!/usr/bin/env python3
"""Exact finite coefficient checks and numerical near-extremizers for harmonic Cesàro commutators.
The unbounded infinite-dimensional result requires the accompanying analytic proof.
"""
from fractions import Fraction as F
from math import factorial, log

def mult(A,B):
 n=len(A)
 return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def exact(n,rmax=5):
 H=[F(0)]
 for j in range(1,n+1): H.append(H[-1]+F(1,j))
 C=[[F(1,i+1) if j<=i else F(0) for j in range(n)] for i in range(n)]
 M=[[H[i+1] if i==j else F(0) for j in range(n)] for i in range(n)]
 powers=[C]
 for k in range(1,rmax+1): powers.append(mult(powers[-1],C))
 K=C
 for r in range(rmax+1):
  for i in range(n):
   for j in range(n):
    expected = (H[i+1]-H[j+1])**r/F(i+1) if j<=i else F(0)
    if r==0 and j<=i: expected=F(1,i+1)
    assert K[i][j]==expected, ('commutator coefficient',n,r,i,j)
    assert K[i][j] <= factorial(r)*powers[r][i][j], ('coefficient domination',n,r,i,j)
  if r<rmax:
   MK=mult(M,K); KM=mult(K,M)
   K=[[MK[i][j]-KM[i][j] for j in range(n)] for i in range(n)]

for n in range(1,23): exact(n)
print('EXACT_ITERATED_COMMUTATOR_AND_HARDY_POWER_DOMINATION_PASS n1_to22 orders0_to5')

# The summation asymptotics use bounded harmonic-number approximants;
# this is a numerical consistency check, not an infinite proof.
N=100000
H=[0.0]*(N+1)
for j in range(1,N+1): H[j]=H[j-1]+1.0/j
for p in (1.5,2.0,3.0):
 for r in (0,1,2,3):
  target=factorial(r)*(p/(p-1))**(r+1)
  # For very large r slow convergence due to logarithmic convolution tail.
  vals=[]
  for i in (1000,10000,100000):
   z=sum(((H[i]-H[j])**r if r else 1.0)*j**(-1.0/p) for j in range(1,i+1))
   vals.append((i**(1.0/p)/i)*z)
  assert vals[-1]<=target*(1+1e-9), ('near extremizer above sharp',p,r)
  assert vals[-1]>vals[0], ('failed monotone saturation',p,r,vals)
print('NEAR_EXTREMIZER_RIEMANN_SUM_CHECKS_PASS p1.5_2_3 orders0_to3 N1000_10000_100000')
print('ALL_HARMONIC_CESARO_CHECKS_PASS')
