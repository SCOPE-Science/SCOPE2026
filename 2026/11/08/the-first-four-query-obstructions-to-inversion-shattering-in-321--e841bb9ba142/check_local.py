#!/usr/bin/env python3
"""Standalone exact finite verification of the local shattering obstructions.
All computations use integer arithmetic and the Python standard library.
"""
from itertools import combinations, permutations
from math import comb

def avoids_321(p):
    n=len(p)
    return all(not (p[i]>p[j]>p[k]) for i in range(n)
               for j in range(i+1,n) for k in range(j+1,n))

def pair_types(n):
    for a,b,c in combinations(range(n),3):
        yield frozenset(((a,b),(b,c)))

def triple_types(n):
    for a,b,c,d in combinations(range(n),4):
        yield frozenset(((a,c),(a,d),(b,c)))
        yield frozenset(((a,c),(b,c),(b,d)))
        yield frozenset(((a,d),(b,c),(b,d)))

def quartic_types(n):
    for a,b,c,d,e,f in combinations(range(n),6):
        yield frozenset(((a,f),(b,c),(b,e),(d,e)))
        yield frozenset(((a,f),(b,d),(b,e),(c,e)))

def check(n):
    ps=list(permutations(range(n)))
    ps=[p for p in ps if avoids_321(p)]
    edges=list(combinations(range(n),2))
    masks=[]
    for p in ps:
        masks.append(sum((p[a]>p[b])<<i for i,(a,b) in enumerate(edges)))
    bad2=set(pair_types(n));bad3=set(triple_types(n));bad4=set(quartic_types(n))
    assert len(bad2)==comb(n,3)
    assert len(bad3)==3*comb(n,4)
    assert len(bad4)==2*comb(n,6)
    expected=(bad2,bad3,bad4)
    sizecounts=[]
    minimal_obs=[0]*5
    for k in range(5):
        total=0
        for idx in combinations(range(len(edges)),k):
            e=frozenset(edges[i] for i in idx)
            characterized=not any(o<=e for obs in expected for o in obs)
            sigs={sum(((p>>i)&1)<<j for j,i in enumerate(idx)) for p in masks}
            observed=(len(sigs)==(1<<k))
            if characterized!=observed:
                raise AssertionError((n,k,sorted(e),observed,characterized))
            total+=observed
            if not observed and all(not(o<=e) for obs in expected[:k-2] for o in obs):
                minimal_obs[k]+=1
        sizecounts.append(total)
    assert minimal_obs[2]==len(bad2)
    assert minimal_obs[3]==len(bad3)
    assert minimal_obs[4]==len(bad4)
    return (n,len(ps),sizecounts,minimal_obs)

if __name__ == '__main__':
    for n in range(1,9):
        print(check(n),flush=True)
    print('AV321_LOCAL_SHATTERING_4_PASS')
