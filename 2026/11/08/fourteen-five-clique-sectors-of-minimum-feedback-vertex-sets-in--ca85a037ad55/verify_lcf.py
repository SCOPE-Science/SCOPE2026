#!/usr/bin/env python3
"""Independent check via the Heawood [5,-5]^7 LCF graph, DFS cycle test, and pair-intersection adjacency."""
from itertools import combinations
from collections import Counter

n=14
adj=[set() for _ in range(n)]
def edge(u,v):adj[u].add(v);adj[v].add(u)
for i in range(n): edge(i,(i+1)%n)
for i in range(0,n,2):edge(i,(i+5)%n)
assert len({tuple(sorted((i,j))) for i in range(n) for j in adj[i]}) == 21
assert all(len(x)==3 for x in adj)

def good(t):
    rem=set(range(n))-set(t)
    vis=set()
    def dfs(v,par):
        vis.add(v)
        for w in adj[v]&rem:
            if w==par:continue
            if w in vis:return False
            if not dfs(w,v):return False
        return True
    return all(dfs(i,-1) for i in sorted(rem) if i not in vis)

assert all(not good(t) for k in range(4) for t in combinations(range(n),k))
F=[frozenset(t) for t in combinations(range(n),4) if good(t)]
assert len(F)==70
J={s:set() for s in F}; T={s:set() for s in F}
for a,b in combinations(F,2):
    if len(a&b)!=3:continue
    J[a].add(b);J[b].add(a)
    x=next(iter(a-b));y=next(iter(b-a))
    if y in adj[x]:T[a].add(b);T[b].add(a)
def comps(G):
    unseen=set(G); c=Counter()
    while unseen:
        s=unseen.pop(); stack=[s]; count=0
        while stack:
            v=stack.pop();count+=1
            near=unseen&G[v];unseen-=near;stack.extend(near)
        c[count]+=1
    return c
assert sum(map(len,J.values()))//2==140
assert Counter(map(len,J.values()))==Counter({4:70})
assert comps(J)==Counter({5:14})
assert sum(map(len,T.values()))==0 and comps(T)==Counter({1:70})
print('LCF_VERIFY_OK; minimum=4; fvs_count=70; jump_edges=140; jump_components=14*K5; slide_edges=0; slide_components=70*K1')
