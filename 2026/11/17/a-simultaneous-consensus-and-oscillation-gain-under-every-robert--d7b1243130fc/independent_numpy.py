#!/usr/bin/env python3
"""Exact finite dynamics check for a quartic girth-five graph and one-bond deletions."""
import numpy as np
import networkx as nx
from collections import Counter

NEIGHBORS = [
[2,3,4,5],[1,6,7,8],[1,9,10,11],[1,12,13,14],[1,15,16,17],
[2,9,12,15],[2,10,13,16],[2,11,14,17],[3,6,13,17],[3,7,14,18],
[3,8,16,19],[4,6,16,18],[4,7,9,19],[4,8,10,15],[5,6,14,19],
[5,7,11,12],[5,8,9,18],[10,12,17,19],[11,13,15,18]]
NEIGHBORS=[[v-1 for v in arr] for arr in NEIGHBORS]
G=nx.Graph()
G.add_nodes_from(range(19))
for v,neighbors in enumerate(NEIGHBORS):
    for w in neighbors:G.add_edge(v,w)
assert G.number_of_nodes()==19 and G.number_of_edges()==38
assert set(dict(G.degree()).values())=={4}
assert nx.girth(G)==5
edges=sorted(tuple(sorted(e)) for e in G.edges)
perms=list(nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter())
assert len(perms)==24
classes=[];unseen=set(edges)
while unseen:
    e=min(unseen)
    orb=set(tuple(sorted((p[e[0]],p[e[1]]))) for p in perms)
    assert orb<=unseen
    unseen-=orb
    classes.append((e,len(orb),orb))
assert sorted(v for _,v,_ in classes)==[2,12,12,12]
print('graph', G.number_of_nodes(), G.number_of_edges(), 'automorphisms',len(perms))

SIZE=1<<19
states=np.arange(SIZE,dtype=np.uint32)

def successor(edge):
    nbs=[list(row) for row in NEIGHBORS]
    if edge:
        u,v=edge
        nbs[u].remove(v);nbs[v].remove(u)
    nxt=np.zeros(SIZE,dtype=np.uint32)
    for v,row in enumerate(nbs):
        # vectorized, no lookup tables or assumptions on temporal period
        count=np.zeros(SIZE,dtype=np.uint8)
        for w in row:count+=np.asarray((states>>w)&1,dtype=np.uint8)
        bit=(count*2>len(row))|((count*2==len(row))&(((states>>v)&1)!=0))
        nxt|=bit.astype(np.uint32)<<v
    return nxt

def classify(edge):
    nxt=successor(edge)
    nxt2=nxt[nxt]
    fixed=int(np.count_nonzero(nxt==states))
    p2states=int(np.count_nonzero((nxt2==states)&(nxt!=states)))
    assert p2states%2==0
    now=states.copy()
    unvisited=np.ones(SIZE,dtype=np.bool_)
    entering=[]
    fixed_bas=twobas=0
    for t in range(25):
        periodic=(nxt[now]==now)|(nxt2[now]==now)
        first=unvisited & periodic
        entering.append(int(np.count_nonzero(first)))
        unvisited &=~periodic
        if not np.any(unvisited):
            maxentry=t
            break
        now=nxt[now]
    else: raise AssertionError('outside 25 rounds')
    consensus=int(np.count_nonzero((now==0)|(now==SIZE-1)))
    return fixed,p2states//2,maxentry,consensus,entering

print('none',classify(None))
for e,n,orb in classes:
    print('edge',tuple(v+1 for v in e),'multiplicity',n,'values',classify(e))
