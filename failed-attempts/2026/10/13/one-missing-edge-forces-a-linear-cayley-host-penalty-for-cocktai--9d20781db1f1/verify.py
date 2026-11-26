#!/usr/bin/env python3
"""Verify the constructive cyclic hosts for the stated graph family."""
from collections import deque

def component_sizes(adj):
    unseen=set(adj)
    out=[]
    while unseen:
        root=min(unseen);unseen.remove(root);Q=deque([root]);num=0
        while Q:
            x=Q.popleft();num+=1
            for y in adj[x]:
                if y in unseen:unseen.remove(y);Q.append(y)
        out.append(num)
    return sorted(out,reverse=True)

def check(r):
    n=3*r-1
    used=[];p=0
    for k in [4]+[2]*(r-2):
        used.extend(range(p,p+k))
        p+=k+1
    assert p==n and len(used)==2*r and len(set(used))==2*r
    # These are the edges of the complement of the induced host.
    nbrs={v:set() for v in used}
    for i,a in enumerate(used):
        for b in used[i+1:]:
            if (a-b)%n in (1,n-1):nbrs[a].add(b);nbrs[b].add(a)
    assert component_sizes(nbrs)==[4]+[2]*(r-2)
    assert sum(len(v) for v in nbrs.values())//2==r+1
    assert sorted(len(x) for x in nbrs.values())==sorted([2,2]+[1]*(2*r-2))
    assert n==3*r-1
    # For any regular complementary host of degree d >= 2,
    # d*(2*r-t) <= 2*(r+1) forces t >= r-1.
    for t in range(r-1):
        for d in range(2,2*r+t):
            assert d*(2*r-t)>2*(r+1)

for r in range(2,101):check(r)
print("PASS: 99 cyclic complementary embeddings (r=2..100), component profiles, edge counts, and lower-bound inequalities")
