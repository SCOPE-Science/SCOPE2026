#!/usr/bin/env python3
"""Exact finite-domain checks for a closed-form nucleon in one-edge augmented bicliques."""
from fractions import Fraction as F
from itertools import combinations

def value(a,b,mask):
    s=(bool(mask&1)+bool(mask&2))
    t=sum(bool(mask&(1<<i)) for i in range(2,a))
    j=sum(bool(mask&(1<<i)) for i in range(a,a+b))
    i=s+t
    return min(i,j)+int(s==2 and i>=j+2)

def pay(a,b):
    if a<b: return [F(1)]*a+[F(0)]*b
    if a==b: return [F(2,3)]*a+[F(1,3)]*b
    if a==b+1: return [F(b,2*b+1)]*(a+b)
    if a==b+2: return [F(1,2)]*2+[F(1,4)]*(a-2)+[F(3,4)]*b
    return [F(1,2)]*2+[F(0)]*(a-2)+[F(1)]*b

def corestage(a,b):
    if a<b: return F(1),None
    if a==b: return F(1),F(1)+F(1,3*(a-1))
    if a==b+1: return F(2*b,2*b+1),None
    if a==b+2: return F(1),F(1)+F(1,4*b)
    return F(1),F(1)+F(1,2*b)

def independent_matching(a,b,mask):
    edges=[(0,1)]+[(i,j) for i in range(a) for j in range(a,a+b)]
    incident=[[] for _ in range(a+b)]
    for i,j in edges: incident[i].append(j); incident[j].append(i)
    cache={0:0}
    def rec(m):
        if m in cache: return cache[m]
        first=(m&-m).bit_length()-1
        best=rec(m & ~(1<<first))
        for j in incident[first]:
            if m>>j&1:
                best=max(best,1+rec(m & ~(1<<first) & ~(1<<j)))
        cache[m]=best
        return best
    return rec(mask)

def checks():
    configs=profiles=0
    for a in range(2,9):
      for b in range(1,9):
        if a+b>13: continue
        n=a+b; x=pay(a,b); vN=value(a,b,(1<<n)-1)
        assert sum(x)==vN,(a,b,'total',x,vN)
        assert all(z>=0 for z in x)
        ratios=[]
        for mask in range(1,(1<<n)-1):
          if n<=10: assert value(a,b,mask)==independent_matching(a,b,mask),(a,b,mask)
          v=value(a,b,mask)
          if v:
            r=sum((x[i] for i in range(n) if mask>>i&1),F(0))/v
            ratios.append((r,mask))
            profiles+=1
        first=min(t for t,_ in ratios)
        expected,second=corestage(a,b)
        assert first==expected,(a,b,'first',first,expected)
        if second is not None:
          varying=[]
          for r,mask in ratios:
            if r==1: continue
            varying.append((r,mask))
          # First ratio strictly >1 following exactly-1 fixed coalitions
          if varying:
            actual=min(r for r,_ in varying)
            assert actual==second,(a,b,'stage2',actual,second)
        if a!=b+1:
          assert all(r>=1 for r,_ in ratios)
        else:
          assert any(r<1 for r,_ in ratios)
        configs+=1
    print('PASS',configs,'graph sizes,',profiles,'positive-valued proper coalitions checked exactly')
if __name__=='__main__': checks()
