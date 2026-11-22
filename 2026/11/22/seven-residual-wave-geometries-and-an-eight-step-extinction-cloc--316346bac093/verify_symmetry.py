"""Verify complete icosahedral symmetry group and its threshold-two wave classes."""
import csv, json
from collections import Counter,defaultdict
from pathlib import Path
adj=[tuple(map(int,line.split())) for line in Path('adjacency.txt').read_text().splitlines()]
assert len(adj)==12
adjset=[set(x) for x in adj]
assert all(len(x)==5 for x in adjset)
assert all(i in adjset[j] for i in range(12) for j in adj[i])
# Five-neighbor rings and unique distance-two contacts give at most 12*10=120 automorphisms.
for v in range(12):
    nbr=adjset[v]
    assert sum(len(nbr & adjset[u]) for u in nbr)==10
    seen={v}|nbr
    second=set(range(12))-seen
    assert len(second)==6
    # The five non-antipodal distance-two nodes each share exactly two neighbors of v.
    assert sorted(len(adjset[w]&nbr) for w in second)==[0,2,2,2,2,2]
    assert len({frozenset(adjset[w]&nbr) for w in second if adjset[w]&nbr})==5
perms=[tuple(p) for p in json.loads(Path('automorphisms.json').read_text())]
assert len(perms)==120 and len(set(perms))==120
for p in perms:
    assert sorted(p)==list(range(12))
    assert all(set(p[j] for j in adj[i])==adjset[p[i]] for i in range(12))
assert tuple(range(12)) in perms
permset=set(perms)
for p in perms:
    # Pairwise closure tests full finite group of 120 elements.
    for q in perms:
        assert tuple(p[q[i]] for i in range(12)) in permset
with open('orbit_roots.csv',newline='') as fh:
    rows=list(csv.DictReader(fh))
roots=[int(r['root_code']) for r in rows]
basins={int(r['root_code']):int(r['basin_size']) for r in rows}
assert len(roots)==len(set(roots))==200
pw=[3**i for i in range(12)]

def succ(code):
    d=[(code//p)%3 for p in pw]
    return sum(pw[i]*(2 if d[i]==1 else (int(sum(d[z]==1 for z in adj[i])>=2) if d[i]==0 else 0)) for i in range(12))
def canon(code):return min(code,succ(code),succ(succ(code)))
for r in roots:
    assert succ(succ(succ(r)))==r and succ(r)!=r
assert roots==sorted(roots)
lookup=set(roots)
parent={r:r for r in roots}
def find(x):
    if parent[x]!=x:parent[x]=find(parent[x])
    return parent[x]
def union(x,y):
    rx,ry=find(x),find(y)
    if rx!=ry:parent[ry]=rx
for root in roots:
    d=[(root//p)%3 for p in pw]
    for p in perms:
        code=sum(pw[p[i]]*d[i] for i in range(12))
        dest=canon(code)
        assert dest in lookup
        union(root,dest)
classes=defaultdict(list)
for root in roots:classes[find(root)].append(root)
summary=[]
for group in classes.values():
    assert len(set(basins[r] for r in group))==1
    r=min(group)
    digits=''.join(str((r//p)%3) for p in pw)
    summary.append((len(group),r,digits,basins[r]))
summary.sort()
with open('orbit_classes.csv','w',newline='') as fh:
    w=csv.writer(fh);w.writerow(['spatial_orbit_size','representative_code','representative_digits','individual_cycle_basin'])
    w.writerows(summary)
print('graph_automorphisms',len(perms))
print('full_group_proved_by_12_times_10_upper_bound',True)
print('geometric_classes',len(classes))
print('size_histogram',sorted(Counter(c[0] for c in summary).items()))
print('class_table: size,root,digits,basin')
for c in summary:print(','.join(map(str,c)))
print('total_temporal_orbits',sum(c[0] for c in summary))
