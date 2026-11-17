#!/usr/bin/env python3
"""Exhaustive integral homotopy and equivariant character certificate.

The graph is the one-dimensional triangle--triangle--quadrilateral bouquet.
Vertices 1,2 and 3,4 form triangles with vertex 0; vertices 5,6,7
form an unfilled four-cycle with vertex 0. All checks use exact integers.
"""
from itertools import permutations, product
from collections import Counter, defaultdict, deque

EDGES = ((0,1),(1,2),(2,0),(0,3),(3,4),(4,0),
         (0,5),(5,6),(6,7),(7,0))
N = 8
NEIGH = [set() for _ in range(N)]
for a,b in EDGES:
    NEIGH[a].add(b)
    NEIGH[b].add(a)
ARCS = tuple(sorted((a,b) for a,b in EDGES) + sorted((b,a) for a,b in EDGES))
ARCS = tuple(sorted(set(ARCS)))
assert len(ARCS) == 20
ARC_ID = {arc:i for i,arc in enumerate(ARCS)}

# Any filtration has a strict total order; in a 1-complex the descending
# link of a new vertex is a discrete set of earlier neighbors. It is a
# nonempty simplicial cone exactly when this set is a singleton.
def strong_matching(order):
    visited=set()
    mask=0
    for v in order:
        lower=NEIGH[v] & visited
        if len(lower)==1:
            mask |= 1 << ARC_ID[(v,next(iter(lower)))]
        visited.add(v)
    return mask

GENERATORS={strong_matching(o) for o in permutations(range(N))}
FACES={0}
for facet in GENERATORS:
    sub=facet
    while sub:
        FACES.add(sub)
        sub=(sub-1)&facet

LAYER=defaultdict(set)
for f in FACES:
    LAYER[f.bit_count()-1].add(f)
assert len(GENERATORS)==345
assert {d:len(fs) for d,fs in LAYER.items()} == {-1:1,0:20,1:108,2:220,3:144}
assert len(FACES)==493

# Explicit all-face acyclic matching on the Hasse diagram. At each stage
# toggle a fixed directed incidence, removing both matched cells.
TOGGLE_ORDER = (14,6,18,8,5,16,19,9,7,10,13,12,2,0,11,15,4,3,1,17)
UNMATCHED=set(FACES)-{0}
PAIRS=[]
for bitindex in TOGGLE_ORDER:
    bit=1<<bitindex
    for lower in sorted(tuple(UNMATCHED)):
        upper=lower|bit
        if not lower&bit and lower in UNMATCHED and upper in UNMATCHED:
            assert upper.bit_count()==lower.bit_count()+1
            UNMATCHED.remove(lower)
            UNMATCHED.remove(upper)
            PAIRS.append((lower,upper))
assert len(PAIRS)==239
assert len(UNMATCHED)==14
assert Counter(f.bit_count()-1 for f in UNMATCHED)=={0:1,3:13}

# Check no directed gradient cycles: unmatched cover edges go downward,
# paired cover edges upward, using an explicit topological sort.
P2={upper:lower for lower,upper in PAIRS}
IND=Counter()
OUT=defaultdict(list)
NONEMPTY=FACES-{0}
for upper in NONEMPTY:
    bits=upper
    while bits:
        b=bits&-bits
        bits-=b
        lower=upper-b
        if lower not in NONEMPTY:
            continue
        if P2.get(upper)==lower:
            start,end=lower,upper
        else:
            start,end=upper,lower
        OUT[start].append(end)
        IND[end]+=1
queue=deque(f for f in NONEMPTY if IND[f]==0)
processed=0
while queue:
    f=queue.popleft()
    processed+=1
    for g in OUT[f]:
        IND[g]-=1
        if IND[g]==0:
            queue.append(g)
assert processed==len(NONEMPTY)

# Independent mod-two homology calculation on ALL faces, not the Morse
# matching. Rank nullity gives reduced Betti vector (0,0,0,13).
def rank_mod2(columns):
    pivots={}
    for column in columns:
        while column:
            hi=column.bit_length()-1
            if hi in pivots:
                column^=pivots[hi]
            else:
                pivots[hi]=column
                break
    return len(pivots)

ranks={}
for d in range(1,4):
    lows={f:i for i,f in enumerate(sorted(LAYER[d-1]))}
    cols=[]
    for upper in sorted(LAYER[d]):
        bits=upper
        col=0
        while bits:
            b=bits&-bits
            bits-=b
            col^=1<<lows[upper-b]
        cols.append(col)
    ranks[d]=rank_mod2(cols)
assert ranks=={1:19,2:89,3:131}
assert 20-1-19==0 and 108-19-89==0 and 220-89-131==0 and 144-131==13

# Complete symmetry group: independent interchange of two triangle
# vertices in each petal, permutation of the two triangles, and flip of
# the square. These are all automorphisms because vertex 0 is the sole
# degree-six vertex and the three components of its complement are two
# edges and one path of length two.
def parity(seq):
    return -1 if sum(seq[i]>seq[j] for i in range(len(seq))
                     for j in range(i+1,len(seq)))%2 else 1

def character(swap, flip0, flip1, squareflip):
    perm={0:0, 6:6}
    for j,flip in enumerate((flip0,flip1)):
        dest=j^swap
        for b in (0,1):
            perm[1+2*j+b]=1+2*dest+(b^flip)
    perm[5]=7 if squareflip else 5
    perm[7]=5 if squareflip else 7
    assert set(perm.values())==set(range(N))
    assert {frozenset((perm[a],perm[b])) for a,b in EDGES} == \
           {frozenset(e) for e in EDGES}
    arcmap={i:ARC_ID[(perm[a],perm[b])] for i,(a,b) in enumerate(ARCS)}
    lefschetz=0
    for f in NONEMPTY:
        indices=[i for i in range(len(ARCS)) if f>>i&1]
        image=[arcmap[i] for i in indices]
        if set(image)==set(indices):
            lefschetz+=(-1)**(len(indices)-1)*parity(image)
    return 1-lefschetz # H_0 = Z; only positive homology in odd degree 3.

CHARS=defaultdict(list)
for swap,flip0,flip1,sq in product((0,1),repeat=4):
    if not swap and not flip0 and not flip1: kind='identity'
    elif not swap and flip0 != flip1: kind='single_triangle_flip'
    elif not swap: kind='double_triangle_flip'
    elif flip0==flip1: kind='triangle_interchange'
    else: kind='four_cycle'
    CHARS[(kind,sq)].append(character(swap,flip0,flip1,sq))
EXPECTED={
 ('identity',0):(1,13),('identity',1):(1,-9),
 ('single_triangle_flip',0):(2,-7),('single_triangle_flip',1):(2,3),
 ('double_triangle_flip',0):(1,5),('double_triangle_flip',1):(1,-1),
 ('triangle_interchange',0):(2,-7),('triangle_interchange',1):(2,3),
 ('four_cycle',0):(2,5),('four_cycle',1):(2,-1)
}
assert set(CHARS)==set(EXPECTED)
for kind,(count,trace) in EXPECTED.items():
    assert CHARS[kind]==[trace]*count, (kind,CHARS[kind])

print('GRAPH_VERTICES=8 GRAPH_EDGES=10 DIRECTED_INCIDENCES=20')
print('FILTRATIONS=40320 DISTINCT_STRONG_MATCHINGS=345')
print('FULL_COMPLEX_F_VECTOR=20,108,220,144 TOTAL_NONEMPTY=492')
print('ACYCLIC_PAIRS=239 CRITICAL_ZERO=1 CRITICAL_THREE=13')
print('HASSE_DAG_NODES=492 ACYCLIC_TOPOLOGICAL_SORT=492')
print('MOD2_BOUNDARY_RANKS=19,89,131')
print('AUTOMORPHISMS=16 CONJUGACY_CLASSES=10')
for k in ('identity','single_triangle_flip','double_triangle_flip',
          'triangle_interchange','four_cycle'):
    print('CHARACTER',k,'no_square_flip',EXPECTED[(k,0)],
          'square_flip',EXPECTED[(k,1)])
print('MIXED_CACTUS_STRONG_MORSE_FULL_CHECK_PASS')
