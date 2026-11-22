#!/usr/bin/env python3
"""Independent exact verifier: enumerate pairings of cube vertices, then
check whether unions of disjoint perfect matchings are single 16-cycles.
"""
from itertools import combinations
from collections import Counter

n=16
edges=[]
for a in range(n):
    for j in range(4):
        b=a^(1<<j)
        if a<b: edges.append((a,b))
assert len(edges)==32
index={p:i for i,p in enumerate(edges)}
neighbor=[[v for v in range(n) if (v^u).bit_count()==1] for u in range(n)]
perfect=[]
def pair(free, mask):
    if not free:
        perfect.append(mask);return
    u=min(free)
    for v in neighbor[u]:
        if v in free:
            j=index[(min(u,v),max(u,v))]
            pair(free-{u,v},mask|(1<<j))
pair(set(range(n)),0)
assert len(perfect)==272

# When two matchings are edge-disjoint, their union is a spanning 2-factor.
# It is Hamiltonian iff connected, checked by graph traversal.
cycles=set()
for p,q in combinations(perfect,2):
    if p&q: continue
    mask=p|q
    adj=[[] for _ in range(n)]
    for j,(u,v) in enumerate(edges):
        if (mask>>j)&1:
            adj[u].append(v);adj[v].append(u)
    if any(len(x)!=2 for x in adj):raise AssertionError('not a 2-factor')
    seen={0};todo=[0]
    while todo:
        u=todo.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v);todo.append(v)
    if len(seen)==n:cycles.add(mask)
assert len(cycles)==1344
# A connected alternating 2-factor has exactly two perfect matching
# decompositions, and hence appears once as an unordered pair.

hist={k:Counter() for k in (1,2,3)}
for k in (1,2,3):
    for ids in combinations(range(len(edges)),k):
        x=sum(1<<j for j in ids)
        w=sum(1-2*((x&c).bit_count()%2) for c in cycles)
        hist[k][w]+=1
assert hist[1]=={0:32}
assert hist[2]=={-448:96,-216:48,-56:96,136:192,168:16,176:48}
assert hist[3]=={-120:64,-56:96,-40:192,-32:384,-24:32,-16:1152,0:1120,16:1152,24:192,32:384,88:192}
print('MATCHING_PASS perfect_matchings=272 Hamilton_cycles=1344')
print('PAIR_HIST',sorted(hist[2].items()))
print('TRIPLE_HIST',sorted(hist[3].items()))
