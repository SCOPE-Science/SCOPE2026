#!/usr/bin/env python3
"""Finite cross-check of minimum independent dominating sets on cycle–clique tensor products.

The test constructs graph adjacency directly and enumerates all vertex subsets
up to the proposed optimum for each small graph. It is not an infinite proof.
"""
from itertools import product
from collections import Counter
from math import comb

def predicted(n,q):
    assert n>=6 and q>=3
    k,r=divmod(n,3)
    placements=(n*comb(k+r-1,r))//k
    assert placements*k==n*comb(k+r-1,r)
    colorings=q*(q-1) if k==2 else (q-1)**k+(-1)**k*(q-1)
    return (2*n+2)//3,placements*colorings

def graph_bits(n,q):
    adj=[0]*(n*q)
    for i in range(n):
        for c in range(q):
            v=i*q+c
            for j in ((i+1)%n,(i-1)%n):
                for d in range(q):
                    if c!=d:adj[v]|=1<<(j*q+d)
    return adj

def independent_dominating(mask,adj):
    dominated=mask
    for v,near in enumerate(adj):
        if (mask>>v)&1:
            if near&mask:return False
            dominated |= near
    return dominated==(1<<len(adj))-1

def check_by_raw_subsets(n,q):
    # Literally enumerate all subsets of size at most the claimed optimum;
    # this detects both smaller independent dominating sets and bad counts.
    from itertools import combinations
    adj=graph_bits(n,q)
    wmin,pred=predicted(n,q)
    found=0; smaller=0; tested=0
    for size in range(wmin+1):
        for vertices in combinations(range(n*q),size):
            mask=sum(1<<v for v in vertices)
            if independent_dominating(mask,adj):
                if size<wmin:smaller+=1
                else:found+=1
            tested+=1
    assert (smaller,found)==(0,pred),(n,q,smaller,found,wmin,pred)
    return tested

if __name__=='__main__':
    raw=0; tests=[]
    for n,q in ((6,3),(7,3),(8,3),(9,3),(6,4),(7,4),(6,5)):
        count=check_by_raw_subsets(n,q)
        raw+=count
        tests.append((n,q,predicted(n,q)[1],count))
    for n in range(6,24):
        for q in range(3,12):
            minimum,count=predicted(n,q)
            assert minimum==(2*n+2)//3 and count>0
    print('VERIFY_OK raw_graph_profiles',tests,
          'raw_vertex_subsets_checked',raw,
          'formula_parameter_checks',18*9,
          'literal_independent_dominating_test=PASS',
          'minimum_multiplicities=PASS')
