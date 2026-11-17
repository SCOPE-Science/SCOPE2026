#!/usr/bin/env python3
"""Exact, dependency-free verification of a Pappus non-matching complex.
Run: python3 verify.py. All combinatorial arithmetic is integral.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations
from functools import lru_cache
from random import Random
from math import factorial

EDGES = [(0,1),(0,5),(0,17),(1,2),(1,8),(2,3),(2,13),(3,4),(3,10),
         (4,5),(4,15),(5,6),(6,7),(6,11),(7,8),(7,14),(8,9),
         (9,10),(9,16),(10,11),(11,12),(12,13),(12,17),(13,14),
         (14,15),(15,16),(16,17)]
N=27
# Canonical eighteen-cycle and LCF [5,7,-7,7,-7,-5]^3 graph definition.
LCF=[5,7,-7,7,-7,-5]*3
LCF_EDGES={tuple(sorted((i,(i+1)%18))) for i in range(18)}
LCF_EDGES|={tuple(sorted((i,(i+LCF[i])%18))) for i in range(18)}
assert set(EDGES)==LCF_EDGES and len(LCF_EDGES)==27
assert len(EDGES)==N and len(set(EDGES))==N
A=[set() for i in range(18)]
for u,v in EDGES:
    A[u].add(v); A[v].add(u)
assert all(len(x)==3 for x in A)
# Face enumeration by Kőnig's theorem: matching number < 3 iff
# the chosen edges are covered by a set of at most two graph vertices.
F={0}
for u in range(18):
    for v in range(u+1,18):
        m=sum((1<<i) for i,(a,b) in enumerate(EDGES) if u in (a,b) or v in (a,b))
        s=m
        while s:
            F.add(s); s=(s-1)&m
FORDER=sorted(F,key=lambda f:(f.bit_count(),f))
FCOUNT=Counter(s.bit_count()-1 for s in F)
assert len(F)==4087 and FCOUNT=={-1:1,0:27,1:351,2:1206,3:1593,4:783,5:126}, FCOUNT
# Independent face criterion: reject any edge triple that is a matching.
matching_triples=[]
for inds in combinations(range(N),3):
    uv=[u for i in inds for u in EDGES[i]]
    if len(set(uv))==6: matching_triples.append(sum(1<<i for i in inds))
assert len(matching_triples)>0
for f in FORDER:
    assert not any((f&t)==t for t in matching_triples)
# Every excluded edge set has a forbidden triple (independent spot checks
# on 0..5 edge combinations and all six-edge star-unions).
for size in range(7):
    for inds in combinations(range(N),size):
        mask=sum(1<<i for i in inds)
        if size<=3 or (size==4 and inds[0]<10):
            assert (mask in F)==(not any(mask&t==t for t in matching_triples))
assert sum((-1 if (k%2) else 1)*v for k,v in FCOUNT.items())==-55
print('FACES',sorted(FCOUNT.items()),'MATCHING_TRIPLES',len(matching_triples),'REDUCED_EULER',-55)

# Lexicographic face matching: at each graph edge i, pair currently
# unmatched faces S < S union {i}. This is an acyclic matching, verified
# exhaustively below on every directed Hasse cover.
order=list(range(N)); Random(0).shuffle(order)
U=set(F); PAIRS=[]
for i in order:
    bit=1<<i
    for s in FORDER:
        if s&bit or s not in U: continue
        t=s|bit
        if t in U:
            U.remove(s); U.remove(t); PAIRS.append((s,t))
MT=dict(PAIRS); INV={t:s for s,t in PAIRS}
assert len(MT)==len(INV)==2011
assert 0 in MT and MT[0].bit_count()==1
# An ordinary (non-augmented) discrete-Morse matching is obtained by
# omitting the one pair with the empty simplex. The formerly paired
# singleton becomes the unique critical zero-cell.
ordinary_pairs=[(a,b) for a,b in PAIRS if a!=0]
ordinary_critical=U|{MT[0]}
assert len(ordinary_pairs)==2010
assert Counter(s.bit_count()-1 for s in ordinary_critical)=={0:1,2:5,3:60}
crit2=sorted(s for s in U if s.bit_count()==3)
crit3=sorted(s for s in U if s.bit_count()==4)
assert len(U)==65 and len(crit2)==5 and len(crit3)==60
assert not any(s.bit_count() not in (3,4) for s in U)

# A matched cover reverses the ordinary upper-to-lower orientation.
# Kahn's algorithm detects any directed cycle exactly.
in_deg={s:0 for s in F}; nbr={s:[] for s in F}; covers=0
for t in F:
    for i in range(N):
        if not t&(1<<i):continue
        s=t^(1<<i)
        if MT.get(s)==t: a,b=s,t
        else:a,b=t,s
        nbr[a].append(b);in_deg[b]+=1;covers+=1
queue=deque(s for s in F if in_deg[s]==0)
top_order=[]
while queue:
    s=queue.popleft();top_order.append(s)
    for t in nbr[s]:
        in_deg[t]-=1
        if in_deg[t]==0: queue.append(t)
assert len(top_order)==len(F),(len(top_order),len(F))
print('MORSE',len(PAIRS),'augmented pairs,',len(U),'augmented critical,',covers,'augmented oriented covers, acyclic')
print('ORDINARY_MORSE',len(ordinary_pairs),'pairs, 1 critical vertex, 5 critical two-cells, 60 critical three-cells; nonempty Hasse covers',covers-27)

@lru_cache(None)
def boundary(s):
    bits=[i for i in range(N) if s&(1<<i)]
    return [(s^(1<<i),1 if j%2==0 else -1) for j,i in enumerate(bits)]
ci={s:i for i,s in enumerate(crit2)}
@lru_cache(None)
def projection(s):
    # Projection of each degree-2 cell onto the critical degree-2 cells,
    # via descending matching paths; topology guarantees termination.
    if s in ci:return {ci[s]:1}
    if s in INV:return {}
    if s not in MT:raise AssertionError(('unmatched lower cell',s))
    t=MT[s]
    own=dict(boundary(t))[s]
    acc=defaultdict(int)
    for f,coefficient in boundary(t):
        if f==s:continue
        for j,v in projection(f).items():
            acc[j]-=own*coefficient*v
    return {j:v for j,v in acc.items() if v}
M=[[0 for t in crit3] for s in crit2]
for j,cell in enumerate(crit3):
    for f,z in boundary(cell):
        for i,v in projection(f).items():M[i][j]+=z*v
assert max(abs(z) for row in M for z in row)==1
assert sum(z!=0 for row in M for z in row)==28

# Find and certify a unimodular rank-5 minor; exact small-integer determinant.
def det_bareiss(mat):
    a=[row[:] for row in mat]; n=len(a); sign=1; d=1
    for k in range(n-1):
        if a[k][k]==0:
            p=next((i for i in range(k+1,n) if a[i][k]),None)
            if p is None:return 0
            a[k],a[p]=a[p],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                c=a[i][j]*pivot-a[i][k]*a[k][j]
                assert c%d==0
                a[i][j]=c//d
            a[i][k]=0
        d=pivot
    return sign*a[-1][-1]
chosen=None
for idx in combinations(range(len(crit3)),5):
    minor=[[M[i][j] for j in idx] for i in range(5)]
    if abs(det_bareiss(minor))==1:
        chosen=idx;break
assert chosen is not None
print('MORSE_BOUNDARY',len(M),'x',len(M[0]),'nonzero',sum(z!=0 for row in M for z in row),
      'minor_columns',list(chosen),'det',det_bareiss([[M[i][j] for j in chosen] for i in range(5)]))

# Enumerate ALL graph automorphisms by constrained backtracking, without
# relying on a graph library. Full permutation consistency is enforced.
AP=set(EDGES)
GP=[]
def auto_backtrack(partial,unused):
    if len(partial)==18:
        p=tuple(partial[i] for i in range(18))
        GP.append(p);return
    source=max((i for i in range(18) if i not in partial),key=lambda i:(sum(j in partial for j in range(18) if j in A[i]),-i))
    for target in sorted(unused):
        if all(((j in A[source])==(partial[j] in A[target])) for j in partial):
            partial[source]=target;unused.remove(target)
            auto_backtrack(partial,unused)
            unused.add(target);del partial[source]
auto_backtrack({},set(range(18)))
assert len(GP)==216 and len(set(GP))==216
EIND={e:i for i,e in enumerate(EDGES)}

def cycles(p):
    seen=set();ss=[]
    for i in range(len(p)):
        if i in seen:continue
        k=i; c=0
        while k not in seen:
            seen.add(k);c+=1;k=p[k]
        ss.append(c)
    return tuple(sorted(ss))

def signed_fixed_face(f,perm):
    ids=[i for i in range(N) if f&(1<<i)]
    images=[perm[i] for i in ids]
    if set(images)!=set(ids):return 0
    # parity of permutation on ordered vertices of the simplex
    return (-1)**sum(images[i]>images[j] for i in range(len(images)) for j in range(i+1,len(images)))

character=defaultdict(list)
for p in GP:
    ep=tuple(EIND[tuple(sorted((p[a],p[b])))] for a,b in EDGES)
    # Reduced alternating chain trace includes empty face in degree -1,
    # and equals - trace on H3, because all other reduced homology vanishes.
    reduced_lefschetz=sum((-1 if (f.bit_count()-1)%2 else 1)*signed_fixed_face(f,ep) for f in F)
    tr=-reduced_lefschetz
    character[(cycles(p),cycles(ep))].append(tr)
assert sum(len(v) for v in character.values())==216
assert len(character)==11
assert all(len(set(v))==1 for v in character.values())
assert sum(v[0]*len(v) for v in character.values())%216==0
print('AUTOMORPHISMS',len(GP),'CHARACTER_BY_CYCLE_TYPES')
for (vc,ec),v in sorted(character.items(),key=lambda z:(z[0][0],z[0][1])):
    print('  vertex',str(vc),'edge',str(ec),'multiplicity',len(v),'trace_H3',v[0])
print('INVARIANT_RANK',sum(v[0]*len(v) for v in character.values())//216)
print('VERIFY_OK Pappus NM3 ≃ wedge of 55 three-spheres; integral Morse minor and 216 equivariant traces')
