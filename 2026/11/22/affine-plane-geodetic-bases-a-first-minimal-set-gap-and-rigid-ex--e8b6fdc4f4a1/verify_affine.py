#!/usr/bin/env python3
"""Exact geodetic-set census in affine incidence graphs over GF(2),GF(3),GF(4).
An independent all-pairs BFS constructs the union of every shortest path.
No precomputed structural formula is used to test subsets.
"""
from itertools import combinations
from collections import deque, Counter


def field(q):
    if q in (2, 3):
        return lambda a,b:(a+b)%q, lambda a,b:(a*b)%q
    if q==4:
        # GF(4) = GF(2)[t]/(t^2+t+1), elements a0+2*a1*t
        def mul(a,b):
            u=(a&1)*(b&1)
            v=((a&1)*((b>>1)&1))^(((a>>1)&1)*(b&1))
            w=((a>>1)&1)*((b>>1)&1)
            return (u^w)|(2*(v^w))
        return lambda a,b:a^b, mul
    raise ValueError(q)

def graph(q):
    plus,times=field(q)
    pts=[(x,y) for x in range(q) for y in range(q)]
    # lines y=m*x+b (m,b) and x=b (vertical)
    lines=[(m,b) for m in range(q) for b in range(q)]+[(q,b) for b in range(q)]
    n=len(pts);adj=[0]*(n+len(lines))
    for i,(x,y) in enumerate(pts):
        for j,(m,b) in enumerate(lines):
            if (x==b if m==q else y==plus(times(m,x),b)):
                k=n+j
                adj[i]|=1<<k;adj[k]|=1<<i
    assert all(x.bit_count()==q+1 for x in adj[:n])
    assert all(x.bit_count()==q for x in adj[n:])
    return adj,pts,lines

def interval_masks(adj):
    N=len(adj)
    d=[[99]*N for _ in range(N)]
    for s in range(N):
        d[s][s]=0;queue=deque([s])
        while queue:
            u=queue.popleft()
            for v in range(N):
                if adj[u]>>v &1 and d[s][v]==99:
                    d[s][v]=d[s][u]+1;queue.append(v)
        assert max(d[s])<99
    return [[sum(1<<v for v in range(N) if d[i][v]+d[v][j]==d[i][j]) for j in range(N)] for i in range(N)]

def classify(q):
    adj,pts,lines=graph(q)
    it=interval_masks(adj)
    n=len(pts);N=len(adj);FULL=(1<<N)-1
    def geodetic(c):
        acc=0
        for i in c:
            for j in c:
                if i<j: acc|=it[i][j]
        return acc==FULL
    family=[frozenset(n+j for j,(m,b) in enumerate(lines) if m==s) for s in range(q+1)]
    assert len(set(family))==q+1
    for F in family:
        assert len(F)==q and geodetic(F)
    bcount=Counter(); extra=[]; qcount=0
    for k in (q,q+1):
        for c in combinations(range(N),k):
            if geodetic(c):
                if k==q:
                    qcount+=1
                    assert frozenset(c) in family,(q,c)
                else:
                    bcount[sum(i>=n for i in c)]+=1
                    if not any(F.issubset(c) for F in family):extra.append(c)
    if q==2:
        assert qcount==3 and len(extra)==6 and all(sum(i>=n for i in c)==1 for c in extra),len(extra)
    else:
        assert qcount==q+1 and not extra,(q,len(extra),extra[:5])
    print('q',q,'vertices',N,'geodetic minimum',qcount,'geodetic size q+1 by selected lines',dict(sorted(bcount.items())),'inclusion-minimal size q+1',len(extra))

if __name__=='__main__':
    for q in (2,3,4): classify(q)
