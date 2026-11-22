#!/usr/bin/env python3
"""Independent exact small-graph enumeration of edge-general-position sets.
Python 3 standard library only. All graph data constructed here."""
from collections import Counter, deque
from itertools import combinations

N=8
edges=set()
for i in range(N):
    for x,y in [(i,(i+1)%N),(i,8+i),(8+i,8+(i+3)%N)]:
        edges.add(tuple(sorted((x,y))))
E=sorted(edges)
assert len(E)==24
idx={e:i for i,e in enumerate(E)}
adj=[[] for _ in range(16)]
for x,y in E: adj[x].append(y);adj[y].append(x)
for row in adj:row.sort()
assert all(len(x)==3 for x in adj)

def distances(s):
    d=[99]*16; d[s]=0; q=deque([s])
    while q:
        x=q.popleft()
        for y in adj[x]:
            if d[y]==99:
                d[y]=d[x]+1;q.append(y)
    return d
D=[distances(s) for s in range(16)]
assert max(max(r) for r in D)==4

# Enumerate all geodesics from every source via strictly increasing distance.
forbidden=set()
for s in range(16):
    def trace(x,path):
        if x>s and len(path)>=3:
            for tri in combinations(path,3):
                forbidden.add(sum(1<<a for a in tri))
        for y in adj[x]:
            if D[s][y]==D[s][x]+1:
                e=idx[tuple(sorted((x,y)))]
                trace(y,path+[e])
    trace(s,[])
assert len(forbidden)==192, len(forbidden)

pair_masks=[[] for _ in range(24)]
for triple in forbidden:
    for i in range(24):
        if triple>>i&1:pair_masks[i].append(triple^(1<<i))

def can_add(mask,i):
    return all(mask&p!=p for p in pair_masks[i])

hist=Counter(); fac=Counter(); tops=[]; good=[]
def dfs(mask,after,count):
    hist[count]+=1
    good.append(mask)
    for i in range(after,24):
        if can_add(mask,i):
            dfs(mask|(1<<i),i+1,count+1)
dfs(0,0,0)
assert len(good)==sum(hist.values())
for mask in good:
    if all(not can_add(mask,i) for i in range(24) if not mask>>i&1):
        fac[mask.bit_count()]+=1

want_hist={0:1,1:24,2:276,3:1832,4:7362,5:17712,6:24468,7:18240,8:7017,9:1576,10:300,11:48,12:4}
want_fac={7:792,8:1329,9:336,10:36,12:4}
assert dict(hist)==want_hist, (dict(hist),want_hist)
assert dict(fac)==want_fac, (dict(fac),want_fac)

codes=[]
for C in combinations(range(16),4):
    closed=[set([c]+adj[c]) for c in C]
    if len(set.union(*closed))==16 and sum(len(x) for x in closed)==16:
        codes.append(C)
assert codes==[(0,4,10,14),(1,5,11,15),(2,6,8,12),(3,7,9,13)]
max_masks=[]
for C in codes:
    mm=sum(1<<i for i,(x,y) in enumerate(E) if x in C or y in C)
    assert mm.bit_count()==12
    assert all(mm&bad!=bad for bad in forbidden)
    max_masks.append(mm)
assert sorted([m for m in good if m.bit_count()==12])==sorted(max_masks)
assert all((a&b).bit_count()==4 for a,b in combinations(max_masks,2))

print('VERIFY_OK')
print('n=16 m=24 diameter=4 geodesic_forbidden_triples=192')
print('valid_sets',len(good),'face_histogram',sorted(hist.items()))
print('facet_histogram',sorted(fac.items()))
print('perfect_codes',codes)
print('maxima',sorted(max_masks),'pairwise_intersections=4')
