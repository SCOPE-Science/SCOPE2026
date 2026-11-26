#!/usr/bin/env python3
"""Finite checks for one-subdivided complete graphs; standard library only."""
from itertools import combinations
from collections import deque,Counter
from math import comb
for n in [4,5,6]:
    original=list(range(n)); pairs=list(combinations(range(n),2)); N=n+len(pairs)
    adj=[set() for _ in range(N)]
    for k,(a,b) in enumerate(pairs):
        v=n+k
        for w in (a,b):adj[v].add(w);adj[w].add(v)
    dist=[]
    for v in range(N):
        d=[-1]*N;d[v]=0;todo=deque([v])
        while todo:
            w=todo.popleft()
            for u in adj[w]:
                if d[u]==-1:d[u]=d[w]+1;todo.append(u)
        assert all(x>=0 for x in d)
        dist.append(d)
    mmd={(i,j) for i in range(N) for j in range(i+1,N) if all(dist[w][j]<=dist[i][j] for w in adj[i]) and all(dist[i][w]<=dist[i][j] for w in adj[j])}
    prediction={(n+i,n+j) for i in range(len(pairs)) for j in range(i+1,len(pairs)) if not(set(pairs[i])&set(pairs[j]))}
    assert mmd==prediction,(n,len(mmd),len(prediction),mmd^prediction)
    # Enumerate all independent subsets of KG(n,2) by an explicit pair-disjointness predicate.
    independent=[]
    for mask in range(1<<len(pairs)):
        chosen=[pairs[i] for i in range(len(pairs)) if mask>>i&1]
        if all(set(a)&set(b) for a,b in combinations(chosen,2)):
            independent.append(mask)
    sizes=Counter(mask.bit_count() for mask in independent)
    expected={0:1,1:comb(n,2),2:n*comb(n-1,2)}
    for k in range(3,n):expected[k]=n*comb(n-1,k)+(comb(n,3) if k==3 else 0)
    assert dict(sizes)==expected,(n,sizes,expected)
    maxsize=max(sizes)
    maxset=[m for m in independent if m.bit_count()==maxsize]
    if n>=5:assert len(maxset)==n
    else:assert len(maxset)==8
    # General vertex-cover correspondence: all n original vertices form isolated SR vertices.
    # Connect two minimum vertex covers at replacement budget r (set symmetric difference <=2r).
    maxr=0;thresh=None; degree_at_thresh=None;diam_at_thresh=None
    for r in range(1,n+2):
        newadj=[set() for _ in maxset]
        for i,j in combinations(range(len(maxset)),2):
            if (maxset[i]^maxset[j]).bit_count()//2<=r:
                newadj[i].add(j);newadj[j].add(i)
        seen={0}; todo=[0]
        for x in todo:
            for y in newadj[x]:
                if y not in seen:seen.add(y);todo.append(y)
        if len(seen)==len(maxset):
            thresh=r;degree_at_thresh=Counter(map(len,newadj))
            diam_at_thresh=max(max(bfs_distance(newadj,src).values()) for src in range(len(maxset))) if False else None
            # BFS independently from each vertex.
            diam_at_thresh=0
            for src in range(len(maxset)):
                d={src:0};q=[src]
                for x in q:
                    for y in newadj[x]:
                        if y not in d:d[y]=d[x]+1;q.append(y)
                assert len(d)==len(maxset)
                diam_at_thresh=max(diam_at_thresh,max(d.values()))
            break
    assert (thresh,diam_at_thresh)==((1,3) if n==4 else (n-2,1))
    print(f'n={n} graph_vertices={N} graph_edges={2*len(pairs)} mmd_edges={len(mmd)} independence_coefficients={[sizes[k] for k in range(n)]} strong_dimension={len(pairs)-maxsize} minimum_bases={len(maxset)} exchange_threshold={thresh} degree_profile={dict(degree_at_thresh)} exchange_diameter={diam_at_thresh}')
print('PASS: direct distance/MMD graph, independent-family polynomial, optimal exchanges.')
