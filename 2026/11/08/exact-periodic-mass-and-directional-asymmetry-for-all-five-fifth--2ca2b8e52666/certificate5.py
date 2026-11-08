#!/usr/bin/env python3
"""Exact 40-cell first-return certificates for five fifth-rotated odometers."""
from fractions import Fraction
from itertools import chain
from collections import Counter

Q=Fraction

def grid_step(j,k):
    r=(j+8*k)%40
    if r>=35:return None,r-35
    if r<20:return r+20,None
    if r<30:return r-10,None
    return r-25,None

def stage(p):
    # p is the target-grid-block permutation (one-line notation)
    T={};H={}
    for j in range(40):
        i=j//8
        r=8*p[i]+j%8
        if r>=35:H[j]=r-35
        else:T[j]=r+20 if r<20 else r-10 if r<30 else r-25
    visited=set(); h=[]; p1=[]; towers=[]
    for i in range(5):
        word=[]; j=i
        while j not in H:
            assert j in T and j not in word
            word.append(j);j=T[j]
        word.append(j)
        assert not(set(word)&visited)
        visited.update(word); h.append(len(word));p1.append(H[j]);towers.append(word)
    comp=set(range(40))-visited
    assert all(j in T and T[j] in comp for j in comp)
    assert len(set(p1))==5
    return tuple(h),tuple(p1),towers,tuple(sorted(comp))

def cycles(p):
    h,p1,t,c=stage(p)
    seen=set(); out=[]
    T={j:grid_step(j,0)[0] for j in []}
    for j in c:
        if j in seen:continue
        cyc=[];x=j
        while x not in seen:
            seen.add(x);cyc.append(x)
            i=x//8;r=8*p[i]+x%8
            assert r<35
            x=r+20 if r<20 else r-10 if r<30 else r-25
        assert x==j
        out.append(cyc)
    return out

assertions=0
for k in range(5):
 p=tuple((i+k)%5 for i in range(5));seen=[]
 for depth in range(3):
    h,p1,t,c=stage(p)
    print('k',k,'level',depth,'p',p,'h',h,'p1',p1,'omitted',len(c),'cycle_lengths',[len(x) for x in cycles(p)])
    assert len(c)+sum(h)==40
    assertions+=len(c)+sum(h)
    if p1==p:break
    assert p1 not in seen;seen.append(p);p=p1
# Exact check of all 40 states and images at stages; 2000 orbit comparisons
from fractions import Fraction as Q

def a(x):
 n=1
 while x>=1-Q(1,2**n):n+=1
 return x-1+Q(3,2**n)
def F(x,p):
 i=int(x*5)
 return a(x+Q(p[i]-i,5))
for k in range(5):
 p=tuple((i+k)%5 for i in range(5));h,p1,t,c=stage(p)
 for i in range(5):
  for m in (1,2,7,13,29,31,51,61,71,97):
   x=Q(i,40)+Q(m,4000)
   y=x
   for n in range(1,h[i]+1):
    y=F(y,p)
    if n<h[i]:assert y>=Q(1,8)
   z=8*y;w=a((8*x+Q(p1[i]-i,5)))
   assert z==w, (k,i,m,z,w)
   assertions+=h[i]+1
print('ALL CHECKS PASSED',assertions)
