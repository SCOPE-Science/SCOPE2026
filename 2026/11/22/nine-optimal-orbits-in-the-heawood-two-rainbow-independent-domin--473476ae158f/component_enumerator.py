#!/usr/bin/env python3
"""Exact Fano-incidence two-rainbow independent domination census.

All loops are exhaustive finite combinatorics. Standard-library only.
"""
from itertools import permutations, product
from collections import Counter

N=14
LINES=[frozenset((i,(i+1)%7,(i+3)%7)) for i in range(7)]
assert len(set(LINES))==7
assert all(len(a&b)==1 for i,a in enumerate(LINES) for b in LINES[i+1:])
ADJ=[set() for _ in range(14)]
for j,L in enumerate(LINES):
    for i in L: ADJ[i].add(j+7); ADJ[j+7].add(i)
assert all(len(x)==3 for x in ADJ)

# Per zero-set, every component of the positive induced graph has exactly
# two alternating colorings. The zero vertices must see both colors.
polynomial=Counter()
all_valid={}
zero_shape=Counter()
component_shape=Counter()
for zeros in range(1<<N):
    pos={v for v in range(N) if not (zeros>>v&1)}
    components=[]
    unseen=set(pos)
    while unseen:
        start=min(unseen); unseen.remove(start)
        side={start:0}; stack=[start]; comp=[start]
        while stack:
            v=stack.pop()
            for w in ADJ[v]&pos:
                if w not in side:
                    side[w]=1-side[v]; unseen.remove(w)
                    stack.append(w); comp.append(w)
                else: assert side[w]!=side[v]
        components.append(side)
    for flips in product((0,1),repeat=len(components)):
        label=[0]*N
        for flip,comp in zip(flips,components):
            for v,side in comp.items(): label[v]=1+(side^flip)
        if all({label[w] for w in ADJ[v] if label[w]}=={1,2}
               for v in range(N) if zeros>>v&1):
            s=tuple(label)
            weight=len(pos)
            polynomial[weight]+=1
            all_valid[s]=weight
            if weight==8:
                zero_shape[(sum(zeros>>i&1 for i in range(7)),len(components))]+=1
                component_shape[tuple(sorted(map(len,components),reverse=True))]+=1

expected={8:868,9:168,10:42,11:28,14:2}
assert dict(polynomial)==expected, dict(polynomial)
print('COEFFICIENTS',sorted(polynomial.items()))
print('OPTIMUM_ZERO_SIDE_COMPONENT_COUNTS',sorted(zero_shape.items()))
print('OPTIMUM_COMPONENT_LENGTHS',sorted(component_shape.items()))

# All incidence-preserving automorphisms: the 168 permutations of points
# preserving the seven Fano lines. A point-line duality doubles to 336.
line_to_idx={L:i for i,L in enumerate(LINES)}
group=[]
for p in permutations(range(7)):
    image=[frozenset(p[x] for x in L) for L in LINES]
    if not all(S in line_to_idx for S in image): continue
    q=[line_to_idx[S] for S in image]
    g=tuple(list(p)+[7+q[i] for i in range(7)])
    group.append(g)
assert len(group)==168
# D: point i -> line (-i); line j -> point (-j)
dual=tuple([7+(-i)%7 for i in range(7)]+[(-i)%7 for i in range(7)])
assert all((dual[v] in ADJ[dual[u]]) == (v in ADJ[u]) for u in range(N) for v in range(N))
group += [tuple(dual[g[v]] for v in range(N)) for g in group]
assert len(group)==336 and len(set(group))==336
assert all(all((g[v] in ADJ[g[u]]) == (v in ADJ[u]) for u in range(N) for v in range(N)) for g in group)

optima={s for s,k in all_valid.items() if k==8}
orbits=[]
while optima:
    representative=min(optima)
    # new label at g(v) is old label at v
    orbit=set()
    for g in group:
        transformed=[0]*14
        for v in range(14):transformed[g[v]]=representative[v]
        orbit.add(tuple(transformed))
    assert orbit<=optima
    optima-=orbit
    orbits.append((len(orbit),''.join(map(str,representative))))
assert sorted(size for size,_ in orbits)==[14,14,56,56,56,168,168,168,168]
print('OPTIMUM_ORBITS',sorted(orbits))
print('CERTIFICATE_OK')
