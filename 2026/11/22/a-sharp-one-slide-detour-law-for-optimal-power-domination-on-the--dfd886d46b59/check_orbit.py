#!/usr/bin/env python3
"""Residue-orbit checks for the Paley 17 classification."""
from itertools import combinations
import json
from pathlib import Path
from collections import Counter

p=17
R=frozenset(a for a in range(1,p) if pow(a,8,p)==1)
assert R==frozenset((1,2,4,8,9,13,15,16))

def connected(a,b):
    return a!=b and (a-b)%p in R

V=frozenset(range(p))
N={x: frozenset(y for y in V if connected(x,y)) for x in V}

def sequence(S):
    seen=frozenset(set(S)|set().union(*(N[v] for v in S)))
    steps=[seen]
    while True:
        added={next(iter(N[v]-seen)) for v in seen if len(N[v]-seen)==1}
        if not added: break
        seen=seen|added;steps.append(seen)
    return steps

assert all(sequence([x])[-1] != V for x in V)
assert len(V-sequence([0,1])[0])==4
assert V-sequence([0,1])[-1] == {6,7,11,12}
assert V-sequence([0,3])[0] == {6,10,14}
assert sequence([0,3])[-1] == V
assert {v: {u for u in sequence([0,3])[0] if N[u]-sequence([0,3])[0]=={v}} for v in (6,10,14)}=={6:{4,7},10:{9,11},14:{13,16}}

S=frozenset(tuple(c) for c in combinations(range(p),2) if not connected(*c))
assert len(S)==68
base=(0,3)
affine=lambda x,r,b:(r*x+b)%p
images={tuple(sorted((affine(0,r,b),affine(3,r,b)))) for r in R for b in range(p)}
assert images==S and len(images)==68

def neigh(e,sliding):
    u,v=e
    candidates=[]
    for w in V-{u,v}:
        for fixed,removed in ((u,v),(v,u)):
            z=tuple(sorted((fixed,w)))
            if z in S and (not sliding or connected(removed,w)):
                candidates.append(z)
    return set(candidates)

L={e:neigh(e,False) for e in S}
G={e:neigh(e,True) for e in S}
assert all(len(L[e])==14 and len(G[e])==8 for e in S)
# Verify abstract graph identifications using adjacency rules on complementary edges.
for e in S:
    for f in S-{e}:
        common=set(e)&set(f)
        assert (f in L[e])==(len(common)==1)
        if len(common)==1:
            u=next(iter(set(e)-common));v=next(iter(set(f)-common))
            assert (f in G[e])==connected(u,v)
        else:assert f not in G[e]

def distances(graph):
    d={base:0}; frontier={base}; level=0
    while frontier:
        next_frontier=set().union(*(graph[u] for u in frontier))-set(d)
        level += 1
        for x in next_frontier: d[x]=level
        frontier=next_frontier
    return d

dL=distances(L); dG=distances(G)
assert len(dL)==len(dG)==68
assert Counter(dL.values())=={0:1,1:14,2:50,3:3}
assert Counter(dG.values())=={0:1,1:8,2:32,3:27}
assert Counter(dG[e]-dL[e] for e in S)=={0:38,1:30}
cert=json.loads(Path(__file__).with_name('root_spheres.json').read_text(encoding='utf8'))
assert cert['modulus']==17 and cert['residues']==sorted(R)
assert len(cert['root_distances'])==68
for row in cert['root_distances']:
    pair=tuple(row['pair'])
    assert pair in S and (row['jump'],row['slide'])==(dL[pair],dG[pair])
# Paley affine automorphisms transport both distance functions from base to every source.
for r in R:
    for b in range(p):
        h=lambda e:tuple(sorted(((r*e[0]+b)%p,(r*e[1]+b)%p)))
        for e in S:
            assert {h(f) for f in G[e]}==G[h(e)]
            assert {h(f) for f in L[e]}==L[h(e)]
print('ORBIT_OK all 68 nonedges affine equivalent, power domination opposite to adjacency')
print('BASE_JUMP_PROFILE 1,14,50,3; BASE_SLIDE_PROFILE 1,8,32,27')
print('BASE_LOCAL_PENALTY 0:38 1:30; TOTAL_UNORDERED 0:1258 1:1020')
