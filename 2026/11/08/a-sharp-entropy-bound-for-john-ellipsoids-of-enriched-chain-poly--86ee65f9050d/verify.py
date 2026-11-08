#!/usr/bin/env python3
"""Exact combinatorial checks for a poset ellipsoid volume bound.

Run with Python 3 and no third-party modules. Finite tests do not replace
its all-dimensional proof.
"""
from fractions import Fraction
from itertools import combinations
from math import log, exp


def profile(n, edge_mask):
    above = [0] * n
    pairs = list(combinations(range(n), 2))
    for k, (i,j) in enumerate(pairs):
        if edge_mask & (1<<k):
            above[i] |= (1<<j)
    for i in range(n-1, -1, -1):
        for j in range(i+1,n):
            if above[i] & (1<<j):
                above[i] |= above[j]
    chains=[]; anti=[]
    for S in range(1,1<<n):
        ids = [i for i in range(n) if S & (1<<i)]
        is_chain=all((above[i] & (1<<j)) for i,j in combinations(ids,2))
        is_anti=all(not (above[i] & (1<<j)) for i,j in combinations(ids,2))
        if is_chain: chains.append(S)
        if is_anti: anti.append(S)
    return above,chains,anti


def test(n, edge_mask):
    _,chains,anti=profile(n,edge_mask)
    h=max(c.bit_count() for c in chains)
    w=max(a.bit_count() for a in anti)
    assert n<=h*w
    A=next(a for a in anti if a.bit_count()==w)
    if h==1:
        assert n==w
        return h,w
    aa=Fraction(w,n)
    bb=Fraction(n-w,n*(h-1))
    assert 0<bb<=aa
    assert aa+(h-1)*bb==1
    assert all(sum(aa if (A>>i)&1 else bb for i in range(n) if (C>>i)&1)<=1 for C in chains)
    # If rectangular, partition into w disjoint longest chains; brute-force certificate.
    if n==h*w:
        longs=[c for c in chains if c.bit_count()==h]
        def cover(left):
            if not left:return True
            first=left & -left
            return any(cover(left^c) for c in longs if (c&first) and (c&left)==c)
        assert cover((1<<n)-1)
        assert aa==bb==Fraction(1,h)
    else:
        assert aa>bb
        t=w/n; s=1/h
        divergence=t*log(t/s)+(1-t)*log((1-t)/(1-s))
        assert divergence>0
        direct=(w*log(float(h*aa))+(n-w)*log(float(h*bb)))/2
        assert abs(direct-n*divergence/2)<1e-12
    return h,w


def groups_for_layers(layers):
    start=0;groups=[]
    for m in layers:
        groups.append(list(range(start,start+m)));start+=m
    return groups


def layered_profile(layers):
    # Complete comparability between successive layers; each layer antichain.
    n=sum(layers)
    start=0
    edges=[]
    groups=[]
    for m in layers:
        groups.append(range(start,start+m));start+=m
    for p in range(len(groups)):
        for q in range(p+1,len(groups)):
            for a in groups[p]:
                for b in groups[q]:edges.append((a,b))
    ids=list(combinations(range(n),2))
    mask=sum(1<<ids.index(e) for e in edges)
    return test(n,mask)


def main():
    counts=0; rectangular=0; nonrectangular=0
    for n in range(1,6):
        for mask in range(1<<(n*(n-1)//2)):
            h,w=test(n,mask)
            counts+=1
            rectangular+=(n==h*w)
            nonrectangular+=(n<h*w)
    for layers in ((2,1),(3,1),(2,2),(3,2),(4,3),(3,2,2),(4,2,2),(2,2,2),(1,1,1,1)):
        h,w=layered_profile(layers)
        d=sum(layers)
        # For these layered families, the actual John axes squared are m_j/d.
        assert h==len(layers) and w==max(layers)
        assert sum(Fraction(m,d) for m in layers)==1
        # Exact optimality certificate: uniform random full chains,
        # formed by picking one element from each layer independently,
        # give each coordinate marginal 1/m_j. Multipliers total d.
        from itertools import product
        full_chains=list(product(*groups_for_layers(layers)))
        for j,group in enumerate(groups_for_layers(layers)):
            for i in group:
                probability=sum(Fraction(1,len(full_chains)) for C in full_chains if i in C)
                assert probability==Fraction(1,layers[j])
                assert Fraction(d,1)*probability==Fraction(d,layers[j])
        if all(m==layers[0] for m in layers):
            assert d==h*w
    print('ENRICHED_CHAIN_JOHN_BOUND_CHECKS_PASSED',
          'finite_poset_profiles=',counts,
          'rectangular=',rectangular,
          'nonrectangular=',nonrectangular,
          'layered_examples=9')

if __name__=='__main__':main()
