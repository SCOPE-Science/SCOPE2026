#!/usr/bin/env python3
"""Exact finite certificate for the two-matching complex of the seven-vertex complete graph."""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations
from sympy import zeros
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

NVERT=7
EDGES=list(combinations(range(NVERT),2))
M=len(EDGES)
INC=[sum(1<<i for i,edge in enumerate(EDGES) if v in edge) for v in range(NVERT)]
FACES={mask for mask in range(1,1<<M) if all((mask&z).bit_count()<=2 for z in INC)}
assert len(FACES)==15795

def boundary(mask):
    ids=[i for i in range(M) if mask>>i&1]
    return [(mask^(1<<i),(-1)**j) for j,i in enumerate(ids) if mask^(1<<i)]

remaining=set(FACES)
lower_to_upper={};upper_to_lower={}
for i in range(M):
    bit=1<<i
    for face in sorted(remaining):
        upper=face|bit
        if face in remaining and not face&bit and upper in remaining:
            remaining.remove(face);remaining.remove(upper)
            lower_to_upper[face]=upper
            upper_to_lower[upper]=face
assert len(lower_to_upper)==7675
assert len(lower_to_upper)*2+len(remaining)==len(FACES)
counts=Counter(mask.bit_count()-1 for mask in remaining)
assert counts==Counter({0:1,4:132,5:312})

# Complete directed Hasse diagram with matched covers reversed.
indeg={f:0 for f in FACES}
out=defaultdict(list)
count_covers=0
for upper in FACES:
    for lower,sign in boundary(upper):
        if lower_to_upper.get(lower)==upper:
            source,target=lower,upper
        else:
            source,target=upper,lower
        out[source].append(target);indeg[target]+=1;count_covers+=1
ready=deque(f for f in sorted(FACES) if indeg[f]==0)
topo=0
while ready:
    f=ready.popleft();topo+=1
    for g in out[f]:
        indeg[g]-=1
        if indeg[g]==0:ready.append(g)
assert topo==len(FACES)

@lru_cache(None)
def reduce_chain(face):
    if face in upper_to_lower:return {}
    if face not in lower_to_upper:return {face:1}
    u=lower_to_upper[face]
    coefficient=next(c for g,c in boundary(u) if g==face)
    accum=defaultdict(int)
    for g,c in boundary(u):
        if g==face:continue
        for h,v in reduce_chain(g).items():
            accum[h]-=coefficient*c*v
    return {h:v for h,v in accum.items() if v}

low=sorted(f for f in remaining if f.bit_count()==5)
high=sorted(f for f in remaining if f.bit_count()==6)
idx={f:i for i,f in enumerate(low)}
mat=zeros(len(low),len(high))
for j,f in enumerate(high):
    for g,sg in boundary(f):
        for h,c in reduce_chain(g).items():
            if h in idx:mat[idx[h],j]+=sg*c
D=smith_normal_form(mat,domain=ZZ)
smith=[abs(int(D[i,i])) for i in range(min(D.rows,D.cols)) if D[i,i]!=0]
assert Counter(smith)==Counter({1:131})
assert len(high)-len(low)+1==181

# Independent ordinary simplicial boundary ranks over F_2.
def gf2_rank(vectors):
    basis={}
    for x in vectors:
        while x:
            i=x.bit_length()-1
            if i in basis:x^=basis[i]
            else:basis[i]=x;break
    return len(basis)
levels={d:sorted(f for f in FACES if f.bit_count()==d+1) for d in range(8)}
ranks={}
for d in range(1,7):
    ix={f:i for i,f in enumerate(levels.get(d-1,[]))}
    ranks[d]=gf2_rank(sum(1<<ix[g] for g,_ in boundary(f)) for f in levels.get(d,[]))
betti={d:len(levels[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(8)}
betti[0]-=1
assert {d:x for d,x in betti.items() if x}=={4:1,5:181}
print('M2_K7_INTEGRAL_MIXED_WEDGE_PASS')
print('edges',M,'faces_nonempty',len(FACES),'hasse_covers',count_covers,'topological_sort_faces',topo)
print('matching_pairs',len(lower_to_upper),'critical_dimension_counts',dict(sorted(counts.items())))
print('morse_boundary_shape',mat.shape,'morse_smith_nonzero',smith)
print('direct_mod2_ranks',dict(sorted(ranks.items())))
print('direct_mod2_reduced_betti',dict(sorted((d,b) for d,b in betti.items() if b)))
