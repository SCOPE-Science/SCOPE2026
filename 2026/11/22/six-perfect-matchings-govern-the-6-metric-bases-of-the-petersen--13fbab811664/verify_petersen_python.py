#!/usr/bin/env python3
"""Exact shortest-path and complete subset verifier for the Petersen line graph.
Run: python3 -S verify_petersen_python.py (standard library only).
"""
from collections import Counter,deque
from itertools import combinations
from math import comb
BASE_EDGES = [[0, 1], [0, 4], [0, 5], [1, 2], [1, 6], [2, 3], [2, 7], [3, 4], [3, 8], [4, 9], [5, 7], [5, 8], [6, 8], [6, 9], [7, 9]]

def main():
    n=len(BASE_EDGES)
    adj=[set() for _ in range(n)]
    for i,j in combinations(range(n),2):
        if set(BASE_EDGES[i]) & set(BASE_EDGES[j]):
            adj[i].add(j); adj[j].add(i)
    assert n==15 and all(len(s)==4 for s in adj)
    dist=[]
    for v in range(n):
        d=[-1]*n;d[v]=0;q=deque([v])
        while q:
            x=q.popleft()
            for y in adj[x]:
                if d[y]==-1: d[y]=d[x]+1;q.append(y)
        assert -1 not in d
        dist.append(d)
    bisectors=[sum(1<<w for w in range(n) if dist[u][w]==dist[v][w])
               for u,v in combinations(range(n),2)]
    assert len(bisectors)==105 and len(set(bisectors))==105
    assert all(x.bit_count()==5 for x in bisectors)
    values=[(99,0)]*11; witnesses=[[] for _ in range(11)]
    for S in range(1<<n):
        score=min(S.bit_count()-(S & E).bit_count() for E in bisectors)
        r=S.bit_count()
        for k in range(1,score+1):
            old,num=values[k]
            if r<old: values[k]=(r,1);witnesses[k]=[S]
            elif r==old: values[k]=(r,num+1);witnesses[k].append(S)
    expected=[(99,0),(4,960),(5,408),(7,3480),(8,1815),(9,375),(10,6),
              (12,455),(13,105),(14,15),(15,1)]
    assert values==expected, values
    matchings=set()
    for indices in combinations(range(n),5):
        endpoints=[u for i in indices for u in BASE_EDGES[i]]
        if len(set(endpoints))==10:
            matchings.add(sum(1<<i for i in indices))
    assert len(matchings)==6
    optimal_complements={(1<<n)-1 ^ S for S in witnesses[6]}
    assert optimal_complements==matchings
    assert all(len(witnesses[k])==comb(n,k+5) for k in range(7,11))
    assert all(any((s & e)==e for e in bisectors) for s in range(1<<n) if s.bit_count()==11)
    for k in range(1,11): print(k,values[k][0],values[k][1])
    print('bisectors:',len(bisectors),'all size five, all distinct')
    print('k=6 complements:',len(matchings),'exactly all perfect matchings')
    print('PASS: exhaustive 32768-subset certificate')
if __name__=='__main__':main()
