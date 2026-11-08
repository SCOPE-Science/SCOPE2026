#!/usr/bin/env python3
"""Finite independent breadth-first-search girth cross-check.
The proof, not this finite test, establishes the infinite theorem.
"""
from collections import deque

def graph_girth(b, c):
    weights = [b**j+c for j in range(3)]
    n=weights[-1]+1
    adj=[[] for _ in range(2*n)]
    for v in weights:
        for r in range(v+1):
            l=r; s=n+v-r
            adj[l].append(s);adj[s].append(l)
    best=10**8
    for root in range(2*n):
        if len(adj[root])<2:continue
        dist=[-1]*(2*n);parent=[-1]*(2*n)
        dist[root]=0;todo=deque([root])
        while todo:
            v=todo.popleft()
            if 2*dist[v]+1>=best:continue
            for u in adj[v]:
                if dist[u]<0:
                    dist[u]=dist[v]+1;parent[u]=v;todo.append(u)
                elif parent[v]!=u:
                    best=min(best,dist[v]+dist[u]+1)
    return None if best==10**8 else best

count=0
for b in range(2,10):
    lower=b*(b-2); upper=b*b-b-1
    for c in sorted(set(range(max(0,lower-2),upper+4))):
        expected=None if c<lower else 2*b+2 if c<upper else 6
        value=graph_girth(b,c)
        assert value==expected,(b,c,expected,value)
        count+=1
print('SHIFTED_GEOMETRIC_GIRTH_BFS_OK',count,'parameter pairs')
