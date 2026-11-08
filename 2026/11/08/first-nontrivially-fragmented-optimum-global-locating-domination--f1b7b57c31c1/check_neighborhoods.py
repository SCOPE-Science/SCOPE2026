#!/usr/bin/env python3
"""Exact finite census using original graph neighborhoods; Python 3 stdlib."""
from itertools import combinations
from collections import Counter


def wheel(n):
    # 0 is the hub; vertices 1,...,n-1 form the rim cycle.
    r=n-1; neighbors=[]
    for i in range(n):
        if i==0: neighbors.append(set(range(1,n)))
        else: neighbors.append({0, 1+((i-2)%r), 1+(i%r)})
    assert all((j in neighbors[i]) == (i in neighbors[j]) for i in range(n) for j in range(n))
    return neighbors


def global_ld(S, adj, n):
    # Separate domination in the graph and its complement, plus locating of all outsiders.
    outside=set(range(n))-S
    labels=[]
    for v in outside:
        a=adj[v]&S
        b=(set(range(n))-{v}-adj[v])&S
        if not a or not b: return False
        labels.append(frozenset(a))
    return len(set(labels))==len(labels)


def components(states,adj):
    index={frozenset(s):i for i,s in enumerate(states)}
    nbrs=[set() for _ in states]
    for i,s in enumerate(states):
        for u in s:
            for v in adj[u]-s:
                t=frozenset((s-{u})|{v})
                j=index.get(t)
                if j is not None:
                    nbrs[i].add(j)
    assert all(i in nbrs[j] for i,x in enumerate(nbrs) for j in x)
    unseen=set(range(len(states)))
    sizes=[]
    while unseen:
        root=unseen.pop(); stack=[root]; count=1
        while stack:
            for j in nbrs[stack.pop()]&unseen:
                unseen.remove(j);stack.append(j);count+=1
        sizes.append(count)
    return Counter(sizes),Counter(map(len,nbrs)),sum(map(len,nbrs))//2


def census(n):
    adj=wheel(n)
    for k in range(1,n+1):
        states=[set(c) for c in combinations(range(n),k) if global_ld(set(c),adj,n)]
        if states:break
    comps,degs,edges=components(states,adj)
    return k,len(states),comps,degs,edges


def run():
    expected={
       4:(4,1,{1:1},0),5:(3,4,{1:4},0),6:(3,5,{1:5},0),
       7:(4,20,{20:1},36),8:(4,21,{21:1},28),
       9:(4,8,{1:8},0),10:(5,54,{54:1},99),
       11:(5,35,{35:1},40),12:(5,11,{1:11},0),
       13:(6,96,{96:1},156),14:(6,26,{2:13},13)}
    for n in range(4,15):
        k,N,comps,degs,E=census(n)
        assert (k,N,dict(comps),E)==expected[n]
        if n==14:assert degs=={1:26}
        print(f'W_{n}: minimum={k}, states={N}, edges={E}, components={dict(sorted(comps.items()))}')
    print('PASS: all 11 exact graph-neighborhood censuses')

if __name__=='__main__':run()
