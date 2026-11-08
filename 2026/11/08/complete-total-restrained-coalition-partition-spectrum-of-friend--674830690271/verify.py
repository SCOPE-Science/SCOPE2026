#!/usr/bin/env python3
"""Finite checks for total restrained coalition partitions of friendship graphs.
Direct graph-adjacency and set-partition enumeration; no closed-form TRD or coalition rules are used in the exhaustive step.
"""
from collections import Counter

def stirling(n,k):
    if k<0 or k>n:return 0
    a=[0]*(k+1); a[0]=1
    for i in range(1,n+1):
        b=[0]*(k+1)
        for j in range(1,min(i,k)+1):b[j]=j*a[j]+a[j-1]
        a=b
    return a[k]

def graph_f(m):
    n=2*m+1
    adj=[0]*n
    for i in range(m):
        u=2*i+1;v=2*i+2
        for a,b in [(0,u),(0,v),(u,v)]:
            adj[a]|=1<<b;adj[b]|=1<<a
    return adj

def is_trd(mask,adj):
    n=len(adj); allmask=(1<<n)-1;outside=allmask^mask
    for v in range(n):
        if mask&(1<<v):
            if not(adj[v]&mask):return False
        else:
            if not(adj[v]&mask):return False
            if not(adj[v]&outside):return False
    return True

def exhaustive(m):
    adj=graph_f(m);n=len(adj);allmask=(1<<n)-1
    good=[is_trd(mask,adj) for mask in range(1<<n)]
    ans=Counter();parts=[1]
    def traverse(v):
        if v==n:
            if any(good[p] for p in parts):return
            k=len(parts)
            edges={(i,j) for i in range(k) for j in range(i+1,k) if good[parts[i]|parts[j]]}
            if any(not any(i in e for e in edges) for i in range(k)):
                return
            hub_index=next(i for i,p in enumerate(parts) if p&1)
            expected={(min(hub_index,j),max(hub_index,j)) for j in range(k) if j!=hub_index}
            assert edges==expected,(m,parts,edges,expected)
            ans[k]+=1
            return
        bit=1<<v
        for i in range(len(parts)):
            parts[i]|=bit
            traverse(v+1)
            parts[i]^=bit
        parts.append(bit)
        traverse(v+1)
        parts.pop()
    traverse(1)
    expect=Counter({2:4**m-2**m+1})
    for k in range(3,m+2):expect[k]=stirling(m,k-1)
    assert ans==expect,(m,ans,expect)
    expected_trd=2**m-1
    assert sum(good)==expected_trd,(m,sum(good),expected_trd)
    print('EXHAUSTIVE_GRAPH_PARTITIONS_OK',m,'n',n,'counts',dict(sorted(ans.items())))

for m in range(1,6):exhaustive(m)
print('VERIFY_OK')
