#!/usr/bin/env python3
"""Exact face-dual matching certificate for zero-field dodecahedral Ising covariance."""
from collections import Counter, deque

EDGES = [(0,1),(0,10),(0,19),(1,2),(1,8),(2,3),(2,6),(3,4),(3,19),(4,5),(4,17),(5,6),(5,15),(6,7),(7,8),(7,14),(8,9),(9,10),(9,13),(10,11),(11,12),(11,18),(12,13),(12,16),(13,14),(14,15),(15,16),(16,17),(17,18),(18,19)]
FACES = [(0,1,8,9,10),(1,0,19,3,2),(1,2,6,7,8),(2,3,4,5,6),(4,3,19,18,17),(5,4,17,16,15),(6,5,15,14,7),(8,7,14,13,9),(10,9,13,12,11),(11,12,16,17,18),(12,13,14,15,16),(19,0,10,11,18)]
N=20
edge_f={e:[] for e in EDGES}
for f,cycle in enumerate(FACES):
    for a,b in zip(cycle,cycle[1:]+cycle[:1]):
        e=tuple(sorted((a,b)))
        assert e in edge_f
        edge_f[e].append(f)
assert len(edge_f)==30 and all(len(a)==2 for a in edge_f.values())
dual_adj=[[] for _ in range(len(FACES))]
for e,(a,b) in edge_f.items():
    dual_adj[a].append((b,e))
    dual_adj[b].append((a,e))
assert all(len(a)==5 for a in dual_adj)

def matchings(mask):
    if mask==0:
        yield ()
        return
    lsb=mask&-mask; a=lsb.bit_length()-1
    for b,e in dual_adj[a]:
        if mask&(1<<b):
            for rest in matchings(mask^(1<<a)^(1<<b)):
                yield (e,)+rest

ms=list(matchings((1<<12)-1))
assert len(ms)==125
assert len(set(tuple(sorted(m)) for m in ms))==125
adj=[[] for _ in range(N)]
for u,v in EDGES:
    adj[u].append(v);adj[v].append(u)
spins=[]
for m in ms:
    frustrated=set(m)
    s=[0]*N; s[0]=1
    queue=deque([0])
    while queue:
        u=queue.popleft()
        for v in adj[u]:
            nxt=s[u]*(1 if tuple(sorted((u,v))) in frustrated else -1)
            if s[v]==0: s[v]=nxt;queue.append(v)
            else: assert s[v]==nxt
    assert all(x in (-1,1) for x in s)
    assert sum(s[a]==s[b] for a,b in EDGES)==6
    spins.extend([tuple(s),tuple(-x for x in s)])
assert len(spins)==250 and len(set(spins))==250
D=[[99]*N for _ in range(N)]
for u in range(N):
    D[u][u]=0
    Q=deque([u])
    while Q:
        a=Q.popleft()
        for b in adj[a]:
            if D[u][b]==99: D[u][b]=D[u][a]+1;Q.append(b)
assert max(map(max,D))==5
S=[[sum(x[u]*x[v] for x in spins) for v in range(N)] for u in range(N)]
nums={d:{S[u][v] for u in range(N) for v in range(N) if D[u][v]==d} for d in range(6)}
assert nums=={0:{250},1:{-150},2:{50},3:{-30},4:{50},5:{-62}},nums
assert Counter(sum(x) for x in spins)=={0:240,4:5,-4:5}
print('PASS: 12 faces, 125 dual icosahedral perfect matchings, 250 spin ground states')
print('Numerators of spin correlation / 250 by graph distance:',[next(iter(nums[d])) for d in range(6)])
print('Magnetization multiplicity:',dict(sorted(Counter(sum(x) for x in spins).items())))
