#!/usr/bin/env python3
"""Self-contained exhaustive verification for power-domination reconfiguration on the Clebsch graph.

Vertices are 0..15; an edge connects x and x xor g for g in {1,2,4,8,15}.
Only the Python standard library is required.
"""
from collections import Counter, deque
from itertools import combinations

N = 16
GEN = (1, 2, 4, 8, 15)
NEIGHBORS = tuple(frozenset(x ^ g for g in GEN) for x in range(N))
ALL = frozenset(range(N))
assert all(len(v) == 5 for v in NEIGHBORS)
assert all(x in NEIGHBORS[y] for y in range(N) for x in NEIGHBORS[y])
assert len({tuple(sorted((x,y))) for x in range(N) for y in NEIGHBORS[x]}) == 40

def edges_in(vertices):
    return sum(b in NEIGHBORS[a] for a,b in combinations(vertices,2))

def initial_observed(vertices):
    observed = set(vertices)
    for x in vertices:
        observed.update(NEIGHBORS[x])
    return frozenset(observed)

def power_dominates(vertices):
    seen = set(initial_observed(vertices))
    while len(seen) < N:
        additions = set()
        for v in seen:
            left = NEIGHBORS[v] - seen
            if len(left) == 1:
                additions.update(left)
        if not additions:
            return False
        seen.update(additions)
    return True

assert not any(power_dominates((x,)) for x in range(N))
assert not any(power_dominates(p) for p in combinations(range(N),2))
TRIPLES = frozenset(frozenset(c) for c in combinations(range(N),3) if power_dominates(c))
assert len(TRIPLES) == 320
assert Counter(edges_in(t) for t in TRIPLES) == {0:160,2:160}
assert all(power_dominates(t) == (edges_in(t) != 1) for t in combinations(range(N),3))
assert all(len(initial_observed(t)) == 13 for t in TRIPLES)

U = {s: ALL - initial_observed(s) for s in TRIPLES}
assert all(len(t)==3 and t in TRIPLES for t in U.values())
assert all(U[U[s]] == s and edges_in(U[s]) == 2 - edges_in(s) for s in TRIPLES)

def graph(sliding):
    adj = {s:set() for s in TRIPLES}
    for s in TRIPLES:
        for a in s:
            for b in ALL-s:
                if sliding and b not in NEIGHBORS[a]:
                    continue
                t = (s-{a})|{b}
                if t in adj:
                    adj[s].add(t)
    assert all(s in adj[t] for s,others in adj.items() for t in others)
    return adj

def distances(adj, start):
    distance={start:0}; q=deque([start])
    while q:
        s=q.popleft()
        for t in adj[s]:
            if t not in distance:
                distance[t]=distance[s]+1;q.append(t)
    return distance

jump,slide=graph(False),graph(True)
assert sum(map(len,jump.values()))//2 == 3360
assert sum(map(len,slide.values()))//2 == 1120
assert Counter(len(jump[s]) for s in TRIPLES) == {21:320}
assert Counter((edges_in(s),len(slide[s])) for s in TRIPLES) == {(0,9):160,(2,5):160}
assert Counter((edges_in(s),edges_in(t)) for s in TRIPLES for t in slide[s]) == {(0,0):960,(0,2):480,(2,0):480,(2,2):320}

pairs=Counter(); hist_jump=Counter(); hist_slide=Counter(); antipodal=0
for s in TRIPLES:
    dj=distances(jump,s);ds=distances(slide,s)
    assert len(dj)==len(ds)==320
    assert max(dj.values()) == 3 and max(ds.values()) == 6
    assert [t for t in ds if ds[t]==6] == [U[s]]
    assert dj[U[s]] == 3
    for t in TRIPLES:
        if tuple(sorted(s)) < tuple(sorted(t)):
            pairs[ds[t]-dj[t]]+=1
            hist_jump[dj[t]]+=1
            hist_slide[ds[t]]+=1
            if ds[t]-dj[t] == 3:
                antipodal += 1
                assert t==U[s]
assert antipodal == 160
assert dict(pairs) == {0:12560,1:27520,2:10800,3:160}
assert dict(hist_jump) == {1:3360,2:20160,3:27520}
assert dict(hist_slide) == {1:1120,2:5840,3:18400,4:20720,5:4800,6:160}
for rep,hj,hs in [
    (frozenset((0,3,5)),(1,21,126,172),(1,9,45,122,118,24,1)),
    (frozenset((0,1,2)),(1,21,126,172),(1,5,28,108,141,36,1))]:
    assert tuple(Counter(distances(jump,rep).values()).get(i,0) for i in range(4))==hj
    assert tuple(Counter(distances(slide,rep).values()).get(i,0) for i in range(7))==hs
print('PASS Cayley construction, all 696 subsets of size at most three, 320 optimum triples, all-pairs distance and unique blind-spot antipodes')
print('classes',Counter(edges_in(t) for t in TRIPLES))
print('jump',len(jump),3360,dict(sorted(hist_jump.items())))
print('slide',len(slide),1120,dict(sorted(hist_slide.items())))
print('penalties',dict(sorted(pairs.items())))
