"""Independent maximal-clique search and cubical-isometry orbit certificate.
No external dependencies. Run: python3 verify_orbits.py
"""
from collections import Counter
from itertools import permutations

N=16
MASK=(1<<N)-1
# Maximal independent sets of Q4 are maximal cliques of its complement.
adj=[]
for v in range(N):
    forbidden=(1<<v)
    for j in range(4): forbidden |= 1<<(v^(1<<j))
    adj.append(MASK & ~forbidden)

hypotheses=[]
def bron_kerbosch(R,P,X):
    if not (P|X):
        hypotheses.append(R)
        return
    px=P|X
    pivot=max((i for i in range(N) if px>>i&1),key=lambda u:(P&adj[u]).bit_count())
    options=P&~adj[pivot]
    while options:
        b=options&-options
        u=b.bit_length()-1
        bron_kerbosch(R|b,P&adj[u],X&adj[u])
        P &= ~b
        X |= b
        options &= ~b
bron_kerbosch(0,MASK,0)
assert len(hypotheses)==42 and len(set(hypotheses))==42
assert Counter(h.bit_count() for h in hypotheses)=={4:24,5:16,8:2}

# Cube automorphism group = all coordinate permutations and translations.
autos=[]
for p in permutations(range(4)):
    for t in range(16):
        autos.append(tuple(t ^ sum(((i>>j)&1)<<p[j] for j in range(4)) for i in range(16)))
assert len(set(autos))==384

def image(S,auto):
    return sum(1<<auto[i] for i in range(N) if S>>i&1)

def orbit(S):
    return {image(S,a) for a in autos}

def bits(vertices):
    return sum(1<<v for v in vertices)

reps2=[(0,15)]
reps4=[(0,3,5,6),(4,7,9,10),(3,5,6,8)]
expected_sizes=[8,16,24,64]
facet_orbits=[orbit(bits(v)) for v in reps2+reps4]
assert [len(o) for o in facet_orbits]==expected_sizes
assert len(set.union(*facet_orbits))==112
facets=set.union(*facet_orbits)
predicted={0}
for F in facets:
    S=F
    while True:
        predicted.add(S)
        if not S:break
        S=(S-1)&F
# The loop above enumerates all submasks of each facet, including 0.
assert Counter(s.bit_count() for s in predicted)=={0:1,1:16,2:88,3:160,4:104}

# Independently compute every Boolean trace, directly from the Bron-Kerbosch set.
actually=set()
for s in range(1<<N):
    seen={tuple(int(bool((m>>v)&1)) for v in range(N) if (s>>v)&1) for m in hypotheses}
    if len(seen)==1<<s.bit_count():
        actually.add(s)
assert actually == predicted
# All 8 maximal pairs are antipodal; distinct 4-facet orbits have sizes 16,24,64.
assert {s for s in facets if s.bit_count()==2}=={bits((i,i^15)) for i in range(16)}
assert all(s.bit_count() in (2,4) for s in facets)
# Three-point shattering iff support independent and has no antipodal pair.
for s in range(1<<N):
    if s.bit_count()!=3:continue
    v=[i for i in range(N) if s>>i&1]
    criterion=all((a^b).bit_count() in (2,3) for a in v for b in v if a<b)
    assert (s in predicted)==criterion
print('Q4_MIS_SHATTER_ORBITS_PASS', 'MIS',len(hypotheses), 'facet_orbits',expected_sizes, 'shattered',len(predicted))
