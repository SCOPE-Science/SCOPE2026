#!/usr/bin/env python3
"""Exact finite verification of the unit-edge truncated tetrahedron Euclidean Rips result.
No external modules are required. All metric tests use integer squared distances, normalized by 8.
"""
from itertools import combinations, permutations
from collections import Counter, deque

TETRA = ((1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1))
PAIRS = tuple((a,b) for a in range(4) for b in range(4) if a != b)
VERT = tuple(tuple(2*TETRA[a][k] + TETRA[b][k] for k in range(3)) for a,b in PAIRS)
INDEX = {p:i for i,p in enumerate(PAIRS)}
D = {(i,j):sum((VERT[i][k]-VERT[j][k])**2 for k in range(3)) for i,j in combinations(range(12),2)}
assert Counter(D.values()) == {8:18, 24:24, 32:12, 40:12}

def admissible(mask, threshold):
    ids = [i for i in range(12) if mask & (1<<i)]
    return all(D[i,j] <= threshold for i,j in combinations(ids,2))

def faces(threshold):
    return {mask for mask in range(1,1<<12) if admissible(mask,threshold)}

STAGE={q:faces(q) for q in (0,8,24,32,40)}
assert [Counter(m.bit_count()-1 for m in STAGE[q]) for q in (0,8,24,32)] == [
    {0:12},{0:12,1:18,2:4},{0:12,1:42,2:48,3:12},
    {0:12,1:54,2:112,3:108,4:48,5:8}]
assert len(STAGE[40]) == 2**12-1

def subfaces(mask):
    return [mask ^ (1<<i) for i in range(12) if mask & (1<<i) and mask.bit_count()>1]

def Morse_matching(active):
    """Deterministic maximal-cell removal/matched-pair elimination."""
    active=set(active); match=[]; critical=[]
    while active:
        possible=[]
        for lo in active:
            ups = [hi for hi in active if hi.bit_count()==lo.bit_count()+1 and (hi&lo)==lo]
            if len(ups)==1: possible.append((lo,ups[0]))
        if possible:
            lo,hi=min(possible,key=lambda p:(-p[0].bit_count(),p[0]))
            active.remove(lo); active.remove(hi); match.append((lo,hi))
        else:
            cell=min(active,key=lambda x:(-x.bit_count(),x))
            assert not any((y&cell)==cell and y!=cell for y in active)
            active.remove(cell); critical.append(cell)
    return match,critical

match,critical=Morse_matching(STAGE[24])
assert len(match)==54 and Counter(m.bit_count()-1 for m in critical)=={0:1,2:5}
assert len({x for a,b in match for x in (a,b)})==2*len(match)
for a,b in match: assert a in subfaces(b)

def directed_hasse_acyclic(cells,match):
    paired=set(match); out={x:[] for x in cells}; indeg={x:0 for x in cells}; incidences=0
    for hi in cells:
        for lo in subfaces(hi):
            if lo not in cells:continue
            if (lo,hi) in paired: u,v=lo,hi
            else: u,v=hi,lo
            out[u].append(v); indeg[v]+=1; incidences+=1
    Q=deque(x for x in cells if indeg[x]==0); removed=0
    while Q:
        x=Q.popleft();removed+=1
        for y in out[x]:
            indeg[y]-=1
            if indeg[y]==0:Q.append(y)
    assert removed==len(cells)
    return incidences

hasse=directed_hasse_acyclic(STAGE[24],match)

# Verify all 12 absent (distance sqrt(5)) edges decompose as 3 disjoint 4-cycles.
far_edges={ij for ij,d in D.items() if d==40}
far_adj={i:set() for i in range(12)}
for i,j in far_edges:far_adj[i].add(j);far_adj[j].add(i)
assert all(len(v)==2 for v in far_adj.values())
components=[];unvisited=set(range(12))
while unvisited:
    u=min(unvisited);seen={u};front=[u]
    while front:
        a=front.pop()
        for b in far_adj[a]:
            if b not in seen:seen.add(b);front.append(b)
    components.append(seen);unvisited-=seen
assert len(components)==3 and all(len(z)==4 for z in components)
assert all(len({next(i for i,a in enumerate(VERT[v]) if abs(a)==3) for v in c})==1 for c in components)

# Integer cycle supported on fourteen triangles in the middle complex.
CYCLE={
(0,1,3):-1,(0,1,6):1,(0,2,6):-1,(0,2,9):1,
(0,3,5):-1,(0,5,9):-1,(1,3,7):1,(1,6,7):-1,
(2,6,11):1,(2,9,11):-1,(3,5,7):1,(5,7,11):-1,
(5,9,11):1,(6,7,11):1,
}
assert all(sum(1<<v for v in tri) in STAGE[24] for tri in CYCLE)
boundary=Counter()
for triangle,weight in CYCLE.items():
    for omit in range(3):boundary[triangle[:omit]+triangle[omit+1:]]+=weight*((-1)**omit)
assert all(v==0 for v in boundary.values())

# Collapse of three disjoint Ind(C4) onto the octahedral 2-sphere.
# A vertex is labelled by its unique coordinate of absolute value 3 and its sign.
def axis_sign(v):
    axis=next(i for i,z in enumerate(VERT[v]) if abs(z)==3)
    return axis,1 if VERT[v][axis]>0 else -1

def parity(values):
    return (-1)**sum(values[i]>values[j] for i in range(len(values)) for j in range(i+1,len(values)))

def image_of_positive_xyz(tri):
    p=[axis_sign(v) for v in tri]
    if sorted(p)!=[(0,1),(1,1),(2,1)]:return 0
    return parity([a for a,s in p])
map_degree=sum(weight*image_of_positive_xyz(tri) for tri,weight in CYCLE.items())
assert map_degree==1

# Complete signed Lefschetz traces, checked for all 24 full tetrahedral symmetries.
def lefschetz_reduced(p,threshold):
    action={i:INDEX[(p[a],p[b])] for i,(a,b) in enumerate(PAIRS)}
    total=0
    for mask in STAGE[threshold]:
        vertices=[i for i in range(12) if mask>>i&1]
        mapped=[action[i] for i in vertices]
        if sorted(vertices)==sorted(mapped):
            total+=((-1)**(len(vertices)-1))*parity([vertices.index(v) for v in mapped])
    return total-1
for perm in permutations(range(4)):
    f=sum(i==p for i,p in enumerate(perm));s=parity(perm)
    assert -lefschetz_reduced(perm,8)==s*(f-1)
    assert lefschetz_reduced(perm,24)==f+s
    assert lefschetz_reduced(perm,32)==s

# Independent complete mod-two persistence reduction, including zero-length pairs.
def all_persistence():
    entries=[]
    for mask in STAGE[40]:
        k=mask.bit_count()
        t=max((D[i,j] for i,j in combinations([i for i in range(12) if mask>>i&1],2)), default=0)
        entries.append((t,k,mask))
    entries.sort();position={m:j for j,(_,_,m) in enumerate(entries)}
    reduced={};born={};intervals=[]
    for j,(time,k,mask) in enumerate(entries):
        col=0
        if k>1:
            for sub in subfaces(mask):col^=1<<position[sub]
        while col:
            low=col.bit_length()-1
            if low in reduced:col^=reduced[low]
            else:break
        if col:
            low=col.bit_length()-1;reduced[low]=col
            intervals.append((entries[low][1]-1,entries[low][0],time))
        else:born[j]=True
    return Counter((dim,birth,death) for dim,birth,death in intervals if birth<death)
assert all_persistence()==Counter({(0,0,8):11,(1,8,24):3,(2,24,32):4,(2,24,40):1})
print('VERIFY_OK; distance_shells=[8:18,24:24,32:12,40:12]')
print('f_vectors=',[(q,dict(sorted(Counter(m.bit_count()-1 for m in STAGE[q]).items()))) for q in (0,8,24,32)])
print('Morse_pairs=54; critical=(one 0-cell,five 2-cells); Hasse_incidences=',hasse)
print('far_edge_components=3 C4; projecting_cycle_size=14; degree=',map_degree)
print('full_S4_character_checks=24 of 24 at each nontrivial stage')
print('mod_two_barcode=[(0,0,8)x11,(1,8,24)x3,(2,24,32)x4,(2,24,40)x1]')
