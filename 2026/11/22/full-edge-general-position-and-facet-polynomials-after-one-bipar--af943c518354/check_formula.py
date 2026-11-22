#!/usr/bin/env python3
"""Independent exact combinatorial coefficient calculator for a one-edge-deleted biclique.
Usage: python3 check_formula.py
"""
from math import comb
from collections import Counter

def mul(p,q):
    out=Counter()
    for a,i in p.items():
        for b,j in q.items():out[a+b]+=i*j
    return out

def form(m,n):
    r,s=m-1,n-1
    P=Counter();F=Counter()
    for a in range(s+1):
      for b in range(r+1):
        coeff=comb(s,a)*comb(r,b)
        for k in range(r*s-a*b+1):
          P[a+b+k]+=coeff*comb(r*s-a*b,k)
        if a>0 and b>0:
          F[r*s+a+b-a*b]+=coeff
    F[r*s+s]+=1
    F[r*s+r]+=1
    return P,F

for m,n in [(3,3),(3,4),(4,4),(4,5),(5,5),(6,8)]:
 p,f=form(m,n)
 E=m*n-1
 assert sum(p.values())<=2**E
 assert sum(f.values())==(2**(m-1)-1)*(2**(n-1)-1)+2
 mx=max(k for k,v in p.items() if v)
 assert mx==(m-1)*(n-1)+max(m-1,n-1)
 print(m,n,'edges',E,'feasible',sum(p.values()),'facet_total',sum(f.values()),'max',mx,'top-count',p[mx], 'facet',sorted(f.items()))
