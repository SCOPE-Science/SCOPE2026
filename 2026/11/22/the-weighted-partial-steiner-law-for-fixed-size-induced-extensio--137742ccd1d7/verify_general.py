#!/usr/bin/env python3
"""Exhaustive small finite partial triple systems; independent packing polynomial."""
from itertools import combinations

def linear_triple_count(n, r):
    v = n+r
    pairs = {p:k for k,p in enumerate(combinations(range(v),2))}
    triples = [t for t in combinations(range(v),3) if max(t) >= n]
    footprints = [sum(1<<pairs[p] for p in combinations(t,2)) for t in triples]
    def rec(k, used):
        if k == len(footprints):return 1
        result = rec(k+1,used)
        if not (used & footprints[k]):result += rec(k+1,used | footprints[k])
        return result
    return rec(0,0)

def packing_polynomial(r):
    pairs = {p:k for k,p in enumerate(combinations(range(r),2))}
    footprints = [sum(1<<pairs[p] for p in combinations(t,2)) for t in combinations(range(r),3)]
    def rec(k,used,s):
        if k == len(footprints):return {s:1}
        d=rec(k+1,used,s)
        if not (used&footprints[k]):
            for j,v in rec(k+1,used|footprints[k],s+1).items():d[j]=d.get(j,0)+v
        return d
    return rec(0,0,0)

if __name__=='__main__':
    pvals={}
    for r in range(1,7):
        p=packing_polynomial(r)
        assert sum(p.values()) == linear_triple_count(0,r)
        pvals[r]=p
        print('r',r,'packing_coefficients',str(p),'unconstrained_extensions',sum(p.values()))
    assert pvals[3] == {0:1,1:1}
    assert pvals[4] == {0:1,1:4}
    assert pvals[5] == {0:1,1:10,2:15}
    for n,r in [(1,2),(2,2),(3,2),(1,3),(2,3),(3,3),(1,4),(2,4),(1,5)]:
        value=linear_triple_count(n,r)
        print('n,r',n,r,'exact_total',value)
    print('GENERAL_FINITE_CHECKS_OK')
