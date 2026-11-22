#!/usr/bin/env python3
"""Unparametrized exhaustive search over all minimum-cardinality vertex subsets.
Uses integer bitmasks, no reliance on functional candidate generation.
"""
from itertools import combinations
from collections import Counter


def process(q):
    words=[(a,b) for a in range(q) for b in range(q) if a!=b]
    masks=[]
    for (a,b) in words:
        ball={(a,b)}|{(b,c) for c in range(q) if c!=b}
        masks.append(sum(1<<words.index(w) for w in ball))
    N=len(words); k=q*(q-2)
    cnt=0; codes=set()
    for slots in combinations(range(N),k):
        m=sum(1<<i for i in slots)
        signatures=[m&v for v in masks]
        if 0 not in signatures and len(set(signatures))==N:
            cnt+=1
            codes.add(m)
    assert cnt==(q-1)**q-q*(q-1), (q,cnt)
    # Every code must have at least q-2 selected in each column:
    # if 2 omitted within a column, these vertices have identical outgoing balls.
    for mask in codes:
        for b in range(q):
            selected=sum(bool((mask>>i)&1) for i,(a,j) in enumerate(words) if j==b)
            assert selected==q-2
    if q==4:
        deg=Counter(sum((x^y).bit_count()==2 for y in codes) for x in codes)
        assert deg == {8:9,7:48,6:12}, deg
        print("independent q4 swap degrees:",dict(deg))
    return cnt

for q in (3,4,5):
    print('q=',q,'unrestricted optimal subsets=',process(q))
