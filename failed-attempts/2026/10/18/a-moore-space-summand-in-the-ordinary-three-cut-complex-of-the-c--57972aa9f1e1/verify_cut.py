#!/usr/bin/env python3
"""Self-contained exact verification of a finite Clebsch graph 3-cut-complex homotopy calculation."""
from itertools import combinations
from collections import Counter,deque
from functools import lru_cache
from math import gcd
from functools import reduce

N=16
FULL=(1<<N)-1
GENERATORS={1,2,4,8,15}
ORDER=[9,15,12,0,7,11,10,14,1,8,6,3,4,5,2,13]

def adj(a,b): return a^b in GENERATORS

def sizes(f): return f.bit_count()-1

# Check the canonical graph, its common-neighbor parameters, and C4 overlap.
for a in range(N):
    assert sum(adj(a,b) for b in range(N) if b!=a)==5
for a,b in combinations(range(N),2):
    common=sum(adj(a,c) and adj(b,c) for c in range(N))
    assert common == (0 if adj(a,b) else 2)
squares=[quad for quad in combinations(range(N),4)
         if all(sum(adj(a,b) for a,b in combinations(tr,2))==2
                for tr in combinations(quad,3))]
assert len(squares)==40
edge_c4=Counter(tuple(sorted((a,b))) for quad in squares
                for a,b in combinations(quad,2) if adj(a,b))
assert len(edge_c4)==40 and set(edge_c4.values())=={4}
print('CLEBSCH_GRAPH',N,'EDGES',40,'SQUARES',len(squares),'SQUARES_PER_EDGE',4)

# Faces of Delta_3(G) from complementary disconnected induced triples.
disconnected=[]
connected=[]
for t in combinations(range(N),3):
    e=sum(adj(a,b) for a,b in combinations(t,2))
    (disconnected if e<2 else connected).append(t)
assert len(disconnected)==400 and len(connected)==160
facets=[FULL^sum(1<<i for i in t) for t in disconnected]
faces={0}
for F in facets:
    m=F
    while m:
        faces.add(m)
        m=(m-1)&F
assert len(faces)==65199, len(facets)==400
counts=Counter(sizes(m) for m in faces if m)
print('CUT_FACES',len(faces),'FACETS',len(facets),'F_VECTOR',sorted(counts.items()))
assert all(F in faces for F in facets)
assert all(len([v for v in disconnected if sum(1<<i for i in v)&F ==0])==1 for F in facets)

# Lexicographic sequence of element matchings, using a single pivot per stage.
current=set(faces)
matching={}
for v in ORDER:
    bit=1<<v
    lower={f for f in current if not f&bit and (f|bit) in current}
    for f in lower: matching[f]=f|bit
    current.difference_update(lower)
    current.difference_update({f|bit for f in lower})
assert len(matching)==(len(faces)-len(current))//2
critical=Counter(sizes(f) for f in current)
assert critical==Counter({11:16,12:1}),critical
print('MATCH_PAIRS',len(matching),'CRITICAL',sorted(critical.items()))
assert (0 in matching)

# Direct Hasse-digraph check, before removing empty-vertex pair.
# Orient unmatched incidences downward; matching edges upward.
out=[[] for _ in range(1<<N)]
indegree=[0]*(1<<N)
incidences=0
for upper in faces:
    if upper==0: continue
    for j in range(N):
        bit=1<<j
        if upper&bit:
            lower=upper^bit
            assert lower in faces
            incidences+=1
            if matching.get(lower)==upper:
                a,b=lower,upper
            else:
                a,b=upper,lower
            out[a].append(b)
            indegree[b]+=1
q=deque(m for m in faces if indegree[m]==0)
visited=0
while q:
    m=q.popleft(); visited+=1
    for w in out[m]:
        indegree[w]-=1
        if indegree[w]==0:q.append(w)
assert visited==len(faces),(visited,len(faces))
print('ACYC' ,visited,'HASSE_INCIDENCES',incidences)

# Compute exact integral Morse boundary from unique critical dimension-12 cell
# to the 16 critical dimension-11 cells.
crit11=sorted(f for f in current if sizes(f)==11)
crit12=next(f for f in current if sizes(f)==12)
idx={f:i for i,f in enumerate(crit11)}
low11_to_high12={low:high for low,high in matching.items() if sizes(low)==11}

def oriented_boundary(upper):
    bits=[i for i in range(N) if upper>>i&1]
    return [(upper^(1<<b),(-1)**j) for j,b in enumerate(bits)]

@lru_cache(None)
def reduce11(face):
    if face in idx:
        return (tuple(1 if i==idx[face] else 0 for i in range(len(crit11))))
    if face not in low11_to_high12:
        return (0,)*len(crit11)
    upper=low11_to_high12[face]
    boundary=oriented_boundary(upper)
    pivot=next(c for f,c in boundary if f==face)
    output=[0]*len(crit11)
    for f,c in boundary:
        if f==face:continue
        r=reduce11(f)
        for j,a in enumerate(r):output[j]-=pivot*c*a
    return tuple(output)

coeff=[0]*len(crit11)
for face,c in oriented_boundary(crit12):
    r=reduce11(face)
    for j,a in enumerate(r):coeff[j]+=c*a
print('MORSE_TOP_BOUNDARY',coeff,'GCD',reduce(gcd,coeff,0),'CACHED_FACES',reduce11.cache_info().currsize)
assert reduce(gcd,coeff,0)==2
assert coeff==[0,0,0,0,-2,2,2,-2,-2,2,-2,0,0,0,0,-2]
assert sum((-1)**d*count for d,count in critical.items()) == -15 # reduced Euler characteristic
print('VERIFY_OK')
