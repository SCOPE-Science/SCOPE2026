#!/usr/bin/env python3
"""Exact standard-library certificate for the Pappus Rips degree-five symmetry module.

The graph, group, join, traces, and primitive integral invariant are all
reconstructed, with no external data files or third-party libraries.
"""
from collections import Counter, defaultdict, deque
from itertools import product
from math import gcd

N = 18

def graph_edges():
    edges = set()
    for x in range(3):
        for y in range(3):
            p = 3*x+y
            for family, val in enumerate((x,y,(y-x)%3)):
                edges.add((p,9+3*family+val))
    return edges

E=graph_edges()
assert len(E)==27
neighbors=[set() for _ in range(N)]
for a,b in E:
    neighbors[a].add(b)
    neighbors[b].add(a)
assert all(len(x)==3 for x in neighbors)

# Identify the configuration without relying on its name: compare with the
# published 18-vertex LCF representation using an explicit bijection.
LCF=(5,7,-7,7,-7,-5)
LCF_edges={tuple(sorted((i,(i+1)%N))) for i in range(N)}
LCF_edges |= {tuple(sorted((i,(i+LCF[i%6])%N))) for i in range(N)}
label=(0,2,8,16,4,14,12,10,6,1,15,11,17,3,7,5,13,9)
assert set(label)==set(range(N))
assert {tuple(sorted((label[a],label[b]))) for a,b in E}==LCF_edges

# Verify full distance data with BFS, including the diameter.
distance=[]
for s in range(N):
    d=[-1]*N
    d[s]=0
    Q=deque([s])
    while Q:
        u=Q.popleft()
        for v in sorted(neighbors[u]):
            if d[v]<0:
                d[v]=d[u]+1
                Q.append(v)
    assert all(z>=0 for z in d)
    distance.append(d)
assert all(distance[i][j]==distance[j][i] for i in range(N) for j in range(N))
assert max(max(row) for row in distance)==4

# The distance-four graph must be six triangles, not merely 2-regular.
remaining=set(range(N));blocks=[]
while remaining:
    u=min(remaining)
    B=tuple(sorted([v for v in range(N) if distance[u][v]==4]+[u]))
    assert len(B)==3 and set(B)<=remaining
    assert all(distance[a][b]==4 for a in B for b in B if a!=b)
    assert all(distance[a][v]!=4 for a in B for v in range(N) if v not in B)
    blocks.append(B)
    remaining.difference_update(B)
assert blocks==[(0,5,7),(1,3,8),(2,4,6),(9,10,11),(12,13,14),(15,16,17)]
block_of={frozenset(B):i for i,B in enumerate(blocks)}

# Independent exhaustive check of the 4095 faces of the Rips complex at 3.
faces=[]
for mask in range(1,1<<N):
    verts=[v for v in range(N) if mask>>v&1]
    if all(distance[a][b]<=3 for a in verts for b in verts if a<b):
        faces.append(mask)
assert len(faces)==4**6-1
assert Counter(f.bit_count() for f in faces)=={1:18,2:135,3:540,4:1215,5:1458,6:729}
print('GRAPH_AND_JOIN_OK vertices=18 edges=27 diameter=4 blocks=6x3 faces=4095')

# Find ALL graph automorphisms. Backtracking over images of each vertex is
# exhaustive because an automorphism preserves all vertex-pair distances.
# A candidate inconsistent with any assigned distance cannot be extended.
automorphisms=[]
search_nodes=0

def all_isometries(partial,used):
    global search_nodes
    search_nodes+=1
    if len(partial)==N:
        automorphisms.append(tuple(partial[i] for i in range(N)))
        return
    u=max((i for i in range(N) if i not in partial),
          key=lambda i:(sum(j in partial for j in neighbors[i]),-i))
    for target in range(N):
        if target in used:continue
        if all(distance[u][j]==distance[target][partial[j]] for j in partial):
            partial[u]=target
            used.add(target)
            all_isometries(partial,used)
            used.remove(target)
            del partial[u]

all_isometries({},set())
assert search_nodes==3313
assert len(automorphisms)==216 and len(set(automorphisms))==216
assert all({tuple(sorted((g[a],g[b]))) for a,b in E}==set(tuple(sorted(e)) for e in E)
           for g in automorphisms)
print('GROUP_OK automorphisms=216 exhaustive_search_nodes=3313')


def permutation_sign(p):
    inversions=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return (-1)**(inversions%2)

# Integral top homology is the graded tensor product of six augmentation
# lattices; block permutations contribute the Koszul sign of the permutation.
def character_join(g):
    p=[block_of[frozenset(g[v] for v in B)] for B in blocks]
    c=permutation_sign(p)
    seen=set()
    for i in range(6):
        if i in seen:continue
        cyc=[];j=i
        while j not in seen:
            seen.add(j);cyc.append(j);j=p[j]
        assert j==i
        fp=0
        for v in blocks[i]:
            w=v
            for _ in cyc:
                w=g[w]
            fp+=(w==v)
        c*=fp-1
    return c

# Completely independent character calculation: signed simplicial Lefschetz
# traces on every fixed face, with the empty face removed (reduced homology).
def character_lefschetz(g):
    total=0
    for face in faces:
        verts=[v for v in range(N) if face>>v&1]
        images=[g[v] for v in verts]
        if sorted(images)!=verts:continue
        # orientation sign of the permutation of the vertices of this face
        sign=permutation_sign(images)
        total+=(-1)**(len(verts)-1)*sign
    # reduced alternating Lefschetz number is total - 1.
    # Only reduced homology H_5 survives, so trace(H_5)=-(total-1).
    return 1-total

values=[]
for g in automorphisms:
    a=character_join(g)
    b=character_lefschetz(g)
    assert a==b,(g,a,b)
    values.append(a)
char_counts=Counter(values)
assert char_counts=={-8:18,-2:36,0:54,1:56,4:42,16:9,64:1}
assert sum(values)==216
assert sum(x*x for x in values)==8424

def is_bipartition_preserving(g):
    return all(g[i]<9 for i in range(9))

preserve=[character_join(g) for g in automorphisms if is_bipartition_preserving(g)]
exchange=[character_join(g) for g in automorphisms if not is_bipartition_preserving(g)]
assert len(preserve)==len(exchange)==108
assert sum(preserve)==324 and sum(exchange)==-108
print('CHARACTER_OK histogram='+repr(sorted(char_counts.items())))
print('FIXED_RANKS_OK full=1 bipartition_preserving=3 character_sum=216')

# Construct the primitive integral invariant by averaging a pure tensor.
# For the ordered triples B_i=(b_i0,b_i1,b_i2), the augmentation lattice
# has basis e_(b_i1)-e_(b_i0), e_(b_i2)-e_(b_i0).
# A tensor basis is encoded by six 0/1 bits.
def basis_action(g, bits):
    p=[block_of[frozenset(g[v] for v in B)] for B in blocks]
    sign=permutation_sign(p)
    local=[None]*6
    for i,bit in enumerate(bits):
        j=p[i]
        bj=blocks[j]
        a=bj.index(g[blocks[i][bit+1]])
        b=bj.index(g[blocks[i][0]])
        local[j]=(int(a==1)-int(b==1),int(a==2)-int(b==2))
    out={}
    for coord in product(range(2),repeat=6):
        c=sign
        for j in range(6):
            c*=local[j][coord[j]]
        if c:out[coord]=c
    return out

seed=(0,)*6
orbit_sum=defaultdict(int)
for g in automorphisms:
    for coord,c in basis_action(g,seed).items():orbit_sum[coord]+=c
orbit_sum={k:v for k,v in orbit_sum.items() if v}
assert len(orbit_sum)==42
assert gcd(*[abs(x) for x in orbit_sum.values()])==12
primitive={coord:coef//12 for coord,coef in orbit_sum.items()}
assert sorted({abs(v) for v in primitive.values()})==[1]
for g in automorphisms:
    transformed=defaultdict(int)
    for coord,c in primitive.items():
        for tgt,d in basis_action(g,coord).items():
            transformed[tgt]+=c*d
    assert {k:v for k,v in transformed.items() if v}==primitive
# A nonzero fixed vector with a unit coefficient is primitive in Z^64.
# Since rank_Z of the fixed sublattice equals rank_Q=1, it generates it.
print('INTEGRAL_FIXED_VECTOR_OK orbit_sum_divisor=12 support=42 coefficients=+1_or_-1')
print('QUOTIENT_RATIONAL_HOMOLOGY_OK reduced_H5_rank=1 other_reduced_ranks=0')
print('ALL_CHECKS_PASS')
