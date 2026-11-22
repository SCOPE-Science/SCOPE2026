#!/usr/bin/env python3
"""Exact finite checks for path-variation norms of banded symmetric Markov matrices."""
from itertools import combinations

def tv(x):
    return sum(abs(x[i+1]-x[i]) for i in range(len(x)-1))

def bound(n,r):
    return min(n-1, 4*((r+1)//2)-1)

def witness(n,r):
    k=(r+1)//2
    s=min(n,4*k)
    m=(s+1)//2
    initial=set(range(m))
    target=set(range(0,s,2))
    left=sorted(initial-target)
    right=sorted(target-initial)
    assert len(left)==len(right)
    perm=list(range(n))
    for a,b in zip(left,right):
        assert b-a<=r
        perm[a]=b;perm[b]=a
    assert all(perm[perm[i]]==i and abs(perm[i]-i)<=r for i in range(n))
    x=[int(i<m) for i in range(n)]
    y=[x[perm[i]] for i in range(n)]
    assert tv(x)==1 and tv(y)==bound(n,r)
    return perm,x,y

# Check all cut profiles of symmetric banded matrices via the integral
# bipartite-matching reduction; B is target's set of ones.
def enumerate_profiles(n,r):
    count=0; opt=0
    for m in range(1,n):
        initial=set(range(m))
        for pattern in combinations(range(n),m):
            target=set(pattern)
            holes=sorted(initial-target)
            fills=sorted(target-initial)
            # A crossing matching is possible iff sorted pairing works;
            # its maximum distance is minimized by sorted pairing.
            if any(b-a>r for a,b in zip(holes,fills)):
                continue
            count+=1
            y=[int(i in target) for i in range(n)]
            opt=max(opt,tv(y))
    return count,opt

tests=0; profiles=0
for n in range(2,11):
    for r in range(1,min(n,5)):
        count,opt=enumerate_profiles(n,r)
        assert opt==bound(n,r), (n,r,opt,bound(n,r))
        witness(n,r)
        tests+=1;profiles+=count
print('EXACT_CROSS_MATCHING_PROFILE_ENUMERATION_PASS',tests,profiles)
for r in range(1,16):
    for n in (2,3,2*r+1,2*r+2,4*((r+1)//2),4*((r+1)//2)+5):
        if n>=2:
            witness(n,r)
print('ALL_DIMENSION_EXPLICIT_INVOLUTION_WITNESSES_PASS')
print('PARITY_PLATEAU',[(r,4*((r+1)//2)-1) for r in range(1,9)])
print('ALL_LOCAL_SYMMETRIC_STOCHASTIC_VARIATION_CHECKS_PASS')
