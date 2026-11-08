#!/usr/bin/env python3
"""Exact finite mathematical certificate for four binary-valued observables.

Run with Python 3 and no external dependencies.
"""
from collections import Counter
from itertools import combinations, permutations

N = 4
L = 1 << N
FULL = L-1

def closure_by_difference(team):
    ds = {a ^ b for a,b in combinations(team,2)}
    out=[]
    for x in range(L):
        bad=0
        for d in ds:
            if d & x == 0:
                bad |= d
        out.append(FULL ^ bad)
    return tuple(out)

def closure_by_agreement(team):
    bad=[0] * L
    for a,b in combinations(team,2):
        d=a^b
        agree=FULL^d
        for x in range(L):
            if x & ~agree == 0:
                bad[x] |= d
    return tuple(FULL ^ v for v in bad)

def rename_bits(mask,p):
    return sum((1<<p[i]) for i in range(N) if (mask>>i)&1)

def rename_closure(cl,p):
    out=[0]*L
    for x in range(L):
        out[rename_bits(x,p)]=rename_bits(cl[x],p)
    return tuple(out)

# Translation by an existing row does not alter equality patterns.
# Every nonempty team has an equivalent translate containing row zero.
profiles={}
for subset in range(1 << (L-1)):
    team=(0,) + tuple(i+1 for i in range(L-1) if (subset>>i)&1)
    cl=closure_by_difference(team)
    sz=len(team)
    if cl not in profiles or sz < profiles[cl][0]:
        profiles[cl]=(sz,team)

# Earlier small dimensions; the first superlinear witness-size jump occurs
# at four attributes (maximum 6 instead of n+1).
for k,expected_count,expected_max in ((1,2,2),(2,5,3),(3,19,4)):
    m=1<<k
    small={}
    for mask in range(1,1<<m):
        vals=[v for v in range(m) if (mask>>v)&1]
        d={a^b for a,b in combinations(vals,2)}
        cl=[]
        for x in range(m):
            bad=0
            for z in d:
                if (z&x)==0:
                    bad |= z
            cl.append((m-1)^bad)
        cl=tuple(cl)
        if cl not in small or len(vals)<small[cl]:small[cl]=len(vals)
    assert (len(small),max(small.values()))==(expected_count,expected_max)

assert len(profiles)==221, len(profiles)
assert Counter(sz for sz,team in profiles.values())=={1:1,2:15,3:35,4:67,5:95,6:8}

perms=list(permutations(range(N)))
classes={}
for cl in profiles:
    canonical=min(rename_closure(cl,p) for p in perms)
    classes.setdefault(canonical,[]).append(cl)
assert len(classes)==32
# Fixed-point counts give an additional exact Burnside check:
# conjugacy types identity, swap, double swap, 3-cycle, 4-cycle.
fixed_representatives = {
    (0,1,2,3):221,
    (1,0,2,3):55,
    (1,0,3,2):25,
    (1,2,0,3):14,
    (1,2,3,0):5,
}
for p,expected in fixed_representatives.items():
    assert sum(rename_closure(cl,p)==cl for cl in profiles)==expected
assert (221+6*55+3*25+8*14+6*5)==24*32
assert sum(len(z) for z in classes.values())==221
assert Counter(profiles[k][0] for k in classes)=={1:1,2:4,3:6,4:10,5:9,6:2}
assert Counter(len(z) for k,z in classes.items() if profiles[k][0]==6)=={4:2}

special = [k for k in classes if profiles[k][0]==6]
expected_special = {
    tuple(15 if x==14 else x for x in range(16)),
    tuple(15 if x in (11,13,14) else x for x in range(16))
}
assert set(special) == expected_special
assert closure_by_difference((1,2,4,6,8,10)) == tuple(15 if x==14 else x for x in range(16))
assert closure_by_difference((0,3,5,6,11,12)) == tuple(15 if x in (11,13,14) else x for x in range(16))

# Separate exhaustive computation directly from *all* 65,535 nonempty
# teams. This covers unanchored teams and uses agreement submasks.
seen=set()
for subset in range(1,1<<L):
    team=[i for i in range(L) if (subset>>i)&1]
    seen.add(closure_by_agreement(team))
assert seen==set(profiles)

# For all possible closure systems, enumerate the 2^15 families containing
# the full universe, testing intersection closure (Moore families).
all_closure_systems=0
for f in range(1<<(L-1)):
    closed=(f | (1<<(L-1)))
    members=[x for x in range(L) if (closed>>x)&1]
    if all((closed>>(a&b))&1 for a in members for b in members):
        all_closure_systems+=1
assert all_closure_systems==2480

print('BOOLEAN_FOUR_SUPERVENIENCE_CERTIFICATE_OK',
      'all_nonempty_teams=65535',
      'anchored_teams=32768',
      'realizable_profiles=221',
      'attribute_relabelling_classes=32',
      'arbitrary_closure_systems=2480',
      'worst_case_minimum_worlds=6')
