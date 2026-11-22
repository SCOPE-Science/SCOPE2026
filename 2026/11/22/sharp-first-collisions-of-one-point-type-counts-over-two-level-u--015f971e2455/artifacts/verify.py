#!/usr/bin/env python3
"""Finite checks for two-level 1/3 ultrametric parameter spaces.

The proof of the general formulas is in the accompanying mathematical text.
This verifier exhaustively enumerates integer partitions through n=16 and,
independently, one-point Katetov maps for small bases.
"""
from itertools import product
from collections import defaultdict, Counter
from math import comb


def partitions(n, minimum=1):
    if n == 0:
        yield ()
    else:
        for first in range(minimum, n+1):
            for rest in partitions(n-first, first):
                yield (first,) + rest


def scalar(partition):
    n = sum(partition)
    return (len(partition)+1)*(2**n) - sum(2**(n-a) for a in partition)


def coeffs_x(partition):
    n=sum(partition)
    return tuple((1 if j == 0 else sum(comb(a,j) for a in partition if a >= j)) for j in range(n+1))


def reconstructed_parts(coeffs):
    out=Counter()
    for j in range(len(coeffs)-1,0,-1):
        out[j] = coeffs[j] - sum(out[a]*comb(a,j) for a in out if a>j)
        assert out[j] >= 0
    return tuple(a for a in sorted(out) for _ in range(out[a]))


def direct(part):
    old_cl=[]
    for i,a in enumerate(part):old_cl += [i]*a
    n=len(old_cl)
    d=lambda i,j:1 if old_cl[i]==old_cl[j] else 3
    counts=Counter()
    for ds in product((1,2,3),repeat=n):
        if all(abs(ds[i]-ds[j]) <= d(i,j) <= ds[i]+ds[j]
               for i in range(n) for j in range(i+1,n)):
            counts[(ds.count(1),ds.count(2),ds.count(3))]+=1
    return counts


def formula(part):
    n=sum(part)
    coeff=Counter()
    for c in range(n+1):
        coeff[(0,n-c,c)]+=comb(n,c)
    for a in part:
        for j in range(1,a+1):
            for c in range(n-a+1):
                coeff[(j,n-j-c,c)]+=comb(a,j)*comb(n-a,c)
    return coeff


def main():
    comparisons=0
    for n in range(1,9):
        for p in partitions(n):
            if n > 7 and len(p)>4: continue
            if n==8 and len(p)>3:continue
            assert direct(p)==formula(p),p
            assert sum(formula(p).values())==scalar(p)
            assert reconstructed_parts(coeffs_x(p))==p
            comparisons+=1
    collisions_by_n=[]
    identical_k_by_n=[]
    for n in range(1,17):
        by_scalar=defaultdict(list)
        by_scalar_k=defaultdict(list)
        all_parts=list(partitions(n))
        expected=(0,1,2,3,5,7,11,15,22,30,42,56,77,101,135,176,231)
        assert len(all_parts)==expected[n], (n,len(all_parts),expected[n])
        for p in all_parts:
            t=scalar(p)
            by_scalar[t].append(p)
            by_scalar_k[(len(p),t)].append(p)
            assert reconstructed_parts(coeffs_x(p))==p
        collisions=[(t, ps) for t,ps in by_scalar.items() if len(ps)>1]
        fixed=[(key, ps) for key,ps in by_scalar_k.items() if len(ps)>1]
        collisions_by_n.append((n,collisions))
        identical_k_by_n.append((n,fixed))
    assert all(len(x)==0 for _,x in collisions_by_n[:9])
    n10=collisions_by_n[9][1]
    assert n10==[(4864, [(1,1,1,1,3,3),(2,2,2,2,2)])],n10
    assert all(len(x)==0 for _,x in identical_k_by_n[:15])
    n16=identical_k_by_n[15][1]
    assert n16==[((6,385024), [(1,3,3,3,3,3),(2,2,2,2,4,4)]),
                 ((5,339968),[(1,3,4,4,4),(2,2,2,5,5)])],n16
    print('PASS independent Katetov-map versus coefficient checks:',comparisons)
    print('PASS complete integer-partition classifications through n=16')
    print('First scalar collision, n=10:',n10)
    print('First fixed-class-count collision, n=16:',n16)
    print('PASS binomial inverse reconstructed every partition through n=16')
    print('Finite enumeration proves the stated finite cutoffs; it does not prove the all-n identities.')

if __name__=='__main__':main()
