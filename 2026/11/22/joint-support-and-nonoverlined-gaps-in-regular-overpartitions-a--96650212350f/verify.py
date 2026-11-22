#!/usr/bin/env python3
"""Exact independent tests for two coupled overpartition gap statistics.
No third-party dependencies; finite tests do not prove asymptotics.
"""
from functools import lru_cache
from math import pi, sqrt, exp


def all_overpartitions(n, ell):
    # Every multiset of allowed parts, with every independent first-copy overline choice.
    def build(left, largest, parts):
        if left == 0:
            distinct = sorted(set(parts))
            for mask in range(1 << len(distinct)):
                overlined = {j for k,j in enumerate(distinct) if (mask >> k) & 1}
                yield tuple(parts), overlined
            return
        for j in range(min(left, largest), 0, -1):
            if j % ell:
                yield from build(left-j, j, parts+(j,))
    yield from build(n,n,())


def gaps(parts, overlined, ell):
    from collections import Counter
    count = Counter(parts)
    j=1
    while j % ell == 0 or count[j]-int(j in overlined)>0:
        j+=1
    a=j
    j=1
    while j % ell == 0 or count[j]>0:
        j+=1
    return a,j


def polynomial_count(n,ell,x,y):
    # Independent Euler product: A requires a positive nonoverlined count up to x,
    # B requires a positive total count up to y. Indices x,y are integer cutoffs.
    coef=[1]+[0]*n
    for j in range(1,max(n,x,y)+1):
        if j%ell==0:continue
        prev=coef
        coef=[0]*(n+1)
        for k in range(n//j+1):
            if j<=x: w=0 if k==0 else (1 if k==1 else 2)
            elif j<=y: w=0 if k==0 else 2
            else: w=1 if k==0 else 2
            if not w:continue
            step=k*j
            for z in range(n-step+1):
                coef[z+step]+=w*prev[z]
    return coef[n]


def overpartition_counts(N,ell):
    a=[1]+[0]*N
    for j in range(1,N+1):
        if j%ell==0:continue
        # Apply geometric factor 1/(1-z^j), then (1+z^j).
        for k in range(j,N+1): a[k]+=a[k-j]
        for k in range(N,j-1,-1):a[k]+=a[k-j]
    return a


def coincidence_count(n,ell,pa):
    out=0;s=0
    for j in range(1,4*n+4):
        if j%ell==0:continue
        if s>n:break
        k=0;z=n-s
        sub=0
        while z>=0:
            sub+=(1 if k==0 else 2*(-1)**k)*pa[z]
            z-=j;k+=1
        assert sub>=0,(n,ell,j,sub)
        out+=sub
        s+=j
    return out


def test():
    tests=0
    for ell in range(2,7):
        for n in range(0,13):
            records=[gaps(parts,mark,ell) for parts,mark in all_overpartitions(n,ell)]
            pa=overpartition_counts(n,ell)
            assert len(records)==pa[n]
            coincidence=sum(a==b for a,b in records)
            assert coincidence==coincidence_count(n,ell,pa)
            tests+=2
            for x,y in ((0,0),(1,1),(2,4),(4,2),(3,5),(6,6)):
                direct=sum(a>x and b>y for a,b in records)
                exact=polynomial_count(n,ell,x,y)
                assert direct==exact, (ell,n,x,y,direct,exact)
                tests+=1
    for ell in (2,3,4,5):
        pa=overpartition_counts(500,ell)
        ratios=[]
        for n in (100,200,350,500):
            actual=coincidence_count(n,ell,pa)/pa[n]
            ratios.append(round(actual,6))
        print('ell',ell,'coincidence shares n=100,200,350,500:',ratios)
    print('PASS:',tests,'exact coefficient and exhaustive marked-multiset comparisons; finite convergence illustration')
if __name__=='__main__':test()
