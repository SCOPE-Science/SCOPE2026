#!/usr/bin/env python3
"""Graph structural and nonisomorphism checks, Python 3 standard library only.
The table of cubic identity graphs supplies completeness of this five-item list.
"""
import json
from collections import Counter,deque

catalog=json.load(open('graph_catalog.json'))['graphs']

def make(edges):
    g=[set() for _ in range(12)]
    for a,b in edges:g[a].add(b);g[b].add(a)
    assert len(edges)==18 and all(len(s)==3 for s in g)
    reach={0};q=[0]
    for v in q:
        for w in g[v]:
            if w not in reach:reach.add(w);q.append(w)
    assert len(reach)==12
    return g

def local_invariants(g):
    data=[]
    for v in range(12):
        triangles=sum(int(a in g[b]) for a in g[v] for b in g[v])//2
        seen={v};d={v:0};q=deque([v])
        while q:
            a=q.popleft()
            for b in g[a]:
                if b not in seen:seen.add(b);d[b]=d[a]+1;q.append(b)
        profile=tuple(Counter(d.values())[i] for i in range(5))
        closed=[]
        counts={v:1}
        for k in range(1,8):
            new=Counter()
            for a,m in counts.items():
                for b in g[a]:new[b]+=m
            counts=new
            closed.append(counts.get(v,0))
        data.append((triangles,profile,tuple(closed)))
    return data

def iso_count(g,h):
    if Counter(local_invariants(g))!=Counter(local_invariants(h)):
        return 0
    sg,sh=local_invariants(g),local_invariants(h)
    choices=[[v for v in range(12) if sg[u]==sh[v]] for u in range(12)]
    found=0
    mapping={};used=set()
    def dfs():
        nonlocal found
        if len(mapping)==12:
            found+=1;return
        best=None; cand_best=None
        for u in range(12):
            if u in mapping:continue
            c=[v for v in choices[u] if v not in used and all((w in g[u])==(mapping[w] in h[v]) for w in mapping)]
            if not c:return
            if cand_best is None or len(c)<len(cand_best):best=u;cand_best=c
        for v in cand_best:
            mapping[best]=v;used.add(v)
            dfs()
            used.remove(v);del mapping[best]
    dfs();return found

Gs=[make(catalog[f'G{i}']['edges']) for i in range(1,6)]
for i,G in enumerate(Gs):
    c=iso_count(G,G)
    print(f'G{i+1} automorphisms={c}')
    assert c==1
for i in range(5):
    for j in range(i+1,5):
        c=iso_count(Gs[i],Gs[j])
        print(f'G{i+1} vs G{j+1}: isomorphisms={c}')
        assert c==0
print('CATALOG_GRAPH_CHECKS_OK')
