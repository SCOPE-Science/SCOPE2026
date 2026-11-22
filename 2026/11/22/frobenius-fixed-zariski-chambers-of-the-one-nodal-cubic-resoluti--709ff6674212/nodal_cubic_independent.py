#!/usr/bin/env python3
"""Independent orbit-block count, not enumerating the list of all 1898 supports."""
from itertools import combinations
from collections import Counter
from math import lcm
import json

P=list(combinations(range(6),2))
partitions=[[1]*6,[2,1,1,1,1],[2,2,1,1],[2,2,2],[3,1,1,1],[3,3],[4,1,1],[4,2],[5,1],[3,2,1],[6]]

def canonical_perm(part):
    p=list(range(6));start=0
    for m in part:
        for j in range(m):p[start+j]=start+(j+1)%m
        start+=m
    return p

def orbits(elements,phi):
    remaining=set(elements);result=[]
    while remaining:
        e=min(remaining);arr=[];v=e
        while v not in arr:
            assert v in remaining
            arr.append(v);v=phi(v)
        assert v==e
        result.append(tuple(arr));remaining.difference_update(arr)
    return result

def polycount(part):
    p=canonical_perm(part)
    Eorbits=orbits(range(6),lambda i:p[i])
    fixed=Counter()
    fixed_Q=Counter()
    # Choose invariant exceptional sets by orbit blocks, then independent line-edge orbit blocks.
    for e_mask in range(1<<len(Eorbits)):
        ex=set().union(*(set(x) for i,x in enumerate(Eorbits) if (e_mask>>i)&1))
        allowed=set(range(6))-ex
        edges={tuple(x) for x in combinations(sorted(allowed),2)}
        P_orbits=orbits(edges,lambda e:tuple(sorted((p[e[0]],p[e[1]]))))
        for l_mask in range(1<<len(P_orbits)):
            L=[e for j,orbit in enumerate(P_orbits) if (l_mask>>j)&1 for e in orbit]
            if any(not(set(a)&set(b)) for a,b in combinations(L,2)):continue
            n=len(ex)+len(L)
            fixed[n]+=1
            if len(ex)<=1:fixed_Q[n+1]+=1
    return [fixed[i]+fixed_Q[i] for i in range(7)],[fixed_Q[i] for i in range(7)]
with open('nodal_cubic_chambers_results.json') as f:ref=json.load(f)
for r in ref['cases']:
    prof,qprof=polycount(r['cycle_type'])
    assert prof==r['fixed_support_size_profile'],(r['cycle_type'],prof,r['fixed_support_size_profile'])
    assert qprof==r['fixed_with_exceptional_minus_two']
    print('INDEPENDENT_CHECK',r['cycle_type'],sum(prof),prof,qprof)
assert polycount([6])[0]==[1,1,0,0,0,0,1]
print('INDEPENDENT_ORBIT_BLOCKS_ALL_11_OK')
