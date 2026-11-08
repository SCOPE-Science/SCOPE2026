#!/usr/bin/env python3
"""Finite checks of exact-two reverse-complement-duplication sphere extremum.
Pure standard-library Python; the all-length theorem is proved separately.
Run with python3 verify_rc_odd.py.
"""
from itertools import product
from math import comb

def rc_duplicate(x, k, start, complement):
    block = x[start:start+k]
    return x[:start+k] + tuple(complement[z] for z in reversed(block)) + x[start+k:]

def descendants(x, k, complement):
    # Keep histories as well as distinct descendants, for collision counting.
    out = {}
    for i in range(len(x)-k+1):
        y = rc_duplicate(x,k,i,complement)
        for j in range(len(y)-k+1):
            z = rc_duplicate(y,k,j,complement)
            out.setdefault(z,[]).append((i,j))
    return out

def bound(n,k):
    return (n-k+1)*(n+1)-comb(max(n-2*k+2,0),2)

def test():
    binary = (1,0)
    tested_sources = 0
    tested_constant = 0
    for k in (1,3,5,7):
        for n in range(k, min(12,k+8)+1):
            threshold = bound(n,k)
            for x in product(range(2),repeat=n):
                size = len(descendants(x,k,binary))
                assert size <= threshold, (k,n,x,size,threshold)
                tested_sources+=1
            for sym in (0,1):
                ds = descendants((sym,)*n,k,binary)
                assert len(ds)==threshold, (k,n,sym,len(ds),threshold)
                assert max(map(len,ds.values()))<=2
                assert sum(len(v)-1 for v in ds.values()) == comb(max(n-2*k+2,0),2)
                tested_constant+=1
    # Two independent complement pairs, including words using all four letters.
    four = (1,0,3,2)
    for k in (1,3,5):
        for n in range(k, min(k+3,6)+1):
            threshold=bound(n,k)
            for x in product(range(4),repeat=n):
                assert len(descendants(x,k,four)) <=threshold
                tested_sources+=1
            assert len(descendants((2,)*n,k,four))==threshold
            tested_constant+=1
    for k in (1,3,5,7,9,11):
        for n in range(k,39):
            ds=descendants((0,)*n,k,binary)
            assert len(ds)==bound(n,k)
            excess=sum(len(v)-1 for v in ds.values())
            assert excess==comb(max(n-2*k+2,0),2)
            assert max(len(v) for v in ds.values())<=2
            tested_constant+=1
    print('ALL_TESTS_PASS', 'sources=', tested_sources, 'constant_histories=',tested_constant)
if __name__=='__main__': test()
