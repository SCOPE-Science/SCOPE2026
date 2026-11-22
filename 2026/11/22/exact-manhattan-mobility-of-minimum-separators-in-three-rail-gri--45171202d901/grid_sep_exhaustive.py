#!/usr/bin/env python3
"""Standalone direct graph check of exact three-rail terminal separators.
No external dependencies. Tests are finite and support, but do not replace, the theorem.
"""
from itertools import combinations
from collections import deque


def check(n):
    V = [(r,c) for r in range(3) for c in range(n)]
    vertices = set(V)
    graph = {v: {w for w in ((v[0]-1,v[1]), (v[0]+1,v[1]),
                    (v[0],v[1]-1),(v[0],v[1]+1)) if w in vertices} for v in V}
    s=(1,0);t=(1,n-1)
    def separates(deleted):
        visited={s}; queue=deque([s])
        while queue:
            v=queue.popleft()
            for w in graph[v]:
                if w not in deleted and w not in visited:
                    visited.add(w); queue.append(w)
        return t not in visited
    # Verify two-vertex deletion cannot separate and hence the minimum is three.
    for p in combinations((v for v in V if v not in (s,t)),2):
        assert not separates(set(p)), (n,p)
    cuts={frozenset(p) for p in combinations((v for v in V if v not in (s,t)),3) if separates(set(p))}
    formula={frozenset(((0,i),(1,j),(2,k)))
             for j in range(1,n-1)
             for i in range(j-1,j+2) for k in range(j-1,j+2)}
    assert cuts==formula, (n,'classification',len(cuts),len(formula))
    seq=list(sorted(cuts, key=lambda c:tuple(sorted(c))))
    lookup={setval:ind for ind,setval in enumerate(seq)}
    adj=[set() for _ in seq]
    for ind,S in enumerate(seq):
        for u in S:
            for v in graph[u]:
                if v in S:continue
                dest=frozenset((S-{u})|{v})
                if dest in lookup:adj[ind].add(lookup[dest])
    assert sum(map(len,adj))//2==16*n-36
    # Independently compute all shortest paths from the ORIGINAL graph adjacency.
    radii=[]
    for ind,S in enumerate(seq):
        d={ind:0};queue=deque([ind])
        while queue:
            x=queue.popleft()
            for y in adj[x]:
                if y not in d: d[y]=d[x]+1;queue.append(y)
        assert len(d)==len(seq),(n,'disconnected',ind)
        a=tuple(next(c for r,c in S if r==row) for row in (0,1,2))
        left=sum(abs(x-1) for x in a)
        right=sum(abs(x-(n-2)) for x in a)
        assert max(d.values())==2+max(left,right),(n,'ecc',a,max(d.values()))
        for other_ind,T in enumerate(seq):
            b=tuple(next(c for r,c in T if r==row) for row in (0,1,2))
            assert d[other_ind]==sum(abs(a[x]-b[x]) for x in range(3)),(n,a,b,d[other_ind])
        radii.append(max(d.values()))
    assert min(radii)==2+(3*(n-3)+1)//2
    assert max(radii)==3*n-5
    print(f'n={n} cuts={len(cuts)} slide_edges={sum(map(len,adj))//2} radius={min(radii)} diameter={max(radii)} all_pairs=verified')

if __name__=='__main__':
    for n in range(3,10):check(n)
    print('DIRECT_GRID_EXHAUSTIVE_OK')
