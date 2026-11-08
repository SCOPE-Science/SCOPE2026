#!/usr/bin/env python3
"""Exact checks for parity-restricted acyclic orientations of complete bipartite graphs.

No external packages or network resources are required.
"""
from itertools import product
from collections import deque


def criterion(m,n,odd):
    return (sum(odd) - m*n) % 2 == 0 and not all(odd)


def is_correct(m,n,odd,arc):
    edges={(i,m+j) for i in range(m) for j in range(n)}
    assert len(arc)==m*n
    assert {frozenset((u,v)) for u,v in arc}=={frozenset(x) for x in edges}
    N=m+n
    indeg=[0]*N; adj=[[] for _ in range(N)]
    for u,v in arc:
        indeg[v]+=1; adj[u].append(v)
    if any((indeg[i]%2)!=odd[i] for i in range(N)):return False
    d=indeg[:]; q=deque(i for i in range(N) if not d[i]); count=0
    while q:
        u=q.popleft(); count+=1
        for v in adj[u]:
            d[v]-=1
            if d[v]==0:q.append(v)
    return count==N


def constructive(m,n,odd):
    """Construct orientation recursively using the safe-source argument."""
    A=list(range(m)); B=list(range(m,m+n)); odd=list(odd)
    def build(A,B,p):
        if len(A)==1:
            h=A[0]
            return [(h,v) if p[v] else (v,h) for v in B]
        if len(B)==1:
            h=B[0]
            return [(h,v) if p[v] else (v,h) for v in A]
        a0=sum(p[v]==0 for v in A); b0=sum(p[v]==0 for v in B)
        q=sum(p[v]==(len(B)%2) for v in A)+sum(p[v]==(len(A)%2) for v in B)
        chosen=None
        for v in A+B:
            if p[v]:continue
            if v in A:
                if a0-1+len(B)-b0>0 and q-(len(B)%2==0)>0:
                    chosen=v; break
            else:
                if b0-1+len(A)-a0>0 and q-(len(A)%2==0)>0:
                    chosen=v; break
        assert chosen is not None,(len(A),len(B),a0,b0,q)
        if chosen in A:
            nxt=p[:]
            for v in B:nxt[v]^=1
            return [(chosen,v) for v in B]+build([v for v in A if v!=chosen],B,nxt)
        else:
            nxt=p[:]
            for v in A:nxt[v]^=1
            return [(chosen,v) for v in A]+build(A,[v for v in B if v!=chosen],nxt)
    assert criterion(m,n,odd)
    return build(A,B,odd)


def direct_signature_set(m,n):
    ed=[(a,m+b) for a in range(m) for b in range(n)]
    N=m+n
    seen=set()
    for mask in range(1<<(m*n)):
        indeg=[0]*N; adj=[[] for _ in range(N)]
        for i,(u,v) in enumerate(ed):
            if mask>>i&1: u,v=v,u
            indeg[v]+=1;adj[u].append(v)
        deg=indeg[:];q=deque(i for i in range(N) if not deg[i]);count=0
        while q:
            u=q.popleft();count+=1
            for v in adj[u]:
                deg[v]-=1
                if deg[v]==0:q.append(v)
        if count==N:
            seen.add(tuple(d%2 for d in indeg))
    return seen


def main():
    for m in range(1,5):
        for n in range(1,5):
            seen=direct_signature_set(m,n)
            should={p for p in product(range(2),repeat=m+n) if criterion(m,n,p)}
            assert seen==should,('EXHAUSTIVE',m,n,seen^should)
            assert len(seen)==2**(m+n-1)-(m%2==0 and n%2==0)
            for p in should:
                arc=constructive(m,n,p)
                assert is_correct(m,n,p,arc),('CONSTRUCT',m,n,p)
            print('ALL_ORIENTATIONS_AND_PARITIES_OK',m,n,len(seen))
    ncase=0
    for m in range(1,13):
        for n in range(1,13):
            for a0 in range(m+1):
                for b0 in range(n+1):
                    odd=([0]*a0+[1]*(m-a0)+[0]*b0+[1]*(n-b0))
                    if not criterion(m,n,odd):continue
                    arc=constructive(m,n,odd)
                    assert is_correct(m,n,odd,arc),(m,n,a0,b0)
                    ncase+=1
    print('ALL_PARITY_COUNT_PROFILES_CONSTRUCTIVE_OK',ncase,'profiles, m,n=1..12')
    print('VERIFY_OK')

if __name__=='__main__':main()
