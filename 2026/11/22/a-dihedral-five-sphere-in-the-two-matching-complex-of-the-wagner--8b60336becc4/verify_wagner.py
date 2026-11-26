"""Exhaustively check the Wagner degree-two complex from its graph definition."""
from collections import Counter
from graphlib import TopologicalSorter
from itertools import combinations, permutations

V = tuple(range(8))
E = tuple((a,b) for a,b in combinations(V, 2) if b-a in (1,4,7))
F = {frozenset(c) for k in range(13) for c in combinations(range(12), k)
     if max(Counter(v for i in c for v in E[i]).values(), default=0) <= 2}
empty = frozenset()
sizes = Counter(map(len, F))
assert tuple(sizes[k] for k in range(1,9)) == (12,66,212,423,516,352,108,7)
facets = Counter(len(f)-1 for f in F if all(f|{i} not in F for i in set(range(12))-f))
assert facets == {6: 52, 7: 7}

left = F.copy()
matched = set()
for j in range(12):
    # All candidates for any one j are disjoint, so order within a round does not matter.
    pairs = [(f,f|{j}) for f in left if j not in f and f|{j} in left]
    left.difference_update(f for p in pairs for f in p)
    matched.update(p for p in pairs if p[0])
F.remove(empty)
critical = sorted(sum(2**i for i in f) for f in F-set().union(*map(set,matched)))
assert len(matched) == 847 and critical == [1,2646]
graph = TopologicalSorter()
for f in F:
    graph.add(f)
    for i in f:
        g = f-{i}
        if g:
            graph.add(*( (f,g) if (g,f) in matched else (g,f) ))
assert len(list(graph.static_order())) == 1696

def pair(a,b):
    return (min(a,b), max(a,b))

edge_set = set(E)
autos = {p for p in permutations(V) if all(pair(p[a],p[b]) in edge_set for a,b in E)}
expected = {tuple((sign*i+c)%8 for i in V) for sign in (1,-1) for c in V}
assert autos == expected

def trace(p):
    image = [E.index(pair(p[a],p[b])) for a,b in E]
    # An invariant simplex is a union of whole edge orbits. Its alternating
    # trace contribution is (-1)^(number of included edge orbits - 1).
    cycles, todo = [], set(range(12))
    while todo:
        i = next(iter(todo)); orbit = set()
        while i not in orbit:
            orbit.add(i); i = image[i]
        cycles.append(orbit); todo -= orbit
    tally = [0]*8
    for k in range(1,len(cycles)+1):
        for subset in combinations(cycles,k):
            f = frozenset().union(*subset)
            if f in F:
                tally[len(f)-1] += (-1)**(k-1)
    return 1-sum(tally), tally

for c in V:
    assert trace(tuple((i+c)%8 for i in V))[0] == (-1)**c
    assert trace(tuple((c-i)%8 for i in V))[0] == (-1)**(c+1)
print('facets', sorted(facets.items()), 'Morse critical masks', critical)
print('Acyclic Hasse vertices', len(F), 'disjoint pairs', len(matched), 'full automorphism order', len(autos))
print('signed H_5 trace and alternating chain trace r:', trace(tuple((i+1)%8 for i in V)))
print('signed H_5 trace and alternating chain trace s:', trace(tuple(-i%8 for i in V)))
