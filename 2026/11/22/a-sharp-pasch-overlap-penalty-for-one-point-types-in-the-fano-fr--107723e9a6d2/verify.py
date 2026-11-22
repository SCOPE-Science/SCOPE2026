#!/usr/bin/env python3
"""Reproducible finite checks for the Fano-free one-point type penalty theorem.
Uses only the Python standard library. No external data or packages.
"""
from itertools import combinations, permutations
from fractions import Fraction
from collections import Counter

# Lines of the unique Fano plane on the seven nonzero vectors of F_2^3.
F0=frozenset(frozenset((a-1,b-1,(a^b)-1))
    for a in range(1,8) for b in range(a+1,8))
assert len(F0)==7
FANO=set()
for perm in permutations(range(7)):
    FANO.add(frozenset(frozenset(perm[i] for i in line) for line in F0))
assert len(FANO)==30

P1=frozenset(map(frozenset,[(0,2,4),(0,3,5),(1,2,5),(1,3,4)]))
P2=frozenset(map(frozenset,[(0,6,8),(0,7,9),(1,6,9),(1,7,8)]))

def is_psts(blocks):
    occurrences=Counter(tuple(sorted(p)) for block in blocks for p in combinations(block,2))
    return max(occurrences.values(),default=0)<=1

def pasches(blocks):
    out={}
    # Four triples, six different points, each in exactly two triples.
    for four in combinations(sorted(blocks, key=lambda s: tuple(sorted(s))),4):
        incidences=Counter(v for e in four for v in e)
        if len(incidences)!=6 or set(incidences.values())!={2}:
            continue
        # Any two of the four triples meet at exactly one point.
        if any(len(e&f)!=1 for e,f in combinations(four,2)):
            continue
        support=frozenset(incidences)
        pairs=frozenset(frozenset({v,w}) for v,w in combinations(support,2)
            if not any({v,w}<=block for block in four))
        assert len(pairs)==3 and len(set().union(*map(set,pairs)))==6
        assert pairs not in out or out[pairs]==frozenset(four)
        out[pairs]=frozenset(four)
    return out

def fano_constraints(n,blocks):
    # Independent direct generation of every Fano copy containing the new point n.
    out=set()
    for six in combinations(range(n),6):
        universe=(*six,n)
        for fano in FANO:
            mapped=frozenset(frozenset(universe[i] for i in e) for e in fano)
            old=frozenset(e for e in mapped if n not in e)
            if old<=blocks:
                link=frozenset(frozenset(e-{n}) for e in mapped if n in e)
                assert len(link)==3
                out.add(link)
    return out

def count_allowed(n,constraints):
    involved=sorted(set().union(*map(set,constraints)),key=lambda x:tuple(sorted(x))) if constraints else []
    total=0
    for binary in range(1<<len(involved)):
        selected={e for j,e in enumerate(involved) if binary>>j&1}
        if not any(C<=selected for C in constraints):
            total+=1
    return total, len(involved)

for name,n,blocks,expected_pasches,expected_fraction in [
    ('one-Pasch',6,P1,1,Fraction(7,8)),
    ('two-Pasch-shared-opposite-pair',10,P1|P2,2,Fraction(25,32)),
    ('two-disjoint-Pasches',12,P1|frozenset(frozenset(v+6 for v in e) for e in P1),2,Fraction(49,64))]:
    assert is_psts(blocks)
    pasch=pasches(blocks)
    direct=fano_constraints(n,blocks)
    assert set(pasch)==direct, (name,pasch,direct)
    assert len(pasch)==expected_pasches
    allowed,k=count_allowed(n,direct)
    ratio=Fraction(allowed,1<<k)
    assert ratio==expected_fraction, (name,ratio,expected_fraction)
    print(f'{name}: n={n}; Pasch={len(pasch)}; link-bits-in-constraints={k}; valid-fraction={ratio}; type-count={ratio*(1<< (n*(n-1)//2))}')

# Distinct Pasch obstructions have at most one common missing pair.
# Exhaustive local exploration based on the canonical six-point Pasch.
from itertools import combinations

def all_pasches(n):
    for six in combinations(range(n),6):
        v=six
        for q in v[1:]:
            a=(v[0],q); remainder=[x for x in v if x not in a]
            for r in remainder[1:]:
                b=(remainder[0],r)
                c=tuple(x for x in remainder if x not in b)
                matching=frozenset(map(frozenset,(a,b,c)))
                for parity in (0,1):
                    trip=frozenset(frozenset((a[i],b[j],c[k]))
                        for i in (0,1) for j in (0,1) for k in (0,1) if (i+j+k)%2==parity)
                    yield matching,trip

for n in range(6,11):
    counts=Counter()
    for matching,other in all_pasches(n):
        if other==P1 or not is_psts(P1|other):continue
        counts[len(matching & next(iter([m for m,t in all_pasches(6) if t==P1])))] += 1
    assert counts[2]==0 and counts[3]==0
    if n<10:assert counts[1]==0
    if n==10:assert counts[1]>0
    print(f'local rigidity through {n} points: compatible constructions by shared opposite pairs = {dict(sorted(counts.items()))}')

# Direct extension test on six old points enumerating all 2^15 link choices.
C=fano_constraints(6,P1)
assert len(C)==1
pairs=list(map(frozenset,combinations(range(6),2)))
valid=sum(not any(F<={pairs[j] for j in range(15) if mask>>j&1} for F in C) for mask in range(1<<15))
assert valid==28672
print(f'exhaustive six-parameter direct link assignments: {valid}/32768 valid')
print('ALL CHECKS PASSED')
