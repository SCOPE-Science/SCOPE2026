#!/usr/bin/env python3
"""Exact independent dynamic program for minimum total multicover of small spiders."""
from itertools import product
from collections import defaultdict
from math import comb

def formula(r,k,ell):
    if ell==3:
        return 2*r*k, (k+1)**r-comb(k+r-1,r)
    if ell==4:
        return (2*r+1)*k, comb(k+r-1,r-1)
    if ell==5:
        return (2*r+2)*k, comb(k+2*r-1,2*r-1)
    raise ValueError

def exact(r,k,ell):
    optimum=None; num=0
    for center in range(k+1):
        arm=[]
        for a in product(range(k+1),repeat=ell):
            if a[-2]!=k: continue # leaf demand
            if a[1]+center<k:continue # first arm vertex
            if any(a[j-1]+a[j+1]<k for j in range(1,ell-1)):continue
            # each internal vertex including final before leaf has both neighbor sums >=k
            arm.append((a[0],sum(a)))
        # DP counts min weights for every capped sum of first arm weights
        dp={0:(0,1)}
        for _ in range(r):
            nxt={}
            for s,(w,mul) in dp.items():
                for a,cost in arm:
                    ns=min(k,s+a);nw=w+cost
                    if ns not in nxt or nw<nxt[ns][0]: nxt[ns]=(nw,mul)
                    elif nw==nxt[ns][0]: nxt[ns]=(nw,nxt[ns][1]+mul)
            dp=nxt
        if k in dp:
            w,mul=dp[k];w+=center
            if optimum is None or w<optimum: optimum,num=w,mul
            elif w==optimum:num+=mul
    return optimum,num

if __name__=='__main__':
    for ell in (3,4,5):
        for r in (2,3,4,5):
            for k in (1,2,3):
                actual=exact(r,k,ell);expected=formula(r,k,ell)
                if actual!=expected:
                    raise AssertionError((ell,r,k,actual,expected))
                print(f'EXACT_DP_OK ell={ell} arms={r} k={k} weight={actual[0]} count={actual[1]}')
    # independent exhaustive raw vertex assignments with no transfer assumptions
    for ell,r,k in ((3,2,2),(4,2,2),(3,3,2),(4,3,1),(5,2,2)):
        n=1+ell*r
        neigh=[[] for _ in range(n)]
        for i in range(r):
            chain=[0]+list(range(1+i*ell,1+(i+1)*ell))
            for u,v in zip(chain,chain[1:]):
                neigh[u].append(v);neigh[v].append(u)
        minw=999;count=0
        for f in product(range(k+1),repeat=n):
            if any(sum(f[j] for j in nei)<k for nei in neigh):continue
            w=sum(f)
            if w<minw:minw,count=w,1
            elif w==minw:count+=1
        if (minw,count)!=formula(r,k,ell):raise AssertionError((ell,r,k,(minw,count),formula(r,k,ell)))
        print(f'FULL_VERTEX_ASSIGNMENTS_OK ell={ell} arms={r} k={k} count={count}')
    print('VERIFY_OK')
