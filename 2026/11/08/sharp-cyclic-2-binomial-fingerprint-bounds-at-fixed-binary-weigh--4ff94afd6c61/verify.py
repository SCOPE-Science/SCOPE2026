#!/usr/bin/env python3
"""Independent finite verification of cyclic 2-binomial fingerprint extremal theorem.
Uses direct scattered-subsequence enumeration; no use of the proof's walk."""
from itertools import product
from math import gcd


def signature(w):
    z = len(w) - sum(w)
    o = sum(w)
    p00 = p01 = p10 = p11 = 0
    for i, x in enumerate(w):
        for y in w[i+1:]:
            if x == 0 and y == 0: p00 += 1
            elif x == 0 and y == 1: p01 += 1
            elif x == 1 and y == 0: p10 += 1
            else: p11 += 1
    return (z,o,p00,p01,p10,p11)


def fingerprint_count(w):
    return len({signature(w[i:]+w[:i]) for i in range(len(w))})


def check():
    total = 0
    for n in range(2,13):
        records={}
        for w in product((0,1),repeat=n):
            k=sum(w)
            if not 0 < k < n:continue
            d=gcd(n,k);L=n//d
            count=fingerprint_count(w)
            assert L<=count<=n-d+1,(w,n,k,count,L,n-d+1)
            base=w[:L]
            assert (count==L)==(base*d==w),(w,count,L)
            x=records.setdefault(k,[n,0])
            x[0]=min(x[0],count)
            x[1]=max(x[1],count)
            total+=1
        for k,(mn,mx) in records.items():
            d=gcd(n,k)
            assert mn==n//d and mx==n-d+1,(n,k,mn,mx)
            assert fingerprint_count((0,)*(n-k)+(1,)*k)==mx
            assert fingerprint_count(((0,)*((n-k)//d)+(1,)*(k//d))*d)==mn
    print(f'VERIFY_OK: all {total} nonconstant binary words of lengths 2..12; exact minima, maxima, and all equality cases')

if __name__=='__main__': check()
