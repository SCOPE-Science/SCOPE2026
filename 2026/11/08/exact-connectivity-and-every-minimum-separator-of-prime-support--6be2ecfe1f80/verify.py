#!/usr/bin/env python3
"""Direct finite checks of subgroup-factorization support connectivity theorem."""
from itertools import combinations
from math import comb
from collections import deque
import random

def graph(r,t):
    V=[S for S in range(1,(1<<r)) if S.bit_count()<=r-t]
    adj={S:set() for S in V}
    for i,S in enumerate(V):
        for T in V[i+1:]:
            if not (S&T): adj[S].add(T);adj[T].add(S)
    return V,adj

def components(V,adj,removed):
    unseen=set(V)-set(removed); parts=[]
    while unseen:
        start=unseen.pop();comp={start};q=[start]
        for s in q:
            for t in adj[s]&unseen:
                unseen.remove(t);comp.add(t);q.append(t)
        parts.append(comp)
    return parts

def check(r,t,exhaustive=False,seed=0):
    V,adj=graph(r,t);d=(1<<t)-1
    mins=[S for S in V if len(adj[S])==d]
    assert len(mins)==comb(r,t),(r,t,'minimum-degree count')
    assert {S.bit_count() for S in mins}=={r-t}
    cuts={frozenset(adj[S]) for S in mins}
    assert len(cuts)==comb(r,t)
    for S in mins:
        parts=components(V,adj,adj[S]);assert len(parts)==2 and {S} in parts
    tests=0
    if exhaustive:
        for k in range(d+1):
            for C in combinations(V,k):
                pieces=components(V,adj,C)
                if k<d:assert len(pieces)==1,(r,t,k,C)
                else:assert (len(pieces)>1)==(frozenset(C) in cuts)
                tests+=1
    else:
        random.seed(seed+r*111+t)
        for k in range(d):
            for i in range(40):
                C=random.sample(V,k)
                assert len(components(V,adj,C))==1
                tests+=1
    print(f'r={r} t={t} vertices={len(V)} delta={d} min_degree_vertices={len(mins)} min_cuts={len(cuts)} deletion_tests={tests} exhaustive={exhaustive}')
    return tests

def integer_check(r,t):
    # The support model is verified directly against actual subgroup orders.
    primes=[2,3,5,7,11,13,17,19,23][:r]
    n=1
    for p in primes:n*=p
    V,adj=graph(r,t)
    for S in V:
        h=1
        for i,p in enumerate(primes):
            if not (S>>i&1):h*=p
        for T in V:
            if S==T:continue
            k=1
            for i,p in enumerate(primes):
                if not(T>>i&1):k*=p
            import math
            assert (h*k//math.gcd(h,k)==n)==(T in adj[S])
    print(f'direct_subgroup_lcm_check r={r} t={t} passed')

if __name__=='__main__':
    count=0
    for r in [4,5,6]:
        count+=check(r,2,True)
        integer_check(r,2)
    count+=check(7,2,False)
    count+=check(8,3,False)
    integer_check(8,3)
    print('VERIFY_OK deletion_cases=',count)
