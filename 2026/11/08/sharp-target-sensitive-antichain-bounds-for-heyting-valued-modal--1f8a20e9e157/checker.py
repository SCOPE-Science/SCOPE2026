#!/usr/bin/env python3
"""Exact finite checks of target-sensitive meet certificates (no external data)."""
from itertools import combinations, product
from random import Random

def posets(n):
    edgelist=list(combinations(range(n),2))
    seen=set()
    for mask in range(1 << len(edgelist)):
        reach=[1 << i for i in range(n)]
        for t,(i,j) in enumerate(edgelist):
            if mask>>t & 1: reach[i] |= 1 << j
        for k in range(n):
            for i in range(n):
                if reach[i]>>k & 1: reach[i] |= reach[k]
        key=tuple(reach)
        if key not in seen:
            seen.add(key)
            yield key

def ideals(P):
    n=len(P)
    return [x for x in range(1<<n) if all(not (x>>j&1) or (x>>i&1) for i in range(n) for j in range(n) if P[i]>>j&1)]

def boundaries(P,m):
    missing=((1<<len(P))-1)^m
    return [j for j in range(len(P)) if missing>>j&1 and all(not (P[i]>>j&1) or not (missing>>i&1) or i==j for i in range(len(P)))]

def common(A,full):
    v=full
    for a in A: v&=a
    return v

def optimum(family,full):
    target=common(family,full)
    for k in range(len(family)+1):
        for ids in combinations(range(len(family)),k):
            if common([family[j] for j in ids],full)==target:
                return k
    assert False

count=0; worst=0; tight=0; exact_ideals=0
for n in (1,2,3):
    for P in posets(n):
        I=ideals(P); full=(1<<n)-1
        exact_ideals+=len(I)
        for mask in range(1<<len(I)):
            S=[v for i,v in enumerate(I) if mask>>i&1]
            target=common(S,full)
            b=len(boundaries(P,target))
            o=optimum(S,full)
            assert o<=b,(P,S,target,b,o)
            worst=max(worst,o)
            count+=1
        for m in I:
            M=boundaries(P,m)
            witnesses=[full & ~P[j] for j in M]
            assert all(x in I for x in witnesses)
            assert common(witnesses,full)==m
            assert optimum(witnesses,full)==len(M)
            tight+=1

rng=Random(0xC0FFEE)
for P in posets(4):
    I=ideals(P); full=(1<<4)-1
    for _ in range(250):
        S=[v for v in I if rng.getrandbits(1)]
        m=common(S,full)
        assert optimum(S,full)<=len(boundaries(P,m))
        count+=1
    for m in I:
        M=boundaries(P,m)
        witnesses=[full&~P[j] for j in M]
        assert common(witnesses,full)==m
        assert optimum(witnesses,full)==len(M)
        tight+=1
print('LOCAL_MEET_BOUND_OK', 'families_checked',count,'sharp_targets',tight,'small_ideals',exact_ideals,'observed_min_size_max',worst)

# Paired one-step box claims: all witnesses are indispensable in a star.
for P in posets(4):
    I=ideals(P); full=(1<<4)-1
    for m1,m2 in product(I,repeat=2):
        M1,M2=boundaries(P,m1),boundaries(P,m2)
        states=[(full&~P[j],full) for j in M1]+[(full,full&~P[j]) for j in M2]
        assert common((a for a,b in states),full)==m1
        assert common((b for a,b in states),full)==m2
        for k in range(len(states)):
            kept=states[:k]+states[k+1:]
            assert (common((a for a,b in kept),full),common((b for a,b in kept),full)) != (m1,m2)
print('JOINT_STAR_SHARPNESS_OK')
