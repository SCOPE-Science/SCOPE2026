#!/usr/bin/env python3
"""Finite exact checks for a sparse-string read-count limit theorem.
Only standard-library Python is required.
"""
from collections import Counter
from itertools import combinations
from math import comb, sqrt, exp, factorial
import random

def counts(word, k):
    return Counter(tuple(word[i:i+k]) for i in range(len(word)-k+1))

def variables(positions, k):
    return [sum(positions[i+1]-positions[i] == d for i in range(len(positions)-1))
            for d in range(1,k)]

def good(positions, n, k):
    return bool(positions) and positions[0]>=k-1 and positions[-1]<=n-k and all(positions[i+2]-positions[i]>=k for i in range(len(positions)-2))

def expected_profile(n, r, k, x):
    c=Counter()
    for d in range(1,k):
        for j in range(k-d):
            mer=(0,)*j+(1,)+(0,)*(d-1)+(1,)+(0,)*(k-d-1-j)
            c[mer]+=x[d-1]
    for j in range(k):
        single = r - sum(x[d-1]*((j<=k-d-1)+(j>=d)) for d in range(1,k))
        c[(0,)*j+(1,)+(0,)*(k-1-j)]=single
    c[(0,)*k]=n-k+1-k*r+sum((k-d)*x[d-1] for d in range(1,k))
    return c

valid=0
for n in range(3,16):
 for k in range(2,min(6,n+1)):
  for r in range(1,min(n,6)+1):
   for p in combinations(range(n),r):
    if good(p,n,k):
     word=[0]*n
     for i in p:word[i]=1
     x=variables(p,k)
     assert counts(word,k)==+expected_profile(n,r,k,x), (n,k,p,x,counts(word,k),expected_profile(n,r,k,x))
     valid+=1
print('good-word literal multiset exact checks:',valid)

# Exact count for the much stronger completely separated event.
checks=0
for n in range(4,30):
 for k in range(2,min(n,6)+1):
  for r in range(1,min(n,5)+1):
   if n-(r+1)*(k-1)<r: continue
   # all boundary and internal zeros >=k-1: positions of ones at least k apart
   observed=sum(1 for p in combinations(range(n),r) if p[0]>=k-1 and p[-1]<=n-k and all(p[i+1]-p[i]>=k for i in range(r-1)))
   expected=comb(n-(r+1)*(k-1),r)
   assert observed==expected,(n,k,r,observed,expected)
   checks+=1
print('separated-family exact enumeration checks:',checks)

# Independent simulation: multivariate-Poisson means/covariances in the sqrt(n) regime.
seed=140319
random.seed(seed)
n=2500; r=50; k=4; samples=15000
vectors=[]; good_count=0
for _ in range(samples):
 p=sorted(random.sample(range(n),r));vectors.append(variables(p,k));good_count+=good(p,n,k)
means=[sum(x[j] for x in vectors)/samples for j in range(k-1)]
covs=[[sum((x[i]-means[i])*(x[j]-means[j]) for x in vectors)/samples for j in range(k-1)] for i in range(k-1)]
lam=r*r/n
print('Monte Carlo n,r,k,samples,seed:',n,r,k,samples,seed)
print('Poisson target mean:',lam)
print('Observed means:',*[round(x,5) for x in means])
print('Observed covariance:',[[round(z,5) for z in row] for row in covs])
print('Good event frequency:',good_count/samples)
print('The simulation is illustrative, not a certificate of convergence.')
