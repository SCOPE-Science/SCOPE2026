#!/usr/bin/env python3
"""Reproduce the finite homotopy certificate for the Heawood induced-forest complex.
No external dependencies. Python 3.9+.

Vertices 0..6 are points of the Fano plane; 7..13 index its lines.
Line t is {t, t+1, t+3} modulo 7.
"""
from collections import Counter, defaultdict, deque

N=14
LINES=tuple(frozenset((t+d)%7 for d in (0,1,3)) for t in range(7))
EDGES=tuple(sorted((p,7+t) for t,L in enumerate(LINES) for p in L))
assert len(LINES)==7 and all(len(x)==3 for x in LINES)
assert all(sum({u,v}<=L for L in LINES)==1 for u in range(7) for v in range(u+1,7))
assert len(EDGES)==21
ADJ=[0]*N
for u,v in EDGES:
    ADJ[u]|=1<<v
    ADJ[v]|=1<<u
assert all(x.bit_count()==3 for x in ADJ)

# Method A: disjoint-set cycle detection by adding induced edges.
def is_forest_unionfind(mask):
    parent=list(range(N))
    def root(a):
        while parent[a]!=a:
            a=parent[a]
        return a
    for a,b in EDGES:
        if ((mask>>a)&1) and ((mask>>b)&1):
            r,s=root(a),root(b)
            if r==s: return False
            parent[r]=s
    return True

# Method B: a graph is a forest iff number of edges is vertices - components.
def is_forest_euler(mask):
    edges=sum((ADJ[i]&mask).bit_count() for i in range(N) if mask & (1<<i))//2
    unseen=mask
    comps=0
    while unseen:
        comps+=1
        start=unseen&-unseen
        reached=start
        fringe=start
        while fringe:
            bit=fringe&-fringe
            fringe-=bit
            vertex=bit.bit_length()-1
            new=ADJ[vertex]&mask&~reached
            reached|=new
            fringe|=new
        unseen &=~reached
    return edges==mask.bit_count()-comps

F={s for s in range(1<<N) if is_forest_unionfind(s)}
assert F=={s for s in range(1<<N) if is_forest_euler(s)}
assert len(F)==12792
NONEMPTY=F-{0}
F_VEC=dict(sorted(Counter(s.bit_count()-1 for s in NONEMPTY).items()))
assert F_VEC=={0:14,1:91,2:364,3:1001,4:2002,5:2975,6:3208,7:2254,8:812,9:70}

# Deterministic stagewise matching, on the nonempty face poset.
# At stage v, pair every remaining face s without v to remaining s U {v}.
remaining=set(NONEMPTY)
matched={}
stages=[]
for v in range(N):
    count=0
    for s in sorted(remaining):
        t=s | (1<<v)
        if not (s&(1<<v)) and t in remaining:
            assert s in remaining
            remaining.remove(s)
            remaining.remove(t)
            matched[s]=t
            count+=1
    stages.append(count)
assert len(matched)==6391
assert stages==[5831,280,128,66,37,22,22,0,0,2,3,0,0,0],stages
assert Counter(s.bit_count()-1 for s in remaining)=={0:1,8:8}
CRITICAL=tuple(sorted(remaining))
assert CRITICAL==(1,15288,15308,15336,15796,15844,16268,16280,16328)

# Full augmented Hasse graph (nonempty faces): reverse exactly matched edges.
indegree={s:0 for s in NONEMPTY}
arrows=defaultdict(list)
cover=0
for upper in NONEMPTY:
    vbits=upper
    while vbits:
        bit=vbits&-vbits
        vbits-=bit
        lower=upper^bit
        if lower==0: continue
        cover+=1
        if matched.get(lower)==upper:
            src,dst=lower,upper
        else:
            src,dst=upper,lower
        arrows[src].append(dst)
        indegree[dst]+=1
assert cover==81634
queue=deque(sorted(s for s in NONEMPTY if indegree[s]==0))
visited=0
while queue:
    s=queue.popleft()
    visited+=1
    for t in arrows[s]:
        indegree[t]-=1
        if indegree[t]==0:queue.append(t)
assert visited==len(NONEMPTY), (visited,len(NONEMPTY))

# Independent F_2 simplicial homology by sparse-column bitset elimination.
# Even though the Morse matching already certifies integral homotopy,
# this check does not depend on the matching or its acyclicity.
bydim=defaultdict(list)
for s in NONEMPTY: bydim[s.bit_count()-1].append(s)
for vals in bydim.values():vals.sort()
rank={}
for d in range(1,max(bydim)+1):
    basis={}; pivots=0
    rows={s:i for i,s in enumerate(bydim[d-1])}
    for sigma in bydim[d]:
        bits=0
        rem=sigma
        while rem:
            bit=rem&-rem
            rem-=bit
            bits^=1<<rows[sigma^bit]
        while bits:
            j=bits.bit_length()-1
            if j in basis:bits^=basis[j]
            else:
                basis[j]=bits
                pivots+=1
                break
    rank[d]=pivots
betti={d:len(bydim[d])-rank.get(d,0)-rank.get(d+1,0) for d in bydim}
betti[0]-=1  # reduced H0 for nonempty connected complex
assert {d:v for d,v in betti.items() if v}!={}
assert {d:v for d,v in betti.items() if v}=={8:8},betti

# Other boundary checks: Euler, maximum faces, number of facets.
euler=sum((-1)**d*cnt for d,cnt in F_VEC.items())
assert euler==9
facets=[s for s in NONEMPTY if all((s|1<<v) not in F for v in range(N) if not(s>>v&1))]
facetvec=dict(sorted(Counter(s.bit_count()-1 for s in facets).items()))
print('GRAPH_VERTICES',N,'GRAPH_EDGES',len(EDGES),'FANO_LINES',len(LINES))
print('FOREST_FACES_INCLUDING_EMPTY',len(F))
print('F_VECTOR',F_VEC)
print('FACETS_DIMENSION_COUNTS',facetvec)
print('MORSE_STAGE_PAIR_COUNTS',stages)
print('MORSE_CRITICAL_FACE_MASKS',CRITICAL)
print('MORSE_PAIRS',len(matched))
print('HASSE_COVER_EDGES',cover)
print('ACYCLIC_VISITED',visited)
print('MOD2_BOUNDARY_RANKS',dict(sorted(rank.items())))
print('MOD2_REDUCED_BETTI',dict(sorted((k,v) for k,v in betti.items() if v)))
print('EULER',euler)
print('INTEGRAL_WEDGE_CERTIFICATE_PASS')
