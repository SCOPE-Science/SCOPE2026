#!/usr/bin/env python3
"""Exact standalone census for two explicitly defined scale-128 maps."""
from collections import deque, Counter
from fractions import Fraction

B = 3200
STATES = range(-B, B + 1)

def nearest_div(n, d):
    """Nearest integer to n/d, choosing even integer at a tie, including n<0."""
    assert isinstance(n,int) and d>0
    q,r = divmod(n,d)
    return q + int(2*r>d or (2*r==d and q%2 != 0))

def successor(i, encoded):
    assert -B <= i <= B
    if i <= -640:
        return nearest_div((51 if encoded else 4)*i,(64 if encoded else 5))+512
    if i<0:
        return 5*i+3200
    if i<640:
        return 5*i-3200
    return nearest_div((51 if encoded else 4)*i,(64 if encoded else 5))-512

def oracle(i,encoded):
    x=Fraction(i,128)
    slope=Fraction(51,64) if encoded else Fraction(4,5)
    if i<=-640: value=slope*x+4
    elif i<0: value=5*x+25
    elif i<640: value=5*x-25
    else: value=slope*x-4
    return round(128*value)

def graph_decomposition(edges):
    n=len(edges)
    indegree=[0]*n
    for j in edges:indegree[j]+=1
    queue=deque(i for i,d in enumerate(indegree) if d==0)
    removed=[]
    while queue:
        i=queue.popleft(); removed.append(i)
        j=edges[i]; indegree[j]-=1
        if indegree[j]==0:queue.append(j)
    cid=[-1]*n; depth=[0]*n; cycles=[]
    for v in range(n):
        if indegree[v]>0 and cid[v]==-1:
            k=len(cycles); cyc=[]; u=v
            while cid[u]<0:
                cid[u]=k;cyc.append(u);u=edges[u]
            assert u==v
            cycles.append(cyc)
    for v in reversed(removed):
        u=edges[v]; cid[v]=cid[u];depth[v]=depth[u]+1
    basins=Counter(cid)
    assert sum(basins.values())==n
    return sorted((len(c),basins[k]) for k,c in enumerate(cycles)),max(depth),cycles

def independent_path_decomposition(edges):
    n=len(edges); visits=Counter(); depths=[]; cycles=set()
    for seed in range(n):
        seen={}; route=[]; x=seed
        while x not in seen:
            seen[x]=len(route);route.append(x);x=edges[x]
        z=seen[x]
        cyc=frozenset(route[z:]); assert len(cyc)>0
        cycles.add(cyc)
        depths.append(z)
        visits[cyc]+=1
    return sorted((len(cyc),visits[cyc]) for cyc in cycles),max(depths)

def check(encoded):
    edges=[]
    for i in STATES:
        j=successor(i,encoded)
        assert j==oracle(i,encoded),(i,j,oracle(i,encoded))
        assert -B<=j<=B
        edges.append(j+B)
    spec,maxdep,cycles=graph_decomposition(edges)
    oracle_spec,oracle_depth=independent_path_decomposition(edges)
    assert spec==oracle_spec and maxdep==oracle_depth
    # The complete cycle sets and all basin sizes are computed from all states.
    expected=([(34,238),(40,6163)],107) if not encoded else (
        [(8,68),(20,2830),(24,253),(24,442),(28,1404),(28,1404)],80)
    assert (spec,maxdep)==expected, (spec,maxdep,expected)
    return edges,spec,maxdep

if __name__=='__main__':
    a,sa,da=check(False)
    b,sb,db=check(True)
    changed=sum(p!=q for p,q in zip(a,b))
    assert changed==5122
    assert len(a)==len(b)==6401
    print('States: 6401')
    print('Exact coefficient: period/basin',sa,'longest transient',da)
    print('Encoded coefficient: period/basin',sb,'longest transient',db)
    print('Different successor edges:',changed)
    print('PASS: two exact nearest-even oracles, two global graph algorithms')
