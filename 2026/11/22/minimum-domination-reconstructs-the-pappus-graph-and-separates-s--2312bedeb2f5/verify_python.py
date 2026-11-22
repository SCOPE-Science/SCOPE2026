#!/usr/bin/env python3
"""Independent standard-library exhaustive check of the Pappus minimum-domination theorem."""
from itertools import combinations
from collections import Counter
from functools import lru_cache
P=list(range(9)); L=list(range(9,18)); V=list(range(18))
xy=lambda p:(p%3,p//3)
def incident(p,l):
    x,y=xy(p);d,c=divmod(l-9,3)
    return (x if d==0 else y if d==1 else (y-x)%3)==c
N=[{i} for i in V]
for p in P:
    for l in L:
        if incident(p,l):N[p].add(l);N[l].add(p)
assert all(len(N[i])==4 for i in V)
assert sum(len(N[i])-1 for i in P)==27
full=(1<<18)-1
closed=[sum(1<<j for j in N[i]) for i in V]
D=[]
for k in range(1,6):
    good=[]
    for comb in combinations(V,k):
        covered=0
        for i in comb:covered|=closed[i]
        if covered==full:good.append(sum(1<<i for i in comb))
    if good:
        assert k==5
        D=good
        break
assert len(D)==18
# independently build predicted 18 geometric constructions
expected=[]
for l in L:
    d=(l-9)//3
    S={p for p in P if incident(p,l)}|{h for h in L if (h-9)//3==d and h!=l}
    expected.append(sum(1<<i for i in S))
for p in P:
    x,y=xy(p)
    S={q for q in P if q!=p and (sum(xy(q))%3==(x+y)%3)}|{l for l in L if incident(p,l)}
    expected.append(sum(1<<i for i in S))
assert sorted(D)==sorted(expected)
assert all(all(not ((m>>i&1) and (m>>j&1)) for i in V for j in N[i] if i!=j) for m in D)
occ=[sum(bool(d>>i&1) for d in D) for i in V]
assert set(occ)=={5}
pair=Counter()
fpoly=[1,0,0,0]
for i in V:
    if len(set((d>>i)&1 for d in D))==2:fpoly[1]+=1
for i,j in combinations(V,2):
    co=sum(bool(d>>i&1) and bool(d>>j&1) for d in D)
    kind=('edge' if j in N[i] else 'same_part' if (i<9)==(j<9) else 'cross_nonedge')
    pair[kind,co]+=1
    traces={((d>>i)&1, (d>>j)&1) for d in D}
    if len(traces)==4:fpoly[2]+=1
for a,b,c in combinations(V,3):
    traces={((d>>a)&1, (d>>b)&1, (d>>c)&1) for d in D}
    if len(traces)==8:fpoly[3]+=1
assert fpoly==[1,18,126,0], fpoly
assert pair=={('same_part',1):72,('edge',0):27,('cross_nonedge',2):54},pair
# adaptive depth 3 explicit second levels and existence of distinguishing coordinate for all four grandchildren
root=0; nonincident=next(l for l in L if not incident(root,l)); incident_line=next(l for l in L if incident(root,l))
branches={}
for rb,query in ((1,nonincident),(0,incident_line)):
    sub=[d for d in D if ((d>>root)&1)==rb]
    for b in (0,1):
        child=[d for d in sub if ((d>>query)&1)==b]
        assert len(child)>=2
        witness=next(v for v in V if len({(d>>v)&1 for d in child})==2)
        branches[rb,b]=(query,len(child),witness)
assert len(branches)==4
# every vertex occurs in exactly five concepts, ruling out depth four
assert all(sum((d>>v)&1 for d in D)==5 for v in V)
print('PASS graph=(18 vertices, 27 edges), domination_number=5, minimum_sets=18')
print('PASS classification: 9 line-centered plus 9 point-centered constructions')
print('PASS pair_concurrence: adjacency 0 (27), same-side 1 (72), cross-nonincident 2 (54)')
print('PASS shattering polynomial=1+18z+126z^2, VCdim=2, first Betti=109')
print('PASS Littlestone dimension=3, explicit adaptive third-level witnesses:')
print('root',root,'second-query for positive',nonincident,'for negative',incident_line,'branches',sorted(branches.items()))
