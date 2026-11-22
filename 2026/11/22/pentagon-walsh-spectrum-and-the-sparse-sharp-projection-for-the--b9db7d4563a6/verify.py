"""Exact standalone checks for Boolean convolution by Petersen pentagons.

Run: python3 verify.py. Python standard library only.
"""
from collections import Counter
from itertools import permutations

N = 5
# Outer rim, spoke and inner-star edge families, in this exact order.
def ordered(a,b):
    return (a,b) if a < b else (b,a)
E = [ordered(i,(i+1)%N) for i in range(N)]
E += [ordered(i,i+N) for i in range(N)]
E += [ordered(i+N,((i+2)%N)+N) for i in range(N)]
assert len(E)==15 and len(set(E))==15
EDGE = {e:i for i,e in enumerate(E)}
ADJ = {v:set() for v in range(10)}
for a,b in E:
    ADJ[a].add(b); ADJ[b].add(a)
assert all(len(ADJ[v])==3 for v in ADJ)

def canonical_cycles(length):
    out=set()
    for path in permutations(range(10),length):
        if path[0]!=min(path) or path[1]>path[-1]:continue
        if all(path[(j+1)%length] in ADJ[path[j]] for j in range(length)):
            m=0
            for j in range(length):
                m ^= 1<<EDGE[ordered(path[j],path[(j+1)%length])]
            assert m.bit_count()==length
            out.add(m)
    return sorted(out)

PENT = canonical_cycles(5)
HEX = canonical_cycles(6)
assert len(PENT)==12 and len(HEX)==10
assert PENT==[31,1187,2374,4748,5680,8504,9604,10337,16977,19208,20674,31744]

# Second cycle enumeration via complements of perfect matchings.
def matchings(remaining):
    if not remaining:
        yield 0
        return
    u=min(remaining)
    for v in sorted(ADJ[u]&remaining):
        edge_bit=1<<EDGE[ordered(u,v)]
        for rest in matchings(remaining-{u,v}):
            yield edge_bit|rest

PM=sorted(matchings(set(range(10))))
assert len(PM)==6
pent_from_matchings=set()
for m in PM:
    remaining_edges=[e for i,e in enumerate(E) if not (m>>i&1)]
    unseen=set(range(10))
    comps=[]
    while unseen:
        stack=[unseen.pop()]
        comp=set(stack)
        while stack:
            u=stack.pop()
            for a,b in remaining_edges:
                v=b if a==u else a if b==u else None
                if v is not None and v in unseen:
                    unseen.remove(v); comp.add(v);stack.append(v)
        comps.append(comp)
    assert sorted(len(c) for c in comps)==[5,5]
    for comp in comps:
        pent_from_matchings.add(sum(1<<EDGE[e] for e in remaining_edges if e[0] in comp))
assert pent_from_matchings==set(PENT)

# The fundamental cycle code. A connected 10-vertex graph with 15 edges
# has dimension 15-10+1=6; closure of the pentagons attains that bound.
def span_words(vecs):
    basis=[]
    for v0 in vecs:
        v=v0
        for b in basis:
            v=min(v,v^b)
        if v:
            basis.append(v)
            basis.sort(reverse=True)
    words={0}
    for b in basis:
        words|={x^b for x in list(words)}
    return basis, words
BASIS,CODE=span_words(PENT)
assert len(BASIS)==6 and len(CODE)==64
assert Counter(v.bit_count() for v in CODE)=={0:1,5:12,6:10,8:15,9:20,10:6}
assert set(PENT)=={c for c in CODE if c.bit_count()==5}
assert set(HEX)=={c for c in CODE if c.bit_count()==6}
FACTORS={c for c in CODE if c.bit_count()==10}
assert len(FACTORS)==6

# Independently determine the six pentagon-pair 2-factors.
FACTORS2={x^y for i,x in enumerate(PENT) for y in PENT[i+1:]
          if (x&y)==0}
assert FACTORS2==FACTORS

# Character sum on the six-dimensional code: every dual assignment
# has exactly 2^9 lifts to the original 15-edge Boolean group.
SIX=[0]*64
for t in range(64):
    # Instead calculate the exact 64×64 Walsh matrix on the basis coordinates.
    for wbits in range(64):
        word=0
        for j,b in enumerate(BASIS):
            if wbits>>j&1:word^=b
        if word in PENT:
            SIX[t]+=1 if (t&wbits).bit_count()%2==0 else -1
EXPECTED64=[
12,4,4,0,4,4,0,-4,
4,4,4,0,0,0,-4,0,
4,0,4,-4,4,0,0,0,
0,-4,0,0,-4,0,0,0,
4,0,0,0,0,4,0,0,
-4,0,0,0,-4,0,-4,4,
0,0,4,0,-4,-4,-4,0,
-4,-4,0,4,-12,-4,-4,0]
assert SIX==EXPECTED64
assert Counter(SIX)=={-12:1,-4:15,0:32,4:15,12:1},Counter(SIX)
assert sum(x*x for x in SIX)==64*12

# The frequency support has inverse Walsh transform equal to
# 1/2 at the identity, +1/8 on all ten six-cycles and -1/8 on
# all six disjoint-pentagon 2-factors, with no other support.
F = [int(x!=0) for x in SIX]
for j in range(6):
    s=1<<j
    for k in range(0,64,2*s):
        for a in range(s):
            u,v=F[k+a],F[k+a+s]
            F[k+a],F[k+a+s]=u+v,u-v
emb=[]
for z in range(64):
    word=0
    for j,b in enumerate(BASIS):
        if z>>j&1:word^=b
    emb.append(word)
for z,v in enumerate(F):
    w=emb[z]
    expected=(32 if w==0 else 8 if w in HEX else -8 if w in FACTORS else 0)
    assert v==expected,(z,w,v,expected)
assert sum(abs(v) for v in F)==160 # norm = 160/64 = 5/2

# Independent full 2^15 Walsh transform of all pentagon indicators:
FULL=[0]*(1<<15)
for word in PENT:FULL[word]=1
for j in range(15):
    s=1<<j
    for k in range(0,1<<15,2*s):
        for a in range(s):
            u,v=FULL[k+a],FULL[k+a+s]
            FULL[k+a],FULL[k+a+s]=u+v,u-v
assert Counter(FULL)=={-12:512,-4:7680,0:16384,4:7680,12:512}
assert min(abs(x) for x in FULL if x)==4
assert sum(x*x for x in FULL)==(1<<15)*12
# Also check frequency zero masks of weight one and two.
assert sum(FULL[1<<i]==0 for i in range(15))==0
assert sum(FULL[(1<<i)|(1<<j)]==0 for i in range(15) for j in range(i+1,15))==60

# Difference-multiplicity check: first principles, independent of transform.
CORR=Counter(a^b for a in PENT for b in PENT)
for w in CODE:
    expect={0:12,6:6,8:4,10:2}.get(w.bit_count(),0)
    assert CORR[w]==expect,(w,CORR[w],expect)
assert set(CORR)<=CODE
print('PASS: 12 pentagons, 10 hexagons, 6 paired-pentagon 2-factors')
print('PASS: 64-element [15,6,5] cycle code; full 32768-character spectrum')
print('PASS: signed spectrum -12:512,-4:7680,0:16384,4:7680,12:512')
print('PASS: sharp projection kernel 1/2 delta_0 + 1/8 hex - 1/8 two-factor')
print('PASS: projection norm 5/2, rank 16384, smallest nonzero magnitude 4')
print('EDGE_ORDER',E)
print('PENTAGON_MASKS',PENT)
print('SIX_BIT_BASIS',BASIS)
