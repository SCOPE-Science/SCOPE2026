#!/usr/bin/env python3
"""Independent exhaustive checker for the two-matching complex of a pentagonal prism.

Requires Python 3.9+ standard library only. In particular it does not import external
mathematics software, stored certificates, or published computations.
"""
from collections import Counter, deque

N=5
VERTICES=2*N
EDGES=tuple(sorted({tuple(sorted((i,(i+1)%N))) for i in range(N)} |
                   {tuple(sorted((i+N,N+(i+1)%N))) for i in range(N)} |
                   {(i,i+N) for i in range(N)}))
assert len(EDGES)==15 and len(set(EDGES))==15
M=len(EDGES)

# Independent exhaustive face characterizations: degrees and forbidden full stars.
incident=[sum(1<<j for j,(a,b) in enumerate(EDGES) if v in (a,b)) for v in range(VERTICES)]
assert all(x.bit_count()==3 for x in incident)
valid_by_star={s for s in range(1<<M) if all((s&star)!=star for star in incident)}
valid_by_degree=set()
for s in range(1<<M):
    deg=[0]*VERTICES
    for i,(a,b) in enumerate(EDGES):
        if (s>>i)&1:
            deg[a]+=1;deg[b]+=1
    if all(d<=2 for d in deg):valid_by_degree.add(s)
assert valid_by_star==valid_by_degree
F=valid_by_star
assert len(F)==10895
f=Counter(s.bit_count()-1 for s in F)
assert [f[k] for k in range(-1,10)]==[1,15,105,445,1245,2358,2985,2400,1100,230,11]

# Repeated-toggle Forman matching in increasing edge order. Deterministic.
remaining=set(F)
pairs=[]
for i in range(M):
    for a in sorted(remaining):
        b=a|(1<<i)
        if ((a>>i)&1)==0 and a in remaining and b in remaining:
            remaining.remove(a);remaining.remove(b)
            pairs.append((a,b))
assert len(remaining)==1
critical=next(iter(remaining))
assert critical.bit_count()==7, (critical,critical.bit_count())
assert len(pairs)==5447
assert (0,1) in pairs
assert all(a.bit_count()+1==b.bit_count() for a,b in pairs)
assert all(a in F and b in F for a,b in pairs)
assert len({x for p in pairs for x in p})==2*len(pairs)

# Remove the augmentation pair (empty set, singleton {first edge}). This leaves
# a genuine discrete Morse matching on the nonempty face poset with one critical
# zero-cell and one critical six-cell. Hasse edges: unmatched upper -> lower,
# matched lower -> upper, per Forman gradient paths.
nonempty=F-{0}
ordinary_pairs=[(a,b) for a,b in pairs if a!=0]
assert len(ordinary_pairs)==5446
matched=set(ordinary_pairs)
assert len(nonempty)==10894
assert {x for x in nonempty if x not in {z for p in ordinary_pairs for z in p}}=={1,critical}

succ={x:[] for x in nonempty}
indeg={x:0 for x in nonempty}
incidences=0
for b in nonempty:
    bits=b
    while bits:
        bit=bits&-bits;bits-=bit
        a=b^bit
        if a==0:continue
        assert a in nonempty
        incidences+=1
        # matched edges point up; unmatched edges point down.
        if (a,b) in matched:
            src,dst=a,b
        else:
            src,dst=b,a
        succ[src].append(dst)
        indeg[dst]+=1
queue=deque(x for x in nonempty if indeg[x]==0)
visited=0
while queue:
    x=queue.popleft()
    visited+=1
    for y in succ[x]:
        indeg[y]-=1
        if indeg[y]==0:queue.append(y)
assert visited==len(nonempty), ('cyclic',visited,len(nonempty))

# A separate Euler characteristic check. A CW complex with one 0-cell and one
# 6-cell has chi=2, hence it must agree with the actual f-vector alternating sum.
chi=sum((-1)**k*f[k] for k in range(10))
assert chi==2,chi
facets=[s for s in nonempty if not any(((s|1<<i) in F) for i in range(M) if not (s>>i)&1)]
facet_sizes=Counter(s.bit_count() for s in facets)
assert all(s.bit_count()<=10 for s in facets)
print('GRAPH_VERTICES',VERTICES)
print('GRAPH_EDGES',len(EDGES))
print('EDGES',EDGES)
print('FACES_INCLUDING_EMPTY',len(F))
print('F_VECTOR_DIM_MINUS_ONE_TO_NINE',[f[k] for k in range(-1,10)])
print('FACET_SIZE_COUNTS',sorted(facet_sizes.items()))
print('EULER_CHARACTERISTIC',chi)
print('REPEATED_TOGGLE_PAIRS_AUGMENTED',len(pairs))
print('REPEATED_TOGGLE_PAIRS_ORDINARY',len(ordinary_pairs))
print('HASSE_INCIDENCES_CHECKED',incidences)
print('DIRECTED_ACYCLICITY_VERTICES_CHECKED',visited)
print('CRITICAL_VERTEX_EDGE_INDEX',0)
print('CRITICAL_SIX_SIMPLEX_EDGE_INDICES',[i for i in range(M) if (critical>>i)&1])
print('CRITICAL_CELLS',[(0,1),(6,1)])
print('INTEGRAL_HOMOTOPY_TYPE','S^6')
print('VERIFICATION','PASS')
