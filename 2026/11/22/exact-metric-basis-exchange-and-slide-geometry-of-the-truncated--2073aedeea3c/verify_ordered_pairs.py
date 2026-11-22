"""Exhaustive, standard-library verification of a truncated-tetrahedron metric-basis classification.

Vertices are the 12 ordered pairs (a,b), a!=b, from four tetrahedron corners.
Edges join reversals and pairs with the same first coordinate.
No graph or scientific-computing libraries are required.
"""
import collections
import itertools
import json

V = tuple((a, b) for a in range(4) for b in range(4) if a != b)
N = len(V)
ADJ = tuple(frozenset(j for j in range(N) if j != i and
                       (V[i][0] == V[j][0] or V[i] == V[j][::-1]))
            for i in range(N))
assert N == 12 and sum(map(len, ADJ)) == 36


def distances(start, neighbors):
    d = {start: 0}
    todo = collections.deque([start])
    while todo:
        x = todo.popleft()
        for y in neighbors(x):
            if y not in d:
                d[y] = d[x] + 1
                todo.append(y)
    return d


D = tuple(distances(i, lambda j: ADJ[j]) for i in range(N))
assert all(len(row) == N for row in D)


def signature_count(landmarks):
    return len({tuple(D[x][j] for j in landmarks) for x in range(N)})


AUT = tuple({i: V.index((p[a], p[b])) for i, (a,b) in enumerate(V)}
            for p in itertools.permutations(range(4)))
assert len(AUT) == 24


def orbit_partition(k):
    unseen = set(itertools.combinations(range(N), k))
    result = []
    while unseen:
        rep = min(unseen)
        orbit = {tuple(sorted(perm[i] for i in rep)) for perm in AUT}
        assert orbit <= unseen
        unseen -= orbit
        result.append((rep, len(orbit), signature_count(rep)))
    assert sum(size for _, size, _ in result) == len(tuple(itertools.combinations(range(N),k)))
    return result


single = orbit_partition(1)
pairs = orbit_partition(2)
triples = orbit_partition(3)
assert len(single) == 1 and len(pairs) == 5 and len(triples) == 13
assert max(nsig for _,_,nsig in pairs) < N
assert [(s,c) for _,s,c in triples] == [
    (4,9),(24,11),(24,12),(24,12),(12,11),(24,12),(24,12),
    (12,12),(8,12),(24,12),(12,12),(24,11),(4,12)]

BASES = tuple(c for c in itertools.combinations(range(N),3)
              if signature_count(c) == N)
ALL = frozenset(BASES)
assert len(BASES) == 156


def graph_moves(local):
    neighbors = {}
    for a in BASES:
        aa = frozenset(a)
        possible = []
        for b in BASES:
            removed = aa - frozenset(b)
            added = frozenset(b) - aa
            if len(removed) != 1 or len(added) != 1:
                continue
            if not local or next(iter(added)) in ADJ[next(iter(removed))]:
                possible.append(b)
        neighbors[a] = tuple(possible)
    return neighbors


JUMP = graph_moves(local=False)
SLIDE = graph_moves(local=True)
assert sum(map(len,JUMP.values()))//2 == 1446
assert sum(map(len,SLIDE.values()))//2 == 450


def graph_stats(neighbors):
    counts = collections.Counter()
    penalties = collections.Counter()
    eccentricities = collections.Counter()
    for k,a in enumerate(BASES):
        d = distances(a, lambda t: neighbors[t])
        assert len(d) == len(BASES)
        eccentricities[max(d.values())] += 1
        for b in BASES[k+1:]:
            value = d[b]
            lower = 3 - len(set(a)&set(b))
            assert value >= lower
            counts[value] += 1
            penalties[value-lower] += 1
    return dict(sorted(counts.items())), dict(sorted(penalties.items())), dict(sorted(eccentricities.items()))


jdist,jextra,jecc = graph_stats(JUMP)
sdist,sextra,secc = graph_stats(SLIDE)
assert jdist == {1:1446,2:6000,3:4644}
assert jextra == {0:12090} and jecc == {3:156}
assert sdist == {1:450,2:1356,3:2812,4:3660,5:2964,6:812,7:36}
assert sextra == {0:2050,1:3708,2:4104,3:2024,4:204}
assert secc == {6:108,7:48}

# The metric-base family is not a matroid base system, despite the isometric
# token-jump network.  A, B are bases, but no exchange for element 4 of A.
a,b = (0,1,4),(0,3,6)
assert a in ALL and b in ALL
assert all(tuple(sorted((set(a)-{4}) | {j})) not in ALL for j in set(b)-set(a))

# Classify all 156 bases into nine tetrahedral-symmetry orbits; eccentricity is
# constant on each orbit, and the orbit data is an independently checkable table.
orb_data = []
for rep, size, sig in triples:
    if sig < N:
        continue
    distances_slide = distances(rep, lambda t: SLIDE[t])
    orb_data.append(dict(rep=list(rep), orbit_size=size,
                         jump_degree=len(JUMP[rep]), slide_degree=len(SLIDE[rep]),
                         slide_eccentricity=max(distances_slide.values())))
assert len(orb_data) == 9 and sum(x['orbit_size'] for x in orb_data) == 156

print(json.dumps(dict(vertices=12,edges=18,metric_dimension=3,basis_count=156,
                      triple_orbits=[[list(a),size,sig] for a,size,sig in triples],
                      orbit_data=orb_data,
                      jump_edges=1446,jump_eccentricities=jecc,jump_distance_hist=jdist,
                      slide_edges=450,slide_eccentricities=secc,slide_distance_hist=sdist,
                      slide_excess_hist=sextra,matroid_exchange_failure=[list(a),list(b),4]),
                 sort_keys=True))
