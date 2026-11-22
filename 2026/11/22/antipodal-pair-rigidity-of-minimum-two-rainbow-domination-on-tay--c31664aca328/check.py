#!/usr/bin/env python3
"""Reproduce the finite two-rainbow classification using standard Python only."""
from itertools import combinations

def icosahedron():
    adj = [set() for _ in range(12)]
    def join(a,b): adj[a].add(b); adj[b].add(a)
    for i in range(5):
        u,v=2+i,7+i
        join(0,u); join(1,v)
        join(u,2+(i+1)%5); join(v,7+(i+1)%5)
        join(u,v); join(u,7+(i-1)%5)
    return adj

def johnson63():
    vertices=list(combinations(range(6),3)); n=len(vertices)
    return [{j for j in range(n) if j!=i and len(set(t)&set(vertices[j]))==2} for i,t in enumerate(vertices)]

def bfs(A,start):
    d={start:0}; q=[start]
    for u in q:
        for v in A[u]:
            if v not in d: d[v]=d[u]+1; q.append(v)
    return d

def verify(A,expected):
    n=len(A); k=len(A[0]); assert n==2*(k+1)
    assert all(len(s)==k and i not in s for i,s in enumerate(A))
    assert all(i in A[j] for i,s in enumerate(A) for j in s)
    D=[bfs(A,i) for i in range(n)]
    assert all(len(x)==n for x in D)
    ant=[next(j for j in range(n) if D[i][j]==3) for i in range(n)]
    assert all(sum(D[i][j]==3 for j in range(n))==1 for i in range(n))
    assert all(ant[ant[i]]==i for i in range(n))
    assert all(not (A[i]&A[ant[i]]) and len(A[i]|A[ant[i]])==n-2 for i in range(n))
    pairs=list(combinations(range(n),2))
    def valid(a,b):
        colored=set(a)|set(b)
        return all((A[v]&set(a)) and (A[v]&set(b)) for v in range(n) if v not in colored)
    candidates=[(a,b) for a in pairs for b in pairs if valid(a,b)]
    predicted={(a,b) for a in pairs if D[a[0]][a[1]]==3 for b in pairs if D[b[0]][b[1]]==3}
    assert set(candidates)==predicted and len(candidates)==expected
    # Exact check that no weight <=3 function exists: no support of size <=1 can cover all empties.
    for s in range(1,4):
        for x in range(s+1):
            y=s-x
            if x>n or y>n: continue
            for aa in combinations(range(n),x):
                for bb in combinations(range(n),y):
                    assert not valid(aa,bb)
    from collections import Counter
    near=Counter((D[i][j],len(A[i]&A[j])) for i,j in pairs)
    print(f"n={n} degree={k} antipodal_pairs={n//2} minimum_weight=4 optimal_named_functions={len(candidates)} pair_profiles={dict(sorted(near.items()))}")
    if n==12:
        assert near=={(1,2):30,(2,2):30,(3,0):6}
        for i,j in pairs:
            if D[i][j]==2:
                leftover=set(range(n))-{i,j}-A[i]-A[j]
                assert len(leftover)==2 and next(iter(leftover)) in A[next(iter(leftover-{next(iter(leftover))}))]

if __name__=='__main__':
    verify(icosahedron(),36)
    verify(johnson63(),100)
    print('PASS')
