#!/usr/bin/env python3
"""Exact finite Ising ground-state profile on the Robertson (4,5)-cage.

Only Python 3 standard library is used; two independent complete enumerations.
"""
from fractions import Fraction

ADJ = {
    1:(2,3,4,5), 2:(1,8,9,10),3:(1,12,14,16),4:(1,11,18,19),
    5:(1,13,15,17),6:(7,14,17,19),7:(6,15,16,18),8:(2,13,14,18),
    9:(2,11,16,17),10:(2,12,15,19),11:(4,9,14,15),12:(3,10,17,18),
    13:(5,8,16,19),14:(3,6,8,11),15:(5,7,10,11),16:(3,7,9,13),
    17:(5,6,9,12),18:(4,7,8,12),19:(4,6,10,13),
}
N=19
V=list(range(1,N+1))
assert sorted(ADJ)==V
assert all(len(ADJ[u])==4 for u in V)
assert all(u in ADJ[v] for u in V for v in ADJ[u])
EDGES=tuple(sorted((u-1,v-1) for u in V for v in ADJ[u] if u<v))
assert len(EDGES)==38
NEIGH=[]
for u in V:
    NEIGH.append(sum(1<<(v-1) for v in ADJ[u]))

# Structural cross-check against Robertson (1964): girth 5, exactly 54 pentagons.
# Check no triangles and no four-cycles by common neighbors, and count
# pentagons through oriented rooted paths (10 times each cycle).
for u in range(N):
    for v in range(u+1,N):
        common=(NEIGH[u]&NEIGH[v]).bit_count()
        if NEIGH[u]>>v&1:assert common==0
        else:assert common<=1
penta=0
for a in range(N):
    for b in range(N):
        if not NEIGH[a]>>b&1:continue
        for c in range(N):
            if c==a or not NEIGH[b]>>c&1:continue
            for d in range(N):
                if d in (a,b) or not NEIGH[c]>>d&1:continue
                for e in range(N):
                    if e in (a,b,c) or not (NEIGH[d]>>e&1 and NEIGH[e]>>a&1):continue
                    penta+=1
assert penta==54*10, penta

EXPECTED_BEST=(0,4,8,12,16,20,24,28,30,30,30,30,28,24,20,16,12,8,4,0)
EXPECTED_COUNTS=(1,19,133,437,703,516,137,4,2,6,6,2,4,137,516,703,437,133,19,1)

def direct():
    best=[-1]*20; cnt=[0]*20
    for mask in range(1<<N):
        k=mask.bit_count()
        cut=sum(((mask>>u)^(mask>>v))&1 for u,v in EDGES)
        if cut>best[k]:best[k]=cut;cnt[k]=1
        elif cut==best[k]:cnt[k]+=1
    return tuple(best),tuple(cnt)

def gray():
    best=[-1]*20; cnt=[0]*20; cut=0;prev=0
    for idx in range(1<<N):
        mask=idx^(idx>>1)
        if idx:
            change=mask^prev
            i=change.bit_length()-1
            ones=(NEIGH[i]&prev).bit_count()
            cut+=(4-2*ones) if not ((prev>>i)&1) else (2*ones-4)
        k=mask.bit_count()
        if cut>best[k]:best[k]=cut;cnt[k]=1
        elif cut==best[k]:cnt[k]+=1
        prev=mask
    return tuple(best),tuple(cnt)

A=direct();B=gray()
assert A==B==(EXPECTED_BEST,EXPECTED_COUNTS), (A,B)
best,cnt=A
assert all(best[k]==best[N-k] and cnt[k]==cnt[N-k] for k in range(N+1))
assert sum(cnt[k] for k in (8,9,10,11))==16
# Prove the field envelope by comparing *every* sector line on each rational open interval
# and every exact critical field, including all ties.
def winners(x):
    L=[Fraction(38-2*best[k])-x*(2*k-19) for k in range(N+1)]
    v=min(L)
    return tuple(k for k in range(N+1) if L[k]==v),v
for x, wanted in [(Fraction(0),(8,9,10,11)),(Fraction(1),(11,)),
                  (Fraction(2),(11,12)),(Fraction(3),(12,)),
                  (Fraction(4),tuple(range(12,20))), (Fraction(5),(19,)),
                  (Fraction(-1),(8,)),(Fraction(-2),(7,8)),(Fraction(-3),(7,)),
                  (Fraction(-4),tuple(range(8))), (Fraction(-5),(0,))]:
    active,_=winners(x)
    assert active==wanted,(x,active,wanted)
# Exact all-real-parameter lower-envelope proof: on each closed interval, every
# competing affine line is above the stated winner at *both* endpoints.
def energy(k,x):
    return Fraction(38-2*best[k]) - Fraction(x)*(2*k-19)
for lo,hi,champ in [(Fraction(0),Fraction(2),11),
                     (Fraction(2),Fraction(4),12)]:
    assert all(energy(k,lo)>=energy(champ,lo) and
               energy(k,hi)>=energy(champ,hi) for k in range(N+1))
# For x>=4, k=19 has the steepest negative slope; inequalities hold at x=4.
assert all(energy(k,4)>=energy(19,4) for k in range(N+1))
# For x<=0, exchange + and - spins; the zero-field tie is explicit.
# x<0 symmetry: 7 is the flip of k=12, etc.
assert sum(cnt[k] for k in range(12,20))==1950
assert sum(cnt[k] for k in (11,12))==6
assert sum(cnt[k] for k in range(8))==1950
print('VERIFIED: 524288 configurations, two algorithms, 20 sector minima, graph invariants, field crossings.')
print('bestcut',best)
print('minimizer_counts',cnt)
print('h=0 degeneracy',16,'h/J=2 degeneracy',6,'h/J=4 degeneracy',1950)
