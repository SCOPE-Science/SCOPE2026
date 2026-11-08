#!/usr/bin/env python3
"""Exact finite verification of two hexagon-flip systems of Heawood matchings.
Uses only the Python standard library; all graph data are constructed here.
"""
from itertools import product
from collections import Counter, deque

D = (0,1,3)
P = range(7)
V = range(14)
E = frozenset((p,7+j) for p in P for j in P if (p-j)%7 in D)
N = {v: set() for v in V}
for a,b in E:
    N[a].add(b); N[b].add(a)
assert len(E)==21 and all(len(N[v])==3 for v in V)

# All injective point-line assignments, via all 3^7 local choices.
matchings=[]
for diffs in product(D,repeat=7):
    lines=tuple((p-diffs[p])%7 for p in P)
    if len(set(lines))==7:
        m=frozenset((p,7+lines[p]) for p in P)
        matchings.append(m)
assert len(matchings)==24 and len(set(matchings))==24
idx={m:i for i,m in enumerate(matchings)}

# Exhaustively list simple undirected six-cycles; canonicalize by edge sets.
cycles=set()
for v in V:
    stack=[(v,(v,))]
    while stack:
        a,path=stack.pop()
        if len(path)==6:
            if v in N[a]:
                c=frozenset(tuple(sorted((path[k],path[(k+1)%6]))) for k in range(6))
                cycles.add(c)
            continue
        for b in N[a]:
            if b not in path:
                stack.append((b,path+(b,)))
assert len(cycles)==28
cycles=sorted(cycles,key=lambda c:tuple(sorted(c)))

# Every six-cycle flip is generated once for each eligible matching.
G={i:set() for i in range(24)}
for i,m in enumerate(matchings):
    usable=0
    for c in cycles:
        if len(m & c)==3:
            other=m ^ c
            assert other in idx
            G[i].add(idx[other]);usable+=1
    assert usable==7
for i in G:
    assert all(i in G[j] for j in G[i])
assert sum(map(len,G.values()))//2==84

def distances(graph, root):
    dist={root:0};q=deque([root])
    while q:
        v=q.popleft()
        for w in graph[v]:
            if w not in dist:
                dist[w]=dist[v]+1;q.append(w)
    return dist

assert all(Counter(distances(G,i).values())==Counter({0:1,1:7,2:14,3:2}) for i in G)
IA=set()
for i in G:
    di=distances(G,i)
    for j in G:
        k=di[j]
        if k==0:continue
        IA.add((k, sum(di[n]==k-1 for n in G[j]),
                sum(di[n]==k for n in G[j]),
                sum(di[n]==k+1 for n in G[j])))
assert IA=={(1,1,2,4),(2,2,4,1),(3,7,0,0)},IA

# Coxeter graph on the 28 Heawood six-cycles, adjacent if vertex-disjoint.
cv=[frozenset(v for e in c for v in e) for c in cycles]
cox={i:{j for j in range(28) if j!=i and not(cv[i]&cv[j])} for i in range(28)}
assert all(len(cox[i])==3 for i in cox)
hepts=[]
for m in matchings:
    h=frozenset(i for i,c in enumerate(cycles) if len(c&m)==3)
    assert len(h)==7
    assert all(len(cox[v]&h)==2 for v in h)
    # A degree-two graph on seven vertices must be connected here.
    q=[next(iter(h))];seen=set(q)
    while q:
        for w in cox[q.pop()]&h:
            if w not in seen:seen.add(w);q.append(w)
    assert seen==h
    hepts.append(h)
assert len(set(hepts))==24
# Also enumerate every simple Coxeter heptagon, independently of matchings.
coxeter_7cycles=set()
for start in range(28):
    stack=[(start,(start,))]
    while stack:
        v,walk=stack.pop()
        if len(walk)==7:
            if start in cox[v]:
                coxeter_7cycles.add(frozenset(walk))
            continue
        for w in cox[v]:
            if w not in walk:
                stack.append((w,walk+(w,)))
assert len(coxeter_7cycles)==24
assert coxeter_7cycles==set(hepts)
# Exact canonical adjacency rule in terms of a common Coxeter 2-path.
for i in range(24):
    for j in range(i+1,24):
        common=hepts[i]&hepts[j]
        common_edges=sum(w in cox[v] for v in common for w in common)//2
        assert (j in G[i])==(len(common)==3 and common_edges==2)

# Oriented 7-hexagon torus map from compatible local rotations.
rot={p:[7+(p-d)%7 for d in D] for p in P}
rot.update({7+j:[(j+d)%7 for d in D] for j in P})
def successor(a,b):
    r=rot[b]
    return (b,r[(r.index(a)+1)%3])
darts={(a,b) for a,b in E}|{(b,a) for a,b in E}
faces=[]
while darts:
    start=next(iter(darts));cur=start;walk=[]
    while True:
        assert cur in darts
        darts.remove(cur);walk.append(cur)
        cur=successor(*cur)
        if cur==start: break
    faces.append(frozenset(tuple(sorted(e)) for e in walk))
assert len(faces)==7 and all(len(f)==6 for f in faces)
assert all(sum(e in f for f in faces)==2 for e in E)

R={i:set() for i in range(24)}
for i,m in enumerate(matchings):
    for f in faces:
        if len(m&f)==3: R[i].add(idx[m^f])
assert all(i in R[j] for i in R for j in R[i])
assert sum(map(len,R.values()))//2==21
components=[];remaining=set(R)
while remaining:
    i=next(iter(remaining));q=[i];c={i}
    while q:
        for j in R[q.pop()]:
            if j not in c:c.add(j);q.append(j)
    components.append(c);remaining-=c
assert Counter(map(len,components))==Counter({1:3,7:3})
assert all(len(R[i])==0 for comp in components if len(comp)==1 for i in comp)
assert all(all(len(R[i])==2 for i in comp) for comp in components if len(comp)==7)

# Direction-counts classify the six resonance components.
def signature(m):
    return tuple(sum((p-(j-7))%7==d for p,j in m) for d in D)
sig=Counter(signature(m) for m in matchings)
assert sig==Counter({(7,0,0):1,(0,7,0):1,(0,0,7):1,
                    (2,4,1):7,(4,1,2):7,(1,2,4):7}),sig
for c in components:
    assert len({signature(matchings[i]) for i in c})==1
print('PASS 24 matchings, 28 hexagons, all-hexagon flip Klein array {7,4,1;1,2,7}')
print('PASS canonical 24 Coxeter heptagons and common-two-path flip criterion')
print('PASS seven-face toroidal resonance 3 isolated plus three 7-cycles')
