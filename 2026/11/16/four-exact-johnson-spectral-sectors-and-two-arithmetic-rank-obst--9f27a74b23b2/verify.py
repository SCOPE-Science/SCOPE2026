#!/usr/bin/env python3
"""Reproducible finite checks for the cubic Walsh slice Gram spectrum.
Uses direct enumeration of the slice and independently assembled Gram matrices.
All claims for unbounded dimension are established by the symbolic proof, not tests.
"""
from itertools import combinations
from math import comb
import numpy as np


def spectrum(n, k):
    s = n - 2*k
    denom6 = n*(n-1)*(n-2)*(n-3)*(n-4)*(n-5)
    values = [
        s*s*(s*s-3*n+2)**2/(6*n*(n-1)*(n-2)),
        (n*n-s*s)*(s*s-n+2)**2/(2*n*(n-1)*(n-2)*(n-3)),
        s*s*(n*n-s*s)*((n-2)**2-s*s)/(n*(n-1)*(n-2)*(n-3)*(n-4)),
        (n*n-s*s)*((n-2)**2-s*s)*((n-4)**2-s*s)/denom6,
    ]
    mult = [1, n-1, comb(n, 2)-n, comb(n, 3)-comb(n, 2)]
    return values, mult


def direct_gram(n,k):
    triples=list(combinations(range(n),3))
    rows=[]
    for neg in combinations(range(n), k):
        mask=sum(1 << i for i in neg)
        rows.append([(-1)**sum((mask >> i)&1 for i in t) for t in triples])
    a=np.asarray(rows,dtype=np.int64)
    return (a.T @ a)/len(rows)


def main():
    tested = 0
    for n in range(6,12):
        for k in range(n+1):
            v,m=spectrum(n,k)
            assert sum(m)==comb(n,3)
            assert all(x >= -1e-11 for x in v),(n,k,v)
            exact=np.sort(np.asarray([x for x,r in zip(v,m) for _ in range(r)]))
            observed=np.linalg.eigvalsh(direct_gram(n,k))
            err=np.max(np.abs(exact-observed))
            assert err<1e-7,(n,k,err)
            expected_rank=sum(r for x,r in zip(v,m) if x>1e-10)
            actual_rank=np.count_nonzero(observed>1e-7)
            assert expected_rank==actual_rank,(n,k,expected_rank,actual_rank)
            tested+=1
    # Deliberately include both nontrivial unbalanced resonance families.
    for n,s in [(11,3),(17,7),(18,4),(22,8)]:
        k=(n-s)//2
        v,m=spectrum(n,k)
        zero=[i for i,x in enumerate(v) if abs(x)<1e-12]
        assert zero==([1] if s*s==n-2 else [0]),(n,k,zero)
        tested+=1
    print(f'PASS: {tested} slice and resonance cases; directly enumerated 57 slice Gram matrices for n=6..11.')

if __name__=='__main__':
    main()
