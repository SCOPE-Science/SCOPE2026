#!/usr/bin/env python3
"""Exhaustive canonical rooted-forest and color-refinement check."""
from functools import lru_cache
from collections import Counter
import json
from itertools import combinations

LEAF=('r',())
@lru_cache(None)
def forests(n):
    if n == 0: return ((),)
    out=[]
    for m in range(1,n+1):
        for t in trees(m):
            for f in forests(n-m):
                if not f or t <= f[0]: out.append((t,)+f)
    return tuple(out)
@lru_cache(None)
def trees(n):
    if n==1:return (LEAF,)
    return tuple(('r',f) for f in forests(n-1))

def graph(forest):
    adj=[]
    def rec(t,ancestors):
        v=len(adj);adj.append(set())
        for a in ancestors:
            adj[a].add(v);adj[v].add(a)
        for child in t[1]:rec(child,ancestors+(v,))
    for t in forest:rec(t,())
    return adj

def forbidden_four(adj):
    for vs in combinations(range(len(adj)),4):
        ds=[sum((w in adj[v]) for w in vs) for v in vs]
        edges=sum(ds)//2
        if edges==3 and sorted(ds)==[1,1,2,2]:return True
        if edges==4 and sorted(ds)==[2,2,2,2]:return True
    return False

def partition_rounds(adj):
    n=len(adj)
    colors=[0]*n
    history=[len(set(colors))]
    for r in range(n+1):
        signatures=[(colors[v],tuple(sorted(Counter(colors[w] for w in adj[v]).items()))) for v in range(n)]
        index={x:i for i,x in enumerate(sorted(set(signatures)))}
        nxt=[index[s] for s in signatures]
        if len(set(nxt))==len(set(colors)):
            return r,history
        colors=nxt
        history.append(len(set(colors)))
    raise AssertionError('failed to stabilize')

def independent_wl(adj):
    # Refine each class using its full neighbor color-count vector; start with one cell.
    classes=[tuple(range(len(adj)))]
    steps=0
    while True:
        id_of={v:j for j,c in enumerate(classes) for v in c}
        nxt=[]
        for c in classes:
            parts={}
            for v in c:
                key=tuple(sum(id_of[w]==j for w in adj[v]) for j in range(len(classes)))
                parts.setdefault(key,[]).append(v)
            nxt.extend(tuple(x) for _,x in sorted(parts.items()))
        if len(nxt)==len(classes):return steps
        steps+=1
        classes=nxt

profile=[]
for n in range(1,10):
    gs=forests(n)
    assert len(gs)==len(set(gs))
    assert all(not forbidden_four(graph(f)) for f in gs)
    all_r=[(f,partition_rounds(graph(f))[0]) for f in gs]
    counts=Counter(r for f,r in all_r)
    mx=max(counts)
    witnesses=[f for f,r in all_r if r==mx]
    assert all(independent_wl(graph(f))==r for f,r in all_r)
    profile.append({'order':n,'number_of_forests':len(gs),'max_splitting_rounds':mx,'maximizers':len(witnesses),'rounds_histogram':dict(sorted(counts.items()))})
    if n<=7:assert mx<=2
    if n==8:
        assert mx==3 and len(witnesses)==1
        star=('r',(LEAF,LEAF,LEAF))
        paw=('r',(LEAF,('r',(LEAF,))))
        assert witnesses[0] == tuple(sorted((star,paw)))
    if n==9:
        tc=[t for t in trees(9) if partition_rounds(graph((t,)))[0]==3]
        assert len(tc)==1
        assert tc[0]==('r',tuple(sorted((star,paw))))
        assert all(partition_rounds(graph((t,)))[0]<=2 for m in range(1,9) for t in trees(m))
        print(json.dumps({'case':'connected_first_three_rounds','order':9,'unique_witness':repr(tc[0])},sort_keys=True))
print(json.dumps({'case':'all_trivially_perfect','profile':profile},sort_keys=True))
print('PASS: canonical enumeration, independent WL algorithm, unique order-8 and connected order-9 witnesses')
