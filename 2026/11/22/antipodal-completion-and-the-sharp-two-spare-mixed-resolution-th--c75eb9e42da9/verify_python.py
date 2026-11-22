#!/usr/bin/env python3
"""Exhaustive mixed metric resolving sets of the icosahedral graph.

Only Python's standard library is needed. This enumerator compares complete
42-element ordered distance signatures, rather than pair-witness masks.
"""
from collections import Counter, deque
from itertools import combinations

N = 12
adj = [set() for _ in range(N)]
def edge(u, v):
    adj[u].add(v)
    adj[v].add(u)
for i in range(5):
    a, b = i + 2, i + 7
    for u, v in ((0,a), (1,b), (a,2+(i+1)%5),
                 (b,7+(i+1)%5), (a,b), (a,7+(i-1)%5)):
        edge(u,v)
E = sorted((u,v) for u in range(N) for v in adj[u] if u < v)
assert len(E) == 30 and all(len(a)==5 for a in adj)
D = []
for source in range(N):
    row=[-1]*N; row[source]=0; q=deque([source])
    while q:
        v=q.popleft()
        for w in adj[v]:
            if row[w]<0:
                row[w]=row[v]+1; q.append(w)
    assert max(row)==3
    D.append(row)
items = [('v',v) for v in range(N)] + [('e',e) for e in E]
assert len(items)==42
# 42 distance responses for each candidate landmark.
response = [[D[s][x] if kind=='v' else min(D[s][x[0]], D[s][x[1]])
             for kind,x in items] for s in range(N)]

def mixed(mask):
    selected = [s for s in range(N) if mask & (1<<s)]
    return len({tuple(response[s][j] for s in selected) for j in range(42)}) == 42

good = {mask for mask in range(1<<N) if mixed(mask)}
all_counts=Counter(mask.bit_count() for mask in good)
assert all_counts == {6:20,7:240,8:405,9:220,10:66,11:12,12:1}
minimals={mask for mask in good if not any(mask^(1<<i) in good for i in range(N) if mask&(1<<i))}
assert Counter(mask.bit_count() for mask in minimals)=={6:20,7:120}
anti=[(u,v) for u,v in combinations(range(N),2) if D[u][v]==3]
assert len(anti)==6 and len({v for pair in anti for v in pair})==12
minimum = {mask for mask in good if mask.bit_count()==6}
expected = {sum(1<<v for pair in triples for v in pair)
            for triples in combinations(anti,3)}
assert minimum==expected and len(expected)==20
# Each selected 3-axis set yields the antipodal completion of eight
# ordinary 3-landmark configurations, one orientation per axis.
for triple in combinations(anti,3):
    for orientation in range(8):
        selectors = [triple[i][(orientation>>i)&1] for i in range(3)]
        assert len({tuple(D[s][v] for s in selectors) for v in range(N)})==N
# The two geometries are induced 6-cycles and pairs of disjoint triangles.
shapes=Counter()
for mask in minimum:
    V=[i for i in range(N) if mask>>i&1]
    degree=[sum(w in adj[v] for w in V) for v in V]
    assert sorted(degree)==[2]*6
    t=sum(all(v in adj[u] for u,v in combinations(tri,2)) for tri in combinations(V,3))
    assert t in (0,2)
    shapes[t]+=1
assert shapes=={0:10,2:10}

# Addition/removal reconfiguration with at most b probes.
component_counts=[]
for budget in (6,7,8):
    states={m for m in good if m.bit_count()<=budget}
    unseen=set(states); sizes=[]; min_per_component=[]
    while unseen:
        s=unseen.pop(); size=0; nmin=0; q=[s]
        while q:
            m=q.pop();size+=1;nmin+=(m in minimum)
            for i in range(N):
                other=m^(1<<i)
                if other in unseen:
                    unseen.remove(other);q.append(other)
        sizes.append(size);min_per_component.append(nmin)
    component_counts.append(len(sizes))
    if budget==6:assert sorted(sizes)==[1]*20
    if budget==7:assert Counter(sizes)=={1:120,7:20} and sorted(min_per_component)==[0]*120+[1]*20
    if budget==8:assert sizes==[665] and min_per_component==[20]
assert component_counts==[20,140,1]
print('ICOSAHEDRAL_MIXED_VERIFY_OK')
print('all', dict(sorted(all_counts.items())))
print('minimal',dict(sorted(Counter(mask.bit_count() for mask in minimals).items())))
print('minimum antipodal-triple selections',len(expected),'C6',shapes[0],'2K3',shapes[2])
print('budget components',component_counts)
