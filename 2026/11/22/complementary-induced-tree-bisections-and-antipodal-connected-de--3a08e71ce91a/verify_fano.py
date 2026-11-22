#!/usr/bin/env python3
"""Exact connected-feedback vertex set and exchange census for Fano incidence graph.
Uses only the Python standard library. Vertex labels are 0..6 for nonzero
GF(2)^3 point vectors 1..7; labels 7..13 for polar line normals 1..7.
"""
from itertools import combinations
from collections import Counter, deque
from math import comb

N=14
FULL=(1<<N)-1
ADJ=[0]*N
for p in range(1,8):
    for normal in range(1,8):
        if ((p&normal).bit_count()%2)==0:
            u,v=p-1,7+normal-1
            ADJ[u]|=1<<v
            ADJ[v]|=1<<u
assert all(a.bit_count()==3 for a in ADJ)
assert sum(a.bit_count() for a in ADJ)==42

# Independent Hamiltonian/LCF model is isomorphic to this incidence model.
# The list maps point/normal vertex indices onto 0..13 of [5,-5]^7.
LCF_ISOMORPHISM=(0,4,6,2,10,12,8,3,1,7,5,9,13,11)
assert sorted(LCF_ISOMORPHISM)==list(range(14))
lcf=[set() for _ in range(14)]
for i in range(14):
    j=(i+1)%14
    lcf[i].add(j)
    lcf[j].add(i)
for i in range(0,14,2):
    j=(i+5)%14
    lcf[i].add(j)
    lcf[j].add(i)
assert all({LCF_ISOMORPHISM[j] for j in range(14) if ADJ[i]>>j&1}==lcf[LCF_ISOMORPHISM[i]] for i in range(14))

def connected(mask):
    if not mask: return False
    visited=mask&-mask
    while True:
        frontier=0
        for v in range(N):
            if visited>>v&1:
                frontier|=ADJ[v]
        nxt=visited|(frontier&mask)
        if nxt==visited: break
        visited=nxt
    return visited==mask

def edges(mask):
    return sum((ADJ[v]&mask).bit_count() for v in range(N) if mask>>v&1)//2

def forest(mask):
    seen=0;comp=0
    for v in range(N):
        b=1<<v
        if mask&b and not seen&b:
            comp+=1
            reach=b
            while True:
                frontier=0
                for u in range(N):
                    if reach>>u&1:frontier|=ADJ[u]
                nxt=reach|(frontier&mask)
                if nxt==reach: break
                reach=nxt
            seen|=reach
    return edges(mask)==mask.bit_count()-comp

def subsets(k):
    for s in combinations(range(N),k):
        yield sum(1<<i for i in s)

plain=[mask for mask in subsets(4) if forest(FULL^mask)]
assert len(plain)==70
assert all(not forest(FULL^mask) for k in range(4) for mask in subsets(k))

opt=[]
for mask in subsets(7):
    if connected(mask) and forest(FULL^mask):opt.append(mask)
assert len(opt)==770
assert all(connected(FULL^mask) and edges(mask)==6 and edges(FULL^mask)==6 for mask in opt)
assert all(not (connected(mask) and forest(FULL^mask)) for k in range(7) for mask in subsets(k))
M=set(opt)
assert all(FULL^m in M for m in M)

# Vertex-to-vertex token jumps, retaining connectedness and acyclicity.
near={}
for s in opt:
    near[s]=set()
    for u in range(N):
        if not(s>>u&1):continue
        for v in range(N):
            if s>>v&1:continue
            t=s^(1<<u)^(1<<v)
            if t in M:near[s].add(t)
assert all(s in near[t] for s,nb in near.items() for t in nb)
count_degrees=Counter(len(near[s]) for s in opt)
assert count_degrees=={16:378,18:56,20:336}
assert sum(map(len,near.values()))//2==6888

# Exact all-pairs distances and comparison with Johnson distance.
distribution=Counter();excess=Counter();ecc=Counter();unreach=0
for s in opt:
    d={s:0};q=deque([s])
    while q:
        a=q.popleft()
        for b in near[a]:
            if b not in d:
                d[b]=d[a]+1;q.append(b)
    assert len(d)==770
    ecc[max(d.values())]+=1
    for t,dist in d.items():
        if s<t:
            distribution[dist]+=1
            excess[dist-(7-(s&t).bit_count())]+=1
assert ecc=={7:770}
assert excess=={0:290605,1:5460}
assert sum(distribution.values())==comb(770,2)

# Independently produce full Fano incidence automorphisms via GL(3,2) and duality.
def transform(v,cols):
    return (cols[0] if v&1 else 0) ^ (cols[1] if v&2 else 0) ^ (cols[2] if v&4 else 0)

perms=[]
for cols in ((x,y,z) for x in range(1,8) for y in range(1,8) for z in range(1,8)):
    images=[transform(v,cols) for v in range(1,8)]
    if len(set(images))<7:continue
    # For a normal, transformed line normal is the unique normal preserving dot products.
    dual=[]
    for normal in range(1,8):
        valid=[w for w in range(1,8) if all(((v&normal).bit_count()%2)==((transform(v,cols)&w).bit_count()%2) for v in range(1,8))]
        assert len(valid)==1
        dual.append(valid[0])
    p=tuple(images[v-1]-1 for v in range(1,8))+tuple(7+dual[v-1]-1 for v in range(1,8))
    assert len(set(p))==14
    perms.append(p)
    # Canonical point-line duality: both end vectors stay identical.
    perms.append(tuple(p[i]+7 if i<7 else p[i]-7 for i in range(14)))
assert len(perms)==336 and len(set(perms))==336
assert all(ADJ[p[i]]==sum(1<<p[j] for j in range(14) if ADJ[i]>>j&1) for p in perms for i in range(14))

def image_mask(mask,p):return sum(1<<p[i] for i in range(N) if mask>>i&1)
unseen=M.copy();orbits=[]
while unseen:
    s=min(unseen)
    orbit={image_mask(s,p) for p in perms}
    assert orbit<=M
    orbits.append((s,orbit))
    unseen-=orbit
assert sorted(len(o) for _,o in orbits)==[42,56,168,168,336]
assert not unseen

print('Fano-incidence verifier: PASS')
print('minimum plain FVS size=4, count=',len(plain))
print('minimum connected FVS size=7, count=',len(opt),'unoriented tree bipartitions=',len(opt)//2)
print('exchange degrees=',sorted(count_degrees.items()))
print('exchange edges=',sum(map(len,near.values()))//2)
print('distance distribution=',sorted(distribution.items()))
print('excess over Johnson lower bound=',sorted(excess.items()))
print('eccentricities=',sorted(ecc.items()))
print('GL3/duality order=',len(perms),'orbits=',sorted(len(o) for _,o in orbits))
print('orbit witnesses=',[(sorted(i for i in range(14) if s>>i&1),len(o)) for s,o in orbits])
