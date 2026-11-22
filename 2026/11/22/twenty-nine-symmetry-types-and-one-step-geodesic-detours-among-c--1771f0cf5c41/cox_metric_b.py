"""Independent stdlib certificate for Coxeter-graph distance resolution and symmetry.

Fano-line exclusion representation, distinct from the modular-layer implementation.
Run: python3 cox_metric_b.py
"""
from collections import Counter, deque
from itertools import combinations, permutations

points = range(7)
fano_lines = {frozenset((r, (r+1)%7, (r+3)%7)) for r in points}
assert len(fano_lines) == 7
triples = [t for t in combinations(points, 3) if frozenset(t) not in fano_lines]
assert len(triples) == 28
lookup = {t:i for i,t in enumerate(triples)}
adjacency = [set() for _ in triples]
for i in range(len(triples)):
    for j in range(i):
        if not (set(triples[i]) & set(triples[j])):
            adjacency[i].add(j)
            adjacency[j].add(i)
assert all(len(nbrs)==3 for nbrs in adjacency)
assert sum(map(len, adjacency))//2==42
# Explicit isomorphism witness between the Fano nonline model and the
# three circulant layers plus seven hub vertices. This checks the labelled
# object rather than merely matching a few numerical invariants.
iso=(0,14,24,2,27,7,11,15,8,16,26,4,5,19,22,25,12,9,20,13,3,17,23,10,18,1,21,6)
assert sorted(iso)==list(range(28))
layered=[set() for _ in range(28)]
def connect(a,b):
    layered[a].add(b)
    layered[b].add(a)
for layer,step in enumerate((1,2,3)):
    for r in range(7):
        connect(7*layer+r,7*layer+(r+step)%7)
for r in range(7):
    for layer in range(3):
        connect(21+r,7*layer+r)
assert all({iso[j] for j in adjacency[i]}==layered[iso[i]] for i in range(28))

def distances(source):
    d = [-1]*len(adjacency)
    d[source] = 0
    q = deque([source])
    while q:
        u = q.popleft()
        for v in adjacency[u]:
            if d[v] < 0:
                d[v] = d[u]+1
                q.append(v)
    assert -1 not in d
    return d

D = [distances(s) for s in range(28)]
assert max(map(max, D))==4

def resolves(S):
    return len({tuple(D[v][s] for s in S) for v in range(28)}) == 28

assert not any(resolves(S) for S in combinations(range(28),3))
bases = [S for S in combinations(range(28),4) if resolves(S)]
assert len(bases)==7728
base_index = {S:i for i,S in enumerate(bases)}
R = [set() for _ in bases]
for i,S in enumerate(bases):
    st = set(S)
    for p in S:
        for q in range(28):
            if q in st:continue
            target = tuple(sorted(st-{p}|{q}))
            if target in base_index:R[i].add(base_index[target])
assert sum(map(len,R))//2==155904
assert Counter(map(len,R)) == {28:168,32:168,34:672,36:1344,38:336,39:672,
 40:504,41:672,42:168,43:1680,46:336,47:672,50:168,54:168}

# The 168 Fano collineations induce permutations of the 28 nonlines.
collineations=[]
for p in permutations(points):
    moved={frozenset(p[x] for x in line) for line in fano_lines}
    if moved==fano_lines:
        collineations.append(tuple(lookup[tuple(sorted(p[x] for x in t))] for t in triples))
assert len(collineations)==168
# A witnessed extra Coxeter involution, in lexicographic order of nonline triples.
extra=(0,4,9,3,1,12,15,8,7,2,16,17,5,23,14,6,10,11,21,24,22,18,20,13,19,25,27,26)
assert sorted(extra)==list(range(28))
assert all({extra[j] for j in adjacency[i]} == adjacency[extra[i]] for i in range(28))
perms=set(collineations)
perms.update(tuple(extra[p[i]] for i in range(28)) for p in collineations)
assert len(perms)==336
assert all(all({p[j] for j in adjacency[i]} == adjacency[p[i]] for i in range(28)) for p in perms)

# The classical fact Aut(Coxeter) has size 336 makes these all automorphisms;
# orbit counting itself does not require that external group-order result.
remaining=set(range(len(bases)))
orbits=[]
while remaining:
    i=min(remaining)
    orbit={base_index[tuple(sorted(p[x] for x in bases[i]))] for p in perms}
    assert orbit <= remaining
    orbits.append(sorted(orbit))
    remaining.difference_update(orbit)
assert len(orbits)==29
assert Counter(map(len,orbits))=={336:18,168:9,84:2}

def bfs(start):
    dd=[-1]*len(bases)
    dd[start]=0
    q=deque([start])
    while q:
        u=q.popleft()
        for v in R[u]:
            if dd[v]<0:
                dd[v]=dd[u]+1
                q.append(v)
    assert -1 not in dd
    return dd

ordered_excess=Counter()
ecc_counts=Counter()
for orbit in orbits:
    root=orbit[0]
    dd=bfs(root)
    ecc_counts[max(dd)] += len(orbit)
    base=set(bases[root])
    for j,other in enumerate(bases):
        johnson=4-len(base.intersection(other))
        difference=dd[j]-johnson
        assert difference in (0,1)
        ordered_excess[difference] += len(orbit)
assert ecc_counts=={4:1680,5:6048}
assert ordered_excess[1]//2==449820
assert (ordered_excess[0]-len(bases))//2==29407308 # exclude 7728 diagonal entries
print('fano_lines=',len(fano_lines),'nonlines=',len(triples),'edges=42')
print('minimum_resolving_sets=',len(bases),'nonresolving_triples=3276')
print('minimum_basis_exchange_edges=',sum(map(len,R))//2)
print('full_automorphism_group_order=',len(perms),'basis_orbits=',len(orbits), 'orbit_sizes=',dict(Counter(map(len,orbits))))
print('eccentricity_histogram=',dict(ecc_counts),'Johnson_plus_one_unordered_pairs=',ordered_excess[1]//2)
print('ALL_CHECKS_PASS')
