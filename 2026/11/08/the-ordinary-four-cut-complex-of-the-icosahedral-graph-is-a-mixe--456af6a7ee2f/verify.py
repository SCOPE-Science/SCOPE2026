#!/usr/bin/env python3
"""Exact finite certificate for the ordinary four-cut complex of the icosahedral graph.

Requires Python 3.9+ and only its standard library. Uses integer bitmasks and
signed cellular boundary formulas throughout; no floating-point tests.
"""
from itertools import combinations
from functools import lru_cache
from collections import Counter, defaultdict, deque
from math import comb

N = 12

def graph_edges():
    edges=set()
    def add(a,b):
        assert a != b
        edges.add(tuple(sorted((a,b))))
    for i in range(5):
        u=1+i; l=6+i
        add(0,u);add(11,l)
        add(u,1+(i+1)%5)
        add(l,6+(i+1)%5)
        add(u,l)
        add(u,6+(i-1)%5)
    assert len(edges)==30
    return edges

EDGES=graph_edges()
NB=[0]*N
for u,v in EDGES:
    NB[u]|=1<<v
    NB[v]|=1<<u
assert all(x.bit_count()==5 for x in NB)

def is_connected(indices):
    members=sum(1<<v for v in indices)
    reached=1<<indices[0]
    while True:
        new=reached
        for u in range(N):
            if reached & (1<<u):new|=NB[u]&members
        if new==reached:return reached==members
        reached=new

def mask_elements(mask):
    return [i for i in range(N) if mask & (1<<i)]

FACETS=set()
for group in combinations(range(N),4):
    if not is_connected(group):
        FACETS.add(((1<<N)-1)^sum(1<<i for i in group))
assert len(FACETS)==285

# A simplicial face is a subset of at least one facet.
FACES={0}
for facet in FACETS:
    sub=facet
    while sub:
        FACES.add(sub)
        sub=(sub-1)&facet
assert len(FACES)==3503
F_VECTOR=[sum(x.bit_count()==k for x in FACES) for k in range(1,9)]
assert F_VECTOR==[12,66,220,495,792,912,720,285]
# The twelve missing 6-element faces are exactly the complements of
# closed vertex neighborhoods (six-vertex wheels).
missing_six={mask for mask in range(1<<N) if mask.bit_count()==6 and mask not in FACES}
closed_neighborhood_complements={((1<<N)-1)^(NB[v]|(1<<v)) for v in range(N)}
assert len(missing_six)==12
assert missing_six==closed_neighborhood_complements

# Completely independent complement characterization on all 4096 subsets.
for mask in range(1<<N):
    complement=[v for v in range(N) if not mask & (1<<v)]
    indirect=(len(complement)>=4 and any(not is_connected(group)
                  for group in combinations(complement,4)))
    assert (mask in FACES)==indirect

@lru_cache(None)
def boundary(mask):
    return [(mask^(1<<i),(-1)**j) for j,i in enumerate(mask_elements(mask))]

# Complete ordered elementary vertex matching; can be checked by matching-graph DAG.
def morse_matching(order):
    remaining=set(FACES)
    pairs=[]
    for v in order:
        stage=[(a,a|(1<<v)) for a in remaining if not a&(1<<v)
               and (a|(1<<v)) in remaining]
        for a,b in stage:
            remaining.remove(a)
            remaining.remove(b)
        pairs.extend(stage)
    assert len(remaining)+2*len(pairs)==len(FACES)
    assert len(set(a for a,b in pairs)|set(b for a,b in pairs))==2*len(pairs)
    return pairs,remaining

# Check complete Forman acyclicity by an independently built directed Hasse diagram.
def verify_acyclic(pairs):
    matched={(a,b) for a,b in pairs}
    indegree={mask:0 for mask in FACES}
    adj=defaultdict(list)
    count=0
    for upper in FACES:
        for lower,_ in boundary(upper):
            assert lower in FACES
            if (lower,upper) in matched:
                src,dst=lower,upper
            else:
                src,dst=upper,lower
            adj[src].append(dst)
            indegree[dst]+=1
            count+=1
    q=deque(x for x in FACES if indegree[x]==0)
    visited=0
    while q:
        a=q.popleft();visited+=1
        for b in adj[a]:
            indegree[b]-=1
            if indegree[b]==0:q.append(b)
    assert visited==len(FACES),('Morse directed cycle',visited,len(FACES))
    return count

# The exact Morse differential is computed by unit elimination in the
# reduced signed simplicial chain complex (the empty simplex is a -1-cell).
def morse_boundary(pairs,critical):
    upward=dict(pairs)
    downward={b:a for a,b in pairs}
    @lru_cache(None)
    def projected(face):
        if face in critical:return {face:1}
        if face in downward:return {}
        parent=upward[face]
        pivot=dict(boundary(parent))[face]
        out=defaultdict(int)
        for other,sgn in boundary(parent):
            if other==face:continue
            for critical_face,coef in projected(other).items():
                out[critical_face]-=pivot*sgn*coef
        return {k:v for k,v in out.items() if v}
    dim6=sorted(f for f in critical if f.bit_count()==7)
    dim7=sorted(f for f in critical if f.bit_count()==8)
    matrix=[]
    for lo in dim6:
        row=[]
        for hi in dim7:
            row.append(sum(c*projected(f).get(lo,0) for f,c in boundary(hi)))
        matrix.append(row)
    return matrix,(len(dim6),len(dim7))

def rank_mod2_of_boundary(degree):
    lows=sorted(x for x in FACES if x.bit_count()==degree)
    uppers=sorted(x for x in FACES if x.bit_count()==degree+1)
    index={m:j for j,m in enumerate(lows)}
    pivots={}
    for face in uppers:
        col=sum(1<<index[lower] for lower,_ in boundary(face))
        while col:
            lead=col.bit_length()-1
            if lead in pivots:col^=pivots[lead]
            else:
                pivots[lead]=col
                break
    return len(pivots)

# Degree-0 through degree-7 chain ranks (the augmentation is rank 1).
RANKS=[rank_mod2_of_boundary(d) for d in range(1,8)]
assert RANKS==[11,55,165,330,462,450,265],RANKS

pairs,critical=morse_matching(range(N))
incidences=verify_acyclic(pairs)
assert len(pairs)==1738
assert Counter(f.bit_count()-1 for f in critical)=={6:6,7:21}
M,shape=morse_boundary(pairs,critical)
assert shape==(6,21)
nonzero_cols=[j for j in range(shape[1]) if any(M[i][j] for i in range(shape[0]))]
assert len(nonzero_cols)==1
col=[M[i][nonzero_cols[0]] for i in range(shape[0])]
assert sum(abs(x)==1 for x in col)>=1
assert all(x in (-1,0,1) for x in col)
# One primitive nonzero attaching column: 6 minus 1 = 5 six-spheres,
# 21 minus 1 = 20 seven-spheres, with no other cells in reduced Morse CW.
assert (shape[0]-1,shape[1]-1)==(5,20)
assert sum((-1)**i*f for i,f in enumerate(F_VECTOR))-1 == -15

# Compare a separate matching order without recycling any cancellation path.
pairs2,critical2=morse_matching(reversed(range(N)))
incidences2=verify_acyclic(pairs2)
M2,shape2=morse_boundary(pairs2,critical2)
# A second exact rational rank, using fraction-free primitive row elimination.
from fractions import Fraction
work=[[Fraction(c) for c in row] for row in M2]
rank=0
for colindex in range(len(work[0])):
    pivot=next((i for i in range(rank,len(work)) if work[i][colindex]),None)
    if pivot is None:continue
    work[rank],work[pivot]=work[pivot],work[rank]
    p=work[rank][colindex]
    for j in range(colindex,len(work[rank])):work[rank][j]/=p
    for i in range(rank+1,len(work)):
        c=work[i][colindex]
        if c:
            for j in range(colindex,len(work[i])):work[i][j]-=c*work[rank][j]
    rank+=1
    if rank==len(work):break
assert (shape2[0]-rank,shape2[1]-rank)==(5,20)

print('ICOSAHEDRAL_4CUT_INTEGRAL_HOMOTOPY_VERIFIED')
print('vertices=12 edges=30 disconnected_four_sets=285 faces=3503')
print('face_vector='+','.join(map(str,F_VECTOR)))
print('missing_six_faces=12_closed_neighborhood_complements')
print('mod2_boundary_ranks='+','.join(map(str,RANKS)))
print('hasse_incidences='+str(incidences))
print('first_matching_pairs=1738 critical_dim6=6 critical_dim7=21')
print('first_morse_matrix_shape=6x21 rank=1 primitive_unit_column=True')
print('alternate_matching_pairs='+str(len(pairs2))+' critical_dim6='+str(shape2[0])+' critical_dim7='+str(shape2[1])+' boundary_rank='+str(rank))
print('reduced_betti_6=5 reduced_betti_7=20 integral_homotopy=S6^5_vee_S7^20')
