#!/usr/bin/env python3
"""Exact checks for the scale-two Rips complex of a cyclic 11-point biplane.
Run: python3 verify_biplane_rips.py  (Python standard library only).
All dimensions and matrices are reconstructed rather than loaded from saved output.
"""
from collections import deque, Counter
from itertools import combinations

N = 11
BASE = (1, 3, 4, 5, 9)
BLOCKS = [frozenset((i + a) % N for a in BASE) for i in range(N)]
assert len(set(BLOCKS)) == 11
assert all(len(b) == 5 for b in BLOCKS)
assert all(sum(p in b for b in BLOCKS) == 5 for p in range(N))
assert all(sum({a,b} <= B for B in BLOCKS) == 2 for a,b in combinations(range(N), 2))
assert all(len(BLOCKS[i] & BLOCKS[j]) == 2 for i,j in combinations(range(N), 2))

EDGES = [(p,b) for p in range(N) for b in range(N) if p in BLOCKS[b]]
assert len(EDGES) == 55
EDGE_INDEX = {e:i for i,e in enumerate(EDGES)}
ADJ = [set() for _ in range(22)]
for p,b in EDGES:
    ADJ[p].add(11+b)
    ADJ[11+b].add(p)
for root in range(22):
    d = [-1]*22
    d[root] = 0
    todo = deque([root])
    while todo:
        x = todo.popleft()
        for y in ADJ[x]:
            if d[y] < 0:
                d[y] = d[x]+1
                todo.append(y)
    assert all(v>=0 for v in d)
    for y in range(22):
        expected = (0 if y == root else
                    2 if ((root < 11) == (y < 11)) else
                    1 if y in ADJ[root] else 3)
        assert d[y] == expected, (root,y,d[y],expected)

# Exhaustively list maximal cliques of the graph of distance <= 2.
SQUARE = [set(range(22))-{x}-{y for y in range(22)
           if (x<11)!=(y<11) and y not in ADJ[x]} for x in range(22)]
def maximal_cliques():
    found=[]
    def extend(R,P,X):
        if not P and not X:
            found.append(frozenset(R)); return
        u=max(P|X, key=lambda v:len(P & SQUARE[v])) if (P|X) else None
        for v in sorted(P - (SQUARE[u] if u is not None else set())):
            extend(R+[v], P&SQUARE[v], X&SQUARE[v])
            P.remove(v);X.add(v)
    extend([],set(range(22)),set())
    return set(found)

expected_facets = {frozenset(range(11)),frozenset(range(11,22))}
for b in range(11):
    expected_facets.add(frozenset([11+b]+sorted(BLOCKS[b])))
for p in range(11):
    expected_facets.add(frozenset([p]+[11+b for b in range(11) if p in BLOCKS[b]]))
for p,r in combinations(range(11),2):
    common = [b for b in range(11) if p in BLOCKS[b] and r in BLOCKS[b]]
    assert len(common) == 2
    expected_facets.add(frozenset((p,r,11+common[0],11+common[1])))
actual_facets = maximal_cliques()
assert actual_facets == expected_facets, (len(actual_facets),len(expected_facets))
assert len(expected_facets) == 79

# Check the exact cellular attaching matrix. Each quadrilateral is oriented
# using point-to-block incidence edges, so its 55-vector has entries (1,-1,1,-1).
SQUARE_CYCLES=[]
for p,r in combinations(range(11),2):
    b,c=[j for j in range(11) if p in BLOCKS[j] and r in BLOCKS[j]]
    chain=[0]*len(EDGES)
    for edge,sgn in (((p,b),1),((r,b),-1),((r,c),1),((p,c),-1)):
        chain[EDGE_INDEX[edge]] += sgn
    assert sum(chain)==0
    for v in range(22):
        bdry=sum(chain[EDGE_INDEX[(v,e)]] for e in range(11) if (v,e) in EDGE_INDEX) if v<11 else -sum(chain[EDGE_INDEX[(p,v-11)]] for p in range(11) if (p,v-11) in EDGE_INDEX)
        assert bdry==0
    SQUARE_CYCLES.append(chain)
assert len(SQUARE_CYCLES)==55

# Rooted breadth-first spanning tree, and its 34 oriented chords.
seen={0};todo=deque([0]);tree=set()
while todo:
    u=todo.popleft()
    for v in sorted(ADJ[u]):
        if v not in seen:
            seen.add(v);todo.append(v)
            tree.add((min(u,v),max(u,v)))
assert len(seen)==22 and len(tree)==21
CHORDS=[e for e in EDGES if (min(e[0],11+e[1]),max(e[0],11+e[1])) not in tree]
assert len(CHORDS)==34
chosen=(27,38,4,40,39,41,22,28,32,7,51,24,15,43,46,18,45,33,3,14,8,29,11,35,10,13,47,44,19,25,49,53,6,26)
assert len(set(chosen))==len(CHORDS)
M=[[SQUARE_CYCLES[j][EDGE_INDEX[e]] for j in chosen] for e in CHORDS]

def bareiss_det(A):
    A=[row[:] for row in A]
    n=len(A)
    if n==0:return 1
    sign=1;previous=1
    for k in range(n-1):
        if A[k][k]==0:
            x=next((i for i in range(k+1,n) if A[i][k]),None)
            if x is None:return 0
            A[k],A[x]=A[x],A[k];sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=A[i][j]*pivot-A[i][k]*A[k][j]
                assert num%previous==0
                A[i][j]=num//previous
        for i in range(k+1,n): A[i][k]=0
        previous=pivot
    return sign*A[-1][-1]
assert bareiss_det(M)==-1

# Direct mod-two simplicial homology, independently of the cellular argument.
F=[set() for _ in range(11)]
for facet in actual_facets:
    vv=sorted(facet)
    for d in range(len(vv)):
        for face in combinations(vv,d+1):F[d].add(face)
assert not F[-1] or max(map(len,F[-1]))==11
ranks=[]
for d in range(1,11):
    source=sorted(F[d]);targets={f:i for i,f in enumerate(sorted(F[d-1]))}
    basis={}
    for face in source:
        col=0
        for k in range(len(face)):
            lower=face[:k]+face[k+1:]
            col ^= 1<<targets[lower]
        while col:
            pos=col.bit_length()-1
            if pos not in basis:
                basis[pos]=col;break
            col ^= basis[pos]
    ranks.append(len(basis))
faces=[len(z) for z in F]
bettis=[]
for d in range(11):
    incoming=ranks[d] if d<len(ranks) else 0
    outgoing=ranks[d-1] if d>0 else 0
    bettis.append(faces[d]-incoming-outgoing)
assert bettis==[1,0,0,21]+[0]*7, (faces,bettis)

print('DESIGN: points=11 blocks=11 incidences=55 common_point_blocks=2')
print('METRIC: diameter=3; square maximal facets=79 (2 pure, 22 stars, 55 rectangles)')
print('INCIDENCE: cycle_rank=34; rectangles=55')
print('INTEGRAL: oriented_4cycle_chord_minor_order=34 determinant=-1')
print('RELATIVE: 55 three_cells; 34 kill_spheres; 21 survive_three_spheres')
print('MOD2: f_vector='+str(faces))
print('MOD2: betti_vector='+str(bettis))
# The vertex actions s(point p)=p+1, s(block b)=b+1 and
# d(point p)=block(-p), d(block b)=point(-b) generate D_22.
def shift(v,a=1):
    return (v+a)%11 if v<11 else 11+(v-11+a)%11
def dual(v):
    return 11+(-v)%11 if v<11 else (-(v-11))%11
assert all(dual(dual(v))==v for v in range(22))
assert all(dual(shift(dual(v)))==shift(v,10) for v in range(22))
assert all(shift(v,11)==v for v in range(22))
allfaces = set().union(*F)
assert sum(map(len,F)) == len(allfaces)
def lefschetz(g):
    assert len({g(v) for v in range(22)})==22
    assert {frozenset(g(v) for v in face) for face in actual_facets} == actual_facets
    fixed_chains={}
    for face in allfaces:
        img=[g(v) for v in face]
        if set(img)!=set(face):continue
        inversions=sum(img[i]>img[j] for i in range(len(img)) for j in range(i+1,len(img)))
        fixed_chains[len(face)-1]=fixed_chains.get(len(face)-1,0) + (-1)**inversions
    Lef=sum((-1)**dim * coef for dim,coef in fixed_chains.items())
    return 1-Lef,fixed_chains
assert lefschetz(lambda v:v)[0]==21
for a in range(1,11):
    assert lefschetz(lambda v,a=a:shift(v,a))[0]==-1
for a in range(11):
    trace,terms=lefschetz(lambda v,a=a:shift(dual(v),a))
    assert trace==1 and terms=={1:-5,3:5},(a,trace,terms)
Q=set(BASE)
paired=[p for p in range(11) if (2*p)%11 in Q]
tetra=[(p,r) for p,r in combinations(paired,2) if (p+r)%11 in Q]
assert paired==[2,6,7,8,10]
assert tetra==[(2,7),(2,10),(6,8),(6,10),(7,8)]
print('DIHEDRAL: order=22 rotations_trace=(21,-1 x 10) reflections_trace=(1 x 11)')
print('REFLECTION: five fixed paired edges (sign -), five fixed tetrahedra (sign +)')
print('RATIONAL: H3=1_trivial + 2*(10_dim_rational_D22_irrep)')
print('DUALITY: plus_eigenspace=11 minus_eigenspace=10')
print('BIPLANE_DIHEDRAL_RIPS_21_S3_CHARACTER_PASS')
