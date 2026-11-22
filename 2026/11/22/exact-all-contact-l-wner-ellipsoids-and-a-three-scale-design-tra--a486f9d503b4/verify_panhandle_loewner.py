#!/usr/bin/env python3
"""Standalone numerical and exhaustive checks for the panhandle Löwner certificate.
Run: python verify_panhandle_loewner.py (Python stdlib and NumPy only)."""
from itertools import combinations
from math import comb, sqrt
import numpy as np


def root(r, s, m):
    a=r*(s-r)
    b=2*r-s-1
    def deriv(w):
        return (s-1)*b/(a+b*w)+m/w-1/(1-w)
    lo,hi=1e-12,1-1e-12
    for _ in range(100):
        mid=(lo+hi)/2
        if deriv(mid)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2


def block_eigen(r,s,m,w):
    n=s+m
    ah=(r*(s-r)+(2*r-s-1)*w)/(s*(s-1))
    at=w/m
    ab=n*w*(1-w)/(s*m)
    return ah,at,ab

count=0
for r in range(3,6):
 for s in range(r,8):
  for m in range(2,6):
   if s+m>10:continue
   n=s+m;d=n-1
   w=root(r,s,m)
   assert 0<w<1
   ah,at,ab=block_eigen(r,s,m,w)
   assert min(ah,at,ab)>0
   v0=[];v1=[]
   for inds in combinations(range(n),r):
    x=np.zeros(n);x[list(inds)]=1
    if inds[-1]<s:v0.append(x)
    elif sum(j>=s for j in inds)==1:v1.append(x)
   assert len(v0)==comb(s,r) and len(v1)==m*comb(s,r-1)
   mu=(1-w)*np.mean(v0,axis=0)+w*np.mean(v1,axis=0)
   xx=(1-w)*(np.array(v0).T@np.array(v0))/len(v0)+w*(np.array(v1).T@np.array(v1))/len(v1)
   Sigma=xx-np.outer(mu,mu)
   spectrum=np.sort(np.linalg.eigvalsh(Sigma))
   theoretical=np.sort(np.array([0]+[ah]*(s-1)+[at]*(m-1)+[ab]))
   assert np.max(abs(spectrum-theoretical))<2e-12,(r,s,m,spectrum,theoretical)
   values, vectors = np.linalg.eigh(Sigma)
   pinv=(vectors*np.where(values>1e-9,1/np.maximum(values,1e-9),0))@vectors.T
   q0=np.array([ (v-mu)@pinv@(v-mu) for v in v0])
   q1=np.array([ (v-mu)@pinv@(v-mu) for v in v1])
   assert max(np.max(abs(q0-d)),np.max(abs(q1-d)))<1e-7,(r,s,m,q0,q1,d)
   for x in v0+v1:
    assert abs(sum(x)-r)<1e-12
   count+=1

r=3;s=900000
for ratio, expected in [(0.2,0.5),(0.5,1.0),(0.9,1.0)]:
 m=round(s*ratio)
 w=root(r,s,m)
 assert abs(w-expected)<0.02
# Sharp supercritical and critical scales for fixed rank.
r=3
for s in [20000,100000,1000000]:
 m=s
 w=root(r,s,m)
 assert abs(s*(1-w)-2)<0.2,(s,w)
 m=s//2
 w=root(r,s,m)
 assert abs(sqrt(s)*(1-w)-2/sqrt(3))<0.045,(s,w)
print(f'PANHANDLE_LOEWNER_PASS configurations={count} asymptotic_tests=9')
