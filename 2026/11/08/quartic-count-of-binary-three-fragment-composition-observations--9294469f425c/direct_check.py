#!/usr/bin/env python3
"""Independent direct exhaustive check of binary short-composition spectra.
Scientific model: all contiguous substrings of lengths 1, 2 and 3.
"""
from collections import defaultdict


def observed(word):
    n=len(word)
    out=[]
    for k in range(1,min(n,3)+1):
        counts=[0]*(k+1)
        for i in range(n-k+1):
            counts[sum(word[i:i+k])]+=1
        out.extend(counts)
    return tuple(out)


def formula(n):
    if n==1:
        return 2
    c=(480,555,456,555)[n%4]
    num=3*n**4-16*n**3+114*n**2-272*n+c
    assert num%96==0
    return num//96


def check(limit=17):
    for n in range(1,limit+1):
        signatures=set()
        for b in range(1<<n):
            word=tuple((b>>i)&1 for i in range(n))
            signatures.add(observed(word))
        count=len(signatures)
        assert count==formula(n),(n,count,formula(n))
        print(n,count)
    print('DIRECT_OK')


if __name__=='__main__':
    check()
