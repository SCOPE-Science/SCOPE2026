#!/usr/bin/env python3
"""Independently count shortest token-slide routes using symmetry-orbit transfer."""
from collections import deque
from math import comb,factorial


def transitions(n,st):
    m=n-1
    if st[0]=='A':
        k=st[1]
        if m-k: yield ('B',1,k),m-k
        if k: yield ('B',0,k-1),k
    else:
        _,side,k=st
        yield ('A', k+1-side),1
        if m-1-k: yield ('B',side,k+1),m-1-k
        if k: yield ('B',side,k-1),k


def shortest(n):
    root=('A',0);end=('A',n-1)
    q=deque([root]);dist={root:0};cnt={root:1}
    while q:
        s=q.popleft()
        for t,mul in transitions(n,s):
            if t not in dist:
                dist[t]=dist[s]+1;cnt[t]=0;q.append(t)
            if dist[t]==dist[s]+1:
                cnt[t]+=mul*cnt[s]
    assert len(dist)==3*n-2,(n,len(dist))
    return dist[end],cnt[end]


def main():
    for n in range(3,101):
        distance,ways=shortest(n)
        exp=factorial(n-1)*comb(n,3)
        assert (distance,ways)==(n+3,exp),(n,distance,ways,exp)
        if n<=12 or n in (25,50,100):
            print(f'weighted-orbit n={n} geodesic_length={distance} shortest_paths={ways} PASS')
    print('INDEPENDENT_WEIGHTED_QUOTIENT_OK n=3..100')

if __name__=='__main__':main()
