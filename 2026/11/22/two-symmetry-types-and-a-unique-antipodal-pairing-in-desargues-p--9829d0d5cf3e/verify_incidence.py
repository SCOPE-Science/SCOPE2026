#!/usr/bin/env python3
"""Exact Desargues graph power-domination and sensor mobility certificate.
Standard library only; run: python3 verify_incidence.py
"""
from itertools import combinations, permutations
from collections import Counter, deque

P = tuple(combinations(range(5), 2))
V = tuple((p, t) for p in P for t in (0, 1))
N = {v: set() for v in V}
for p, q in combinations(P, 2):
    if set(p).isdisjoint(q):
        for t in (0, 1):
            N[(p,t)].add((q,1-t))
            N[(q,1-t)].add((p,t))
assert len(V) == 20 and all(len(N[v]) == 3 for v in V)

def monitor(s):
    observed = set(s)
    for v in s: observed.update(N[v])
    while True:
        added = {next(iter(unseen)) for v in observed
                 if len(unseen := N[v] - observed) == 1}
        if not added: return len(observed) == 20
        observed.update(added)

def graph_distances():
    distances = {}
    for s in V:
        dist={s: 0}; queue=deque((s,))
        while queue:
            v=queue.popleft()
            for w in N[v]:
                if w not in dist:
                    dist[w]=dist[v]+1;queue.append(w)
        assert len(dist)==20
        distances[s]=dist
    return distances
D = graph_distances()
def signature(s):
    return tuple(sorted(D[a][b] for a,b in combinations(s,2)))

assert all(not monitor(s) for size in (1,2) for s in combinations(V,size))
opt = tuple(frozenset(s) for s in combinations(V,3) if monitor(s))
assert len(opt) == 240
classes = Counter(signature(s) for s in opt)
assert classes == {(2,3,5): 120, (3,3,4): 120}, classes
assert all((frozenset(s) in set(opt)) ==
           (signature(s) in {(2,3,5), (3,3,4)}) for s in combinations(V,3))
index = {s:i for i,s in enumerate(opt)}
assert len(index) == 240
jump = [set() for _ in opt]
slide = [set() for _ in opt]
for i,s in enumerate(opt):
    for out in s:
        for incoming in V:
            if incoming not in s:
                j=index.get((s - {out}) | {incoming})
                if j is not None:
                    jump[i].add(j)
                    if incoming in N[out]: slide[i].add(j)
assert Counter((signature(s),len(jump[i])) for i,s in enumerate(opt)) == {
    ((2,3,5),17):120, ((3,3,4),13):120}
assert Counter(map(len,slide))=={4:240}
assert sum(map(len,jump))//2==1800
assert sum(map(len,slide))//2==480

def spectrum(adj):
    out=Counter();ecc=Counter(); long_pairs=[]
    for source in range(len(opt)):
        dis={source:0};queue=deque((source,))
        while queue:
            i=queue.popleft()
            for j in adj[i]:
                if j not in dis: dis[j]=dis[i]+1;queue.append(j)
        assert len(dis)==240
        ecc[(signature(opt[source]),max(dis.values()))]+=1
        for other,d in dis.items():
            if other>source:
                out[d]+=1
                if d==8:long_pairs.append((source,other))
    assert sum(out.values())==240*239//2
    return dict(sorted(out.items())),ecc,long_pairs
sj,ej,_=spectrum(jump)
ss,es,ap=spectrum(slide)
assert sj == {1:1800,2:8160,3:18480,4:240}
assert ss == {1:480,2:1440,3:3540,4:6780,5:9000,6:6000,7:1380,8:60}
assert es=={((2,3,5),7):120,((3,3,4),8):120}
assert len(ap)==60 and len({x for p in ap for x in p})==120
assert all(signature(opt[x])==signature(opt[y])==(3,3,4)
           and not(opt[x]&opt[y]) for x,y in ap)
# Explicit antipodal partner on the four-label support of each type-B set.
# A pair of same-layer vertices is a matching on four labels. Exchange
# that perfect matching for the unused one, and complement the lone edge.
for i, s in enumerate(opt):
    if signature(s) != (3,3,4): continue
    layers={h:[p for p,t in s if t==h] for h in (0,1)}
    h=next(h for h in (0,1) if len(layers[h])==2)
    a,b=layers[h]
    universe=set(a)|set(b)
    assert len(universe)==4
    lone=layers[1-h][0]
    complement=tuple(sorted(universe-set(lone)))
    rest=[p for p in P if set(p)<=universe and p not in (a,b,lone,complement)]
    assert len(rest)==2
    partner=frozenset(((complement,1-h),(rest[0],h),(rest[1],h)))
    assert partner in index
    assert (min(i,index[partner]),max(i,index[partner])) in ap
# The natural S5 x C2 group preserves the graph and has two size-120 orbits.
orbits=[]; seen=set()
for seed in range(240):
    if seed in seen: continue
    orb=set()
    for perm in permutations(range(5)):
        for flip in (0,1):
            s=frozenset((tuple(sorted(perm[x] for x in v[0])),v[1]^flip)
                        for v in opt[seed])
            orb.add(index[s])
    orbits.append(orb);seen|=orb
assert len(seen)==240 and sorted(map(len,orbits))==[120,120]
assert {tuple(signature(opt[i]) for i in orbit)[:1] for orbit in orbits}=={((2,3,5),),((3,3,4),)}
print('representation: 2-subset double cover of Petersen')
print('minimum cardinality: 3; optimum sets: 240; symmetry orbits:',[len(x) for x in orbits])
print('distance signatures:',dict(classes))
print('jump: 1800 edges; diameter 4; histogram:',sj)
print('slide: 480 edges; radius 7; diameter 8; histogram:',ss)
print('eccentricities:',dict(es))
print('diametral pairs: 60, disjoint and confined to signature (3,3,4)')
print('PASS')
