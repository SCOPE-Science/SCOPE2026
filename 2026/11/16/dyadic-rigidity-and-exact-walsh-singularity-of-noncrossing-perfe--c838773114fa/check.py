#!/usr/bin/env python3
"""Exact integer checks for Fourier sums of noncrossing matchings.
No external dependencies; Python 3.10+."""
from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
from math import comb
from random import Random


def catalan(n):
    return comb(2*n,n)//(n+1)

def edges(n):
    return [(i,j) for i in range(2*n) for j in range(i+1,2*n) if (j-i)%2]

def reflected(n, edge):
    i,j=edge; nn=2*n
    a,b=(-i)%nn,(-j)%nn
    return (min(a,b),max(a,b))

def signed_sum(n, minus_edges):
    b=set(minus_edges)
    @lru_cache(None)
    def rec(i,j):
        if i>j: return 1
        return sum((-1 if (i,k) in b else 1)*rec(i+1,k-1)*rec(k+1,j)
                   for k in range(i+1,j+1,2))
    return rec(0,2*n-1)

def matchings(i,j):
    if i>j:
        yield ()
        return
    for k in range(i+1,j+1,2):
        for a in matchings(i+1,k-1):
            for b in matchings(k+1,j):
                yield ((i,k),)+a+b

def signed_sum_direct(n, minus_edges):
    B=set(minus_edges)
    return sum((-1)**sum(e in B for e in M) for M in matchings(0,2*n-1))

def zero_witness(n):
    """Return a set of negative chords if n+1 is not a power of two."""
    if (n+1)&n==0:
        raise ValueError('Catalan count is odd; no Walsh zero')
    N=2*n
    neg=set()
    if n%2:
        m=(n-1)//2
        inner=zero_witness(m)
        for i,j in inner:
            e=(i+1,j+1)
            neg.add(e)
            neg.add(reflected(n,e))
    # Every non-central root chord at k>n is negative, its reflection at k<n positive.
    neg.update((0,k) for k in range(n+1,2*n) if k%2)
    return neg


def v2(a):
    if not a: return float('inf')
    return (abs(a)&-abs(a)).bit_length()-1

def run():
    # All frequencies for 1..4 pairs, including all 65536 signings for n=4.
    for n in range(1,5):
        E=edges(n)
        t=(n+1).bit_count()-1
        seenzero=False
        zero_count=0
        for mask in range(1<<len(E)):
            B={e for j,e in enumerate(E) if (mask>>j)&1}
            x=signed_sum(n,B)
            assert x%(1<<t)==0,(n,mask,x,t)
            if n<=3:
                assert x==signed_sum_direct(n,B),(n,mask)
            seenzero |= not x
            zero_count += (x==0)
        assert seenzero == ((n+1)&n != 0), n
        print('exhaustive',n,len(E),1<<len(E),'zeros',zero_count,'v2 Catalan',t)
    # Closed-form constructed zeros, including a sparse 511-point test.
    for n in range(1,132):
        if (n+1)&n==0:continue
        z=zero_witness(n)
        assert signed_sum(n,z)==0, (n,z)
    for n in [255,256]:
        if (n+1)&n:
            assert signed_sum(n,zero_witness(n))==0
    print('constructive zeros n=1..131 and n=256 PASS')
    # Independent vertex-switch orbit enumeration at three singular dimensions.
    for n in (2,4,5):
        root=zero_witness(n); seen=set()
        E=edges(n)
        for mask in range(1<<(2*n)):
            bb=frozenset(e for e in E if ((e in root) ^ bool((mask>>e[0])&1) ^ bool((mask>>e[1])&1)))
            seen.add(bb)
            if n<=4:
                assert signed_sum(n,bb)==0
        assert len(seen)==1<<(2*n-1),(n,len(seen))
    print('vertex-switch null orbits n=2,4,5 PASS')
    # Random independently generated signs, including lengths beyond enumeration.
    rng=Random(872341)
    for n in range(1,33):
        t=(n+1).bit_count()-1
        for _ in range(120):
            B={e for e in edges(n) if rng.getrandbits(1)}
            assert signed_sum(n,B)%(1<<t)==0,(n,t)
        assert v2(catalan(n))==t
    print('random residues n=1..32, Catalan valuations PASS')
    print('NONCROSSING_WALSH_EXACT_PASS')
if __name__=='__main__':run()
