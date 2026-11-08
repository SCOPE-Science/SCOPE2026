#!/usr/bin/env python3
"""Independent exhaustive recurrent-class verification for paired cliques.
Requires Python 3.10+ and NetworkX 3.x.
Run: python verify_components.py
"""
from collections import Counter
from itertools import product
from math import comb
import networkx as nx


def neighbors(n, t):
    v = [[] for _ in range(2*n)]
    for side in range(2):
        for i in range(n):
            for j in range(i+1,n):
                a,b=side*n+i,side*n+j
                v[a].append(b);v[b].append(a)
    for i in range(t):
        v[i].append(n+i);v[n+i].append(i)
    return v


def transitions(s, neigh):
    for i, ns in enumerate(neigh):
        c=(s>>i)&1
        same=sum(((s>>j)&1)==c for j in ns)
        opposite=len(ns)-same
        if same+1>opposite:
            yield s^(1<<i)


def max_cut(s, n, t):
    a=s&((1<<n)-1)
    b=s>>n
    i=a.bit_count();j=b.bit_count()
    return i*(n-i)+j*(n-j)+((a^b)&((1<<t)-1)).bit_count()


def theoretical_classes(n,t):
    m=n//2
    top=2*(n*n//4)+t
    by={}
    for s in range(1<<(2*n)):
        if max_cut(s,n,t)!=top:continue
        key = (s,) if n%2==0 else ((s&((1<<t)-1)),)
        by.setdefault(key,set()).add(s)
    return {frozenset(v) for v in by.values()}


def run(n,t):
    neigh=neighbors(n,t)
    G=nx.DiGraph()
    G.add_nodes_from(range(1<<(2*n)))
    for s in range(1<<(2*n)):
        for v in transitions(s,neigh):G.add_edge(s,v)
    cc=list(nx.strongly_connected_components(G))
    idx={s:i for i,v in enumerate(cc) for s in v}
    outgoing={idx[s] for s,v in G.edges() if idx[s]!=idx[v]}
    recurrent={frozenset(v) for i,v in enumerate(cc) if i not in outgoing}
    expected=theoretical_classes(n,t)
    assert recurrent==expected, (n,t,len(recurrent),len(expected))
    return len(recurrent),sum(len(c) for c in recurrent)

if __name__=='__main__':
    configs=0;instances=0
    for n in range(2,7):
        for t in range(n+1):
            k,r=run(n,t)
            print(f'n={n} t={t} classes={k} recurrent={r}')
            configs+=1<<(2*n);instances+=1
    print(f'PASS components: instances={instances}, labelled_configurations={configs}')
