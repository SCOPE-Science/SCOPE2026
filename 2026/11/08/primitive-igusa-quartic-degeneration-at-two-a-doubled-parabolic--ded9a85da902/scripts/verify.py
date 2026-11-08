#!/usr/bin/env python3
"""Exact finite-field incidence and point counts for a characteristic-two quadric."""
from itertools import combinations
from collections import Counter

def matching(parts):
    if not parts:
        yield ()
        return
    a=parts[0]
    for b in parts[1:]:
        for rest in matching(tuple(x for x in parts[1:] if x!=b)):
            yield ((a,b),)+rest

def e2_binary(mask):
    return (mask.bit_count()*(mask.bit_count()-1)//2)&1

def mod2_points():
    return {a for a in range(1,64) if a.bit_count()%2==0 and e2_binary(a)==0}

def v(pair):
    return 63^sum(1<<i for i in pair)

def all_quadratic_lines():
    Q=mod2_points()
    return {frozenset((a,b,a^b)) for a,b in combinations(sorted(Q),2) if a^b in Q}

P=mod2_points()
assert len(P)==15 and {p.bit_count() for p in P}=={4}
matchings=list(matching(tuple(range(6))))
assert len(matchings)==15 and len({tuple(sorted(m)) for m in matchings})==15
special={frozenset(v(pair) for pair in m) for m in matchings}
assert all(len(L)==3 for L in special)
assert len(special)==15 and special==all_quadratic_lines()
inc=Counter(p for L in special for p in L)
assert set(inc)==P and set(inc.values())=={3}
assert Counter(len(A&B) for A,B in combinations(special,2))=={0:60,1:45}
# finite-field arithmetic GF(4)=F2[u]/(u^2+u+1), where coefficients 0..3 encode (c0,c1)
def mul(a,b):
    x=0
    for i in range(2):
        if (b>>i)&1:x^=a<<i
    if x&8:x^=0b1100
    if x&4:x^=0b111
    return x

def count_Q_F4():
    # Set x5 = x0+...+x4. Each nonzero vector of this 5D space
    # is projectively equivalent to three others.
    zero=0
    for aa in range(4**5):
        coords=[]
        for i in range(5):
            coords.append((aa>>(2*i))&3)
        coords.append(coords[0]^coords[1]^coords[2]^coords[3]^coords[4])
        if all(a==0 for a in coords):continue
        q=0
        for i,j in combinations(range(6),2):q^=mul(coords[i],coords[j])
        if q==0:zero+=1
    assert zero%3==0
    return zero//3

assert count_Q_F4()==85
assert 85-(15*(4+1)-30)==40
# General formulas checked at q=2,4 (not substituted for proof).
for q in (2,4):
    Qnum=(q+1)*(q*q+1)
    Dnum=15*(q+1)-30
    Unum=q**3+q**2-14*q+16
    assert Qnum-Dnum==Unum
    print(f'q={q} | Q={Qnum}, D={Dnum}, U={Unum}')
print('15 rational Q-points, 15 generator lines, 45 meeting pairs; all incidences exactly 3')
print('VERIFY_OK')
