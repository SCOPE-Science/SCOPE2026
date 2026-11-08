#!/usr/bin/env python3
"""Reproducible checks for vertex shattering of monotone paths in a three-column strip."""
from itertools import combinations
from functools import lru_cache
from math import comb, floor, log2

def concepts(b):
    return [(r,s) for r in range(b+1) for s in range(r,b+1)]

def queries(b):
    return [('L',y) for y in range(1,b+1)] + [('M',y) for y in range(b+1)] + [('R',y) for y in range(b)]

def incidence(q,h):
    c,y=q; r,s=h
    if c=='L':return r>=y
    if c=='M':return r<=y<=s
    if c=='R':return s<=y
    raise ValueError(q)

def classifies_pair(q1,q2,b):
    a,i=q1;c,j=q2
    if a==c=='M':return i!=j
    if (a,c)==('L','M'):return i<=j and i<b
    if (a,c)==('M','L'):return j<=i and j<b
    if (a,c)==('M','R'):return i<=j and j>=1
    if (a,c)==('R','M'):return j<=i and i>=1
    if (a,c)==('L','R'):return i<=j
    if (a,c)==('R','L'):return j<=i
    return False

def direct_paths(b):
    # Independently enumerate all position words with exactly two E steps.
    a=[]
    for E in combinations(range(b+2),2):
        x=y=0;v=set()
        for z in range(b+2):
            if z in E:x+=1
            else:y+=1
            v.add((x,y))
        a.append(v)
    return a

def check():
    for b in range(2,13):
        H=concepts(b);Q=queries(b)
        assert len(H)==(b+1)*(b+2)//2
        assert len(Q)==3*b+1
        assert all(0 < sum(incidence(q,h) for h in H)<len(H) for q in Q)
        pairs=0
        for q1,q2 in combinations(Q,2):
            T={(incidence(q1,h),incidence(q2,h)) for h in H}
            is_shattered=len(T)==4
            assert is_shattered==classifies_pair(q1,q2,b),(b,q1,q2,is_shattered)
            pairs+=is_shattered
        assert pairs==2*b*b+b-2,(b,pairs)
        # This is an exhaustive check of all three-query candidates.
        for sub in combinations(Q,3):
            T={tuple(incidence(q,h) for q in sub) for h in H}
            assert len(T)<8,(b,sub)
        if b<=7:
            P=direct_paths(b)
            assert len(P)==len(H)
            x2h=[]
            for vertices in P:
                x2h.append(tuple(int(((0,y) if c=='L' else (1,y) if c=='M' else (2,y)) in vertices) for c,y in Q))
            t2h=[tuple(int(incidence(q,h)) for q in Q) for h in H]
            assert set(x2h)==set(t2h)
    # Online lower and cardinality upper bounds, tested with exact recursive dimension.
    for b in range(2,11):
        H=concepts(b);Q=queries(b)
        patterns=[sum((1<<i) for i,h in enumerate(H) if incidence(q,h)) for q in Q]
        @lru_cache(None)
        def feasible(state,d):
            if d==0:return True
            if state.bit_count() < (1<<d):return False
            for p in patterns:
                a=state&p;c=state&~p
                if a.bit_count()>=(1<<(d-1)) and c.bit_count()>=(1<<(d-1)):
                    if feasible(a,d-1) and feasible(c,d-1):return True
            return False
        state=(1<<len(H))-1
        d=max(t for t in range(len(H).bit_length()) if feasible(state,t))
        k=(b+1)//2
        lower=max(2,2*(k.bit_length()-1))
        upper=len(H).bit_length()-1
        assert lower<=d<=upper,(b,d,lower,upper)
    print('THREE_COLUMN_MONOTONE_PATH_VC_ONLINE_PASS')

if __name__=='__main__':check()
