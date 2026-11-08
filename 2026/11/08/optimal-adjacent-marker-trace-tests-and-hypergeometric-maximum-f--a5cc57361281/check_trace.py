#!/usr/bin/env python3
"""Exact finite checks for adjacent-marker deletion-trace testing formulas.
All computations of probabilities and total variation use fractions.Fraction.
"""
from fractions import Fraction
from math import comb, sqrt, isclose
from collections import defaultdict
from itertools import product

def binpmf(m,k,p):
    return Fraction(comb(m,k))*p**k*(1-p)**(m-k) if 0 <= k <= m else Fraction(0)

def mass_by_masks(n,i,p):
    source=[0]*n
    source[i]=1  # zero-based index
    out=defaultdict(Fraction)
    for mask in range(1 << n):
        word=tuple(source[j] for j in range(n) if (mask>>j)&1)
        k=mask.bit_count()
        out[word]+=p**k*(1-p)**(n-k)
    assert sum(out.values())==1
    return out

def tv(P,Q):
    return sum((abs(P.get(x,0)-Q.get(x,0)) for x in P.keys()|Q.keys()), Fraction())/2

def sample_mean_formula(n,i,p):
    a,b=i,n-i
    E=sum((binpmf(a,u,p)*binpmf(b,v,p)*abs(Fraction(u,a)-Fraction(v,b))
         for u in range(a+1) for v in range(b+1)), Fraction())
    return p*E/(2*(1-p))

def hypergeom_max_formula(n,i,p):
    a,b=i-1,n-i-1
    m=n-2
    return p*p*sum((p**t*(1-p)**(m-t)*max(comb(a,u)*comb(b,t-u)
        for u in range(max(0,t-b),min(a,t)+1))
        for t in range(m+1)),Fraction())

def central_formula(r,p):
    a=r-1
    return p*p*sum((binpmf(a,k,p)*binpmf(a,k+delta,p)
                   for k in range(a+1) for delta in (0,1)), Fraction())

def central_affinity(r,p):
    a=r-1
    return float(1-p)+float(p)*sum(sqrt(float(binpmf(a,k,p)*binpmf(a+1,k,p)))
                                    for k in range(a+2))**2

ct=0
for n in range(2,10):
 for i in range(1,n):
  for p in (Fraction(1,4),Fraction(1,2),Fraction(2,3)):
   P=mass_by_masks(n,i-1,p)
   Q=mass_by_masks(n,i,p)
   exact=tv(P,Q)
   assert exact==hypergeom_max_formula(n,i,p),(n,i,p,'hypergeom')
   # Check the rate-independent likelihood ordering on every positive-mass trace.
   for w in P.keys()|Q.keys():
    if 1 not in w:
     assert P[w]==Q[w]
     continue
    u=w.index(1)
    v=len(w)-u-1
    sign=(i*v-(n-i)*u)
    observed=P[w]-Q[w]
    assert (observed>0)-(observed<0)==(sign>0)-(sign<0),(n,i,p,w)
   assert exact==sample_mean_formula(n,i,p),(n,i,p,exact,sample_mean_formula(n,i,p))
   if n%2==0 and i==n//2:
    assert exact==central_formula(n//2,p),(n,i,p,exact,central_formula(n//2,p))
    affinity=sum(sqrt(float(P.get(w,0)*Q.get(w,0))) for w in P.keys()|Q.keys())
    assert isclose(affinity,central_affinity(n//2,p),abs_tol=1e-13)
    if p==Fraction(1,2):
     assert exact==Fraction(comb(n-1,n//2),2**n)
   ct+=1
print('EXACT_MASK_TESTS',ct,'PASS')
for p in (Fraction(1,4),Fraction(1,2),Fraction(2,3)):
 print('p',str(p),'r=10,40,100 central TV times sqrt(r), H2 times r')
 for r in (10,40,100):
  t=float(central_formula(r,p))
  h2=1-central_affinity(r,p)
  print(r,round(t*sqrt(r),9),round(h2*r,9))
 print('limit_tv',float(p)**1.5/sqrt(3.141592653589793*(1-float(p))))
 print('limit_h2',float(p)**2/(4*(1-float(p))))
