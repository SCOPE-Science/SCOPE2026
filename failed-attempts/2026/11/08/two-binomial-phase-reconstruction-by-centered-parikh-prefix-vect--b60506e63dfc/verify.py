#!/usr/bin/env python3
"""Direct finite verification of cyclic two-binomial phase criterion."""
from itertools import product
from collections import Counter

def deck(w):
    counts=Counter(w)
    pairs=Counter()
    seen=Counter()
    for z in w:
        for x,n in seen.items(): pairs[(x,z)] += n
        seen[z]+=1
    return tuple(sorted(counts.items())),tuple(sorted(pairs.items()))

def key(u,i):
    p=len(u); a=Counter(u);c=Counter(u[:i])
    return tuple(p*c[x]-i*a[x] for x in sorted(a))

cases=0; comparisons=0; collision_cases=0
for q in (2,3,4):
    for p in range(2,9 if q==2 else (8 if q==3 else 7)):
        for u in product(range(q),repeat=p):
            if len(set(u))<2: continue
            keys=[key(u,i) for i in range(p)]
            for m in (1,2,3):
                decks=[deck((u[i:]+u[:i])*m) for i in range(p)]
                for i in range(p):
                    for j in range(i+1,p):
                        comparisons+=1
                        eq=decks[i]==decks[j]
                        assert eq == (keys[i]==keys[j]),(u,p,m,i,j,eq,keys[i],keys[j])
                        if eq: collision_cases+=1
                cases+=1
# Distinct-run all q letters, all powers m. No collisions.
from itertools import permutations
for q in (3,4,5):
    for a in product(range(1,5),repeat=q):
        for ordering in permutations(range(q)) if q<=4 else [tuple(range(q))]:
            u=tuple(x for x,l in zip(ordering,a) for _ in range(l))
            p=len(u)
            keys=[key(u,i) for i in range(p)]
            assert len(set(keys))==p,(ordering,a,keys)
            cases+=1
print('VERIFY_OK',cases,comparisons,collision_cases)
