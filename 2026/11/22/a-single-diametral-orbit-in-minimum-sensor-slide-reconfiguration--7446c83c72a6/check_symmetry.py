#!/usr/bin/env python3
"""Symmetry check for the unique orbit of diametral slide pairs."""
from collections import Counter, deque
from itertools import combinations, permutations
import json

V = tuple(permutations((0, 1, 2, 3)))
name = {v: i for i, v in enumerate(V)}
nei = [set() for _ in V]
for i, p in enumerate(V):
    for j in range(1, 4):
        q = list(p)
        q[0], q[j] = q[j], q[0]
        nei[i].add(name[tuple(q)])

def propagated(initial):
    marked = set(initial)
    for i in initial:
        marked |= nei[i]
    while True:
        new = set()
        for x in marked:
            if len(nei[x] - marked) == 1:
                new |= nei[x] - marked
        if not new - marked:
            return len(marked) == 24
        marked |= new

states = [frozenset(c) for c in combinations(range(24), 3) if propagated(c)]
assert len(states) == 576
indices = {s: i for i, s in enumerate(states)}
edge = [[] for _ in states]
for i, s in enumerate(states):
    for v in s:
        for w in nei[v] - s:
            k = indices.get(frozenset((s - {v}) | {w}))
            if k is not None:
                edge[i].append(k)
assert all(len(set(row)) == 4 for row in edge)

# The 144 automorphisms act by relabelling the four values and permuting three occupied coordinates.
actions = set()
for relabel in permutations((0, 1, 2, 3)):
    for coord in permutations((1, 2, 3)):
        perm = tuple(name[(relabel[p[0]],) + tuple(relabel[p[j]] for j in coord)] for p in V)
        assert all({perm[y] for y in nei[x]} == nei[perm[x]] for x in range(24))
        actions.add(perm)
assert len(actions) == 144

remaining = set(states)
orbits = []
while remaining:
    representative = min(remaining, key=lambda x: tuple(sorted(x)))
    orbit = {frozenset(a[x] for x in representative) for a in actions}
    assert orbit <= remaining
    remaining -= orbit
    orbits.append(orbit)
assert sorted(map(len, orbits)) == [72, 72, 144, 144, 144]
# The five published representatives are GP labels, mapped into the arrangement presentation.
iso_to_gp = [0,18,22,8,4,14,12,6,10,20,16,2,17,7,11,13,21,3,5,19,23,1,9,15]
inv = {gp: i for i, gp in enumerate(iso_to_gp)}
reps_gp = ((0,18,22),(0,17,18),(0,18,21),(0,3,6),(0,7,10))
reps = [frozenset(inv[j] for j in gp) for gp in reps_gp]
assert all(r in states for r in reps)
assert sorted(len(next(o for o in orbits if r in o)) for r in reps) == [72,72,144,144,144]
assert len({next(i for i,o in enumerate(orbits) if r in o) for r in reps}) == 5

# Check distances and the exact extremal pair orbit.
diametric = set()
eccentricity = {}
for i, s in enumerate(states):
    distances = {i: 0}
    queue = deque([i])
    while queue:
        v = queue.popleft()
        for w in edge[v]:
            if w not in distances:
                distances[w] = distances[v] + 1
                queue.append(w)
    assert len(distances) == 576
    eccentricity[s] = max(distances.values())
    for j in range(i + 1, len(states)):
        if distances[j] == 10:
            diametric.add(frozenset((s, states[j])))
assert len(diametric) == 72
at_ten = {s for s in states if eccentricity[s] == 10}
assert len(at_ten) == 144
assert Counter(len(o & at_ten) for o in orbits) == {0: 4, 144: 1}
assert Counter(v for p in diametric for v in p) == {s:1 for s in at_ten}
assert reps[1] in at_ten and all(reps[k] not in at_ten for k in (0,2,3,4))

S = frozenset(inv[x] for x in (0,2,16))
T = frozenset(inv[x] for x in (6,8,22))
rep_pair = frozenset((S,T))
assert rep_pair in diametric
orbit_pairs = {
    frozenset((frozenset(a[x] for x in S), frozenset(a[x] for x in T)))
    for a in actions
}
assert orbit_pairs == diametric
print(json.dumps({
    'model': 'arrangement_A_4_3',
    'automorphisms': len(actions),
    'configuration_orbit_sizes': sorted(map(len, orbits)),
    'eccentricity_ten_orbit_size': len(at_ten),
    'diameter_ten_pairs': len(diametric),
    'pair_orbits': 1,
    'distinct_ends_of_diametral_pairs': len(at_ten),
    'representative_pair_in_GP_labels': [[0,2,16],[6,8,22]],
},sort_keys=True,separators=(',',':')))
