#!/usr/bin/env python3
"""Exact finite verification of EFX conditions for unit-valued multi-stars."""
from itertools import product
from math import comb, prod

def efx_direct(rs, x):
    # Each parallel edge is a distinct item; the first x[i] go to leaf i.
    vals=[]; bundles=[[] for _ in range(len(rs)+1)]
    for i,r in enumerate(rs,1):
        for t in range(r):
            item=(i,t)
            bundles[i if t<x[i-1] else 0].append(item)
    for i in range(len(rs)+1):
        def v(item):return int(i==0 or item[0]==i)
        own=sum(map(v,bundles[i]))
        for j in range(len(rs)+1):
            if i==j:continue
            for g in bundles[j]:
                other=sum(v(h) for h in bundles[j] if h!=g)
                if own<other:return False
    return True

def efx_reduced(rs,x):
    ys=[r-a for r,a in zip(rs,x)]
    S=sum(ys)
    for i,(r,a) in enumerate(zip(rs,x)):
        if a<ys[i]-(int(S==ys[i])):return False
    return S+1>=max(x)

def count_exact(rs):
    good=total=0
    for x in product(*(range(r+1) for r in rs)):
        assert efx_direct(rs,x)==efx_reduced(rs,x),(rs,x)
        good+=int(efx_reduced(rs,x))*prod(comb(r,a) for r,a in zip(rs,x))
    return good,2**sum(rs)

def run():
    N=0
    for k in range(2,5):
        for rs in product(range(1,4),repeat=k):
            if sum(rs)>8:continue
            count_exact(rs);N+=1
    print('PASS direct edge-bundle EFX vs reduced all-item criterion:',N,'stars')
    for rs in [(1,1),(2,2),(3,2),(3,3,2),(2,3,2,1),(3,1,2,2)]:
        a,b=count_exact(rs)
        print(rs,a,b,a/b)
    # For a dominant spoke, verify the analytic binomial-slice formula.
    for m in range(8,17):
      for satellites in [(1,1),(2,1),(1,2),(2,2)]:
        R=sum(satellites)
        if not m>3*R+2: continue
        rs=(m,)+satellites
        full,_=count_exact(rs)
        reduced=0
        for xs in product(*(range(r+1) for r in satellites)):
          if any(2*x<r for r,x in zip(satellites,xs)):continue
          Y=sum(r-x for r,x in zip(satellites,xs))
          weight=prod(comb(r,x) for r,x in zip(satellites,xs))
          lo=(m+1)//2
          hi=(m+Y+1)//2
          reduced+=weight*sum(comb(m,x) for x in range(lo,hi+1))
          if m%2 and Y==0:reduced+=weight*comb(m,(m-1)//2)
        assert full==reduced,(rs,full,reduced)
    print('PASS dominant-spoke exact binomial-slice comparisons')
if __name__=='__main__':run()
