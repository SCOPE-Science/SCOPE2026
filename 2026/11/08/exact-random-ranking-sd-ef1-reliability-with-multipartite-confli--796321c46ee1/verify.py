#!/usr/bin/env python3
"""Reproduce finite assignment tests and asymptotic numerical illustrations."""
from itertools import product, combinations
from collections import Counter
from math import comb, factorial, floor, sqrt, erf

def falling(a,b):
    if b>a: return 0
    v=1
    for j in range(b):v*=a-j
    return v

def formula(sizes, ell, last):
    N=sum(sizes)
    assert N//2<ell<=N and len(last)==N-ell
    t=len(last)
    ctr=Counter()
    for g in last:
        a=0
        for i,z in enumerate(sizes):
            a+=z
            if g<a:
                ctr[i]+=1
                break
    ans=factorial(ell)
    for i,ni in enumerate(sizes):
        x=ctr[i]
        ans*=falling(ni-x,x)
    return ans

def direct_count(sizes,ell,rank):
    N=sum(sizes)
    belongs=sum(([i]*sizes[i] for i in range(len(sizes))),[])
    num=0
    for ass in product(range(ell),repeat=N):
        # no conflicting vertices in same allocation class
        owners={}
        good=True
        for j,u in enumerate(ass):
            if u in owners and owners[u]!=belongs[j]:
                good=False;break
            owners[u]=belongs[j]
        if not good: continue
        counts=[0]*ell
        for j,g in enumerate(rank):
            counts[ass[g]]+=1
            if max(counts)-min(counts)>1:
                good=False;break
        if good: num+=1
    return num


def direct_sd_ef1(ass, rank, ell):
    # Independently implement the existential item-removal definition.
    pos={g:i for i,g in enumerate(rank)}
    bundles=[[g for g,who in enumerate(ass) if who==i] for i in range(ell)]
    for i in range(ell):
        for j in range(ell):
            if i==j: continue
            options=bundles[j] if bundles[j] else [None]
            works=False
            for rem in options:
                if all(sum(pos[g]<=k for g in bundles[i]) >=
                       sum(pos[g]<=k for g in bundles[j] if g!=rem)
                       for k in range(len(rank))):
                    works=True;break
            if not works: return False
    return True

def definition_crosscheck():
    tests=0
    for sizes in [(1,1),(2,2),(1,2,2),(2,2,2)]:
        N=sum(sizes)
        for ell in range(N//2+1,N+1):
            for ass in product(range(ell),repeat=N):
                rank=tuple(range(N))
                f=direct_sd_ef1(ass,rank,ell)
                counts=[0]*ell
                g=True
                for j in rank:
                    counts[ass[j]]+=1
                    if max(counts)-min(counts)>1:
                        g=False;break
                assert f==g,(sizes,ell,ass,f,g)
                tests+=1
    print('PASSED direct existential-removal SD-EF1/prefix equivalence:',tests,'tests')

def checks():
    definition_crosscheck()
    size_cases=[(1,1),(1,2),(2,2),(1,3),(2,3),(3,3),(1,1,1),(1,1,2),(1,2,2),(2,2,2),(1,1,1,1),(1,1,3),(1,2,3),(1,1,1,2),(1,1,1,3)]
    ct=0
    for sizes in size_cases:
        N=sum(sizes)
        for ell in range(N//2+1,N+1):
            for last in combinations(range(N),N-ell):
                rank=tuple(g for g in range(N) if g not in last)+last
                a=direct_count(sizes,ell,rank)
                b=formula(sizes,ell,last)
                assert a==b,(sizes,ell,last,a,b)
                ct+=1
    print('PASSED independent brute assignments:',ct,'instances; group sizes:',len(size_cases))
    for sizes in [(2,2),(2,3),(3,3),(3,3,3),(4,5),(2,3,4),(1,2,2)]:
        N=sum(sizes)
        chi=N-min(sizes)//2
        for ell in range(N//2+1,N+1):
            all_yes=all(formula(sizes,ell,last)>0 for last in combinations(range(N),N-ell))
            assert all_yes==(ell>=chi),(sizes,ell,all_yes,chi)
    print('PASSED all-order thresholds in seven graph families')
    for m in (100,400,1600):
        for c in (0.5,1.,2.):
            s=max(1,round(c*sqrt(m)));t=m-s
            low=max(0,t-m//2)
            hi=min(t,m//2)
            p=sum(comb(m,x)*comb(m,t-x) for x in range(low,hi+1))/comb(2*m,t)
            limit=erf(c)
            print('m=%d c=%.1f prob=%.7f Gaussian=%.7f'%(m,c,p,limit))
    print('ALL CHECKS PASSED')
if __name__=='__main__':checks()
