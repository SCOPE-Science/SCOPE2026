#!/usr/bin/env python3
"""Independent exact verification of power domination on the Clebsch graph."""
from itertools import combinations
from collections import Counter, deque

V = range(16)
D = frozenset((1,2,4,8,15))
adj = {v: frozenset(v ^ d for d in D) for v in V}
assert all(len(adj[v]) == 5 for v in V)
assert sum(u in adj[v] for v in V for u in adj[v]) == 80
assert all(not (adj[v] & adj[u]) for v in V for u in adj[v])
assert all(len(adj[u] & adj[v]) == 2 for u in V for v in V if u != v and v not in adj[u])

def closure(seed):
    obs = set(seed)
    for v in seed:
        obs.update(adj[v])
    waves = 0
    while True:
        forced = set()
        for v in obs:
            white = adj[v] - obs
            if len(white) == 1:
                forced.update(white)
        if not forced:
            return frozenset(obs),waves
        obs.update(forced)
        waves += 1

P = {frozenset(c): closure(c) for k in range(17) for c in combinations(V,k)}
valid = {s for s,(o,_) in P.items() if len(o) == 16}
assert len(P) == 65536
count = Counter(map(len,valid))
assert count == Counter({3:320,4:1760,**{k:__import__('math').comb(16,k) for k in range(5,17)}})

def edges(s):
    return sum(v in adj[u] for u,v in combinations(sorted(s),2))
for s,(o,w) in P.items():
    if len(s) == 3:
        assert (s in valid) == (edges(s) in (0,2))
    elif len(s)==4:
        match = sorted(len(adj[v] & s) for v in s)==[1]*4
        assert (s not in valid) == match
    elif len(s)>=5:
        assert s in valid
    elif len(s)<=2:
        assert s not in valid
    if s in valid:
        assert w <= 1
minima = {s for s in valid if len(s)==3}
assert Counter(edges(s) for s in minima) == {0:160,2:160}
fail3 = {s for s in P if len(s)==3 and s not in valid}
maxfail = {s for s in P if len(s)==4 and s not in valid}
assert len(fail3)==240 and len(maxfail)==60
assert all(sum(s<=f for f in maxfail)==1 for s in fail3)

# Exchange graph: all optimal triples, with one sensor replaced.
network = {s:set() for s in minima}
for s in minima:
    for outgoing in s:
        for incoming in V:
            if incoming not in s:
                t=(s-{outgoing})|{incoming}
                if t in minima:network[s].add(frozenset(t))
assert all(len(network[s])==21 for s in minima)
assert sum(len(q) for q in network.values())//2==3360
assert all(s in network[t] for s in minima for t in network[s])
for root in minima:
    dist={root:0}; queue=deque([root])
    while queue:
        s=queue.popleft()
        for t in network[s]:
            if t not in dist:
                dist[t]=dist[s]+1; queue.append(t)
    assert Counter(dist.values())=={0:1,1:21,2:126,3:172}
assert all(len(P[s][0])==16 for s in minima)
print('PYTHON_VERIFY_OK states=65536 min=320 failed3=240 failed4=60 unique_extension=240 edges=3360 diameter=3')
