#!/usr/bin/env python3
"""Independent finite tests for edge-general-position sets of simple cycles.

Run: python3 verify.py
Uses the definition through every consecutive shortest path, not the
counting proof, to determine feasibility.
"""
from itertools import combinations
from math import comb


def closed_formula(n):
    if 3 <= n <= 5:
        return [comb(n,k) for k in range(n+1)], {n: 1}
    h = n // 2
    if n % 2 == 0:
        triples = h*(h-1)*(h+4)//3
        fours = h*(h-1)//2
        max_triples = h*(h-1)*(h-2)//3
    else:
        triples = n*(h*h+7*h-6)//6
        fours = n*(h-1)
        max_triples = n*(h-2)*(h-3)//6
    return [1, n, comb(n,2), triples, fours], {3: max_triples, 4: fours}


def geodesic_masks(n):
    h=n//2
    return [sum(1<<((s+j)%n) for j in range(length))
            for s in range(n) for length in range(3,h+1)]


def from_definition(mask, paths):
    for p in paths:
        if (mask & p).bit_count() >= 3:
            return False
    return True


def cyclic_gaps(indices,n):
    return [b-a for a,b in zip(indices,indices[1:]+[indices[0]+n])]


def check(n):
    paths=geodesic_masks(n)
    good=[from_definition(mask,paths) for mask in range(1<<n)]
    hist=[0]*(n+1)
    facets=[0]*(n+1)
    for mask, valid in enumerate(good):
        if not valid: continue
        size=mask.bit_count()
        hist[size]+=1
        if all(not good[mask | (1<<e)] for e in range(n) if not(mask>>e)&1):
            facets[size]+=1
        if n>=6 and size in (3,4):
            indices=[e for e in range(n) if (mask>>e)&1]
            gaps=cyclic_gaps(indices,n)
            if size==3:
                assert (max(gaps)<=((n+1)//2))
                extendable=any(g>=n//2 for g in gaps)
                assert extendable==(any(good[mask | (1<<e)] for e in range(n) if not (mask>>e)&1))
            else:
                h=n//2
                assert all(gaps[j]+gaps[(j+1)%4]>=h for j in range(4))
    expected, maximal=closed_formula(n)
    assert hist == expected + [0]*(n+1-len(expected)), (n,hist,expected)
    assert {k:x for k,x in enumerate(facets) if x}=={k:v for k,v in maximal.items() if v}, (n,facets,maximal)
    return (1<<n),sum(hist),sum(facets)

if __name__=='__main__':
    subsets=sets=facets=0
    for n in range(3,19):
        s,t,f=check(n)
        subsets+=s; sets+=t; facets+=f
        assert n>=6 or t==(1<<n)
        print('CYCLE',n,'candidate_subsets',s,'valid_sets',t,'facets',f)
    # Independently enumerate all feasible 3-, 4- and forbidden 5-subsets
    # on larger orders, without relying on whole-power-set enumeration.
    larger=0
    for n in range(19,27):
        paths=geodesic_masks(n)
        expected, maximal=closed_formula(n)
        for k in (3,4,5):
            count=0
            for indices in combinations(range(n),k):
                mask=sum(1<<i for i in indices)
                count+=from_definition(mask,paths)
            larger+=comb(n,k)
            assert count == (expected[k] if k<=4 else 0), (n,k,count)
    print('VERIFY_OK exhaustive_orders=3..18 full_subsets='+str(subsets)
          +' admissible='+str(sets)+' facets='+str(facets)
          +' additional_order_19..26_subsets='+str(larger)
          +' geodesic_path_checks=PASS cyclic_gap_classes=PASS'
          +' exact_polynomial=PASS maximal_facets=PASS')
