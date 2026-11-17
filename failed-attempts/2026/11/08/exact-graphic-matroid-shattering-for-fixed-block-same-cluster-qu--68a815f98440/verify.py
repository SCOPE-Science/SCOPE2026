#!/usr/bin/env python3
"""Finite cross-check of pairwise same-block shattering for fixed-block partitions."""
from itertools import combinations
from functools import lru_cache


def partitions(n):
    def extend(a, largest):
        if len(a)==n:
            yield tuple(a)
        else:
            for j in range(largest+2):
                yield from extend(a+[j],max(largest,j))
    yield from extend([0],0)


def forest(n,edges):
    parent=list(range(n))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]];x=parent[x]
        return x
    for u,v in edges:
        a,b=find(u),find(v)
        if a==b:return False
        parent[a]=b
    return True


def support_shattered(subset,concepts):
    if not subset:return bool(concepts)
    target=1<<len(subset)
    if len(concepts)<target:return False
    observations=set()
    for word in concepts:
        code=sum(((word>>i)&1)<<j for j,i in enumerate(subset))
        observations.add(code)
        if len(observations)==target:return True
    return False


def check(n,sample=False):
    edges=list(combinations(range(n),2)); m=len(edges)
    all_masks={k:[] for k in range(2,n+1)}
    for p in partitions(n):
        k=max(p)+1
        if k>=2:
            all_masks[k].append(sum((p[u]==p[v])<<i for i,(u,v) in enumerate(edges)))
    supports=range(1<<m) if not sample else (set([0, (1<<m)-1]) | {s for s in range(1<<m) if s.bit_count()<=3 or (s*37+17)%59==0})
    total=0
    for S in supports:
        idx=[i for i in range(m) if (S>>i)&1]
        acyclic=forest(n,[edges[i] for i in idx])
        for k in range(2,n+1):
            predicted=acyclic and len(idx)<=n-k
            found=support_shattered(idx,all_masks[k])
            assert predicted==found, (n,k,idx,predicted,found)
            total+=1
    return total


def exchange(n):
    edges=list(combinations(range(n),2)); m=len(edges)
    for k in range(2,n+1):
        rank=n-k
        bases=[set(c) for c in combinations(range(m),rank) if forest(n,[edges[i] for i in c])]
        for B in bases:
            for D in bases:
                for e in B-D:
                    assert any(forest(n,[edges[i] for i in (B-{e})|{f}]) for f in D-B), (n,k,B,D,e)
    return True



def trace_feasibility(n, positive, negative, q, edge_list):
    """Contraction/chromatic test; no partition witnesses used."""
    parent=list(range(n))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]];x=parent[x]
        return x
    for i,(a,b) in enumerate(edge_list):
        if positive>>i&1:
            x,y=find(a),find(b);parent[x]=y
    roots=[find(i) for i in range(n)]
    names={x:j for j,x in enumerate(sorted(set(roots)))}
    comps=len(names)
    if q>comps:return False
    adj=[0]*comps
    for i,(a,b) in enumerate(edge_list):
        if negative>>i&1:
            x,y=names[roots[a]], names[roots[b]]
            if x==y:return False
            adj[x]|=1<<y;adj[y]|=1<<x
    order=sorted(range(comps), key=lambda i:adj[i].bit_count(),reverse=True)
    col=[-1]*comps
    def rec(k):
        if k==comps:return True
        i=order[k]
        for color in range(q):
            if not any(col[j]==color for j in range(comps) if adj[i]>>j&1):
                col[i]=color
                if rec(k+1):return True
                col[i]=-1
        return False
    return rec(0)


def check_trace(n, sample=False):
    edges=list(combinations(range(n),2)); m=len(edges)
    full=(1<<m)-1
    concepts={q:[] for q in range(1,n+1)}
    for p in partitions(n):
        q=max(p)+1
        w=sum((p[a]==p[b])<<i for i,(a,b) in enumerate(edges))
        concepts[q].append(w)
    total=0
    for P in range(1<<m):
        rest=full ^ P
        N=rest
        while True:
            if (not sample) or ((P+37*N)%47==0):
                for q in range(1,n+1):
                    expected=trace_feasibility(n,P,N,q,edges)
                    actual=any(w&P==P and w&N==0 for w in concepts[q])
                    assert expected==actual, (n,q,P,N,expected,actual)
                    total+=1
            if N==0:break
            N=(N-1)&rest
    return total

if __name__=='__main__':
    t=0
    for n in range(2,6):
        q=check(n); t+=q
        assert exchange(n)
        print('all subsets checked for n',n,':',q,'partition-support pairs')
    for n in range(2,6):
        t_trace=check_trace(n,sample=(n==5));print('trace checks at n',n,':',t_trace)
    q=check(6,sample=True);t+=q
    print('sampled subsets checked for n 6:',q)
    print('FIXED_BLOCK_PARTITION_SHATTERING_PASS',t,'partition-support cases')
