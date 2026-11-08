#!/usr/bin/env python3
"""Exact independent checks for the line-avoidance complex of PG(2,3).

Python 3 standard library only. Every face, incidence and projective symmetry
is reconstructed from finite-field arithmetic; no stored boundary matrices.
"""
from itertools import product
from collections import Counter, defaultdict
from functools import lru_cache
from heapq import heappop, heappush

Q = 3
N = 13
POINTS = tuple(x for x in product(range(Q), repeat=3)
               if any(x) and next(z for z in x if z) == 1)
assert len(POINTS) == N and len(set(POINTS)) == N
LINES = tuple(sum(1 << j for j, p in enumerate(POINTS)
                  if sum(a*b for a,b in zip(v,p)) % Q == 0) for v in POINTS)
assert len(set(LINES)) == N
assert all(b.bit_count() == 4 for b in LINES)
assert all(sum(bool(b & (1 << i)) for b in LINES) == 4 for i in range(N))
assert all(sum((b >> i & 1) and (b >> j & 1) for b in LINES) == 1
           for i in range(N) for j in range(i+1, N))
assert all((a & b).bit_count() == 1 for i,a in enumerate(LINES)
           for b in LINES[i+1:])

# Independent face enumerators: direct filtering and increasing-index recursion.
FACES = {m for m in range(1 << N) if all((m & line) != line for line in LINES)}
RECURSIVE = set()
def grow(m, nxt):
    RECURSIVE.add(m)
    for j in range(nxt, N):
        w = m | (1 << j)
        if all((w & line) != line for line in LINES):
            grow(w, j + 1)
grow(0, 0)
assert FACES == RECURSIVE
FV = Counter(m.bit_count()-1 for m in FACES)
assert tuple(FV[d] for d in range(-1, 9)) == (1,13,78,286,702,1170,1248,702,117,13)
assert len(FACES) == 4330

# A filtered pivot matching on the augmented face poset.  Including the empty
# simplex is convenient for computing reduced homology; the empty--point
# matched pair is replaced by one ordinary critical vertex in the CW model.
REMAIN = set(FACES)
PAIRS = []
for j in range(N):
    b = 1 << j
    lower = sorted(m for m in REMAIN if not m & b and (m | b) in REMAIN)
    for m in lower:
        assert m in REMAIN and (m | b) in REMAIN
        REMAIN.remove(m)
        REMAIN.remove(m | b)
        PAIRS.append((m, m | b))
assert len(PAIRS) == 2145
assert len(REMAIN) == 40
assert Counter(m.bit_count()-1 for m in REMAIN) == Counter({5:1,6:39})
LOWER_TO_UPPER = dict(PAIRS)
UPPER_TO_LOWER = {b:a for a,b in PAIRS}
assert len(LOWER_TO_UPPER) == len(UPPER_TO_LOWER) == len(PAIRS)
assert {x for a,b in PAIRS for x in (a,b)}.isdisjoint(REMAIN)

# Direct full directed-Hasse cycle verification, independent of the usual
# patchwork proof that a sequence of pivot matchings is acyclic.
INDEG = {m:0 for m in FACES}
ADJ = defaultdict(list)
covers = 0
for upper in FACES:
    for j in range(N):
        if not upper >> j & 1: continue
        lower = upper ^ (1 << j)
        if LOWER_TO_UPPER.get(lower) == upper:
            src,dst = lower,upper
        else:
            src,dst = upper,lower
        ADJ[src].append(dst)
        INDEG[dst] += 1
        covers += 1
q = [m for m in FACES if not INDEG[m]]
import heapq
heapq.heapify(q)
ordered = 0
while q:
    m = heapq.heappop(q)
    ordered += 1
    for w in ADJ[m]:
        INDEG[w] -= 1
        if INDEG[w] == 0: heapq.heappush(q,w)
assert ordered == len(FACES)

# Signed integer Morse boundary; oriented simplices have increasing labels.
def boundary(m):
    return [(m ^ (1<<j), -1 if idx&1 else 1)
            for idx,j in enumerate(i for i in range(N) if m>>i&1)]
CRIT5 = sorted(x for x in REMAIN if x.bit_count() == 6)
CRIT6 = sorted(x for x in REMAIN if x.bit_count() == 7)
assert len(CRIT5)==1 and len(CRIT6)==39
BASIS5 = {x:k for k,x in enumerate(CRIT5)}
@lru_cache(None)
def project5(face):
    if face in BASIS5: return {BASIS5[face]:1}
    if face in UPPER_TO_LOWER: return {}
    assert face in LOWER_TO_UPPER
    upper = LOWER_TO_UPPER[face]
    own = dict(boundary(upper))[face]
    out = defaultdict(int)
    for other,sgn in boundary(upper):
        if other == face: continue
        for i,v in project5(other).items():
            out[i] -= own * sgn * v
    return {i:v for i,v in out.items() if v}
MORSE_COLS = []
for upper in CRIT6:
    out = defaultdict(int)
    for lower,sgn in boundary(upper):
        for i,v in project5(lower).items(): out[i] += sgn*v
    MORSE_COLS.append(tuple(out.get(i,0) for i in range(len(CRIT5))))
assert len(MORSE_COLS)==39 and all(row==(0,) for row in MORSE_COLS)

# Independent mod-two homology by bitset Gaussian elimination, not the matching.
DIMFACES={k:sorted(x for x in FACES if x.bit_count()==k) for k in range(10)}
RANK={0:0}
for k in range(1,10):
    rows = {m:j for j,m in enumerate(DIMFACES[k-1])}
    piv={}
    for m in DIMFACES[k]:
        col=0
        for lower,_ in boundary(m): col ^= 1<<rows[lower]
        while col:
            top=col.bit_length()-1
            if top not in piv:
                piv[top]=col
                break
            col ^=piv[top]
    RANK[k]=len(piv)
RANK[10]=0
MOD2_BETTI={k-1:len(DIMFACES[k])-RANK[k]-RANK[k+1] for k in range(1,10)}
assert MOD2_BETTI=={0:0,1:0,2:0,3:0,4:0,5:1,6:39,7:0,8:0}
assert -sum((-1)**m.bit_count() for m in FACES)==38

# All projective linear transformations, quotienting scalar matrices by
# normalizing the first nonzero entry of a representative matrix to 1.
def normalized(p):
    lead = next(v for v in p if v)
    return tuple((v if lead==1 else 2*v)%3 for v in p)
def det(a):
    x,y,z=a
    return (x[0]*(y[1]*z[2]-y[2]*z[1])-x[1]*(y[0]*z[2]-y[2]*z[0])+x[2]*(y[0]*z[1]-y[1]*z[0]))%3
LOOKUP={p:i for i,p in enumerate(POINTS)}
PROJECTIVE_PERMUTATIONS=set()
L_HIST=Counter()
CYCLE_L_HIST=Counter()
SUM_L=0
for entries in product(range(Q),repeat=9):
    if next((z for z in entries if z),0)!=1:continue
    matrix=(entries[:3],entries[3:6],entries[6:9])
    if det(matrix)==0:continue
    p=tuple(LOOKUP[normalized(tuple(sum(row[j]*v[j] for j in range(3))%3
                                        for row in matrix))] for v in POINTS)
    assert p not in PROJECTIVE_PERMUTATIONS
    PROJECTIVE_PERMUTATIONS.add(p)
    for line in LINES:
        moved=sum(1 << p[i] for i in range(N) if line >> i&1)
        assert moved in LINES
    visited=set(); cycles=[]
    for j in range(N):
        if j in visited:continue
        cyc=[];k=j
        while k not in visited:
            visited.add(k);cyc.append(k);k=p[k]
        cycles.append(cyc)
    cm = [sum(1<<j for j in c) for c in cycles]
    # Signed trace of permutation of oriented faces:
    # contribution of an invariant subset of cycles = (-1)^(#cycles selected-1).
    total = 0
    for mask in range(1<<len(cm)):
        subset=0
        for j,bitmask in enumerate(cm):
            if mask>>j & 1: subset|=bitmask
        if subset in FACES:
            total += (-1 if mask.bit_count()%2==0 else 1)
    L_HIST[total] += 1
    CYCLE_L_HIST[(tuple(sorted(map(len,cycles))),total)] += 1
    SUM_L += total
assert len(PROJECTIVE_PERMUTATIONS)==5616
assert L_HIST==Counter({-1:2352,-2:1755,0:1404,2:104,38:1})
assert SUM_L==-5616
EXPECTED_CYCLES={
    ((1,)*13,38):1,
    ((1,)*5+(2,)*4,-2):117,
    ((1,)*4+(3,)*3,2):104,
    ((1,)*2+(2,3,6),-2):936,
    ((1,)+(2,)*2+(4,)*2,-2):702,
    ((1,)+(3,)*4,-1):624,
    ((1,4,8),0):1404,
    ((13,),-1):1728,
}
assert dict(CYCLE_L_HIST)==EXPECTED_CYCLES
# PGL_3(F3)=SL_3(F3), generated by elementary matrices, each a commutator.
# Thus its integral rank-one H_5 action is trivial. Rational transfer and
# Lefschetz averaging give H_6 invariants dimension (sum L)/|G|+1=0.
assert SUM_L//5616 + 1==0

print('points=13 lines=13 line_size=4')
print('faces_including_empty=4330')
print('fvec_dimensions_0_to_8='+' '.join(str(FV[d]) for d in range(9)))
print('augmented_discrete_morse_pairs=2145')
print('critical_dimensions='+' '.join(f'{d}:{v}' for d,v in sorted(Counter(m.bit_count()-1 for m in REMAIN).items())))
print('hasse_covers='+str(covers)+' acyclic_ordered_faces='+str(ordered))
print('signed_morse_boundary_shape=1x39 all_zero='+str(all(v==(0,) for v in MORSE_COLS)))
print('reduced_mod2_betti='+' '.join(str(MOD2_BETTI[d]) for d in range(9)))
print('pgl_order='+str(len(PROJECTIVE_PERMUTATIONS)))
print('reduced_lefschetz_histogram='+' '.join(f'{i}:{L_HIST[i]}' for i in sorted(L_HIST)))
print('sum_reduced_lefschetz='+str(SUM_L))
for (ct,lf),n in sorted(CYCLE_L_HIST.items()):
    print('cycle_type='+'+'.join(map(str,ct))+' count='+str(n)+' H6_trace='+str(lf+1))
print('quotient_reduced_rational_betti_degree5=1 degree6=0')
print('ALL_CHECKS_PASS')
