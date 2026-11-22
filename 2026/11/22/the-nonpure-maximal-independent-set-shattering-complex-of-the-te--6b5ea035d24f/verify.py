"""Independent standard-library verification of H(3,3) maximal-independent-set shattering."""
from itertools import product, combinations
from collections import Counter
P=list(product(range(3),repeat=3))
assert len(P)==27
neighbor=[{j for j in range(27) if j!=i and sum(a!=b for a,b in zip(P[i],P[j]))==1} for i in range(27)]

# Construct every independent subset via increasing-index backtracking.
indep=[frozenset()]
def enum(prefix, start):
    for v in range(start,27):
        if neighbor[v].isdisjoint(prefix):
            new=prefix|{v};indep.append(new);enum(new,v+1)
enum(frozenset(),0)
assert len(indep)==11776
concepts=[s for s in indep if all(v in s or not neighbor[v].isdisjoint(s) for v in range(27))]
assert len(concepts)==390
assert Counter(map(len,concepts))=={5:54,7:324,9:12}

# For every independent support, test all 2**|support| traces. The downward
# closure pruning is safe because every subset of a shattered set is shattered.
shattered={frozenset()}
for size in range(1,10):
    for s in (t for t in indep if len(t)==size):
        if any(s-{v} not in shattered for v in s):continue
        vertices=tuple(sorted(s))
        traces={sum((1<<j) for j,v in enumerate(vertices) if v in c) for c in concepts}
        if len(traces)==(1<<size):shattered.add(s)
counts=Counter(map(len,shattered))
assert counts=={0:1,1:27,2:270,3:1278,4:2862,5:2322}, counts
facets={s for s in shattered if all(s|{v} not in shattered for v in range(27) if v not in s)}
assert Counter(map(len,facets))=={3:36,5:2322}

# The lower-dimensional facets are exactly the 36 three-word, 3-coordinate
# transversals (each coordinate takes three distinct values).
diagonal={frozenset(t) for t in combinations(range(27),3) if all(len({P[i][k] for i in t})==3 for k in range(3))}
assert len(diagonal)==36
assert {s for s in facets if len(s)==3}==diagonal

# The following four generators give the entire S_3 wr S_3 action.
def swap_coord(p,i,j):
    v=list(p);v[i],v[j]=v[j],v[i];return tuple(v)
def swap_values(p,i,a,b):
    v=list(p)
    if v[i]==a:v[i]=b
    elif v[i]==b:v[i]=a
    return tuple(v)
fns=[lambda p:swap_coord(p,0,1),lambda p:swap_coord(p,1,2),lambda p:swap_values(p,0,0,1),lambda p:swap_values(p,0,1,2)]
gens=[[P.index(f(p)) for p in P] for f in fns]
def orbit_sizes(supports):
    unvisited=set(supports);sizes=[]
    while unvisited:
        seed=min(unvisited,key=lambda s:tuple(sorted(s)))
        todo=[seed];seen={seed}
        for s in todo:
            for g in gens:
                t=frozenset(g[v] for v in s)
                assert t in supports
                if t not in seen:seen.add(t);todo.append(t)
        sizes.append(len(seen));unvisited.difference_update(seen)
    return sorted(sizes)
assert orbit_sizes({s for s in facets if len(s)==3})==[36]
assert orbit_sizes({s for s in facets if len(s)==5})==[54,324,648,648,648]
print('TERNARY_HAMMING_MIS_SHATTER_PASS')
print('Independent supports:',len(indep))
print('Maximal independent sets:',len(concepts),dict(Counter(map(len,concepts))))
print('Shattering coefficients:',dict(sorted(counts.items())))
print('Facet sizes:',dict(Counter(map(len,facets))))
print('Five-face symmetry orbits:',[54,324,648,648,648])
