#!/usr/bin/env python3
"""Exhaustive bitset verifier for optimum power domination in H(3,3)."""
from itertools import combinations, product
from collections import Counter, deque

V = list(product(range(3), repeat=3))
assert len(V)==27
N = len(V)
FULL = (1<<N)-1
adj = [sum(1<<j for j in range(N) if sum(x!=y for x,y in zip(V[i],V[j]))==1) for i in range(N)]

def power_dominates(mask):
    observed = mask
    for p in range(N):
        if (mask>>p)&1:
            observed |= adj[p]
    while True:
        next_observed = observed
        for p in range(N):
            if (observed>>p)&1:
                remaining = adj[p] & ~observed
                if remaining and (remaining&(remaining-1))==0:
                    next_observed |= remaining
        if next_observed == observed:
            return observed == FULL
        observed = next_observed

for k in (1,2):
    assert not any(power_dominates(sum(1<<i for i in c)) for c in combinations(range(N),k))

states=[]
for t in combinations(range(N),3):
    bm=sum(1<<i for i in t)
    if power_dominates(bm):
        states.append(bm)
assert len(states)==1296
index={state:i for i,state in enumerate(states)}

def signature(mask):
    pts=[i for i in range(N) if (mask>>i)&1]
    return tuple(sorted(sum(a!=b for a,b in zip(V[x],V[y])) for x,y in combinations(pts,2)))

assert Counter(signature(m) for m in states)=={
    (1,3,3):324, (2,2,3):648, (2,3,3):324
}

def make_edges(sliding):
    graph=[set() for _ in states]
    for i,mask in enumerate(states):
        for x in range(N):
            if not (mask>>x)&1: continue
            for y in range(N):
                if ((mask>>y)&1) or (sliding and not ((adj[x]>>y)&1)):
                    continue
                other=mask^(1<<x)^(1<<y)
                j=index.get(other)
                if j is not None:
                    graph[i].add(j)
    return [sorted(s) for s in graph]

jump=make_edges(False)
slide=make_edges(True)
assert all(i in g[j] for g in (jump,slide) for j in range(len(g)) for i in g[j])
assert sum(map(len,jump))==48600
assert sum(map(len,slide))==14580
assert Counter(len(g) for g in jump)=={35:648,37:324,43:324}
assert Counter(len(g) for g in slide)=={10:972,15:324}

def bfs(graph,root):
    distances=[-1]*len(graph)
    distances[root]=0
    q=deque([root])
    while q:
        p=q.popleft()
        for v in graph[p]:
            if distances[v]<0:
                distances[v]=distances[p]+1
                q.append(v)
    return distances

jhist=Counter(); shist=Counter(); gaps=Counter(); j_ecc=Counter();s_ecc=Counter()
for a in range(len(states)):
    dj=bfs(jump,a)
    ds=bfs(slide,a)
    assert -1 not in dj and -1 not in ds
    j_ecc[(signature(states[a]),max(dj))]+=1
    s_ecc[(signature(states[a]),max(ds))]+=1
    for b in range(a+1,len(states)):
        jhist[dj[b]]+=1
        shist[ds[b]]+=1
        gaps[ds[b]-dj[b]]+=1
assert jhist=={1:24300,2:224208,3:590328,4:324},jhist
assert shist=={1:7290,2:45360,3:170262,4:336960,5:244620,6:34668},shist
assert gaps=={0:103356,1:370008,2:324648,3:41148},gaps
assert j_ecc=={((1,3,3),3):324,((2,2,3),4):648,((2,3,3),3):324},j_ecc
assert s_ecc=={((1,3,3),6):324,((2,2,3),6):648,((2,3,3),6):324},s_ecc
assert sum(jhist.values())==1296*1295//2
assert all(sum(1 for d in bfs(jump,i) if d==4)==(signature(states[i])==(2,2,3)) for i in range(len(states)))
print('BITMASK_OK minimum=3 states=1296 jump_edges=24300 slide_edges=7290 jump_diameter=4 slide_diameter=6 jump_diameter_pairs=324 slide_diameter_pairs=34668 max_detour=3')
print('JUMP_PAIRS',dict(sorted(jhist.items())))
print('SLIDE_PAIRS',dict(sorted(shist.items())))
print('DETOUR_PAIRS',dict(sorted(gaps.items())))
