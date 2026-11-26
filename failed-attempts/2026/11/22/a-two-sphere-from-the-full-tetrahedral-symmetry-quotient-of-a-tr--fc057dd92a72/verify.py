#!/usr/bin/env python3
"""Exact finite verification of the truncated tetrahedron independence orbit quotient."""
import collections
import itertools
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
LABELS = tuple((i,j) for i in range(4) for j in range(4) if i != j)
INDEX = {pair:i for i,pair in enumerate(LABELS)}
assert len(LABELS)==12
EDGES = {tuple(sorted((i,j))) for i,v in enumerate(LABELS)
         for j,w in enumerate(LABELS) if i<j and (v[0]==w[0] or v==w[::-1])}
assert len(EDGES)==18
ADJ = [sum(1 << j for j in range(12) if tuple(sorted((i,j))) in EDGES) for i in range(12)]
GROUP=[]
for p in itertools.permutations(range(4)):
    perm=tuple(INDEX[p[i],p[j]] for (i,j) in LABELS)
    assert len(set(perm)) == 12
    assert {tuple(sorted((perm[a],perm[b]))) for a,b in EDGES} == EDGES
    GROUP.append(perm)
assert len(set(GROUP))==24

def independent(mask):
    return all(not (ADJ[j] & mask) for j in range(12) if mask & (1 << j))

FACES = [m for m in range(1, 1<<12) if independent(m)]
FACE_SET = set(FACES)
assert collections.Counter(m.bit_count() for m in FACES) == {1:12, 2:48, 3:72, 4:30}
# Separate representation: independent sets are partial functions without two-cycles.
FUNCTION_FACES=[]
for choices in itertools.product(range(-1,4),repeat=4):
    if any(choices[i]==i for i in range(4)):
        continue
    if any(choices[i]>=0 and choices[choices[i]]==i for i in range(4) if choices[i]>=0):
        continue
    mask=0
    for i,j in enumerate(choices):
        if j>=0:mask|=1<<INDEX[i,j]
    if mask:FUNCTION_FACES.append(mask)
assert set(FUNCTION_FACES)==FACE_SET and len(FUNCTION_FACES)==len(FACES)

ACTED=[]
for p in GROUP:
    lookup=[1<<p[i] for i in range(12)]
    ACTED.append({m:sum(lookup[i] for i in range(12) if m>>i &1) for m in FACES})

def normal(chain):
    return min(tuple(g[m] for m in chain) for g in ACTED)

BY_TOP={}
ALL_CHAINS=[]
for m in sorted(FACES,key=lambda x:(x.bit_count(),x)):
    c=[(m,)]
    for sub in FACES:
        if sub !=m and sub&m==sub:
            c.extend(prev+(m,) for prev in BY_TOP[sub])
    BY_TOP[m]=c
    ALL_CHAINS.extend(c)
assert len(ALL_CHAINS)==3342
CELLS=sorted({normal(chain) for chain in ALL_CHAINS},key=lambda x:(len(x),x))
assert len(CELLS)==146
assert collections.Counter(len(c)-1 for c in CELLS)=={0:11,1:42,2:63,3:30}
POSITION={c:i for i,c in enumerate(CELLS)}
BOUNDARIES=[]
COFACES=[set() for _ in CELLS]
for k,c in enumerate(CELLS):
    b=[POSITION[normal(c[:j]+c[j+1:])] for j in range(len(c))] if len(c)>1 else []
    assert len(b)==len(set(b))
    BOUNDARIES.append(b)
    for s in b:COFACES[s].add(k)

CERT = json.loads((ROOT/'collapse_pairs.json').read_text(encoding='utf-8'))
assert CERT['schema_version']==1 and CERT['cell_count']==146
active=set(range(len(CELLS)))
assert len(CERT['pairs'])==60
for step,(f,c) in enumerate(CERT['pairs']):
    assert isinstance(f,int) and isinstance(c,int)
    assert f in active and c in active,(step,f,c)
    assert len(CELLS[c])==len(CELLS[f])+1 and f in BOUNDARIES[c]
    assert COFACES[f] == {c}, (step,f,c,COFACES[f])
    assert COFACES[c] == set(), (step,f,c,COFACES[c])
    active.difference_update((f,c))
    for lower in BOUNDARIES[f]:COFACES[lower].discard(f)
    for lower in BOUNDARIES[c]:COFACES[lower].discard(c)
assert len(active)==26
assert collections.Counter(len(CELLS[i])-1 for i in active)=={0:6,1:12,2:8}
assert sorted(active)==CERT['remaining_indices']
V={j for j in active if len(CELLS[j])==1}
E={j for j in active if len(CELLS[j])==2}
T={j for j in active if len(CELLS[j])==3}
assert all(len([x for x in BOUNDARIES[e] if x in active])==2 for e in E)
assert all(len([e for e in BOUNDARIES[t] if e in active])==3 for t in T)
assert all(len(COFACES[e])==2 for e in E)
# Check every two-dimensional cell is an embedded triangle with three distinct vertices.
for t in T:
    edges=[e for e in BOUNDARIES[t] if e in active]
    vertices={v for e in edges for v in BOUNDARIES[e] if v in V}
    assert len(vertices)==3
    assert sorted(sum(v in BOUNDARIES[e] for e in edges) for v in vertices)==[2,2,2]
# Vertex links (a vertex of the link is an incident 1-cell; each triangle creates a link edge).
for v in V:
    incident={e for e in E if v in BOUNDARIES[e]}
    link={e:collections.Counter() for e in incident}
    for t in T:
        adjacent=[e for e in BOUNDARIES[t] if e in incident]
        if adjacent:
            assert len(adjacent)==2
            a,b=adjacent
            link[a][b]+=1;link[b][a]+=1
    assert all(sum(neighbors.values())==2 for neighbors in link.values()),(v,link)
    visited={next(iter(link))}
    todo=list(visited)
    while todo:
        for nei in link[todo.pop()]:
            if nei not in visited:visited.add(nei);todo.append(nei)
    assert len(visited)==len(link),(v,len(link),len(visited))
# Connectivity of the core 1-skeleton.
start=next(iter(V));seen={start};front=[start]
while front:
    v=front.pop()
    for e in E:
        if v in BOUNDARIES[e]:
            for w in BOUNDARIES[e]:
                if w not in seen:seen.add(w);front.append(w)
assert seen==V
assert len(V)-len(E)+len(T)==2
# Closed connected surface of Euler characteristic two is S^2.
print('PASS_TRUNCATED_TETRAHEDRON_FULL_QUOTIENT_SPHERE')
print('independent faces', len(FACES), 'flags', len(ALL_CHAINS),
      'S4 orbit cells',len(CELLS),'collapses',len(CERT['pairs']),'core',(len(V),len(E),len(T)))
