#!/usr/bin/env python3
"""Full-automorphism orbit check. Requires networkx >= 2.8."""
from itertools import combinations
from collections import Counter
import networkx as nx
G=nx.Graph();G.add_nodes_from(range(27))
for beta in range(3):
    for alpha in range(9):
        u=9*beta+alpha
        for a,b in ((4*alpha+1,beta-1),(4*alpha-1,beta-1),
                    (7*alpha+7,beta+1),(7*alpha-7,beta+1)):
            G.add_edge(u, 9*(b%3)+a%9)
assert len(G)==27 and G.number_of_edges()==54 and nx.is_connected(G)
assert min(dict(G.degree()).values())==4
assert nx.diameter(G)==3
# Reconstruct the same abstract graph independently from the semidirect-product Cayley model.
H=nx.Graph();H.add_nodes_from(range(27))
for y in range(3):
    for x in range(9):
        t=(1,7,4)[y]
        u=9*y+x
        for xx,yy in ((x+t,y),(x-t,y),(x+2*t,y+1),(x+t,y+2)):
            H.add_edge(u,9*(yy%3)+xx%9)
assert len(H)==27 and H.number_of_edges()==54
assert nx.is_isomorphic(G,H)
perms=list(nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter())
assert len(perms)==54

def propagates(s):
    seen=set(s)
    for u in s:seen.update(G[u])
    rounds=1
    while len(seen)!=27:
        new=set(seen)
        for u in seen:
            rem=set(G[u])-seen
            if len(rem)==1:new.update(rem)
        if new==seen:return 0
        rounds+=1;seen=new
    return rounds
S={t for t in combinations(range(27),3) if propagates(t)}
assert len(S)==567
remaining=set(S);hist=Counter();reps=[]
while remaining:
    r=min(remaining)
    orbit={tuple(sorted(p[v] for v in r)) for p in perms}
    assert orbit<=S
    remaining.difference_update(orbit)
    hist[len(orbit)]+=1
    reps.append((r,len(orbit)))
assert hist=={27:1,54:10}
print('PASS: |Aut(Holt)|=54, 11 optimal-triple orbits, lengths',dict(hist))
print('Orbit representatives (base-nine b-layer labels):',reps)
# Distinguish the two natural metric types of optimal triples.
pairtype=Counter(tuple(sorted(nx.shortest_path_length(G,u,v)
                             for u,v in combinations(s,2))) for s in S)
assert pairtype == {(2,3,3):513,(3,3,3):54}
print('PASS pair-distance type counts',dict(pairtype))
# Determine the symmetry types of the maximum relocation penalty.
ss=sorted(S); index={s:i for i,s in enumerate(ss)}
jump=[[] for _ in ss];slide=[[] for _ in ss]
for i,s in enumerate(ss):
    for old in s:
        for new in range(27):
            if new in s:continue
            v=index.get(tuple(sorted((set(s)-{old})|{new})))
            if v is not None:
                jump[i].append(v)
                if G.has_edge(old,new):slide[i].append(v)
from collections import deque
def distances(A,root):
    d={root:0};q=deque([root])
    while q:
        u=q.popleft()
        for v in A[u]:
            if v not in d:d[v]=d[u]+1;q.append(v)
    assert len(d)==len(ss)
    return d
exception=set()
for i in range(len(ss)):
    dj,dt=distances(jump,i),distances(slide,i)
    for j in range(i+1,len(ss)):
        if dt[j]-dj[j]==5:exception.add((ss[i],ss[j]))
assert len(exception)==351
remaining=exception.copy();orbits=Counter()
while remaining:
    a,b=min(remaining)
    o={tuple(sorted((tuple(sorted(m[u] for u in a)),tuple(sorted(m[u] for u in b)))))
       for m in perms}
    assert o<=exception
    remaining.difference_update(o)
    orbits[len(o)]+=1
assert orbits=={27:3,54:5}
print('PASS: maximal five-slide penalty has 351 pairs in eight automorphism orbits',dict(orbits))
