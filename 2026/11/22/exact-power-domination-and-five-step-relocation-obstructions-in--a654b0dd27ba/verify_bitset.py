#!/usr/bin/env python3
"""Exhaustive, standard-library verification of optimal PMU relocation on the Holt graph.
Run: python3 verify_bitset.py
"""
from collections import Counter, deque
from itertools import combinations

V = [(x, y) for y in range(3) for x in range(9)]
ID = {p: i for i, p in enumerate(V)}
adj = [0] * 27
for x, y in V:
    v = ID[(x, y)]
    for xx, yy in ((4*x+1,y-1),(4*x-1,y-1),(7*x+7,y+1),(7*x-7,y+1)):
        adj[v] |= 1 << ID[(xx % 9, yy % 3)]
assert sum(m.bit_count() for m in adj) == 108
assert all(bool(adj[i] & (1 << j)) == bool(adj[j] & (1 << i)) for i in range(27) for j in range(27))
full = (1 << 27) - 1

def completion_rounds(mask):
    seen = 0
    for i in range(27):
        if mask & (1 << i):
            seen |= adj[i] | (1 << i)
    round_number = 1
    while seen != full:
        nxt = seen
        for i in range(27):
            if seen & (1 << i):
                rem = adj[i] & ~seen
                if rem and rem & (rem - 1) == 0:
                    nxt |= rem
        if nxt == seen:
            return 0
        seen = nxt
        round_number += 1
    return round_number

assert all(completion_rounds(1 << i) == 0 for i in range(27))
for i,j in combinations(range(27),2):
    assert completion_rounds((1 << i)|(1 << j)) == 0
sets=[]; round_count=Counter()
for a,b,c in combinations(range(27),3):
    mask=(1<<a)|(1<<b)|(1<<c)
    rounds=completion_rounds(mask)
    if rounds:
        sets.append(mask)
        round_count[rounds]+=1
assert len(sets) == 567 and round_count == {5:351,6:216}
I={m:i for i,m in enumerate(sets)}
J=[[] for _ in sets]; T=[[] for _ in sets]
for z,m in enumerate(sets):
    for old in range(27):
        if not m & (1<<old):
            continue
        for new in range(27):
            if m & (1<<new):
                continue
            v=I.get(m ^ (1<<old) ^ (1<<new))
            if v is not None:
                J[z].append(v)
                if adj[old] & (1<<new):
                    T[z].append(v)
assert sum(map(len,J))//2 == 5400
assert sum(map(len,T))//2 == 1242
assert Counter(map(len,T)) == {2:81,3:108,4:108,5:162,6:54,8:54}

def distances(edges, start):
    d=[-1]*len(edges)
    d[start]=0
    q=deque([start])
    while q:
        a=q.popleft()
        for b in edges[a]:
            if d[b]<0:
                d[b]=d[a]+1
                q.append(b)
    assert all(v>=0 for v in d)
    return d

joint=Counter(); excess=Counter(); ecc_J=Counter(); ecc_T=Counter()
for s in range(len(sets)):
    dj=distances(J,s)
    dt=distances(T,s)
    ecc_J[max(dj)]+=1
    ecc_T[max(dt)]+=1
    for t in range(s+1,len(sets)):
        joint[(dj[t],dt[t])]+=1
        excess[dt[t]-dj[t]]+=1
assert sum(joint.values()) == 567*566//2 == 160461
assert ecc_J == {4:567}
assert ecc_T == {7:432,8:135}
assert excess == {0:12501,1:34830,2:54189,3:47250,4:11340,5:351}
assert sum(count for (dj,dt),count in joint.items() if dj==1 and dt==6) == 54
assert joint[(3,8)] == 189
print('PASS: 567 minimum triples, 5400 jump edges, 1242 slide edges')
print('PASS: round spectrum', dict(round_count))
print('PASS: jump eccentricities',dict(ecc_J),'slide eccentricities',dict(ecc_T))
print('PASS: slide-minus-jump distance spectrum',dict(sorted(excess.items())))
print('PASS: 54 one-jump pairs need 6 slides; 351 pairs have penalty 5')
