#!/usr/bin/env python3
"""Exact reproducible cell-level certificate for Hom(C5,H(2,3)).
Only Python's standard library is required. Run: python3 verify.py
"""
from collections import Counter, defaultdict
from itertools import product
import json

N=9
ADJ=tuple(sum(1<<j for j in range(N) if j!=i and (i//3==j//3 or i%3==j%3)) for i in range(N))

def compatible(x,y):
    return all((ADJ[i]&y)==y for i in range(N) if x>>i&1)

def valid(c):
    return all(compatible(c[i],c[(i+1)%5]) for i in range(5))

def dim(c):
    return sum(mask.bit_count()-1 for mask in c)

# Algorithm A: exhaustive graph homomorphisms, then all allowed cell extensions.
verts={tuple(1<<i for i in seq) for seq in product(range(N),repeat=5)
       if all(ADJ[seq[k]]>>(seq[(k+1)%5])&1 for k in range(5))}
assert len(verts)==900
allcells=set(verts)
frontier=verts
while frontier:
    new=set()
    for c in frontier:
        for k in range(5):
            for j in range(N):
                if c[k]>>j&1:continue
                t=list(c);t[k]|=1<<j;t=tuple(t)
                if t not in allcells and valid(t):new.add(t)
    allcells.update(new);frontier=new
cells={d:sorted(c for c in allcells if dim(c)==d) for d in range(4)}
assert {d:len(cells[d]) for d in cells}=={0:900,1:2160,2:1440,3:180}
assert sum(len(a) for a in cells.values())==4680

# Algorithm B: independent neighborhood-intersection enumeration.
valid_mask={}
for mask in range(1,1<<N):
    neigh=(1<<N)-1
    for j in range(N):
        if mask>>j&1: neigh&=ADJ[j]
    if neigh:valid_mask[mask]=neigh
subs={neigh:[m for m in valid_mask if not m&~neigh]
      for neigh in set(valid_mask.values())}
by_neighborhood=set()
for a,na in valid_mask.items():
    for b in subs[na]:
        for c in subs[valid_mask[b]]:
            for d in subs[valid_mask[c]]:
                nd=valid_mask[d]&na
                for e in subs.get(nd,[]):
                    by_neighborhood.add((a,b,c,d,e))
assert by_neighborhood==allcells

idx={d:{cell:j for j,cell in enumerate(cells[d])} for d in cells}
up={d:[set() for _ in cells[d]] for d in range(3)}
down={d:[set() for _ in cells[d]] for d in range(1,4)}
coef={d:{} for d in range(1,4)}
for d in range(1,4):
    for k,cell in enumerate(cells[d]):
        prefix=0
        for coord,mask in enumerate(cell):
            if mask.bit_count()>1:
                for j in range(N):
                    if mask>>j&1:
                        lower=list(cell);lower[coord]=mask^(1<<j)
                        i=idx[d-1][tuple(lower)]
                        sign=(-1)**(prefix+(mask&((1<<j)-1)).bit_count())
                        assert i not in down[d][k]
                        down[d][k].add(i);up[d-1][i].add(k)
                        coef[d][i,k]=sign
            prefix+=mask.bit_count()-1
assert [len(coef[d]) for d in (1,2,3)]==[4320,5040,720]
# d^2=0 via direct sparse integer cancellation
for d in (2,3):
    for upper,facets in enumerate(down[d]):
        sums=defaultdict(int)
        for mid in facets:
            for low in down[d-1][mid]:
                sums[low]+=coef[d][mid,upper]*coef[d-1][low,mid]
        assert not any(sums.values())

# Entire one-skeleton component calculation (union-find, independent of collapse).
parent=list(range(len(cells[0])))
def root(i):
    while parent[i]!=i:
        parent[i]=parent[parent[i]];i=parent[i]
    return i
def union(i,j):
    i,j=root(i),root(j)
    if i!=j:parent[i]=j
for e,ends in enumerate(down[1]):
    a,b=sorted(ends)
    union(a,b)
classes=defaultdict(set)
for v in range(len(cells[0])):classes[root(v)].add(v)
assert len(classes)==4
assert sorted(map(len,classes.values()))==[225]*4

# Deterministic elementary collapses: a codimension-one free face with one
# surviving cofacet, itself maximal, is removed together with that cofacet.
alive={d:[True]*len(cells[d]) for d in cells}
steps=Counter()
while True:
    choice=None
    for d in (3,2,1):
        for f in range(len(cells[d-1])):
            if not alive[d-1][f]:continue
            cofaces=[c for c in up[d-1][f] if alive[d][c]]
            if len(cofaces)!=1:continue
            top=cofaces[0]
            if d<3 and any(alive[d+1][j] for j in up[d][top]):continue
            choice=d,f,top
            break
        if choice:break
    if choice is None:break
    d,f,top=choice
    assert alive[d-1][f] and alive[d][top]
    assert sum(alive[d][j] for j in up[d-1][f])==1
    assert d==3 or all(not alive[d+1][j] for j in up[d][top])
    for facet in down[d][top]:up[d-1][facet].discard(top)
    if d>=2:
        for facet in down[d-1][f]:up[d-2][facet].discard(f)
    alive[d-1][f]=False;alive[d][top]=False;steps[d]+=1
assert steps=={3:180,2:180}
assert [sum(alive[d]) for d in range(4)]==[900,1980,1080,0]

# Classify each surviving 2-dimensional connected component.
def representative(cell):
    return tuple(mask&-mask for mask in cell)
comp_id={k:i for i,k in enumerate(sorted(classes))}
which={d:{} for d in cells}
for d in cells:
    for j,cell in enumerate(cells[d]):
        if alive[d][j]:which[d][j]=comp_id[root(idx[0][representative(cell)])]
rem=defaultdict(lambda:[0]*4)
for d in cells:
    for j,c in which[d].items():rem[c][d]+=1
assert len(rem)==4
assert all(v==[225,495,270,0] for v in rem.values())

# Every surviving edge has two surviving faces.
assert all(sum(alive[2][f] for f in up[1][e])==2
           for e in range(len(cells[1])) if alive[1][e])
# Every vertex link is a single combinatorial circle, not a disjoint cycle union.
link_degrees=Counter()
for v in range(len(cells[0])):
    incident=[e for e in up[0][v] if alive[1][e]]
    assert len(incident)>0
    link={e:set() for e in incident}
    touching=set()
    for e in incident:
        touching.update(f for f in up[1][e] if alive[2][f])
    for f in touching:
        sides=[e for e in down[2][f] if alive[1][e] and v in down[1][e]]
        assert len(sides)==2
        a,b=sides;link[a].add(b);link[b].add(a)
    assert all(len(neigh)==2 for neigh in link.values())
    seen=set(); todo=[incident[0]]
    while todo:
        e=todo.pop()
        if e in seen:continue
        seen.add(e);todo.extend(link[e]-seen)
    assert len(seen)==len(incident)
    link_degrees[len(incident)]+=1
assert link_degrees=={4:600,5:240,6:60}

# Coherent orientation: all adjacent 2-cells induce opposite edge orientations.
orientation={}
for f in range(len(cells[2])):
    if not alive[2][f] or f in orientation:continue
    orientation[f]=1;todo=[f]
    while todo:
        a=todo.pop()
        for e in down[2][a]:
            if not alive[1][e]:continue
            adj=[x for x in up[1][e] if alive[2][x]]
            assert len(adj)==2
            b=adj[0] if adj[1]==a else adj[1]
            needed=-orientation[a]*coef[2][e,a]*coef[2][e,b]
            if b not in orientation:orientation[b]=needed;todo.append(b)
            else:assert orientation[b]==needed
assert len(orientation)==1080
# A closed, connected orientable 2-manifold has chi=2-2g;
# the recorded 225-495+270=0 in each of the four components gives genus 1.
assert all(sum((-1)**d*v for d,v in enumerate(vals))==0 for vals in rem.values())

print(json.dumps({
  'graph':'H(2,3) = K3 square K3 = Paley(9)',
  'hom_source':'C5',
  'polyhedral_f_vector':[900,2160,1440,180],
  'boundary_entries':[4320,5040,720],
  'full_components':4,
  'component_vertices':[225]*4,
  'collapse_pairs_by_upper_dimension':dict(sorted(steps.items())),
  'collapsed_f_vector':[900,1980,1080,0],
  'per_component_spine':[225,495,270],
  'spine_vertex_link_lengths':dict(sorted(link_degrees.items())),
  'orientable':True,
  'homotopy_type':'four disjoint orientable surfaces of genus one',
  'reduced_integral_homology':{'H0':'Z^3','H1':'Z^8','H2':'Z^4','other':'0'},
  'all_checks':'PASS'
},sort_keys=True))
