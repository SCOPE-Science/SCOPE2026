#!/usr/bin/env python3
"""Finite rational verification of bottleneck identities; not an infinite proof.
No third-party packages. Reproduce: python3 verify.py
"""
from fractions import Fraction
from itertools import product
from math import exp, log, pi, sqrt, ceil, isclose

tests=0

def assert_eq(a,b):
 global tests
 assert a==b,(a,b)
 tests+=1

def assert_near(a,b,tol):
 global tests
 assert abs(a-b)<=tol,(a,b,tol)
 tests+=1

def b(r,m,j):
 x=(1-r)**m
 for h in range(1,j+1):x*=(1-r**h)**m
 return x

def original_finite_event(r,m,j,T):
 x=((1-r)/(1-r**(j+1)))**m
 for t in range(j+2,T+1):
  x*=((1-r**(t-j-1))/(1-r**t))**m
 return x

def stationary_truncated(r,m,k):
 return b(r,m,k-1)

def local_stationary_probability(r,m,k,indices):
 # multiply probabilities of the simultaneous lag restrictions at each time
 req={}
 for j in indices:
  for h in range(1,k+1):
   t=j+h
   bound=1 if h==1 else h-1
   req[t]=min(req.get(t,bound),bound)
 result=Fraction(1)
 for threshold in req.values(): result*=(1-r**threshold)**m
 return result

def enumeration_original(r,m,j,T):
 # Exact enumeration of all independent conditional parent choices up to horizon T.
 choices=[]
 for t in range(1,T+1):
  dist=[(l,(1-r)*r**(l-1)/(1-r**t)) for l in range(1,t+1)]
  for _ in range(m):choices.append((t,dist))
 s=Fraction(0)
 for draws in product(*[dist for _,dist in choices]):
  event=True
  probability=Fraction(1)
  for (t,_),(lag,prob) in zip(choices,draws):
   probability*=prob
   if t==j+1 and lag!=1:event=False
   if t>=j+2 and lag>t-j-1:event=False
  if event:s+=probability
 return s

for r in [Fraction(1,2),Fraction(2,3),Fraction(3,4)]:
 for m in [1,2]:
  for k in range(1,10):
   assert_eq(stationary_truncated(r,m,k),local_stationary_probability(r,m,k,[0]))
   for d in range(1,k):
    assert_eq(local_stationary_probability(r,m,k,[0,d]), b(r,m,k-1)*b(r,m,d-1))
  for j in range(4):
   for T in range(j+1,8):
    assert_eq(original_finite_event(r,m,j,T),
     ((1-r)/(1-r**(j+1)))**m *
       (Fraction(1) if T==j+1 else
        __import__('functools').reduce(lambda x,t:x*((1-r**(t-j-1))/(1-r**t))**m,range(j+2,T+1),Fraction(1))))
for r in [Fraction(1,2),Fraction(2,3)]:
 for m in [1,2]:
  for j,T in [(0,3),(1,4),(2,4)]:
   assert_eq(enumeration_original(r,m,j,T),original_finite_event(r,m,j,T))

for beta in [.3,.2,.13,.1,.07]:
 r=exp(-beta)
 L=ceil(12/beta) # high accuracy q-product
 log_product=sum(log(-__import__('math').expm1(-beta*h)) for h in range(1,L+1))
 actual_log=log(-__import__('math').expm1(-beta))+log_product
 asymptotic_log=.5*log(2*pi*beta)-pi*pi/(6*beta)
 assert_near(actual_log,asymptotic_log-11*beta/24,beta*beta/5+.002)
 # exact early-cluster sum is negligible compared with finite-window K-dependence budget
 K=ceil(beta**-2)
 bvals=[(-__import__('math').expm1(-beta))]
 s=bvals[0]
 for d in range(1,K):
  s*=(-__import__('math').expm1(-beta*d))
  bvals.append(s)
 assert sum(bvals)<=10*beta
 tests+=1
print('CHECKS_OK',tests)
