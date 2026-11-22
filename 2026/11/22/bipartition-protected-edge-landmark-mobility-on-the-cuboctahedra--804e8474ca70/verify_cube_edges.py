#!/usr/bin/env python3
"""Exact finite verification using cube-edge incidence and breadth-first search."""
from itertools import combinations, permutations
from collections import Counter, deque
import json

CUBE_EDGES = tuple((u,v) for u in range(8) for v in range(u+1,8) if (u^v).bit_count()==1)
assert len(CUBE_EDGES)==12
V=range(12)
LINKS=tuple((i,j) for i in V for j in range(i+1,12)
            if set(CUBE_EDGES[i]) & set(CUBE_EDGES[j]))
assert len(LINKS)==24
NEIGH=[set() for _ in V]
for i,j in LINKS:NEIGH[i].add(j);NEIGH[j].add(i)
assert {len(n) for n in NEIGH}=={4}
def distances(s):
    ds=[-1]*12;ds[s]=0;todo=deque([s])
    while todo:
        u=todo.popleft()
        for v in NEIGH[u]:
            if ds[v]<0:ds[v]=ds[u]+1;todo.append(v)
    return ds
D=[distances(i) for i in V]
ED=[[min(D[i][u],D[i][v]) for u,v in LINKS] for i in V]

def bases(k,columns):
    m=len(columns[0]);result=[]
    for subset in combinations(V,k):
        if len({tuple(columns[s][x] for s in subset) for x in range(m)})==m:
            result.append(sum(1<<s for s in subset))
    return result

def reconfiguration(bases):
    ids={m:i for i,m in enumerate(bases)}
    jump=[set() for _ in bases];slide=[set() for _ in bases]
    for i,m in enumerate(bases):
        for u in V:
            if m&(1<<u):
                for v in V:
                    if not m&(1<<v):
                        nb=ids.get(m^(1<<u)^(1<<v))
                        if nb is not None:
                            jump[i].add(nb)
                            if v in NEIGH[u]: slide[i].add(nb)
    return jump,slide

def summary(adj):
    unvisited=set(range(len(adj))); comps=[];shells=Counter();eccs=[]
    while unvisited:
        s=min(unvisited);stack=[s];comp={s};unvisited.remove(s)
        while stack:
            v=stack.pop()
            for u in adj[v]:
                if u in unvisited:unvisited.remove(u);comp.add(u);stack.append(u)
        dia=0;rad=10**9
        for s in comp:
            dst={s:0};q=deque([s])
            while q:
                u=q.popleft()
                for v in adj[u]:
                    if v not in dst:dst[v]=dst[u]+1;q.append(v)
            assert len(dst)==len(comp)
            mx=max(dst.values());dia=max(dia,mx);rad=min(rad,mx)
            eccs.append(mx)
            for v,d in dst.items():
                if v>s:shells[d]+=1
        comps.append((len(comp),rad,dia,tuple(sorted(comp))))
    return {'n':len(adj),'edges':sum(map(len,adj))//2,
            'components':[(n,r,d) for n,r,d,_ in comps],
            'degree_counts':dict(sorted(Counter(map(len,adj)).items())),
            'distance_counts':dict(sorted(shells.items())),
            'eccentricity_counts':dict(sorted(Counter(eccs).items()))},comps

assert not bases(4,ED)
EB=bases(5,ED)
assert len(EB)==168
assert not bases(2,D)
VB=bases(3,D)
assert len(VB)==96
EJ,ES=reconfiguration(EB)
VJ,VS=reconfiguration(VB)
ej, _=summary(EJ);es,ecs=summary(ES);vj,_=summary(VJ);vs,_=summary(VS)
assert ej['edges']==948 and ej['components']==[(168,5,5)]
assert es['edges']==360 and [(n,r,d) for n,r,d,*_ in es['components']]==[(84,6,6),(84,6,6)]
assert vs['components']==[(96,7,8)]
missing={}
for i,m in enumerate(EB):
    covered={v for j,(u,v) in enumerate(CUBE_EDGES) if m&(1<<j) for v in (u,v)}
    absent=set(range(8))-covered
    assert len(absent)==1
    missing[i]=next(iter(absent))
assert Counter(missing.values())==Counter({i:21 for i in range(8)})
for i,adj in enumerate(ES):
    assert all(missing[i].bit_count()%2==missing[j].bit_count()%2 for j in adj)
for n,r,d,c in ecs:
    assert len({missing[i].bit_count()%2 for i in c})==1
assert {missing[i].bit_count()%2 for i in ecs[0][3]} != {missing[i].bit_count()%2 for i in ecs[1][3]}

# Automorphism orbit sizes via coordinate permutations and bit flips.
autos=set()
for p in permutations(range(3)):
    for toggle in range(8):
        def f(x):return sum(((x>>i)&1)<<p[i] for i in range(3))^toggle
        autos.add(tuple(CUBE_EDGES.index(tuple(sorted((f(u),f(v))))) for u,v in CUBE_EDGES))
assert len(autos)==48
unseen=set(EB);orbits=[]
while unseen:
    m=min(unseen)
    o={sum(1<<a[j] for j in V if m&(1<<j)) for a in autos}
    assert o<=unseen or not unseen.isdisjoint(o)
    unseen-=o;orbits.append(len(o))
assert sorted(orbits)==[24,48,48,48]
print(json.dumps({'edge_dim':5,'edge_bases':168,'metric_dim':3,'metric_bases':96,
                  'missing_counts':dict(sorted(Counter(missing.values()).items())),
                  'automorphism_orbit_sizes':sorted(orbits),
                  'edge_jump':ej,'edge_slide':es,
                  'vertex_jump':vj,'vertex_slide':vs},sort_keys=True))
