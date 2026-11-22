#!/usr/bin/env python3
"""Exact-rational finite checks for the two-mode residual-difference dynamics."""
from fractions import Fraction as F

def dot(u,v): return sum((x*y for x,y in zip(u,v)),F(0))
def diag(v,L): return (L*v[0], v[1])
def subtract(u,v): return tuple(x-y for x,y in zip(u,v))
def normsq(v): return dot(v,v)

n=0
for L in [F(2),F(3),F(5,2),F(7,3)]:
  for a,b in [(F(1),F(1)),(F(2),F(3)),(F(3),F(-2)),(F(1),F(1,2)),(F(1),L), (F(1),F(1)/L)]:
    r=(a,b)
    ratios=[L*L*(r[0]/r[1])**2]
    B=diag(r,L)
    alpha=normsq(r)/dot(r,B)
    r1=subtract(r,tuple(alpha*v for v in B))
    assert r1[0] and r1[1]
    e0=(a/b)**2
    assert (r1[0]/r1[1])**2 == 1/e0
    n+=2
    ratios.append(L*L*(r1[0]/r1[1])**2)
    assert ratios[0]*ratios[1]==L**4
    n+=1
    past,cur=r,r1
    for k in range(1,8):
      d=subtract(cur,past)
      alpha=normsq(d)/dot(d,diag(d,L))
      predicted=(1+ratios[k-1])/(1+L*ratios[k-1])
      assert alpha==predicted
      n+=1
      nxt=subtract(cur,tuple(alpha*v for v in diag(cur,L)))
      assert nxt[0] and nxt[1]
      ratio=L*L*(nxt[0]/nxt[1])**2
      assert ratio==ratios[k]/(ratios[k-1]**2)
      ratios.append(ratio)
      n+=2
      past,cur=cur,nxt
for L in [F(2),F(3),F(7,2)]:
  for v in [(F(1),F(0)),(F(0),F(1))]:
    alpha=normsq(v)/dot(v,diag(v,L))
    r1=subtract(v,tuple(alpha*x for x in diag(v,L)))
    assert r1==(F(0),F(0))
    n+=1
print('VERIFY_OK',n,'exact rational assertions')
