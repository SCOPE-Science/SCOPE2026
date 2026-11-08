#!/usr/bin/env python3
"""Exact all-source switch distances for labelled binary 5x5 matrices of degree two."""
from itertools import combinations, product
from collections import Counter, deque

N=5
row_masks=tuple(sum(1<<j for j in p) for p in combinations(range(N),2))
states=tuple(rows for rows in product(row_masks,repeat=N)
             if all(sum((r>>j)&1 for r in rows)==2 for j in range(N)))
index={s:i for i,s in enumerate(states)}
assert len(states)==2040 and len(index)==2040
adj=[set() for _ in states]
for i,s in enumerate(states):
    for a,b in combinations(range(N),2):
        for x,y in combinations(range(N),2):
            p=((s[a]>>x)&1,(s[a]>>y)&1,(s[b]>>x)&1,(s[b]>>y)&1)
            if p==(1,0,0,1) or p==(0,1,1,0):
                t=list(s)
                t[a]^=(1<<x)|(1<<y)
                t[b]^=(1<<x)|(1<<y)
                adj[i].add(index[tuple(t)])
assert sum(map(len,adj))==52200
assert all(i in adj[j] for i,nb in enumerate(adj) for j in nb)
# Verify an explicit six-switch path between the canonical Hamiltonian state and an antipode.
path=[(3,6,12,24,17),(3,3,12,24,20),(10,3,12,17,20),
      (10,3,24,5,20),(12,3,24,3,20),(12,10,17,3,20),
      (12,24,17,3,6)]
assert len(path)==7 and all(index[path[j+1]] in adj[index[path[j]]] for j in range(6))

def half_lengths(rows):
    g=[[] for _ in range(10)]
    for a,m in enumerate(rows):
        for b in range(5):
            if m>>b&1:
                g[a].append(5+b)
                g[5+b].append(a)
    seen=set(); lengths=[]
    for v in range(10):
        if v in seen: continue
        seen.add(v); q=[v]
        for u in q:
            for w in g[u]:
                if w not in seen:seen.add(w);q.append(w)
        assert len(q)%2==0
        lengths.append(len(q)//2)
    return tuple(sorted(lengths))

classes=[half_lengths(s) for s in states]
assert Counter(classes)=={(5,):1440,(2,3):600}
assert {len(adj[i]) for i,c in enumerate(classes) if c==(5,)}=={25}
assert {len(adj[i]) for i,c in enumerate(classes) if c==(2,3)}=={27}

pair_hist=Counter();profiles={}; ecc=Counter(); anti_count=Counter();peripheral=0
for i in range(len(states)):
    dist=[-1]*len(states);dist[i]=0;q=deque([i])
    while q:
        a=q.popleft()
        for b in adj[a]:
            if dist[b]==-1:
                dist[b]=dist[a]+1;q.append(b)
    assert -1 not in dist
    shell=tuple(Counter(dist).get(k,0) for k in range(7))
    if classes[i]==(5,):
        assert shell==(1,25,230,810,831,141,2)
        assert all(classes[j]==(5,) for j,t in enumerate(dist) if t==6)
        peripheral+=2
    else:
        assert shell==(1,27,242,840,810,120,0)
    profiles.setdefault(classes[i],shell)
    e=max(dist);ecc[e]+=1
    anti_count[(e,dist.count(e))]+=1
    for j in range(i+1,len(states)):pair_hist[dist[j]]+=1
assert ecc=={5:600,6:1440}
assert anti_count=={(5,120):600,(6,2):1440}
assert dict(sorted(pair_hist.items()))=={1:26100,2:238200,3:835200,4:841320,5:137520,6:1440}
assert sum(pair_hist.values())==2040*2039//2
print('PYTHON_EXHAUSTIVE_PASS states=2040 edges=26100 radius=5 diameter=6')
print('PYTHON_PROFILES',profiles)
print('PYTHON_DIAMETRAL_PAIRS',pair_hist[6])
