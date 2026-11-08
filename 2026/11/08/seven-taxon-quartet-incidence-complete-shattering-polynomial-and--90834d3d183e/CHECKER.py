"""Exact finite enumeration for quartet-query shattering on seven leaves.

All tree generation, quartet traces, complete-search and orbit calculations
use integer arithmetic; no external libraries or stored tables are required.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations

N = 7
LEAVES = tuple(range(N))
UNIVERSE = (1 << N) - 1


def canon_quartet(u, v):
    return tuple(sorted((tuple(sorted(u)), tuple(sorted(v)))))


QUARTETS = tuple(
    canon_quartet(u, v)
    for a, b, c, d in combinations(LEAVES, 4)
    for u, v in (((a, b), (c, d)), ((a, c), (b, d)), ((a, d), (b, c)))
)
QINDEX = {q: i for i, q in enumerate(QUARTETS)}
assert len(QINDEX) == 105


# Method A: recursively enumerate full rooted binary hierarchies on leaves
# 1,...,6, rooting the unrooted tree at leaf 0. Every nonroot cluster of
# size at least two is an internal split avoiding leaf 0.
@lru_cache(None)
def hierarchies(mask):
    if mask.bit_count() == 1:
        return (frozenset(),)
    pivot = mask & -mask
    out = []
    for sub in range(1, mask):
        if sub & ~mask or not (sub & pivot) or sub == mask:
            continue
        other = mask ^ sub
        for left in hierarchies(sub):
            for right in hierarchies(other):
                out.append(frozenset(left | right | {mask}))
    return tuple(out)


root_mask = UNIVERSE ^ 1
TREE_SPLITS = tuple(frozenset(s - {root_mask}) for s in hierarchies(root_mask))
assert len(TREE_SPLITS) == len(set(TREE_SPLITS)) == 945
assert all(len(t) == 4 for t in TREE_SPLITS)


def displays_split(t, q):
    (a, b), (c, d) = q
    return any(
        ((m >> a) & 1) == ((m >> b) & 1)
        and ((m >> c) & 1) == ((m >> d) & 1)
        and ((m >> a) & 1) != ((m >> c) & 1)
        for m in t
    )


Q_BITS = tuple(
    sum(1 << i for i, t in enumerate(TREE_SPLITS) if displays_split(t, q))
    for q in QUARTETS
)
FULL = (1 << len(TREE_SPLITS)) - 1
assert all(x.bit_count() == 315 for x in Q_BITS)


# Method B: independently generate the unrooted trees by leaf insertion and
# independently test quartets by the four-point tree-distance criterion.
def edge_tree_generation(n):
    trees = [tuple(sorted((tuple(sorted(edge)) for edge in ((0, -1), (1, -1), (2, -1)))))]
    for m in range(3, n):
        new_trees = []
        internal = 1 - m
        for tree in trees:
            for a, b in tree:
                e = (a, b)
                replacement = [f for f in tree if f != e]
                replacement += [(a, internal), (b, internal), (m, internal)]
                new_trees.append(tuple(sorted(tuple(sorted(f)) for f in replacement)))
        trees = new_trees
    return trees


def tree_distances(t):
    graph = {}
    for a, b in t:
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)
    distance = {}
    for leaf in LEAVES:
        dist = {leaf: 0}
        queue = [leaf]
        for x in queue:
            for y in graph[x]:
                if y not in dist:
                    dist[y] = dist[x] + 1
                    queue.append(y)
        for target in LEAVES:
            distance[leaf, target] = dist[target]
    return distance


def displayed_by_distance(dist, q):
    (a, b), (c, d) = q
    return (dist[a,b] + dist[c,d] < dist[a,c] + dist[b,d]
            and dist[a,b] + dist[c,d] < dist[a,d] + dist[b,c])


def edge_split_set(tree):
    graph = {}
    for a, b in tree:
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)
    out = set()
    for a, b in tree:
        seen = {a}
        queue = [a]
        for x in queue:
            for y in graph[x]:
                if (x == a and y == b) or (x == b and y == a) or y in seen:
                    continue
                seen.add(y)
                queue.append(y)
        mask = sum(1 << x for x in seen if 0 <= x < N)
        if mask & 1:
            mask = UNIVERSE ^ mask
        if 2 <= mask.bit_count() <= N-2:
            out.add(mask)
    return frozenset(out)


EDGE_TREES = edge_tree_generation(N)
assert len(EDGE_TREES) == 945
by_split = {edge_split_set(t): t for t in EDGE_TREES}
assert len(by_split) == 945 and set(by_split) == set(TREE_SPLITS)
for splitset, tree in by_split.items():
    dist = tree_distances(tree)
    for q in QUARTETS:
        assert displays_split(splitset, q) == displayed_by_distance(dist, q)


# Exact depth-first search over all shattered supports containing query 0.
# Extension by a query succeeds iff it splits every existing trace cell.
COUNTS = Counter({1: 1})
EXAMPLES = {1: (0,)}
TOP = []
EXPLORED = 0


def explore(cells, next_q, chosen):
    global EXPLORED
    EXPLORED += 1
    if len(chosen) == 6:
        TOP.append(chosen)
    for idx in range(next_q, len(QUARTETS)):
        posmask = Q_BITS[idx]
        newcells = []
        for cell in cells:
            pos = cell & posmask
            if not pos or pos == cell:
                break
            newcells.extend((pos, cell ^ pos))
        else:
            k = len(chosen) + 1
            COUNTS[k] += 1
            EXAMPLES.setdefault(k, chosen + (idx,))
            explore(tuple(newcells), idx + 1, chosen + (idx,))


explore((Q_BITS[0], FULL ^ Q_BITS[0]), 1, (0,))
assert EXPLORED == 206992
assert [COUNTS[i] for i in range(1,8)] == [1, 102, 4887, 125928, 75570, 504, 0]
COEFFICIENTS = [1] + [(105*COUNTS[k])//k for k in range(1,8)]
assert COEFFICIENTS == [1,105,5355,171045,3305610,1586970,8820,0]
assert all(105*COUNTS[k] % k == 0 for k in range(1,8))
assert len(TOP) == 504


# Every relabeling permutes quartet queries. The 504 extremal supports with
# query zero partition into 3 relabeling orbits with full sizes below.
PERM_MAPS = []
for p in permutations(LEAVES):
    PERM_MAPS.append(tuple(
        QINDEX[canon_quartet((p[a],p[b]),(p[c],p[d]))]
        for (a,b),(c,d) in QUARTETS
    ))
remaining = set(TOP)
ORBIT_SIZES = []
ORBIT_SEEDS = []
while remaining:
    seed = min(remaining)
    orbit = {
        tuple(sorted(mapping[i] for i in seed))
        for mapping in PERM_MAPS
    }
    local = {s for s in orbit if s[0] == 0}
    assert local <= remaining
    ORBIT_SIZES.append(len(orbit))
    ORBIT_SEEDS.append(seed)
    remaining -= local
assert sorted(ORBIT_SIZES) == [1260, 2520, 5040]
assert sum(ORBIT_SIZES) == 8820


# Explicit 64-pattern certificate for one six-query shattered support.
CERT_QUERY_INDICES = (0,21,42,54,76,82)
CERT_QUARTETS = tuple(QUARTETS[i] for i in CERT_QUERY_INDICES)
WITNESSES = {}
for t in TREE_SPLITS:
    pattern = sum(1 << j for j, qi in enumerate(CERT_QUERY_INDICES)
                  if displays_split(t, QUARTETS[qi]))
    WITNESSES.setdefault(pattern, tuple(sorted(t)))
assert len(WITNESSES) == 64
for pattern, splits in WITNESSES.items():
    assert len(splits) == 4
    actual = sum(1 << j for j, q in enumerate(CERT_QUARTETS)
                 if displays_split(splits, q))
    assert actual == pattern


print('QUARTET7_PASS trees=945 queries=105 searched=206992')
print('face_coefficients=', COEFFICIENTS)
print('six_support_orbits=', sorted(ORBIT_SIZES))
print('six_query_witnesses=', len(WITNESSES))
print('certificate_query_indices=', CERT_QUERY_INDICES)
print('quartets=', CERT_QUARTETS)


def small_profile(n):
    # Full direct combinations, without the fixed-query symmetry reduction.
    leafset = tuple(range(n))
    out_queries = tuple(
        canon_quartet(u, v)
        for a,b,c,d in combinations(leafset,4)
        for u,v in (((a,b),(c,d)),((a,c),(b,d)),((a,d),(b,c)))
    )
    univ = (1<<n)-1
    root = univ^1
    h = [frozenset(T-{root}) for T in hierarchies(root)]
    bits = [sum(1<<i for i,t in enumerate(h) if displays_split(t,q))
            for q in out_queries]
    full = (1<<len(h))-1
    count = []
    for k in range(1,5):
        v = 0
        for choice in combinations(range(len(bits)),k):
            cells = (full,)
            for idx in choice:
                next_cells = []
                for c in cells:
                    pos = c & bits[idx]
                    if not pos or pos==c:
                        break
                    next_cells.extend((pos,c^pos))
                else:
                    cells = tuple(next_cells)
                    continue
                break
            else:
                v += 1
        count.append(v)
    return count

assert small_profile(4) == [3,0,0,0]
assert small_profile(5) == [15,90,0,0]
assert small_profile(6) == [45,945,10665,0]
print('small_VC=[1,2,3] for n=[4,5,6]')

# Check that the separately embedded readable witness file is the exact
# certificate advertised in the mathematical exposition.
import json
from pathlib import Path
certificate = json.loads(Path(__file__).with_name('WITNESSES.json').read_text('utf-8'))
assert certificate['query_indices'] == list(CERT_QUERY_INDICES)
assert len(certificate['witnesses']) == 64
for s, splits in certificate['witnesses'].items():
    target = int(s)
    assert sorted(splits) in [list(sorted(T)) for T in TREE_SPLITS]
    observed = sum(1 << j for j, q in enumerate(CERT_QUARTETS)
                   if displays_split(splits, q))
    assert observed == target
print('external_witness_file=64_verified')
