#!/usr/bin/env python3
"""Independent full state-graph BFS check of the non-surjective word model."""
from itertools import product
from collections import deque, Counter
for n in range(4,10):
    states=[w for w in product(range(3),repeat=n) if len(set(w))<=2]
    key={w:i for i,w in enumerate(states)}
    assert len(states)==3*2**n-3
    g=[]
    for w in states:
        edges=[]
        for j in range(n):
            for sym in range(3):
                if sym==w[j]:continue
                cand=w[:j]+(sym,)+w[j+1:]
                if cand in key:edges.append(key[cand])
        g.append(edges)
    assert sum(map(len,g))//2==3*n*(2**(n-1)+1)
    diameter=0
    for i in range(len(states)):
        ds=[-1]*len(states)
        ds[i]=0
        q=deque([i])
        while q:
            a=q.popleft()
            for b in g[a]:
                if ds[b]<0:
                    ds[b]=ds[a]+1
                    q.append(b)
        assert all(v>=0 for v in ds), ('disconnect',n,i)
        diameter=max(diameter,max(ds))
    assert diameter==n+n//2-1,(n,diameter)
    print(f'n={n} words={len(states)} edges={sum(map(len,g))//2} diameter={diameter} connected')
print('WORD_BFS_OK')
