#!/usr/bin/env python3
"""Standalone exact checks of two-point sumset inverse fibers.
No external modules needed. The proof, not this finite verification, establishes all dimensions.
"""
from itertools import product
from collections import Counter
from math import comb

def plus(x, y): return tuple(a+b for a,b in zip(x,y))
def minus(x, y): return tuple(a-b for a,b in zip(x,y))
def expected_fiber(T, v):
    if not T or any(vv < 0 for vv in v) or not any(v): raise ValueError
    runs = []
    for x in sorted(T):
        if minus(x,v) in T: continue
        length=0; y=x
        while y in T:
            length+=1; y=plus(y,v)
        runs.append(length)
    if sum(runs)!=len(T): raise AssertionError('not a ray decomposition')
    if min(runs)<2: return {}
    poly={0:1}
    for ell in runs:
        local={r:comb(r-1,ell-1-r) for r in range((ell+1)//2,ell) if 0<=ell-1-r<=r-1}
        nex=Counter()
        for a,aa in poly.items():
            for b,bb in local.items(): nex[a+b] += aa*bb
        poly=dict(nex)
    return poly

def actual_fiber(T,v):
    points=sorted(T); count=Counter()
    for mask in range(1,1<<len(points)):
        if not mask&1: # points[0] need not be zero in general; choose direct membership
            pass
        Y=frozenset(points[i] for i in range(len(points)) if mask>>i&1)
        if (0,)*len(v) not in Y: continue
        if Y | frozenset(plus(y,v) for y in Y) == T: count[len(Y)] += 1
    return dict(count)

def exhaustive(points,v):
    assert (0,)*len(v) in points
    count=0
    for mask in range(1<<len(points)):
        if not mask & 1: continue
        T=frozenset(points[i] for i in range(len(points)) if mask>>i&1)
        assert actual_fiber(T,v)==expected_fiber(T,v),(v,T, actual_fiber(T,v),expected_fiber(T,v))
        count+=1
    return count

def compositions(n, least=2):
    if n==0: yield ();return
    for v in range(least,n+1):
        for r in compositions(n-v,least): yield (v,)+r

def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a

def poly_of_runs(runs):
    poly={0:1}
    for l in runs:
        q={r:comb(r-1,l-1-r) for r in range((l+1)//2,l) if 0<=l-1-r<=r-1}
        new=Counter()
        for i,a in poly.items():
            for j,b in q.items(): new[i+j]+=a*b
        poly=dict(new)
    return poly

def main():
    tests=0
    for length in range(2,10):
        pts=[(j,) for j in range(length)]
        for v in [(1,),(2,),(3,)]: tests+=exhaustive(pts,v)
    points=[(i,j) for i in range(3) for j in range(3)]
    for v in [(1,0),(0,1),(1,1),(2,1),(1,2),(2,2)]: tests+=exhaustive(points,v)
    for n in range(2,17):
        ideal=poly_of_runs((n,))
        assert sum(ideal.values())==fib(n-1)
        for parts in compositions(n):
            p=poly_of_runs(parts)
            assert sum(p.values())<=fib(n-1)
            assert all(p.get(r,0)<=ideal.get(r,0) for r in p), (n,parts)
            if len(parts)>1: assert p!=ideal
    print('VERIFY_OK', 'exhaustive_targets',tests,'rank_polynomial_cutoff',16)
if __name__=='__main__': main()
