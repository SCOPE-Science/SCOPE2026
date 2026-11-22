#!/usr/bin/env python3
"""Exact, finite verification of minimum power domination and sensor relocation."""
from collections import Counter, deque
from itertools import combinations
from pathlib import Path
from hashlib import sha256

N = 19
EDGES = [tuple(map(int, line.split())) for line in
         Path(__file__).with_name('graph_edges.txt').read_text().splitlines()
         if line and not line.startswith('#')]
assert len(EDGES) == 38 and len(set(EDGES)) == 38
assert all(1 <= x < y <= N for x, y in EDGES)
neighbor = [0] * N
for x,y in EDGES:
    neighbor[x-1] |= 1 << (y-1)
    neighbor[y-1] |= 1 << (x-1)
assert all(v.bit_count() == 4 for v in neighbor)
# Exhaustively certify the girth without using a graph-library oracle.
def girth():
    best=20
    for u,v in EDGES:
        start,end=u-1,v-1
        steps={start:0};queue=deque([start])
        while queue:
            x=queue.popleft()
            for y in range(N):
                if not (neighbor[x]>>y)&1 or {x,y}=={start,end}:continue
                if y not in steps:steps[y]=steps[x]+1;queue.append(y)
        best=min(best,steps[end]+1)
    return best
assert girth()==5
ALL = (1<<N)-1

def complete(s):
    observed = s
    for v in range(N):
        if s & (1<<v):
            observed |= neighbor[v]
    t = 1
    while observed != ALL:
        updated = observed
        for v in range(N):
            if observed & (1<<v):
                available = neighbor[v] & (~observed)
                if available and available & (available-1) == 0:
                    updated |= available
        if updated == observed:
            return 0
        observed = updated
        t += 1
    return t

config = {}
for size in range(1,4):
    layer = {}
    for selected in combinations(range(N),size):
        bits = sum(1<<v for v in selected)
        t = complete(bits)
        if t:layer[bits] = t
    if size < 3: assert not layer
    else:config = layer
assert len(config) == 753
assert Counter(config.values()) == {2:109,3:320,4:204,5:120}
states = sorted(config)
ids = {s:i for i,s in enumerate(states)}
sliding = [[] for _ in states]
jumping = [[] for _ in states]
for i,code in enumerate(states):
    for leaving in range(N):
        if not (code>>leaving)&1: continue
        for entering in range(N):
            if (code>>entering)&1: continue
            nxt = code ^ (1<<leaving) ^ (1<<entering)
            if nxt not in ids:continue
            jumping[i].append(ids[nxt])
            if (neighbor[leaving]>>entering)&1:
                sliding[i].append(ids[nxt])
assert sum(map(len,jumping))//2 == 14538
assert sum(map(len,sliding))//2 == 3452

def full_distances(edges):
    dist=[]
    for root in range(len(states)):
        d=[-1]*len(states)
        q=deque([root]);d[root]=0
        while q:
            u=q.popleft()
            for v in edges[u]:
                if d[v] < 0:d[v]=d[u]+1;q.append(v)
        assert -1 not in d
        dist.append(d)
    return dist
J = full_distances(jumping)
S = full_distances(sliding)
assert Counter(max(row) for row in J) == {3:753}
assert Counter(max(row) for row in S) == {6:717,7:36}
jdist=Counter();sdist=Counter();penalty=Counter();extreme=[]
for i in range(len(states)):
    for j in range(i+1,len(states)):
        a,b=J[i][j],S[i][j]
        jdist[a]+=1;sdist[b]+=1;penalty[b-a]+=1
        if b-a == 4:extreme.append((states[i],states[j]))
assert jdist == {1:14538,2:104022,3:164568}
assert sdist == {1:3452,2:20484,3:67788,4:110994,5:70116,6:10270,7:24}
assert penalty == {0:29788,1:131574,2:109054,3:12688,4:24}
assert len(extreme)==24 and all(S[ids[a]][ids[b]]==7 and J[ids[a]][ids[b]]==3 for a,b in extreme)
assert all(a & b == 0 and config[a]==4 and config[b]==4 for a,b in extreme)
def of(*vertices):return sum(1 << (v-1) for v in vertices)
a,b=of(1,3,8),of(11,14,15)
assert S[ids[a]][ids[b]]==7 and J[ids[a]][ids[b]]==3

def transform(mask, perm):
    return sum(1<<perm[i] for i in range(N) if mask>>i&1)
# Two validated automorphisms generate a 24-element subgroup of Aut(G).
g1 = (0,1,2,17,18,9,8,7,6,5,13,12,11,10,16,15,14,3,4)
g2 = (12,13,5,4,8,9,18,6,7,2,1,0,15,14,3,11,10,16,17)
I=tuple(range(N))
def compose(a,b): return tuple(a[b[i]] for i in range(N))
seen={I};pending=[I]
while pending:
    p=pending.pop()
    for g in (g1,g2):
        v=compose(p,g)
        if v not in seen:seen.add(v);pending.append(v)
assert len(seen)==24
E={frozenset(pair) for pair in extreme}
for p in seen:
    assert all((neighbor[p[i]]>>p[j])&1 for i in range(N) for j in range(N) if (neighbor[i]>>j)&1)
seed=extreme[0]
assert {frozenset((transform(seed[0],p),transform(seed[1],p))) for p in seen} == E
assert len({v for pair in E for v in pair})==36
assert {v for pair in E for v in pair}=={states[i] for i,row in enumerate(S) if max(row)==7}
print('PASS: Robertson graph, 753 minimum three-sensor placements; latency 109/320/204/120')
print('PASS: jumping 14538 edges, diameter 3; sliding 3452 edges, radius 6, diameter 7')
print('PASS: sharp surcharge 4 on 24 unordered pairs, one symmetry orbit')
print('PASS: all 283128 pairs; J', sorted(jdist.items()), 'S', sorted(sdist.items()), 'excess', sorted(penalty.items()))
