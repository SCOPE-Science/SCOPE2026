"""Structural enumeration and independent bounded-state metric certificate.

Reconstructs the six degree-profile classes without searching 24 choose 8 subsets.
"""
from itertools import combinations, product
from collections import Counter, deque

R=range(4);C=range(6)

def matrix(rows):
    return frozenset((r,c) for r,cells in enumerate(rows) for c in cells)

families={'two_full_columns':set(), 'three_active_columns':set(),
          'four_double_columns':set(), 'one_high_row':set(), 'two_high_rows':set()}

for cols in combinations(C,2):
    families['two_full_columns'].add(matrix([cols for _ in R]))

for cols in combinations(C,3):
    for omitted in product(range(3),repeat=4):
        if max(Counter(omitted).values())>2:continue
        rows=[[cols[j] for j in range(3) if j!=omitted[r]] for r in R]
        families['three_active_columns'].add(matrix(rows))

for cols in combinations(C,4):
    for choices in product(list(combinations(cols,2)), repeat=4):
        degrees=Counter(c for pair in choices for c in pair)
        if all(degrees[c]==2 for c in cols):
            families['four_double_columns'].add(matrix(choices))

for special in C:
    singles=[c for c in C if c!=special]
    for high in R:
        rows=[[special] for _ in R];rows[high]=singles
        families['one_high_row'].add(matrix(rows))
    for hi in combinations(R,2):
        for with_special in hi:
            other=next(x for x in hi if x!=with_special)
            for pair in combinations(singles,2):
                rows=[[special] for _ in R]
                rows[with_special]=[special,*pair]
                rows[other]=[c for c in singles if c not in pair]
                families['two_high_rows'].add(matrix(rows))

expected={'two_full_columns':15,'three_active_columns':1080,
          'four_double_columns':1350,'one_high_row':24,'two_high_rows':720}
assert {k:len(v) for k,v in families.items()}==expected
all_sets=set()
for v in families.values():
    assert all_sets.isdisjoint(v)
    all_sets.update(v)
assert len(all_sets)==3189
for s in all_sets:
    assert len(s)==8
    row=[sum((r,c) in s for c in C) for r in R]
    col=[sum((r,c) in s for r in R) for c in C]
    assert all(row[r]+col[c]-2*((r,c) in s)>=2 for r in R for c in C)
print('structural families',sorted(expected.items()),'total',len(all_sets))

states={tuple(x) for x in product(range(3),repeat=4) if max(Counter(x).values())<=2}
assert len(states)==54
adj={s:{t for t in states if sum(a!=b for a,b in zip(s,t))==1} for s in states}
assert Counter(map(len,adj.values()))==Counter({6:36,4:18})
assert sum(map(len,adj.values()))//2==144
all_distances={}
for s in states:
    distances={s:0};q=deque([s]);parents={s:None}
    while q:
        u=q.popleft()
        for v in adj[u]:
            if v not in distances:
                distances[v]=distances[u]+1;parents[v]=u;q.append(v)
    assert len(distances)==54
    for t,d in distances.items():all_distances[s,t]=d
assert max(all_distances.values())==5
witness=next((s,t) for (s,t),d in sorted(all_distances.items()) if d==5)
assert all_distances[witness]==5
print('mobile component',len(states),'vertices',sum(map(len,adj.values()))//2,'edges','diameter',max(all_distances.values()))
print('distance-five witness',witness)
print('STRUCTURAL CHECKS PASSED')
