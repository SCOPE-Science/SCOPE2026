#!/usr/bin/env python3
"""Direct state enumeration independent of the matrix-power rank checker."""
from collections import Counter

def graph_path(n):return [(i,i+1) for i in range(n-1)]
def graph_cycle(n):return graph_path(n)+[(n-1,0)]
def neighbors(n,edges):
    adj=[0]*(2*n)
    for u,v in edges: adj[u]|=1<<v;adj[v]|=1<<u
    for i in range(n):adj[i]|=1<<(n+i);adj[n+i]|=1<<i
    return adj

def step(u,v,adj):
    out=0
    for i,b in enumerate(adj):
        if (u & b).bit_count()&1:out|=1<<i
    return (out^v,u)

def brute(adj):
    m=len(adj);count=Counter()
    for state in range(1<<(2*m)):
        u=state & ((1<<m)-1);v=state>>m
        start=(u,v);t=0
        while True:
            u,v=step(u,v,adj);t+=1
            if (u,v)==start:break
            if t>3*(1<<m):raise AssertionError('bound')
        count[t]+=1
    return dict(sorted(count.items()))

def predicted(blocks,q=2):
    d={1:1};F=1
    for j in range(0,max((2*s-1).bit_length() for s in blocks)+1):
        now=q**(2*sum(min(2*s,1<<j) for s in blocks))
        d[3*(1<<j)]=now-F;F=now
    return {t:c for t,c in d.items() if c}

if __name__=='__main__':
    cases=[('isolated',1,[] ,[1]),('path3',3,graph_path(3),[3]),('cycle4',4,graph_cycle(4),[2,2])]
    count=0
    for name,n,edges,blocks in cases:
        adj=neighbors(n,edges)
        actual=brute(adj);expect=predicted(blocks)
        assert actual==expect,(name,actual,expect)
        examined=1<<(4*n);count+=examined
        print(name,'states',examined,'cycles',actual)
    print('total states',count,'PASS')
