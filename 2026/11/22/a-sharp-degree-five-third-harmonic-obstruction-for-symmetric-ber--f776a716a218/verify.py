#!/usr/bin/env python3
"""Numerical cross-checks of analytic Bernstein/Fourier identities.
Requires numpy. Universal quantifiers are proved separately in RESULT.md.
"""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss
x,w=leggauss(160);u=(x+1)/2;w=w/2
count=0

def check(c,msg):
 global count
 if not c:raise AssertionError(msg)
 count+=1

def bern(n,j):return math.comb(n,j)*u**j*(1-u)**(n-j)
def fourier(P,k):return float(np.dot(w*P,np.cos(k*math.pi*u)))
def majority(n):return sum((1 if 2*j<n else(-1 if 2*j>n else 0))*bern(n,j) for j in range(n+1))
for n in range(5,32):
 check(fourier(majority(n),3)<-0.0001,f'negative majority {n}')
for r in range(3,20):
 check(np.max(np.abs(majority(2*r-1)-majority(2*r)))<2e-9, f'elevation {r}')
I5=80*(4-3*math.pi**2)/(81*math.pi**6)
check(abs(fourier(majority(5),3)-I5)<1e-12,'exact I5')
for n in range(5,25):
 eps=0.0001/n
 nodes=[j*eps if 2*j<n else (math.pi/2 if 2*j==n else math.pi-(n-j)*eps) for j in range(n+1)]
 check(all(nodes[j]<nodes[j+1] for j in range(n)),'strict nodes')
 P=sum(math.cos(nodes[j])*bern(n,j) for j in range(n+1))
 check(fourier(P,3)<-0.0001,'strict cluster')
 check(fourier(P,1)>0.01,'first mode')
for n in range(1,5):
 for s in range(1,10):
  nodes=[0.0]*(n+1)
  for j in range(n+1):
   if j==0:nodes[j]=0
   elif j==n:nodes[j]=math.pi
   elif 2*j==n:nodes[j]=math.pi/2
   elif 2*j<n:nodes[j]=math.pi*j/(n+1)*s/10
   else:nodes[j]=math.pi-nodes[n-j]
  P=sum(math.cos(nodes[j])*bern(n,j) for j in range(n+1))
  for k in range(0,28):check(fourier(P,k)>-1e-10,'low degree all modes')
for r in (20,40,80,120):
 # stable beta law: normalize directly at nodes
 rho=(u*(1-u))**(r-1)
 expectation=np.dot(w*rho,np.sin(3*math.pi*u))/np.dot(w,rho)
 exact=2*expectation/(3*math.pi)
 approx=-2/(3*math.pi)+3*math.pi/(4*(2*r+1))
 check(abs(exact-approx)<100/r**2,'asymptotic estimate')
print(count,'supplementary assertions passed')
