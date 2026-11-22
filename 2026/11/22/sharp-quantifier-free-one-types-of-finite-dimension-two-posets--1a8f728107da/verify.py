#!/usr/bin/env python3
"""Reproduce the two-dimensional poset quantifier-free type bound.

Run: python3 verify.py.  No dependencies outside the Python standard library.
"""
from itertools import permutations

def signatures(p):
    m=len(p)
    out=set()
    for r in range(m+1):
        for s in range(m+1):
            lower=tuple(i+1 for i,v in enumerate(p) if i<r and v<=s)
            upper=tuple(i+1 for i,v in enumerate(p) if i>=r and v>s)
            out.add((lower,upper))
    return out

def reverse_witness(m):
    p=tuple(range(m,0,-1))
    sig=signatures(p)
    expected={((),())}
    for a in range(1,m+1):
        for b in range(a,m+1):
            interval=tuple(range(a,b+1))
            expected.add((interval,()))
            expected.add(((),interval))
    assert sig==expected, (m,len(sig),len(expected))

for m in range(0,9):
    for p in permutations(range(1,m+1)):
        n=len(signatures(p))
        assert n<=m*m+m+1,(m,p,n)
    reverse_witness(m)
    print(f'm={m} maximum_nonparameter={m*m+m+1} maximum_including_equality={(m+1)**2}')
print('VERIFY_OK')
