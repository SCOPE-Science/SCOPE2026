#!/usr/bin/env python3
"""Exact checks for Fourier analysis of even-block vertex sets in set partitions."""
from collections import Counter
from functools import lru_cache
from math import comb

@lru_cache(None)
def bell(n):
    if n == 0:
        return 1
    return sum(comb(n-1,j) * bell(j) for j in range(n))

@lru_cache(None)
def moment(k,c):
    return sum(comb(k,j)*c**(k-j)*bell(j) for j in range(k+1))

@lru_cache(None)
def signed(k,l):
    if k == 0:
        return bell(l)
    s=0
    for a in range(k):
        for b in range(l+1):
            weight=(-1)**(a+1) if ((a+b+1)%2==0) else 1
            s+=comb(k-1,a)*comb(l,b)*weight*signed(k-1-a,l-b)
    return s

def partitions(n):
    blocks=[]
    def rec(i):
        if i==n:
            yield tuple(tuple(z) for z in blocks)
            return
        for z in blocks:
            z.append(i)
            yield from rec(i+1)
            z.pop()
        blocks.append([i])
        yield from rec(i+1)
        blocks.pop()
    yield from rec(0)

def direct_fourier_by_weight(n):
    a=[0]*(1<<n)
    for pi in partitions(n):
        mask=0
        for b in pi:
            if len(b)%2==0:
                for x in b:
                    mask|=1<<x
        a[mask]+=1
    m=1
    while m<len(a):
        for i in range(0,len(a),2*m):
            for j in range(i,i+m):
                u,v=a[j],a[j+m]
                a[j]=u+v;a[j+m]=u-v
        m*=2
    return a

def poisson_formula(k,l):
    return sum(moment(k, sum(len(b)%2==0 for b in pi)-sum(len(b)%2==1 for b in pi)) for pi in partitions(l))

def run():
    tests=0
    # Independently enumerate all partitions and the full spectrum in each small dimension.
    for n in range(0,10):
        a=direct_fourier_by_weight(n)
        for mask,v in enumerate(a):
            assert v==signed(mask.bit_count(),n-mask.bit_count()), (n,mask,v)
            tests+=1
        assert a[0]==bell(n)
        tests+=1
    # A separate Poisson/Dobinski computation checks the independent exponential formula.
    for l in range(0,9):
        for k in range(0,13):
            assert poisson_formula(k,l)==signed(k,l), (k,l)
            tests+=1
    # Exact positivity in checked finite orders is a consistency check, not the all-order proof.
    for n in range(1,31):
        for k in range(n+1):
            assert signed(k,n-k)==signed(n-k,k), (n,k)
            tests+=1
            if k%2==0 or n%2==1:
                assert signed(k,n-k)>0, (n,k)
                tests+=1
    assert [signed(k,2-k) for k in range(3)]==[2,0,2]
    tests+=1
    # Two representative spectra expose the order-sensitive non-monotonic bands.
    for n,expected in [(5,[52,4,12,12,4,52]),(7,[877,41,193,85,85,193,41,877]),(8,[4140,162,908,66,684,66,908,162,4140])]:
        assert [signed(k,n-k) for k in range(n+1)]==expected
        tests+=1
    print('PASS exact assertions:',tests)
    print('Odd n=7 spectrum:',[signed(k,7-k) for k in range(8)])
    print('Even n=8 spectrum:',[signed(k,8-k) for k in range(9)])
    print('Exhaustive partitions n=9:',bell(9))

if __name__=='__main__':
    run()
