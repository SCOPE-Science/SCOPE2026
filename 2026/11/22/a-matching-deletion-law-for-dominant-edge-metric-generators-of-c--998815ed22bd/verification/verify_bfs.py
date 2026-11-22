#!/usr/bin/env python3
"""Independent shortest-path and exhaustive sensor-set verifier for matching-deleted bicliques."""
from collections import Counter, deque
from math import comb


def predicted(m, n, t):
    N=m+n
    c=Counter()
    for j in range(t+1):
        c[j]+=2*comb(t,j)
        c[j+1]+=(N-2*t)*comb(t,j)
    c[0]-=1
    c[2]+=t
    return Counter({i:v for i,v in c.items() if v})


def predicted_minimal(m,n,t):
    N=m+n;u=m-t;v=n-t
    c=Counter()
    c[N-t-1]+=u+v
    c[N-2]+=t
    c[N-t]+=int(u==0)+int(v==0)
    return Counter({i:x for i,x in c.items() if x})


def verify(m,n,t):
    N=m+n
    edges=[(a,m+b) for a in range(m) for b in range(n) if not(a==b and a<t)]
    adj=[[] for _ in range(N)]
    for a,b in edges:
        adj[a].append(b);adj[b].append(a)
    D=[]
    for source in range(N):
        dist=[-1]*N;dist[source]=0;Q=deque([source])
        while Q:
            v=Q.popleft()
            for w in adj[v]:
                if dist[w]<0:dist[w]=dist[v]+1;Q.append(w)
        assert min(dist)>=0, (m,n,t,'disconnected')
        D.append([min(dist[a],dist[b]) for a,b in edges])
    counts=Counter()
    minimum_counts=Counter()
    feasible=set()
    for mask in range(1<<N):
        if any(not(mask>>a&1 or mask>>b&1) for a,b in edges):continue
        codes=[tuple(D[v][i] for v in range(N) if mask>>v&1) for i in range(len(edges))]
        if len(set(codes))==len(edges):
            counts[N-mask.bit_count()]+=1
            if all((mask & ~(1<<v)) not in feasible for v in range(N) if mask>>v&1):
                minimum_counts[mask.bit_count()]+=1
            feasible.add(mask)
    assert counts==predicted(m,n,t),(m,n,t,counts,predicted(m,n,t))
    assert minimum_counts==predicted_minimal(m,n,t),(m,n,t,minimum_counts,predicted_minimal(m,n,t))
    return sum(counts.values())

if __name__=='__main__':
    cases=0
    for m in range(3,7):
        for n in range(3,7):
            if m+n>11:continue
            for t in range(min(m,n)+1):
                verify(m,n,t)
                cases+=1
    print('PASS: BFS all-pairs edge-distance signatures, explicit vertex-cover and minimality checks,')
    print(f'      all {cases} parameter cases with m,n>=3, m+n<=11, 0<=t<=min(m,n).')
