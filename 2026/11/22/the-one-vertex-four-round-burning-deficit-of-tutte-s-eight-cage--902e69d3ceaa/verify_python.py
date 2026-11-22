#!/usr/bin/env python3
"""Exact standalone checker for four-round covering on the Tutte–Coxeter graph.
No third-party packages. Python >=3.9."""
from itertools import combinations, product
from collections import Counter, deque

LABELS = range(6)
DUADS = list(combinations(LABELS, 2))

def make_matchings(left):
    if not left:
        yield ()
        return
    a=left[0]
    for b in left[1:]:
        rest=tuple(c for c in left if c!=a and c!=b)
        for suffix in make_matchings(rest):
            yield ((a,b),)+suffix

SYNTHEMES=list(make_matchings(tuple(LABELS)))
assert len(SYNTHEMES)==15
DUAD_IND={e:i for i,e in enumerate(DUADS)}
ADJ=[set() for _ in range(30)]
for j,M in enumerate(SYNTHEMES):
    for e in M:
        i=DUAD_IND[e]
        ADJ[i].add(15+j)
        ADJ[15+j].add(i)
assert sum(map(len,ADJ))==90 and all(len(a)==3 for a in ADJ)
# Explicit point-line dual automorphism for the fixed duad/syntheme ordering.
DUAL=(15,22,20,28,24,27,25,19,23,16,26,18,21,29,17,
      0,9,14,11,7,2,12,1,8,4,6,10,5,3,13)
assert set(DUAL)==set(range(30))
assert all(DUAL[DUAL[u]]==u for u in range(30))
assert all({DUAL[v] for v in ADJ[u]}==ADJ[DUAL[u]] for u in range(30))
assert all((DUAL[u]<15)!=(u<15) for u in range(30))

DIST=[]
for s in range(30):
    d=[-1]*30;d[s]=0;q=deque([s])
    while q:
        u=q.popleft()
        for v in ADJ[u]:
            if d[v]==-1:
                d[v]=d[u]+1;q.append(v)
    DIST.append(d)
assert all(Counter(d)==Counter({0:1,1:3,2:6,3:12,4:8}) for d in DIST)
BALLS=[[sum(1<<v for v in range(30) if DIST[u][v]<=r) for u in range(30)] for r in range(5)]
ALL=(1<<30)-1
# Independently check the local intersection bounds for all 900 ordered pairs.
for a,b in product(range(30),repeat=2):
    distant = ALL ^ BALLS[3][a]
    i2=(BALLS[2][b]&distant).bit_count()
    i1=(BALLS[1][b]&distant).bit_count()
    expect={0:(0,0),1:(0,0),2:(4,0),3:(2,2),4:(4,1)}[DIST[a][b]]
    assert (i2,i1)==expect

total=0; distsecond=Counter(); first=Counter(); omitted=Counter(); omitted_distance=Counter()
strict_count=0; nonstrict_29=0; maxcov=0; histogram=Counter()
for a in range(30):
    for b in range(30):
        first_two=BALLS[3][a]|BALLS[2][b]
        for c in range(30):
            first_three=first_two|BALLS[1][c]
            for d in range(30):
                covered=first_three|(1<<d)
                pop=covered.bit_count();histogram[pop]+=1
                maxcov=max(maxcov,pop)
                if pop==29:
                    valid=(DIST[a][b]>=1 and DIST[a][c]>=2 and DIST[a][d]>=3
                           and DIST[b][c]>=1 and DIST[b][d]>=2 and DIST[c][d]>=1)
                    if not valid:nonstrict_29+=1
                    miss=(ALL^covered).bit_length()-1
                    omitted[(a,miss)]+=1
                    omitted_distance[DIST[a][miss]]+=1
                    total+=1;first[a]+=1;distsecond[DIST[a][b]]+=1
assert maxcov==29 and total==2160 and nonstrict_29==0
assert all(first[a]==72 for a in range(30))
assert len(omitted)==240 and all(x==9 for x in omitted.values())
assert distsecond=={2:720,4:1440}
assert omitted_distance=={4:2160}
# Distances of pairwise-intersecting duads are four; the five named ignitions are legal.
seq=tuple(DUAD_IND[(0,v)] for v in (1,2,3,4,5))
assert all(DIST[seq[i]][seq[j]]>=j-i for i in range(5) for j in range(i+1,5))
assert set().union(*(set(j for j in range(30) if DIST[seq[i]][j]<=4-i) for i in range(5)))==set(range(30))
print('CHECKER_PYTHON_OK')
print('vertices=30 edges=45 diameter=4 girth>=8')
print('explicit_point_line_duality=verified_involutory_automorphism')
print('maximum_four_round_coverage=',maxcov)
print('four_round_schedules_29=',total)
print('by_second_distance=',dict(sorted(distsecond.items())))
print('first_source_count_set=',sorted(set(first.values())))
print('ordered_antipodal_source_survivor_pairs=',len(omitted),'per_pair=',sorted(set(omitted.values())))
print('all_29_schedules_strict=',nonstrict_29==0)
print('five_round_example=',seq)
print('coverage_histogram=',dict(sorted(histogram.items())))
