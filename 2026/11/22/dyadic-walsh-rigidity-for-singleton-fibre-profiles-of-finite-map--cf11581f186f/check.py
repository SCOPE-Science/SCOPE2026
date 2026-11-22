#!/usr/bin/env python3
"""Exact, dependency-free checks for singleton-fibre Walsh multipliers.

Run with: python3 check.py
All integer arithmetic is exact; tested finite ranges do not replace the all-n proof.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial

def analytic(n, k):
    """Selected singleton urns by inclusion-exclusion (0**0=1)."""
    return sum(((-2)**j)*comb(k,j)*(factorial(n)//factorial(n-j))*(n-j)**(n-j)
               for j in range(k+1))

def via_egf(n,k):
    """Independent exponential generating function coefficient extraction."""
    assert 1 <= n and 0 <= k <= n
    a=[Fraction(1,factorial(j)) for j in range(n+1)]
    b=a[:]
    b[1]-=2
    poly=[Fraction(1)]+[Fraction(0)]*n
    for t in range(n):
        factor=b if t<k else a
        nxt=[Fraction(0)]*(n+1)
        for i in range(n+1):
            for j in range(n+1-i):
                nxt[i+j]+=poly[i]*factor[j]
        poly=nxt
    val=poly[n]*factorial(n)
    assert val.denominator==1
    return val.numerator

def v2(t):
    assert t!=0
    t=abs(t)
    return (t&-t).bit_length()-1

def kernel_from_maps(n):
    counts=[0]*(1<<n)
    for image in product(range(n),repeat=n):
        occ=[0]*n
        for y in image: occ[y]+=1
        mask=sum(1<<i for i in range(n) if occ[i]==1)
        counts[mask]+=1
    return counts

def walsh(counts):
    v=counts[:]
    span=1
    while span<len(v):
        for start in range(0,len(v),2*span):
            for j in range(start,start+span):
                x,y=v[j],v[j+span]
                v[j],v[j+span]=x+y,x-y
        span*=2
    return v

def run():
    tests=0
    for n in range(1,7):
        counts=kernel_from_maps(n)
        assert sum(counts)==n**n
        transform=walsh(counts)
        for mask, val in enumerate(transform):
            assert val==analytic(n,mask.bit_count()),(n,mask)
            tests+=1
    for n in range(1,13):
        for k in range(n+1):
            assert analytic(n,k)==via_egf(n,k),(n,k)
            tests+=1
    for n in range(1,161):
        for k in range(n+1):
            val=analytic(n,k)
            if n==2:
                assert [analytic(2,i) for i in range(3)]==[4,0,4]
                tests+=1
                continue
            if n%2:
                assert val%2==1
            elif n>=4:
                if k==0: assert v2(val)==n*v2(n)
                else: assert v2(val)==1+v2(n)+v2(k),(n,k,v2(val))
            assert val!=0
            tests+=1
    for n in range(1,41):
        spectrum=[analytic(n,k) for k in range(n+1)]
        rank=sum(comb(n,k) for k,t in enumerate(spectrum) if t)
        assert rank==(2 if n==2 else 2**n)
        if n%2==0 and n>=4:
            determinant_v=sum(comb(n,k)*v2(t) for k,t in enumerate(spectrum))
            predicted=n*v2(n)+(2**n-1)*(1+v2(n))+sum(comb(n,k)*v2(k) for k in range(1,n+1))
            assert determinant_v==predicted
        tests+=1
    print('PASS',tests,'exact assertions; exhaustive maps through n=6; EGF through n=12; valuations through n=160; determinant valuations through n=40')

if __name__=='__main__':run()
