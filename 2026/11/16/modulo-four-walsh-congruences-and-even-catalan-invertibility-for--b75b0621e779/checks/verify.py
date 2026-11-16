#!/usr/bin/env python3
"""Exact checks for Walsh congruences on noncrossing-partition indicators.

Run: python3 nc_mod4_checker.py
Requires Python 3, NumPy. No external data or network access.
"""
from itertools import combinations
from math import comb
import random
import numpy as np


def catalan(k):
    return comb(2*k, k)//(k+1)


def partitions(n):
    def rec(a, greatest):
        if len(a) == n:
            yield tuple(a)
        else:
            for c in range(greatest+2):
                a.append(c)
                yield from rec(a, max(greatest,c))
                a.pop()
    yield from rec([0], 0)


def noncrossing(p):
    n = len(p)
    for a in range(n):
        for b in range(a+1,n):
            for c in range(b+1,n):
                if p[a]!=p[c]:
                    continue
                for d in range(c+1,n):
                    if p[b]==p[d] and p[a]!=p[b]:
                        return False
    return True


def masks(n):
    edges = list(combinations(range(n),2))
    data=[]
    for p in partitions(n):
        if noncrossing(p):
            data.append(sum(1<<t for t,(i,j) in enumerate(edges) if p[i]==p[j]))
    return edges,data


def fwht(a):
    n=len(a)
    h=1
    while h<n:
        b=a.reshape(-1,2*h)
        x=b[:,:h].copy()
        b[:,:h]+=b[:,h:]
        b[:,h:]=x-b[:,h:]
        h*=2
    return a


def predicted_remainder(n,mask,edges):
    c=catalan(n)
    for t,(i,j) in enumerate(edges):
        if mask>>t&1:
            d=j-i
            c-=2*catalan(d)*catalan(n-d)
    return c%4


def exact_mod4(n,random_count=0):
    edges,m=masks(n)
    assert len(m)==catalan(n),(n,len(m))
    count_by_edge=[sum(x>>i&1 for x in m) for i in range(len(edges))]
    assert all(count_by_edge[t] == catalan(j-i)*catalan(n-(j-i))
               for t,(i,j) in enumerate(edges))
    if n<=7:
        w=np.zeros(1<<len(edges),dtype=np.int64)
        w[m]=1
        fwht(w)
        indexes=np.arange(len(w),dtype=np.uint32)
        expected=np.full(len(w),catalan(n)%4,dtype=np.int16)
        for t,(i,j) in enumerate(edges):
            coeff=(-2*catalan(j-i)*catalan(n-j+i))%4
            expected=(expected+coeff*((indexes>>t)&1))%4
        assert np.array_equal(w%4,expected)
        assert np.all(w%2==catalan(n)%2)
        count2=int(np.count_nonzero(w%4==2))
        if n%2 and catalan(n)%4==2:
            assert np.all(w!=0)
        print('EXHAUSTIVE n={} Catalan={} frequencies={} val1_count={} zeros={}'.format(
            n,len(m),len(w),count2,int(np.count_nonzero(w==0))))
    else:
        rng=random.Random(7410+n)
        for _ in range(random_count):
            mask=rng.getrandbits(len(edges))
            actual=sum(-1 if (x&mask).bit_count()%2 else 1 for x in m)
            assert actual%4==predicted_remainder(n,mask,edges)
            if n%2 and catalan(n)%4==2:
                assert actual%4==2
        print('DIRECT_SAMPLE n={} Catalan={} frequencies_sampled={}'.format(n,len(m),random_count))


def main():
    for n in range(2,8):
        exact_mod4(n)
    for n in (8,9,10):
        exact_mod4(n,200)
    for n in range(2,501):
        c=catalan(n)
        odd_distances=[d for d in range(1,n) if catalan(d)%2 and catalan(n-d)%2]
        if n%2:
            assert not odd_distances
        else:
            expected=[d for d in range(1,n) if (d+1).bit_count()==1 and (n-d+1).bit_count()==1]
            assert odd_distances==expected
        assert (c//(c&-c))%2==1
        if n%2 and (n+1).bit_count()==2:
            assert c%4==2
    print('NONCROSSING_WALSH_MOD4_PASS')

if __name__=='__main__':
    main()
