#!/usr/bin/env python3
"""Finite exhaustive certificate of power-domination and relocation on QR(17)."""
import itertools
import json
from pathlib import Path
from collections import Counter, deque

P = 17
res = {pow(i, 2, P) for i in range(1, P)}
adj = [sum(1 << j for j in range(P) if j != i and (j-i) % P in res) for i in range(P)]
full = (1 << P) - 1
assert len(res) == 8 and all(a.bit_count() == 8 for a in adj)

def dominates(selected):
    seen = selected
    for u in range(P):
        if selected >> u & 1: seen |= adj[u]
    while seen != full:
        nxt = seen
        for u in range(P):
            if seen >> u & 1:
                remain = adj[u] & ~seen
                if remain and (remain & (remain - 1)) == 0: nxt |= remain
        if nxt == seen: break
        seen = nxt
    return seen == full

assert not dominates(0)
assert all(not dominates(1 << i) for i in range(P))
opt = [sum(1 << x for x in t) for t in itertools.combinations(range(P), 2) if dominates(sum(1 << x for x in t))]
assert len(opt) == 68
assert all(((adj[u] >> v) & 1) == 0 for s in opt for u,v in [tuple(i for i in range(P) if s>>i&1)])
index = {s: i for i,s in enumerate(opt)}
J = [set() for _ in opt]
T = [set() for _ in opt]
for i,s in enumerate(opt):
    for j,t in enumerate(opt):
        if j <= i: continue
        removed = s & ~t
        inserted = t & ~s
        if removed.bit_count() != 1 or inserted.bit_count() != 1: continue
        J[i].add(j); J[j].add(i)
        u = removed.bit_length()-1; v = inserted.bit_length()-1
        if (adj[u] >> v) & 1:
            T[i].add(j);T[j].add(i)

def bfs(A, origin):
    dist = {origin:0}; q=deque([origin])
    while q:
        v=q.popleft()
        for w in A[v]:
            if w not in dist:
                dist[w]=dist[v]+1; q.append(w)
    return dist

assert len(J)==len(T)==68
assert all(len(J[i]) == 14 and len(T[i]) == 8 for i in range(68))
assert sum(map(len,J))//2 == 476 and sum(map(len,T))//2 == 272
hj=Counter(); ht=Counter();gap=Counter()
for i in range(68):
    dj=bfs(J,i); dt=bfs(T,i)
    assert len(dj)==len(dt)==68
    assert Counter(dj.values())=={0:1,1:14,2:50,3:3}
    assert Counter(dt.values())=={0:1,1:8,2:32,3:27}
    for j in range(i+1,68):
        hj[dj[j]]+=1;ht[dt[j]]+=1;gap[dt[j]-dj[j]]+=1
assert dict(hj)=={1:476,2:1700,3:102}
assert dict(ht)=={1:272,2:1088,3:918}
assert dict(gap)=={0:1258,1:1020}
cert=json.loads(Path(__file__).with_name('root_spheres.json').read_text(encoding='utf8'))
root = index[(1<<0)|(1<<3)]
dj=bfs(J,root); dt=bfs(T,root)
assert cert['root'] == [0,3]
for row in cert['root_distances']:
    pair=row['pair']; index_of_pair=index[sum(1<<i for i in pair)]
    assert (row['jump'],row['slide'])==(dj[index_of_pair],dt[index_of_pair])
assert len(cert['root_distances'])==68
print('DIRECT_OK optimal=68 jump_edges=476 slide_edges=272')
print('JUMP_PAIRS 1:476 2:1700 3:102')
print('SLIDE_PAIRS 1:272 2:1088 3:918')
print('SLIDE_MINUS_JUMP 0:1258 1:1020')
