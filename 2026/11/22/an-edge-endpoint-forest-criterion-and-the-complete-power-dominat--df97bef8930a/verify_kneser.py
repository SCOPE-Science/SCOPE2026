#!/usr/bin/env python3
"""Exhaustive verification of line-Petersen power domination."""
from itertools import combinations, permutations
from collections import Counter
import json

V = list(combinations(range(5), 2))
E = [(i, j) for i, a in enumerate(V) for j, b in enumerate(V)
     if i < j and set(a).isdisjoint(b)]
assert len(V) == 10 and len(E) == 15
N = len(E)
ADJ = [set() for _ in range(N)]
for i, (a, b) in enumerate(E):
    for j, (c, d) in enumerate(E):
        if i != j and ({a, b} & {c, d}):
            ADJ[i].add(j)
assert all(len(x) == 4 for x in ADJ)

def dominates(mask):
    observed = {i for i in range(N) if (mask >> i) & 1}
    for i in tuple(observed):
        observed.update(ADJ[i])
    while True:
        pending = set()
        for i in observed:
            missing = ADJ[i] - observed
            if len(missing) == 1:
                pending.update(missing)
        if not pending:
            break
        observed.update(pending)
    return len(observed) == N

def induced_forest(mask):
    covered = set()
    for i, (a, b) in enumerate(E):
        if (mask >> i) & 1:
            covered.update((a, b))
    parent = list(range(10))
    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for a, b in E:
        if a not in covered and b not in covered:
            x, y = root(a), root(b)
            if x == y:
                return False
            parent[x] = y
    return True

# Simple unoriented cycles, canonicalized by their edge sets.
P_ADJ = [set() for _ in range(10)]
for a, b in E:
    P_ADJ[a].add(b)
    P_ADJ[b].add(a)
edge_index = {e: i for i, e in enumerate(E)}
cycles = set()
def traverse(first, path):
    if len(path) > 10:
        return
    for w in P_ADJ[path[-1]]:
        if w == first and len(path) >= 3:
            bits = 0
            for a, b in zip(path, path[1:] + [first]):
                bits |= 1 << edge_index[(min(a, b), max(a, b))]
            cycles.add(bits)
        elif w not in path:
            traverse(first, path + [w])
for first in range(10):
    traverse(first, [first])
by_length = Counter(s.bit_count() for s in cycles)
assert by_length == {5: 12, 6: 10, 8: 15, 9: 20}, by_length
star_masks = [sum(1 << i for i, e in enumerate(E) if v in e) for v in range(10)]
pentagons = sorted(s for s in cycles if s.bit_count() == 5)
obstructions = star_masks + pentagons
assert len(set(obstructions)) == 22

def forbidden(mask):
    return any(mask & ~s == 0 for s in obstructions)

pd = [dominates(m) for m in range(1 << N)]
assert all(pd[m] == induced_forest(m) == (not forbidden(m)) for m in range(1 << N))
counts = Counter(m.bit_count() for m, good in enumerate(pd) if good)
assert [counts[k] for k in range(16)] == [0,0,15,325,1305,2991,5005,6435,6435,5005,3003,1365,455,105,15,1]
minimal = [m for m in range(1 << N) if pd[m] and all(not pd[m ^ (1 << i)] for i in range(N) if m >> i & 1)]
assert Counter(m.bit_count() for m in minimal) == {2: 15, 3: 140}
max_failed = [m for m in range(1 << N) if not pd[m] and all(pd[m | (1 << i)] for i in range(N) if not m >> i & 1)]
assert set(max_failed) == set(obstructions)

missing = []
for a, b in E:
    omitted = set(range(5)) - set(V[a]) - set(V[b])
    assert len(omitted) == 1
    missing.append(next(iter(omitted)))
opt = [m for m in range(1 << N) if pd[m] and m.bit_count() == 2]
assert all(len({missing[i] for i in range(N) if m >> i & 1}) == 1 for m in opt)
assert Counter(missing) == {0:3,1:3,2:3,3:3,4:3}

# The token-jumping graph on all optimal sensor pairs.
def components(states, neighbors):
    state_set = set(states)
    seen = set()
    out = []
    for m in states:
        if m in seen:
            continue
        seen.add(m)
        queue = [m]
        for u in queue:
            for v in neighbors(u):
                if v in state_set and v not in seen:
                    seen.add(v)
                    queue.append(v)
        out.append(queue)
    return out

def token_jumps(s):
    for i in range(N):
        if s >> i & 1:
            for j in range(N):
                if not (s >> j & 1):
                    yield s ^ (1 << i) ^ (1 << j)

TJ = components(opt, token_jumps)
assert Counter(map(len, TJ)) == {3: 5}
for c in TJ:
    assert all(sum(x in set(token_jumps(y)) for y in c if x != y) == 2 for x in c)

def tar(s):
    for i in range(N):
        yield s ^ (1 << i)

tar_summary = {}
for budget, wanted in ((2, {1:15}), (3, {1:140,40:5}), (4,{1645:1})):
    states = [m for m in range(1 << N) if pd[m] and m.bit_count() <= budget]
    comps = components(states, tar)
    size_count = Counter(map(len, comps))
    assert size_count == wanted, (budget, size_count)
    tar_summary[budget] = dict(sorted(size_count.items()))

# S5 orbit certificates for sensor subsets with at most 3 vertices.
index_v = {frozenset(x):i for i,x in enumerate(V)}
index_e = {e:i for i,e in enumerate(E)}
perm_maps = []
for pi in permutations(range(5)):
    vertex_map = [index_v[frozenset(pi[z] for z in x)] for x in V]
    perm_maps.append([index_e[tuple(sorted((vertex_map[a],vertex_map[b])))] for a,b in E])
assert len(perm_maps) == 120
orbit_certificate = {}
for k in (1,2,3):
    remains = set(combinations(range(N), k))
    found=[]
    while remains:
        rep=min(remains)
        orbit = {tuple(sorted(perm_map[i] for i in rep)) for perm_map in perm_maps}
        assert orbit <= remains
        remains -= orbit
        yes = pd[sum(1 << i for i in rep)]
        assert all(pd[sum(1 << i for i in x)] == yes for x in orbit)
        found.append([list(rep), len(orbit), bool(yes)])
    orbit_certificate[k] = found
assert len(orbit_certificate[1])==1 and len(orbit_certificate[2])==3 and len(orbit_certificate[3])==9

# For no four-element inclusion-minimal set, only examine 4 different omitted-symbol classes.
remains = {c for c in combinations(range(N),4) if len({missing[i] for i in c})==4}
four_class_orbits = []
while remains:
    rep=min(remains)
    orbit={tuple(sorted(p[i] for i in rep)) for p in perm_maps}
    assert orbit <= remains
    remains -= orbit
    yes = pd[sum(1<<i for i in rep)]
    tri_count = sum(pd[sum(1<<i for i in tri)] for tri in combinations(rep,3))
    assert all(pd[sum(1<<i for i in c)] == yes for c in orbit)
    assert all(sum(pd[sum(1<<i for i in tri)] for tri in combinations(c,3))==tri_count for c in orbit)
    assert yes == (tri_count > 0)
    four_class_orbits.append([list(rep),len(orbit),yes,tri_count])
assert len(four_class_orbits)==6

summary = {
    'underlying_petersen_vertices':len(V),'underlying_edges_and_line_vertices':N,
    'cycle_counts':dict(sorted(by_length.items())),
    'maximal_failed_sets_by_size':dict(sorted(Counter(m.bit_count() for m in max_failed).items())),
    'failed_count_by_size': {k: __import__('math').comb(N,k)-counts[k] for k in range(6)},
    'power_dominating_count_by_size':{k:counts[k] for k in range(16)},
    'minimal_sets_by_size':dict(sorted(Counter(m.bit_count() for m in minimal).items())),
    'optimal_token_jump_component_sizes':sorted(map(len,TJ)),
    'tar_component_distributions':tar_summary,
    'small_orbits':orbit_certificate,
    'four_distinct_class_orbits':four_class_orbits,
    'all_32768_masks_agree_between_direct_and_forest_checks':True
}
print(json.dumps(summary,sort_keys=True,indent=2))
