#!/usr/bin/env python3
"""Exact finite verification of tetrahedral matching-complex homology characters.
Only Python 3 standard library is required.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations

LABELS = tuple(range(4))
VERTICES = tuple((a,b) for a in LABELS for b in LABELS if a != b)
VID = {v:i for i,v in enumerate(VERTICES)}
EDGE_PAIRS = set()
for a in LABELS:
    neighbors = [VID[a,b] for b in LABELS if b!=a]
    for u,v in combinations(neighbors,2):
        EDGE_PAIRS.add(tuple(sorted((u,v))))
for a,b in combinations(LABELS,2):
    EDGE_PAIRS.add(tuple(sorted((VID[a,b],VID[b,a]))))
EDGES = tuple(sorted(EDGE_PAIRS))
EID = {e:i for i,e in enumerate(EDGES)}
assert len(VERTICES)==12 and len(EDGES)==18

CONFLICT = []
for i,e in enumerate(EDGES):
    CONFLICT.append(sum(1<<j for j,f in enumerate(EDGES)
                        if j!=i and (e[0] in f or e[1] in f)))

FACES=[0]
def enumerate_matchings(candidates, face):
    while candidates:
        bit=candidates&-candidates
        idx=bit.bit_length()-1
        candidates ^=bit
        nxt=face|bit
        FACES.append(nxt)
        enumerate_matchings(candidates & ~CONFLICT[idx], nxt)
enumerate_matchings((1<<len(EDGES))-1,0)
FACES=tuple(sorted(FACES))
assert len(FACES)==1010 and len(FACES)==len(set(FACES))
LAYERS={k:tuple(m for m in FACES if m.bit_count()==k) for k in range(7)}
VECTOR=tuple(len(LAYERS[k]) for k in range(1,7))
assert VECTOR==(18,117,332,390,144,8)
# Independent vertex-deletion matching-polynomial recurrence. For each
# induced graph, either omit its least vertex or match it to one neighbor.
from functools import lru_cache
NBR=[0]*len(VERTICES)
for u,v in EDGES:
    NBR[u]|=1<<v
    NBR[v]|=1<<u
@lru_cache(None)
def matching_polynomial(vmask):
    if not vmask:
        return (1,)
    bit=vmask&-vmask
    v=bit.bit_length()-1
    rest=vmask^bit
    ans=list(matching_polynomial(rest))
    nbrs=rest&NBR[v]
    while nbrs:
        wbit=nbrs&-nbrs
        nbrs^=wbit
        sub=matching_polynomial(rest^wbit)
        for k,coef in enumerate(sub):
            if len(ans)<k+2: ans.extend([0]*(k+2-len(ans)))
            ans[k+1]+=coef
    return tuple(ans)
assert matching_polynomial((1<<len(VERTICES))-1)==(1,)+VECTOR

# Augmented boundary maps C_{k-1}->C_{k-2} including C_{-1}.
def rank_f2(k):
    lower={m:i for i,m in enumerate(LAYERS[k-1])}
    pivots={}
    for mask in LAYERS[k]:
        vector=0
        rem=mask
        while rem:
            bit=rem&-rem
            vector^=1<<lower[mask ^ bit]
            rem^=bit
        while vector:
            leading=vector.bit_length()-1
            if leading not in pivots:
                pivots[leading]=vector
                break
            vector ^=pivots[leading]
    return len(pivots)
RANKS=tuple(rank_f2(k) for k in range(1,7))
assert RANKS==(1,17,100,232,136,8)
BETTI={k-1:len(LAYERS[k])-(RANKS[k-1] if k>=1 else 0)
                   -(RANKS[k] if k<6 else 0) for k in range(7)}
# RANKS[k-1] is boundary out of C_{k-1}, RANKS[k] is boundary into it
assert BETTI=={-1:0,0:0,1:0,2:0,3:22,4:0,5:0}
assert sum((-1)**(k-1)*len(LAYERS[k]) for k in range(7))==-22

# Four local 3-cliques exhaust all triangles, forcing every graph
# automorphism to permute these components and then their reversal edges.
VERTEX_EDGES=set(EDGES)
TRIANGLES=[t for t in combinations(range(12),3)
           if all(tuple(sorted(e)) in VERTEX_EDGES for e in combinations(t,2))]
assert len(TRIANGLES)==4
assert {frozenset(t) for t in TRIANGLES}=={
    frozenset(VID[a,b] for b in LABELS if b!=a) for a in LABELS}

def edge_action(perm):
    vact={VID[a,b]:VID[perm[a],perm[b]] for a,b in VERTICES}
    eact=tuple(EID[tuple(sorted((vact[u],vact[v])))] for u,v in EDGES)
    assert len(set(eact))==len(EDGES)
    return eact

def cycle_type(perm):
    seen=set(); out=[]
    for i in LABELS:
        if i in seen:continue
        j=i;count=0
        while j not in seen:
            seen.add(j);count+=1;j=perm[j]
        out.append(count)
    return tuple(sorted(out,reverse=True))

def lefschetz_character(eact):
    # Reduced alternating trace L=Σ_{nonempty faces} (-1)^{dim} sign
    # plus the degree -1 term (-1)^(-1)=-1. Since H~ only degree 3,
    # the homology trace equals -L.
    trace=0
    for face in FACES:
        n=face.bit_count()
        if not n:
            trace -= 1
            continue
        indices=[j for j in range(len(EDGES)) if face & (1<<j)]
        images=[eact[j] for j in indices]
        new_mask=sum(1<<a for a in images)
        if new_mask!=face:continue
        inversions=sum(images[i]>images[j] for i in range(n) for j in range(i+1,n))
        trace+=(-1)**(n-1+inversions)
    return -trace

def orbit_character(eact):
    # Fixed matchings are unions of cycles on graph edges. A cycle
    # of size s has simplex orientation sign (-1)^(s-1). Together
    # with the alternating face sign its contribution is (-1) per
    # selected orbit, independently of its length. Thus chi=I(-1)
    # of the admissible orbit-conflict graph.
    seen=set(); cycles=[]
    for i in range(len(EDGES)):
        if i in seen:continue
        orb=[];j=i
        while j not in seen:
            seen.add(j);orb.append(j);j=eact[j]
        cycles.append(orb)
    valid=[]
    for orb in cycles:
        union=0;ok=True
        for i in orb:
            if CONFLICT[i]&union:ok=False
            union|=1<<i
        if ok: valid.append(union)
    total=0
    def enumerate_orbits(idx,selected,sign):
        nonlocal total
        if idx==len(valid):
            total+=sign
            return
        enumerate_orbits(idx+1,selected,sign)
        if all(not (CONFLICT[i]&selected) for i in range(len(EDGES)) if valid[idx]&(1<<i)):
            enumerate_orbits(idx+1,selected|valid[idx],-sign)
    enumerate_orbits(0,0,1)
    return total

CHAR={}; CLASSES=defaultdict(list)
for p in permutations(LABELS):
    t=cycle_type(p)
    action=edge_action(p)
    a=lefschetz_character(action)
    b=orbit_character(action)
    assert a==b,(p,a,b)
    CHAR[p]=a
    CLASSES[t].append(a)
TYPES=((1,1,1,1),(2,1,1),(2,2),(3,1),(4,))
assert tuple(len(CLASSES[t]) for t in TYPES)==(1,6,3,8,6)
assert tuple(next(iter(set(CLASSES[t]))) for t in TYPES)==(22,0,2,-2,-2)
assert all(len(set(CLASSES[t]))==1 for t in TYPES)

IRREPS={
 '[4]':(1,1,1,1,1),
 '[1,1,1,1]':(1,-1,1,1,-1),
 '[3,1]':(3,1,-1,0,-1),
 '[2,1,1]':(3,-1,-1,0,1),
 '[2,2]':(2,0,2,-1,0),
}
CLASSESIZE=[len(CLASSES[t]) for t in TYPES]
HCHAR=[CLASSES[t][0] for t in TYPES]
DECOMP={name:sum(n*a*b for n,a,b in zip(CLASSESIZE,HCHAR,irr))//24
        for name,irr in IRREPS.items()}
assert all(sum(n*a*b for n,a,b in zip(CLASSESIZE,HCHAR,irr))%24==0
           for irr in IRREPS.values())
assert DECOMP=={'[4]':0,'[1,1,1,1]':1,'[3,1]':3,'[2,1,1]':2,'[2,2]':3}
assert sum(DECOMP[name]*irr[0] for name,irr in IRREPS.items())==22

# Natural subgroup averages on ordinary topological quotients.
def parity(p):
    return (-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
A4=[p for p in CHAR if parity(p)==1]
V4=[p for p in CHAR if cycle_type(p) in {(1,1,1,1),(2,2)}]
S3=[p for p in CHAR if p[0]==0]
assert len(A4)==12 and len(V4)==4 and len(S3)==6

def inv(group):
    x=sum(CHAR[p] for p in group)
    assert x%len(group)==0
    return x//len(group)
assert (inv(list(CHAR)),inv(A4),inv(V4),inv(S3))==(0,1,7,3)

print('GRAPH_VERTICES',len(VERTICES),'GRAPH_EDGES',len(EDGES))
print('MATCHING_F_VECTOR',*VECTOR)
print('AUGMENTED_F2_BOUNDARY_RANKS',*RANKS)
print('REDUCED_F2_BETTI',BETTI)
print('AUTOMORPHISMS',len(CHAR))
for t in TYPES:
    print('S4_CLASS',','.join(map(str,t)), 'SIZE',len(CLASSES[t]),'TRACE',CLASSES[t][0])
print('IRREDUCIBLE_MULTIPLICITIES',DECOMP)
print('SUBGROUP_FIXED_DIMENSIONS','S4',inv(list(CHAR)),'A4',inv(A4),'V4',inv(V4),'S3',inv(S3))
print('TRUNCATED_TETRAHEDRON_MATCHING_CHARACTER_PASS')
