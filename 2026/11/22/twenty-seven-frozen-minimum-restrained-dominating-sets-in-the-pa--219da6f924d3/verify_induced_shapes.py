"""Exhaustive restrained-domination and mobility census for the Pappus graph."""
from collections import Counter
from itertools import combinations, permutations, product

V = range(18)
P = list(product(range(3), repeat=2))
blocks = [frozenset(p for p, (x,y) in enumerate(P) if (x,y,(x+y)%3)[d] == a)
          for d, a in product(range(3), repeat=2)]
N = {9+j: set(B) for j, B in enumerate(blocks)}
N.update({p: {9+j for j, B in enumerate(blocks) if p in B} for p in range(9)})


def distances(adj, root):
    d, q = {root: 0}, [root]
    for u in q:
        for v in adj[u] - d.keys():
            d[v] = d[u] + 1
            q.append(v)
    return d


assert all(len(N[v]) == 3 for v in V) and set(distances(N, 0)) == set(V)
ordinary, restrained, optimum = Counter(), Counter(), set()
for k in range(19):
    for selected in combinations(V, k):
        S = frozenset(selected)
        out = set(V) - S
        if any(N[v] <= out for v in out):
            continue
        ordinary[k] += 1
        if any(N[v] <= S for v in out):
            continue
        restrained[k] += 1
        if k == 6:
            optimum.add(S)
assert min(ordinary) == 5 and ordinary[5] == 18
assert restrained == dict(zip((*range(6,17),18), (207,1242,3429,5040,4671,3294,1809,756,297,54,27,1)))

autos = []
for s in (0,9):
    lookup = {frozenset(N[i]): i for i in range(9-s,18-s)}
    shore = []
    for images in permutations(range(s,s+9)):
        targets = tuple(lookup.get(frozenset(images[p] for p in B)) for B in blocks)
        if None not in targets:
            assert len(set(targets)) == 9
            shore.append(images + targets)
    assert len(shore) == 108
    autos.extend(shore)


def mask(S):
    return sum(1 << i for i in S)


def degrees(S):
    return tuple(sorted(len(N[v] & S) for v in S))


todo = optimum.copy()
shapes = {}
while todo:
    S = min(todo, key=mask)
    orbit = {frozenset(g[v] for v in S) for g in autos}
    assert orbit <= todo and {degrees(T) for T in orbit} == {degrees(S)}
    todo -= orbit
    shapes[mask(S)] = (len(orbit), degrees(S))
assert shapes == {3682: (9,(1,1,1,1,1,1)), 3591: (18,(0,0,1,1,1,3)),
                  38150: (18,(0,0,0,0,0,0)), 5040: (54,(0,0,0,0,0,0)),
                  6020: (108,(0,0,0,0,1,1))}
frozen = {S for S in optimum if sum(degrees(S)) == 6}
assert len(frozen) == 27

for slide, ecount, degs, ecc in [(False,432,{0:27,4:108,6:72},6), (True,324,{0:27,2:108,6:72},8)]:
    adj = {S: set() for S in optimum}
    for S,T in combinations(optimum, 2):
        if len(S & T) == 5 and (not slide or next(iter(S-T)) in N[next(iter(T-S))]):
            adj[S].add(T)
            adj[T].add(S)
    assert {S for S in optimum if not adj[S]} == frozen
    assert Counter(map(len, adj.values())) == degs
    assert sum(map(len, adj.values())) == 2*ecount
    main = optimum - frozen
    assert len(main) == 180
    for S in main:
        d = distances(adj, S)
        assert set(d) == main and max(d.values()) == ecc
print('PASS: complete polynomial, 216 automorphisms, five orbits, both move graphs, and 9 matching + 18 claw frozen states')
