#!/usr/bin/env python3
"""Exact, independent checks for Walsh congruences of triangulation ear profiles.

Run: python3 check_triangulation_ears.py
Only uses the Python standard library. Finite tests corroborate, not replace, proof.
"""
from functools import lru_cache
from math import comb


def catalan(k):
    return comb(2*k, k)//(k+1)


def binary_ones(x):
    return x.bit_count()


def valuation2(x):
    assert x != 0
    return (abs(x) & -abs(x)).bit_length() - 1


@lru_cache(None)
def triangulations(a, b):
    """Sets of internal diagonals triangulating consecutive vertices [a,b]."""
    if b <= a+2:
        return (frozenset(),)
    out=[]
    for k in range(a+1, b):
        root = set()
        if k > a+1:
            root.add((a,k))
        if k < b-1:
            root.add((k,b))
        for left in triangulations(a,k):
            for right in triangulations(k,b):
                out.append(frozenset(root | left | right))
    return tuple(out)


def geometric_profile_counts(n):
    counts=[0]*(1<<n)
    all_triangs=triangulations(0,n-1)
    assert len(all_triangs)==catalan(n-2)
    for diag in all_triangs:
        mask=0
        for i in range(n):
            a=(i-1)%n
            b=(i+1)%n
            if (min(a,b),max(a,b)) in diag:
                mask |= 1<<i
        counts[mask]+=1
    return counts


def fwht(vals):
    a=vals[:]
    h=1
    while h<len(a):
        for i in range(0,len(a),h<<1):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h <<= 1
    return a


def ear_formula(n):
    size=1<<n
    a=[0]*size
    full=size-1
    for mask in range(size):
        k=mask.bit_count()
        if (mask & ((mask<<1)&full)) or ((mask&1) and (mask&(1<<(n-1)))):
            continue
        if n-k >= 3 or (n==4 and n-k==2):
            a[mask]=(-2)**k*catalan(n-2-k)
    for j in range(n):
        bit=1<<j
        for mask in range(size):
            if mask&bit:
                a[mask]+=a[mask^bit]
    return a


def checks():
    exact=0
    for n in range(5,12):
        direct=fwht(geometric_profile_counts(n))
        algebra=ear_formula(n)
        assert direct==algebra, ('triangulation mismatch',n)
        exact+=1<<n
    for n in range(4,19):
        w=ear_formula(n)
        c=catalan(n-2)
        v=binary_ones(n-1)-1
        mod=1<<(v+1)
        assert valuation2(c)==v
        for mask,value in enumerate(w):
            if n%2==1 or mask.bit_count()%2==0:
                assert (value-c)%mod==0, (n,mask,value,'uniform residue')
                assert value!=0 and valuation2(value)==v, (n,mask,value,'valuation')
            else:
                assert value%mod==0, (n,mask,value,'even-order cancellation class')
    print('PASS: 4<=n<=18 congruences; independent geometric enumeration vs formula for 5<=n<=11; exact frequency checks =',exact)


if __name__=='__main__':
    checks()
