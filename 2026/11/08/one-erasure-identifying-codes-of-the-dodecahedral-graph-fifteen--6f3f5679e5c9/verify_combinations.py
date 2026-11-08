#!/usr/bin/env python3
"""Independent cardinality-by-cardinality verification of one-erasure identifying codes."""
from itertools import combinations
from collections import Counter
N=20
adj=[set() for _ in range(N)]
for i in range(10):
    for a,b in ((i,(i+1)%10),(i,10+i),(10+i,10+(i+2)%10)):
        adj[a].add(b); adj[b].add(a)
assert all(len(a)==3 for a in adj)
closed=[frozenset({i}|adj[i]) for i in range(N)]
# Under removal of any one selected detector, all vertex signatures must
# stay nonempty and pairwise distinct; exactly the following criteria work.
requirements=closed + [closed[i]^closed[j] for i,j in combinations(range(N),2)]
assert len(requirements)==210
minima=[]
for k in range(10,13):
    found=[]
    for vertices in combinations(range(N),k):
        C=frozenset(vertices)
        if all(len(C & r)>=2 for r in requirements):
            found.append(C)
    if k<12: assert not found
    else: minima=found
assert len(minima)==15
M=sorted(sum(1<<i for i in c) for c in minima)
minima=[frozenset(i for i in range(N) if m & (1<<i)) for m in M]
assert M==[102135,203247,372636,406494,439923,507177,575355,710094,744249,777876,811965,878823,912714,980133,1014354]
counts=Counter(len(a&b) for a,b in combinations(minima,2))
assert counts=={6:60,8:45}, counts
assert all(len(a-b)!=1 for a,b in combinations(minima,2))
# Vertices of the intersection-8 graph indexed by disjoint pairs in K_6.
labels=[(0,1),(2,3),(3,5),(0,4),(2,5),(1,4),(3,4),(1,5),(0,5),(2,4),(1,2),(4,5),(0,2),(0,3),(1,3)]
for i,j in combinations(range(15),2):
    assert (len(minima[i]&minima[j])==8)==(not set(labels[i])&set(labels[j]))
print('lower_bound_for_2_coverage=10; searched_cardinalities=10,11,12')
print('minimum_size=12 optimum_count=15')
print('intersection_spectrum=6:60,8:45; token_jump_graph=15K1')
print('intersection_8_graph=KG(6,2)')
print('independent_combination_certificate=PASS')
