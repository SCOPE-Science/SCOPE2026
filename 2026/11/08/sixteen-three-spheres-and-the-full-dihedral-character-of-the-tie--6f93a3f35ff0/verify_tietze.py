#!/usr/bin/env python3
"""Finite certificate for the ordinary matching complex of the Tietze graph.
Run: python3 tietze_check.py. Only the Python standard library is required.
"""
from collections import Counter, deque
from itertools import combinations

# The Petersen graph with one degree-three vertex inflated to a triangle.
# Vertex labels are 1,...,12; edge order is used as bit positions.
EDGES = [(1,2),(1,6),(1,10),(2,3),(2,7),(3,4),(3,8),
         (4,9),(4,11),(5,7),(5,8),(5,12),(6,8),(6,9),(7,9),
         (10,11),(10,12),(11,12)]
PIVOTS = [11,9,0,16,2,15,10,3,5,17,14,6,7,8,4,1,13,12]
N = len(EDGES)
assert N == 18 and len(set(EDGES)) == N
assert Counter(v for e in EDGES for v in e) == {v:3 for v in range(1,13)}

# First construction: dynamic-programming bit masks, including the empty face.
vertex_masks=[(1 << a)|(1 << b) for a,b in EDGES]
possible=bytearray(1<<N)
possible[0]=1
occupied=[0]*(1<<N)
for m in range(1, 1<<N):
    b=m&-m; i=b.bit_length()-1;prev=m^b
    if possible[prev] and occupied[prev]&vertex_masks[i]==0:
        possible[m]=1
        occupied[m]=occupied[prev]|vertex_masks[i]
faces=[m for m in range(1<<N) if possible[m]]
assert len(faces)==1052
bydim=Counter(m.bit_count()-1 for m in faces if m)
assert [bydim[d] for d in range(6)] == [18,117,335,408,165,8]
facets=Counter(m.bit_count()-1 for m in faces if m and all(
    not possible[m|(1<<i)] for i in range(N) if not m&(1<<i)))
assert facets=={3:15,4:117,5:8}

# Second construction: direct backtracking over edge subsets, independent of DP.
rec_faces=[]
def add_matchings(index, seen, face):
    if index==N:
        rec_faces.append(face)
        return
    add_matchings(index+1, seen, face)
    if not seen&vertex_masks[index]:
        add_matchings(index+1, seen|vertex_masks[index], face|(1<<index))
add_matchings(0,0,0)
assert len(rec_faces)==len(faces) and set(rec_faces)==set(faces)

# A fully specified staged toggling matching on the augmented face poset.
# Remove the empty face and retain its former singleton partner as critical.
remaining=set(faces)
pairs=[]
for i in PIVOTS:
    bit=1<<i
    for m in faces:
        if (m not in remaining) or m&bit:
            continue
        bigger=m|bit
        if bigger in remaining:
            remaining.remove(m)
            remaining.remove(bigger)
            pairs.append((m,bigger))
assert len(pairs)==518 and remaining=={
    834,1172,4740,4868,9252,33928,41480,41992,69776,
    69904,73808,81954,132130,132228,147522,147524}
assert (0,1<<11) in pairs
ordinary_pairs=[(u,v) for u,v in pairs if u]
paired_low={a:b for a,b in ordinary_pairs}
paired_high={b:a for a,b in ordinary_pairs}
assert len(ordinary_pairs)==517
critical=[x for x in faces if x and x not in paired_low and x not in paired_high]
assert len(critical)==17 and Counter(x.bit_count()-1 for x in critical)=={0:1,3:16}

# Acyclicity is checked on *every* ordinary face-poset covering relation.
indeg={m:0 for m in faces if m}
arrows={m:[] for m in faces if m}
cover_count=0
for upper in faces:
    if not upper:continue
    for i in range(N):
        if not upper&(1<<i):continue
        lower=upper^(1<<i)
        if not lower:continue
        cover_count+=1
        if paired_low.get(lower)==upper:
            source,target=upper,lower
        else:
            source,target=lower,upper
        arrows[source].append(target)
        indeg[target]+=1
queue=deque(m for m in indeg if indeg[m]==0)
visited=0
while queue:
    m=queue.popleft();visited+=1
    for nxt in arrows[m]:
        indeg[nxt]-=1
        if indeg[nxt]==0:queue.append(nxt)
assert cover_count==3744 and visited==1051
print('FACE_COUNTS',*(bydim[d] for d in range(6)))
print('MAXIMAL_FACE_COUNTS_DIM_3_4_5',*[facets[d] for d in (3,4,5)])
print('MATCHING',len(ordinary_pairs),'critical_vertex',critical[0] if critical[0].bit_count()==1 else (1<<11),'critical_3cells',16)
print('ACYCLIC',visited,'of',len(faces)-1,'cover_relations',cover_count)

# Independent simplicial-chain computation modulo 2 and 3.
# Columns = simplicial upper faces, with oriented alternating boundaries.
face_by_dim={d: sorted(m for m in faces if m and m.bit_count()==d+1) for d in range(6)}
def boundary_ranks(p):
    ranks={}
    for d in range(1,6):
        row={m:i for i,m in enumerate(face_by_dim[d-1])}
        basis={}
        for upper in face_by_dim[d]:
            vector={}
            j=0
            for k in range(N):
                if upper&(1<<k):
                    lower=upper^(1<<k)
                    c=(1 if j%2==0 else p-1)
                    vector[row[lower]]=c
                    j+=1
            while vector:
                pivot=min(vector)
                if pivot not in basis:
                    inv=pow(vector[pivot],-1,p)
                    basis[pivot]={k:(v*inv)%p for k,v in vector.items()}
                    break
                mult=vector[pivot]
                for k,v in basis[pivot].items():
                    w=(vector.get(k,0)-mult*v)%p
                    if w:vector[k]=w
                    else:vector.pop(k,None)
        ranks[d]=len(basis)
    betti=[len(face_by_dim[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(6)]
    assert betti==[1,0,0,16,0,0]
    print('BOUNDARY_MOD',p,'RANKS',*[ranks[d] for d in range(1,6)],'BETTI',*betti)
for modulus in (2,3):boundary_ranks(modulus)

# Exact group automorphisms, with independent brute-force backtracking.
V=tuple(range(1,13))
adj={v:set() for v in V}
for a,b in EDGES:
    adj[a].add(b);adj[b].add(a)
Eset={frozenset(e) for e in EDGES}
triangles={frozenset(t) for t in combinations(V,3) if all(frozenset(e) in Eset for e in combinations(t,2))}
assert triangles=={frozenset((10,11,12))}
colors={v:int(v in (10,11,12)) for v in V}
autos=[]
def generate_maps(partial, unused):
    if not unused:
        if len(partial)==12: autos.append(tuple(partial[v] for v in V))
        return
    unassigned=[v for v in V if v not in partial]
    def candidates(v):
        return [w for w in V if w in unused and colors[v]==colors[w]
                and all((u in adj[v])==(partial[u] in adj[w]) for u in partial)]
    v=min(unassigned,key=lambda t:(len(candidates(t)),-len(adj[t].intersection(partial)),t))
    for w in candidates(v):
        partial[v]=w
        generate_maps(partial, unused-{w})
        del partial[v]
generate_maps({},set(V))
assert len(autos)==12 and len(set(autos))==12

def compose(g,h):
    return tuple(g[h[v-1]-1] for v in V)
def power(g,n):
    t=V
    for _ in range(n):t=compose(g,t)
    return t
r=(5,7,2,1,4,8,9,3,6,12,10,11)
s=(1,2,7,5,4,6,3,9,8,10,12,11)
assert r in autos and s in autos
assert power(r,6)==V and all(power(r,a)!=V for a in range(1,6))
assert power(s,2)==V and compose(compose(s,r),s)==power(r,5)
assert {compose(power(r,a),power(s,b)) for a in range(6) for b in range(2)}==set(autos)
print('AUTOMORPHISMS',len(autos),'isomorphic_to_dihedral_order12')

# Lefschetz signed-simplex traces determine the rational H3 character.
idx={e:i for i,e in enumerate(EDGES)}
def edgeperm(g):
    return tuple(idx[tuple(sorted((g[a-1],g[b-1])))] for a,b in EDGES)
def homology_trace(g):
    ep=edgeperm(g)
    lef=0
    for m in faces:
        if not m:continue
        listed=[i for i in range(N) if m&(1<<i)]
        mapped=[ep[i] for i in listed]
        if set(mapped)!=set(listed):continue
        inds=[listed.index(j) for j in mapped]
        inv=sum(inds[a]>inds[b] for a in range(len(inds)) for b in range(a+1,len(inds)))
        sign=(-1)**inv
        lef+=(-1)**(len(listed)-1)*sign
    return 1-lef
T={}
for a in range(6):
    for b in range(2):
        T[(a,b)]=homology_trace(compose(power(r,a),power(s,b)))
assert [T[(a,0)] for a in range(6)]==[16,0,-2,0,-2,0]
assert [T[(a,1)] for a in range(6)]==[0]*6

# Ordinary character orthogonality for D6: four 1D and two 2D irreps.
chi1={}
for u in (1,-1):
    for v in (1,-1):
        key=(u,v)
        chi1[key]={(a,b):u**a*v**b for a in range(6) for b in range(2)}
chars2={1:(2,1,-1,-2,-1,1),2:(2,-1,-1,2,-1,-1)}
multiplicities={}
for name,char in chi1.items():
    num=sum(T[k]*char[k] for k in T)
    assert num%12==0
    multiplicities[str(name)]=num//12
for k,values in chars2.items():
    num=sum(T[(a,0)]*values[a] for a in range(6))
    assert num%12==0
    multiplicities['2dim_'+str(k)]=num//12
assert list(multiplicities.values())==[1,1,1,1,3,3]
print('CHAR_ROTATIONS',*[T[(a,0)] for a in range(6)])
print('CHAR_REFLECTIONS',*[T[(a,1)] for a in range(6)])
print('IRREDUCIBLE_MULTIPLICITIES',multiplicities)
print('TIETZE_MATCHING_WEDGE_AND_DIHEDRAL_CHARACTER_PASS')
