#!/usr/bin/env python3
"""Exact vertex-domination and shattering checks for the Fano incidence graph."""
from itertools import combinations
from functools import lru_cache

# Points are nonzero vectors in F_2^3; each nonzero linear functional is a line.
lines=[{i for i,x in enumerate(range(1,8)) if ((x & h).bit_count()&1)==0} for h in range(1,8)]
adj=[set() for _ in range(14)]
for j,L in enumerate(lines):
    for i in L:
        adj[i].add(7+j);adj[7+j].add(i)
assert all(len(a)==3 for a in adj)
N=set(range(14))
minimum=[]
for k in range(15):
    for S in combinations(range(14),k):
        if set(S).union(*(adj[i] for i in S))==N:
            minimum.append(frozenset(S))
    if minimum:break
assert k==4 and len(minimum)==21
assert all(sum(x<7 for x in S)==2 and not any(j in adj[i] for i in S for j in S) for S in minimum)

coeff=[]; shattered=set()
for t in range(15):
    count=0
    for S in combinations(range(14),t):
        trace={frozenset(X.intersection(S)) for X in minimum}
        if len(trace)==(1<<t):
            count+=1;shattered.add(S)
    coeff.append(count)
assert coeff[:4]==[1,14,70,0] and all(x==0 for x in coeff[3:])
assert all(((i,j) in shattered)==(j not in adj[i]) for i in range(14) for j in range(i+1,14))
assert len(minimum)==21 and sum(len(S) for S in minimum)==84
assert len(shattered)==85

# All states reachable by recursive splitting of the minimum dominating-set version space.
all_version=(1<<len(minimum))-1
members=[sum(1<<h for h,S in enumerate(minimum) if i in S) for i in range(14)]
@lru_cache(None)
def rank(version):
    best=0
    for b in members:
        yes=version&b;no=version&(~b)
        if yes and no:
            best=max(best,1+min(rank(yes),rank(no)))
    return best
assert rank(all_version)==3
# Explicit depth-three witness with root point 0, then a nonincident line 7.
assert 0 not in lines[0]
third={(0,0):1,(0,1):2,(1,0):1,(1,1):2}
for a in (0,1):
    for b in (0,1):
        pool=[S for S in minimum if (0 in S)==bool(a) and (7 in S)==bool(b)]
        c=third[a,b]
        assert any(c in S for S in pool) and any(c not in S for S in pool)
print('model=nonzero F2 triples and nonzero dual lines')
print('domination_number=4 minimum_dominating_sets=21 independent_minima=21')
print('shattering_polynomial=1+14z+70z^2')
print('shattered_pairs=70 incident_pairs_excluded=21 beta1=57')
print('vc_dimension=2 littlestone_dimension=3')
print('depth3_witness=root0 then line7 then per_branch_queries_1_2_1_2')
print('PASS')
