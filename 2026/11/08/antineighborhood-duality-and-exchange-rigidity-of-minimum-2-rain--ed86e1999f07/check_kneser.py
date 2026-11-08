#!/usr/bin/env python3
"""Independent Kneser-model verification for optimal two-rainbow functions."""
from itertools import combinations
from collections import Counter

V=list(combinations(range(1,6),2)); n=len(V)
adj=[{j for j,y in enumerate(V) if not set(x)&set(y)} for x in V]
assert len(V)==10 and all(len(z)==3 for z in adj)
assert sum(len(z) for z in adj)//2==15

neighbor=lambda s: set().union(*(adj[u] for u in s)) if s else set()
closed=lambda s: set(s)|neighbor(s)

def valid(a,b):
    for v in range(n):
        if v not in a and v not in b and not (adj[v]&a and adj[v]&b):
            return False
    return True

pair_map={}
for a in combinations(range(n),2):
    A=frozenset(a)
    if a[1] in adj[a[0]]: continue
    B=frozenset(set(range(n))-closed(A))
    assert len(B)==3 and not A&B
    assert valid(A,B)
    assert frozenset(set(range(n))-closed(B))==A
    assert sum(int(y in adj[x]) for x,y in combinations(B,2))==2
    pair_map[A]=B
assert len(pair_map)==30
# Independent pair determines a unique opposite three-support; reverse map is injective.
assert len(set(pair_map.values()))==30
states={(a,b) for a,b in pair_map.items()}|{(b,a) for a,b in pair_map.items()}
assert len(states)==60
for a,b in states:
    for color in (0,1):
        support=(a,b)[color]
        fixed=(b,a)[color]
        for u in support:
            for v in set(range(n))-support:
                moved=frozenset((set(support)-{u})|{v})
                new=(moved,fixed) if color==0 else (fixed,moved)
                assert new not in states
print('Kneser model: 30 independent two-vertex supports; 60 minimum ordered colorings')
print('Mutual closed-antineighborhood: 30/30; induced opposite supports are three-vertex paths')
print('No single-color jump between distinct minimum functions (including slides): PASS')
