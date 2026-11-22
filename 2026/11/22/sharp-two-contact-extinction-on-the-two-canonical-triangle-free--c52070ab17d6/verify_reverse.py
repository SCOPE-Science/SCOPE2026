#!/usr/bin/env python3
"""Complete functional-graph checker for two finite threshold-two excitation maps.

Usage: python3 verify_reverse.py
Requires graph_data.json in this directory, and only the Python standard library.
"""
from collections import Counter, deque
from pathlib import Path
import json

def graph_properties(n, edges):
    neighbors=[set() for _ in range(n)]
    for u,v in edges:
        assert 0<=u<v<n and v not in neighbors[u]
        neighbors[u].add(v);neighbors[v].add(u)
    assert not any(u in neighbors[v] for u in range(n) for v in neighbors[u] if u==v)
    assert all(not (neighbors[u]&neighbors[v]) for u,v in edges), "triangle-free"
    def colorable(k):
        order=sorted(range(n),key=lambda v:-len(neighbors[v]));color=[-1]*n
        def search(i):
            if i==n:return True
            v=order[i]
            forbidden={color[w] for w in neighbors[v] if color[w]>=0}
            for c in range(k):
                if c not in forbidden:
                    color[v]=c
                    if search(i+1):return True
                    color[v]=-1
            return False
        return search(0)
    assert not colorable(3) and colorable(4)
    return neighbors

def run(name, data):
    n=data['vertices'];edges=data['edges']; N=3**n
    ng=graph_properties(n,edges)
    p=[3**i for i in range(n)]
    # Base-three transition assembled by independently evaluated vertex rules.
    def nxt(s):
        a=[s//b%3 for b in p]; t=0
        for v in range(n):
            if a[v]==1:b=2
            elif a[v]==2:b=0
            else:b=int(sum(a[w]==1 for w in ng[v])>=2)
            t+=b*p[v]
        return t
    successor=[nxt(s) for s in range(N)]
    indeg=[0]*N
    for t in successor:indeg[t]+=1
    q=deque(s for s in range(N) if indeg[s]==0)
    removed=[]
    while q:
        s=q.popleft();removed.append(s);t=successor[s]
        indeg[t]-=1
        if indeg[t]==0:q.append(t)
    assert all(indeg[s]==0 for s in removed)
    cyc=[s for s in range(N) if indeg[s]>0]
    assert cyc==[0], "Only all-rest may be cyclic"
    first=[-1]*N;first[0]=0
    for s in reversed(removed):
        first[s]=1+first[successor[s]]
    assert min(first)==0 and max(first)==data['extinction_cutoff']
    counts=[first.count(i) for i in range(max(first)+1)]
    witness=next(s for s in range(N) if first[s]==max(first))
    print(name,json.dumps({'n':n,'edges':len(edges),'states':N,'degree_sequence':sorted(len(v) for v in ng),
        'extinction_histogram':counts,'max_extinction_time':max(first),'first_max_witness':witness,
        'only_periodic_state':0},sort_keys=True))
    # Separate threshold-one three-period witness, checked under the same graph.
    def one_contact(state):
        a=[state//b%3 for b in p]
        return sum(p[v]*(2 if a[v]==1 else 0 if a[v]==2 else
                         int(any(a[w]==1 for w in ng[v]))) for v in range(n))
    w=448; w1=one_contact(w); w2=one_contact(w1); w3=one_contact(w2)
    assert w3==w and w1!=w and w2!=w
    return counts

if __name__=='__main__':
    d=json.loads((Path(__file__).resolve().parent/'graph_data.json').read_text())
    for name,data in d.items():run(name,data)
