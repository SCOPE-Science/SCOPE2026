#!/usr/bin/env python3
"""Exact finite tests of spatially sampled first-feasible coverage probabilities.
These tests are diagnostics, not a proof of the infinite-limit statements.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
import math

def fibonacci_order_d(d,N):
    F=[1]*d
    for n in range(d,N+1): F.append(F[n-1]+F[n-d])
    return F

def weights(d,r,m):
    F=fibonacci_order_d(d,d-1+r+(m-1)*d)
    return [F[d-1+r+j*d] for j in range(m)]

def v2(n):
    assert n>0
    return (n&-n).bit_length()-1

def symbolic_law(ws):
    m=len(ws); prev=sum(ws[:-1]); last=ws[-1];
    gap=[ws[j]-sum(ws[:j]) for j in range(m)]
    assert min(gap)>0
    hist={Fraction(1,2):gap[m-1]}
    for t in range(1,2**(m-1)):
        k=Fraction(1,2)+Fraction(t,2**m)
        hist[k]=gap[v2(t)]
    assert sum(hist.values())==last
    return {k:Fraction(v,last) for k,v in hist.items()}

def brute_law(ws):
    m=len(ws); lo=sum(ws[:-1])+1; hi=lo+ws[-1]-1
    ss=[sum(w for j,w in enumerate(ws) if mask>>j &1) for mask in range(2**m)]
    assert len(set(ss))==2**m
    h=Counter()
    for delta in range(lo,hi+1):
        count=sum(s<delta for s in ss)
        h[Fraction(count,2**m)] += 1
    return {k:Fraction(v,ws[-1]) for k,v in h.items()}

def rho_d(d):
    lo,hi=1.0,2.0
    for _ in range(120):
        mid=(lo+hi)/2
        if mid**d-mid**(d-1)>1:hi=mid
        else:lo=mid
    return (lo+hi)/2

def limiting_law(d,J):
    Q=rho_d(d)**d
    L=1/(Q-1)
    z={Fraction(1,2):1-L}
    for j in range(1,J+1):
        for i in range(2**(j-1)):
            z[Fraction(1,2)+Fraction(2*i+1,2**(j+1))]=(1-L)*Q**(-j)
    return z

checks=0
for d in range(2,8):
 for r in range(d):
  for m in range(1,7 if d<=4 else 5):
   ws=weights(d,r,m)
   a=symbolic_law(ws);b=brute_law(ws)
   assert a==b,(d,r,m,a,b)
   checks+=1
   expected=Fraction(1,2)+Fraction(sum(ws[:-1]),4*ws[-1])
   assert sum(k*v for k,v in a.items())==expected,(d,r,m)
   checks+=1
   for j in range(m):
    assert ws[j]>sum(ws[:j])
    checks+=1
for d in [2,3,4,6]:
 Q=rho_d(d)**d
 assert Q>2
 L=1/(Q-1)
 for r in range(d):
  ws=weights(d,r,28)
  for j in range(1,8):
   t=2**(28-j-1)
   k=Fraction(1,2)+Fraction(t,2**28)
   p=Fraction(ws[28-j-1]-sum(ws[:28-j-1]),ws[-1])
   pred=(1-L)*Q**(-j)
   assert abs(float(p)-pred)<5e-6,(d,r,j,p,pred)
   checks+=1
print('PASS',checks,'exact finite assertions / asymptotic diagnostic comparisons')
# Exact doubling boundary: powers of two give precisely uniform discrete dyadic ranks.
for m in range(1,13):
    ws=[2**j for j in range(m)]
    h=symbolic_law(ws)
    assert len(h)==2**(m-1)
    assert set(h.values())=={Fraction(1,2**(m-1))}
    checks+=2
# Integer geometric ratio three: fixed dyadic atoms and the outer plateau.
for m in range(3,18):
    ws=[3**j for j in range(m)]
    h=symbolic_law(ws)
    assert h[Fraction(1,2)]==Fraction(3**(m-1)+1,2*3**(m-1))
    checks+=1
    for depth in range(1,min(m,7)):
        k=Fraction(1,2)+Fraction(1,2**(depth+1))
        v=h[k]
        assert v==Fraction(3**(m-depth-1)+1,2*3**(m-1))
        checks+=1
print('PASS cumulative',checks)
