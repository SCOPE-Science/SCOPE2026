#!/usr/bin/env python3
"""Finite checks for six-support cycles and label symmetries of Kneser triple complexes."""
from itertools import combinations, permutations, product
from math import comb, factorial
from collections import defaultdict

BASE = tuple(range(6))
TRIPLES = tuple(combinations(BASE, 3))
COMP = lambda x: tuple(i for i in BASE if i not in x)
PAIRS = tuple(sorted(set(tuple(sorted((t, COMP(t)))) for t in TRIPLES)))
assert len(PAIRS) == 10
AXES = {p: i for i, p in enumerate(PAIRS)}

F = ((0,1,2),(0,1,3),(0,2,4),(0,2,5),(0,3,4),(0,3,5),(0,4,5),(1,4,5),(2,3,4),(2,3,5))
assert len(F) == 10 and all(set(a)&set(b) for a,b in combinations(F,2))
assert set().union(*map(set,F)) == set(BASE)
assert not any(all(set(c)&set(t) for t in F) for c in combinations(BASE,2))
assert {frozenset((t, COMP(t))) for t in F} == {frozenset(p) for p in PAIRS}

def parity(seq):
    return -1 if sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))%2 else 1

def axis_det(g):
    axis_perm, flips = [], 1
    for a,b in PAIRS:
        gp=tuple(sorted(g[i] for i in a))
        gb=tuple(sorted(g[i] for i in b))
        p=tuple(sorted((gp, gb)))
        axis_perm.append(AXES[p])
        if gp != p[0]: flips *= -1
    assert sorted(axis_perm) == list(range(10))
    return parity(axis_perm)*flips

for g in permutations(BASE):
    assert axis_det(g) == parity(g)

# The oriented join of ten S^0 factors, with canonical ordered-vertex chains.
def canonical_oriented_face(selection):
    original = tuple(PAIRS[i][bit] for i,bit in enumerate(selection))
    coeff = (-1)**sum(selection) * parity(original)
    return tuple(sorted(original)), coeff

Z={}
for bits in product((0,1),repeat=10):
    face,coef=canonical_oriented_face(bits)
    assert face not in Z
    Z[face]=coef
assert len(Z)==1024
boundary=defaultdict(int)
for face,coef in Z.items():
    for i in range(10): boundary[face[:i]+face[i+1:]] += coef*(-1)**i
assert not any(boundary.values())
for i,j in combinations(BASE,2):
    g=list(BASE); g[i],g[j] = g[j],g[i]
    acted=defaultdict(int)
    for face,coef in Z.items():
        ordered=tuple(tuple(sorted(g[x] for x in v)) for v in face)
        acted[tuple(sorted(ordered))] += coef*parity(ordered)
    assert all(acted[face]==-coef for face,coef in Z.items())

# Each six-set has a globally maximal nine-face with a unique six-element support.
facets=0
for m in range(6,11):
    for S in combinations(range(m),6):
        lab={i:S[i] for i in BASE}
        fs=tuple(frozenset(lab[i] for i in t) for t in F)
        assert len(fs)==10 and len(set().union(*fs))==6
        assert all(a&b for a,b in combinations(fs,2))
        all_v=(frozenset(u) for u in combinations(range(m),3))
        assert not any(u not in fs and all(u&v for v in fs) for u in all_v)
        facets+=1

# Rank and character of the sixth exterior power of the permutation module.
char_cases=0
for m in range(6,11):
    for g in [tuple(range(m)), (1,0)+tuple(range(2,m)),
              (1,0,3,2)+tuple(range(4,m))]:
        c=0
        for S in combinations(range(m),6):
            if tuple(sorted(g[i] for i in S))==S:
                c+=parity(tuple(S.index(g[i]) for i in S))
        # Determinant generating function: one factor per cycle.
        visited=set(); poly=[1]
        for x in range(m):
            if x in visited: continue
            y=x; length=0
            while y not in visited:
                visited.add(y); length+=1; y=g[y]
            nxt=poly+[0]*length
            for k,a in enumerate(poly): nxt[k+length]+=a*((-1)**(length-1))
            poly=nxt
        assert c == (poly[6] if len(poly)>6 else 0)
        char_cases+=1
    assert comb(m,6) == comb(m-1,5)+(comb(m-1,6) if m>=7 else 0)
print(f'ALL_VERIFY_OK S6_determinants={factorial(6)} direct_chain_facets={len(Z)} boundary_terms={len(boundary)} transposition_chain_checks={comb(6,2)} maximal_faces={facets} character_checks={char_cases}')
