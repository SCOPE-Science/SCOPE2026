#!/usr/bin/env python3
"""Exact independent reachability BFS and constructive / potential checks."""
from collections import deque, Counter
from itertools import combinations, permutations
from math import comb

def step(n,H,c):
    H=set(H)
    if c=='a':
        return frozenset((h+1)%n for h in H)
    if n-1 in H:
        return frozenset(H)
    if 0 in H:
        H.remove(0)
    H.add(n-1)
    return frozenset(H)

def potential(n,H):
    h=tuple(sorted(H)); k=len(h)
    if k==0:return 0
    if k==1:return 1 if h[0]==n-1 else h[0]+2
    if k==2:
        u,v=h
        if v==n-1:return n+2 if u==0 else u+3
        return n+u+3 if v==u+1 else v+3
    if k==3:
        u,v,w=h
        edges=sum((x+1)%n in H for x in H)
        if edges==0:return v+4 if w==n-1 else w+4
        if edges==1:
            if (v,w)==(n-2,n-1):return n+2
            if u==0 and w==n-1:return n+3
            x=next(x for x in (u,v) if x+1 in H)
            return n+x+4
        if (u,v,w)==(n-3,n-2,n-1):return 2*n+1
        if (u,v,w)==(0,n-2,n-1):return 2*n+2
        if (u,v,w)==(0,1,n-1):return 2*n+3
        assert v==u+1 and w==v+1
        return 2*n+u+4
    raise ValueError('only ranks up to 3')

def witnessing_word(n,H):
    # Optimization over all strictly rank-decreasing merge schedules.
    best=None
    for newest,middle,oldest in permutations(H):
        r=(newest+1)%n
        d=(middle-newest)%n
        e=(oldest-middle)%n
        if d<2 or e<2 or (d+e)%n in (0,1):continue
        w='b'+'a'*e+'b'+'a'*d+'b'+'a'*r
        if best is None or len(w)<len(best):best=w
    return best

def bfs(n):
    start=frozenset()
    dist={start:0};q=deque([start])
    while q:
        s=q.popleft()
        for a in 'ab':
            t=step(n,s,a)
            if len(t)>3:continue
            if t not in dist:
                dist[t]=dist[s]+1;q.append(t)
    return dist

def expected_hist(n):
    if n==4:return {k:1 for k in (9,10,11,12)}
    out={}
    for k in range(7,n+3):out[k]=comb(k-5,2)
    for k in range(n+3,2*n+1):out[k]=n-4
    out[2*n+1]=n-3
    for k in range(2*n+2,3*n+1):out[k]=1
    return out

def main():
    counts=Counter()
    for n in range(4,19):
        D=bfs(n)
        target={frozenset(s) for s in combinations(range(n),3)}
        assert target.issubset(D),('unreachable',n,len(target-set(D)))
        for H in target:
            p=potential(n,H)
            assert p==D[H],('BFS',n,H,p,D[H])
            w=witnessing_word(n,H)
            assert w is not None and len(w)==p,('witness_length',n,H)
            x=frozenset()
            for a in w:x=step(n,x,a)
            assert x==H,('witness_target',n,H)
            counts['bfs_triples']+=1
        hist=Counter(D[H] for H in target)
        assert dict(hist)==expected_hist(n),('hist',n,hist,expected_hist(n))
        assert sum(hist.values())==comb(n,3)
        counts['bfs_histograms']+=1
    for n in range(4,96):
        for k in range(4):
            for members in combinations(range(n),k):
                H=frozenset(members)
                for a in 'ab':
                    T=step(n,H,a)
                    if len(T)>3:continue
                    assert potential(n,T)<=potential(n,H)+1,('potential',n,H,a,T,potential(n,H),potential(n,T))
                    counts['bellman_edges']+=1
    print('VERIFY_OK')
    for name in sorted(counts):print(name,counts[name])

if __name__=='__main__':main()
