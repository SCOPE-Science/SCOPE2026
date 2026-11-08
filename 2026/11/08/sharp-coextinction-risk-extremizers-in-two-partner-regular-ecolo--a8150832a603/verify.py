#!/usr/bin/env python3
"""Exact polynomial and direct habitat-loss checks for a two-partner coextinction model."""
from functools import lru_cache
from itertools import combinations
from math import comb


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b, sign=1):
    return trim([(a[i] if i < len(a) else 0) + sign*(b[i] if i < len(b) else 0)
                 for i in range(max(len(a),len(b)))])


def mul(a, b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            z[i+j] += x*y
    return trim(z)


def cycle(m):
    if m == 0:
        return [2]
    if m == 1:
        return [1]
    if m == 2:
        return [1,2]
    if m < 0:
        raise ValueError(m)
    return [1]+[m*comb(m-k,k)//(m-k) for k in range(1,m//2+1)]


def graph(parts):
    ans=[1]
    for a in parts:
        ans=mul(ans,cycle(a))
    return ans


def shift(a,k,sign=1):
    return [0]*k+[sign*z for z in a]

@lru_cache(None)
def partitions(n,lo=3):
    if not n:
        return ((),)
    return tuple((a,)+p for a in range(lo,n+1) for p in partitions(n-a,a))


def minimum(n):
    if n in (3,4,5):return (n,)
    r=n%3
    return (3,)*((n-{0:0,1:4,2:5}[r])//3)+({0:(),1:(4,),2:(5,)}[r])


def maximum(n):
    if n in (3,4,5,6,7):return (n,)
    r=n%4
    return (4,)*((n-{0:0,1:5,2:6,3:7}[r])//4)+({0:(),1:(5,),2:(6,),3:(7,)}[r])


def direct_count(n, parts):
    edges=[]; start=0
    for size in parts:
        edges.extend((start+i,start+(i+1)%size) for i in range(size))
        start+=size
    return [sum(all(not(u in s and v in s) for u,v in edges)
                for s in map(set,combinations(range(n),t)))
            for t in range(n+1)]


def check():
    # Algebraic splitting/merging identity from the two roots of T^2-T-z.
    merges=0
    for a in range(3,25):
        for b in range(3,25):
            left=add(mul(cycle(a),cycle(b)),cycle(a+b),-1)
            right=shift(cycle(abs(a-b)),min(a,b),(-1)**min(a,b))
            assert trim(left)==trim(right),(a,b,left,right)
            merges+=1
    # All six exceptional replacement steps needed for the maximum.
    transformations=[
        ((5,5),(4,6)), ((5,6),(4,7)), ((5,7),(4,4,4)),
        ((6,6),(4,4,4)), ((6,7),(4,4,5)), ((7,7),(4,4,6)),
    ]
    for old,new in transformations:
        p=add(graph(new),graph(old),-1)
        assert any(p) and all(x>=0 for x in p),(old,new,p)
    transformations_min=[((4,4),(3,5)),((4,5),(3,3,3)),((5,5),(3,3,4))]
    for old,new in transformations_min:
        p=add(graph(old),graph(new),-1)
        assert any(p) and all(x>=0 for x in p),(old,new,p)
    census=0; ncount=0
    for n in range(3,37):
        polys=[(parts,graph(parts)) for parts in partitions(n)]
        lo=graph(minimum(n));hi=graph(maximum(n))
        for parts,poly in polys:
            for i in range(max(len(lo),len(poly),len(hi))):
                a=poly[i] if i<len(poly) else 0
                l=lo[i] if i<len(lo) else 0
                h=hi[i] if i<len(hi) else 0
                assert l<=a<=h,(n,i,parts,l,a,h)
            # Strict at at least one activity exponent unless it is the correct extremal graph.
            if parts != minimum(n):assert poly !=lo,(n,parts,'min')
            if parts != maximum(n):assert poly !=hi,(n,parts,'max')
            census+=1
        ncount+=1
    direct=0
    for n in range(3,12):
        for parts in partitions(n):
            assert trim(direct_count(n,parts)) == graph(parts),(n,parts)
            direct+=1
    assert cycle(3)==[1,3] and cycle(4)==[1,4,2] and cycle(5)==[1,5,5]
    assert graph((3,3,3))[3]==27 and graph((4,5))[3]==30
    assert comb(9,3)==84
    print('VERIFIED',{'merge_identities':merges,'exceptional_rewrites':len(transformations)+len(transformations_min),
                      'orders':ncount,'cycle_partitions':census,'direct_subset_distributions':direct,
                      'nine_site_safe_sets_t3':(27,30),'nine_site_total_sets_t3':84})

if __name__=='__main__':
    check()
