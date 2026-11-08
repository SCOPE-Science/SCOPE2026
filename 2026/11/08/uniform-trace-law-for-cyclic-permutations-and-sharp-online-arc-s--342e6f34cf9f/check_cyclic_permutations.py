#!/usr/bin/env python3
"""Finite verification of directed n-cycle arc-incidence trace theorems.
No third-party libraries. All test ranges explicit; not a universal proof.
"""
from itertools import permutations, combinations
from collections import defaultdict
from math import comb, factorial


def ncycles(n):
    # Every n-cycle has a unique order after anchoring at 0.
    for tail in permutations(range(1, n)):
        v=(0,)+tail
        yield frozenset((v[i],v[(i+1)%n]) for i in range(n))


def multiplicity(n,k,f):
    return sum((-1)**j*comb(k-f,j)*factorial(n-f-j-1)
               for j in range(k-f+1))


def check(n):
    cycles=tuple(ncycles(n))
    assert len(cycles)==factorial(n-1)
    possible=set()
    for cycle in cycles:
        a=tuple(sorted(cycle))
        for k in range(n+1):
            for sub in combinations(a,k):
                possible.add(frozenset(sub))
    expected=[factorial(n)*comb(n-1,k)//factorial(n-k)
              for k in range(n-1)] + [0,0]
    sh=[0]*(n+1)
    checked=0
    for sup in possible:
        a=tuple(sorted(sup))
        k=len(a)
        traces=defaultdict(int)
        for c in cycles:
            trace=tuple(e in c for e in a)
            traces[trace]+=1
        if k<=n-2:
            assert len(traces)==2**k, (n,a,len(traces),k)
            for bits in __import__('itertools').product((False,True),repeat=k):
                f=sum(bits)
                assert traces[bits]==multiplicity(n,k,f), (n,a,bits,traces[bits],multiplicity(n,k,f))
            sh[k]+=1
        else:
            assert len(traces)<2**k,(n,a)
        checked+=1
    assert sh == expected,(n,sh,expected)
    print('n=',n,'cycles=',len(cycles),'candidate_supports=',checked,'shattered_coefficients=',sh)

if __name__=='__main__':
    for n in range(3,7):
        check(n)
    print('CYCLIC_PERMUTATION_ARC_TRACE_PASS')
