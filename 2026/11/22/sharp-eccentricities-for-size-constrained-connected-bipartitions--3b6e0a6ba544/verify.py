#!/usr/bin/env python3
"""Exhaustive independent checker for two unnamed connected cyclic districts.
Run: python3 verify.py
No external dependencies.
"""
from collections import Counter, deque


def states(n, s):
    return [(a,b) for a in range(n) for b in range(a+1,n)
            if s <= b-a <= n-s]


def adjacency(n, ss):
    lookup={p:i for i,p in enumerate(ss)}
    adj=[set() for _ in ss]
    for i, (a,b) in enumerate(ss):
        for old in (a,b):
            for new in ((old-1)%n,(old+1)%n):
                p=tuple(sorted(({a,b}-{old})|{new}))
                j=lookup.get(p)
                if j is not None and j != i:
                    adj[i].add(j)
    return adj


def transport(n,A,B):
    a,b=A; c,d=B
    return min(
        [abs(c+q*n-a)+abs(d+q*n-b) for q in range(-2,3)]+ \
        [abs(d+q*n-a)+abs(c+(q+1)*n-b) for q in range(-2,3)]
    )


def check(n,s):
    ss=states(n,s); adj=adjacency(n,ss)
    assert len(ss)==n*(n-2*s+1)//2,(n,s,len(ss))
    assert sum(map(len,adj))//2==n*(n-2*s),(n,s,'edges')
    paircount=0
    if n==2*s:
        assert all(len(v)==0 for v in adj)
        return len(ss),paircount
    for i,A in enumerate(ss):
        dist=[-1]*len(ss);dist[i]=0; dq=deque([i])
        while dq:
            x=dq.popleft()
            for y in adj[x]:
                if dist[y]<0:
                    dist[y]=dist[x]+1;dq.append(y)
        assert -1 not in dist,(n,s,i,'disconnected')
        d=min((A[1]-A[0]),n-(A[1]-A[0]))
        assert max(dist)==max(n//2,n-s-d),(n,s,A,'ecc',max(dist))
        for j,B in enumerate(ss):
            predicted=transport(n,A,B)
            assert dist[j]==predicted, (n,s,A,B,dist[j],predicted)
            paircount+=1
    return len(ss),paircount

if __name__=='__main__':
    tested=0;pairs=0; states_total=0
    for n in range(3,31):
        for s in range(1,n//2+1):
            nstates,npairs=check(n,s)
            tested+=1; pairs+=npairs; states_total+=nstates
    print(f'PASS: {tested} (n,s) cases, {states_total} case-state incidences, {pairs} ordered-pair distances')
    print('Verified n=3..30 and every s=1..floor(n/2), including frozen n=2s.')
