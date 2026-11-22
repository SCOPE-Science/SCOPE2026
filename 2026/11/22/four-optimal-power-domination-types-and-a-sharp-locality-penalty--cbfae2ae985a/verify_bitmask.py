"""Self-contained exhaustive certificate for optimal power-domination relocation on the Folkman graph."""
from itertools import combinations
from collections import Counter, deque
import json

PAIRS = list(combinations(range(5), 2))
EDGE_INDEX = {p: k + 10 for k, p in enumerate(PAIRS)}
N = [0] * 20
for k, (i, j) in enumerate(PAIRS, 10):
    for endpoint in (i, j):
        for twin in (0, 1):
            v = 2 * endpoint + twin
            N[k] |= 1 << v
            N[v] |= 1 << k
ALL = (1 << 20) - 1
assert all(x.bit_count() == 4 for x in N)
assert sum(x.bit_count() for x in N) // 2 == 40

def monitor(chosen):
    """Initial closed-neighborhood observation, followed by simultaneous unique-neighbor forcing."""
    known = chosen
    for v in range(20):
        if chosen >> v & 1:
            known |= N[v]
    while True:
        add = 0
        for v in range(20):
            if known >> v & 1:
                unknown = N[v] & ~known
                if unknown and unknown & (unknown - 1) == 0:
                    add |= unknown
        if add == 0:
            return known == ALL
        known |= add

def masks(k):
    for t in combinations(range(20), k):
        yield sum(1 << v for v in t)

counts = {k: sum(map(monitor, masks(k))) for k in range(5)}
assert counts == {0: 0, 1: 0, 2: 0, 3: 0, 4: 560}, counts
states = sorted(s for s in masks(4) if monitor(s))
state_index = {s: k for k, s in enumerate(states)}

def relabel(s, perm, flip_vertex_zero=False):
    out = 0
    for v in range(20):
        if not s >> v & 1:
            continue
        if v < 10:
            original = v // 2
            twin = v % 2
            if flip_vertex_zero and original == 0:
                twin ^= 1
            w = 2 * perm[original] + twin
        else:
            i, j = PAIRS[v - 10]
            w = EDGE_INDEX[tuple(sorted((perm[i], perm[j])))]
        out |= 1 << w
    return out

generators = [((1, 0, 2, 3, 4), False), ((1, 2, 3, 4, 0), False), (tuple(range(5)), True)]
def orbits(k):
    remaining = set(masks(k))
    result = []
    while remaining:
        seed = min(remaining)
        orbit = {seed}
        queue = [seed]
        for s in queue:
            for permutation, flip in generators:
                nxt = relabel(s, permutation, flip)
                if nxt not in orbit:
                    orbit.add(nxt)
                    queue.append(nxt)
        assert orbit <= remaining
        remaining -= orbit
        result.append((seed, orbit, monitor(seed)))
    return result
orbit_totals = {k: (len(orbits(k)), sum(flag for _, _, flag in orbits(k))) for k in range(5)}
assert orbit_totals == {0: (1, 0), 1: (2, 0), 2: (6, 0), 3: (16, 0), 4: (40, 4)}
success = sorted((len(o), tuple(v for v in range(20) if seed >> v & 1)) for seed, o, passed in orbits(4) if passed)
assert success == [(80, (4, 6, 8, 10)), (120, (6, 8, 10, 11)), (120, (8, 10, 12, 14)), (240, (0, 8, 12, 14))]

def reconfig(slide):
    adjacent = [set() for _ in states]
    for i, s in enumerate(states):
        for old in range(20):
            if not s >> old & 1:
                continue
            for new in range(20):
                if s >> new & 1 or (slide and not (N[old] >> new & 1)):
                    continue
                t = s ^ (1 << old) ^ (1 << new)
                j = state_index.get(t)
                if j is not None:
                    adjacent[i].add(j)
    assert all(i in adjacent[j] for i, nei in enumerate(adjacent) for j in nei)
    return adjacent

def all_distances(adj):
    distances = []
    histogram = Counter()
    ecc = Counter()
    for src in range(len(adj)):
        dist = [-1] * len(adj)
        dist[src] = 0
        q = deque([src])
        while q:
            v = q.popleft()
            for w in adj[v]:
                if dist[w] == -1:
                    dist[w] = dist[v] + 1
                    q.append(w)
        assert min(dist) >= 0
        ecc[max(dist)] += 1
        histogram.update(dist[src + 1:])
        distances.append(dist)
    return distances, histogram, ecc

jump = reconfig(False)
slide = reconfig(True)
dj, histj, eccj = all_distances(jump)
ds, hists, eccs = all_distances(slide)
assert sum(map(len, jump)) // 2 == 4680
assert sum(map(len, slide)) // 2 == 1920
assert Counter(map(len, jump)) == Counter({15:80, 16:120, 17:240, 18:120})
assert Counter(map(len, slide)) == Counter({4:240, 8:240, 12:80})
assert histj == Counter({1:4680, 2:22440, 3:64960, 4:64440})
assert hists == Counter({1:1920, 2:9000, 3:23760, 4:50280, 5:42240, 6:24700, 7:4080, 8:540})
assert eccj == Counter({4:560})
assert eccs == Counter({7:80, 8:480})
penalty = Counter()
type_of_max = Counter()
for i in range(len(states)):
    for j in range(i + 1, len(states)):
        delta = ds[i][j] - dj[i][j]
        assert delta >= 0
        penalty[delta] += 1
        if delta == 4:
            type_of_max[(dj[i][j], ds[i][j])] += 1
assert penalty == Counter({0:38400, 1:65940, 2:41400, 3:9460, 4:1320})
assert type_of_max == Counter({(2,6):780, (4,8):540})
center = {states[i] for i in range(len(states)) if max(ds[i]) == 7}
assert center == {s for s in states if (s & ((1 << 10) - 1)).bit_count() == 3}

summary = {
    'vertices':20, 'edges':40, 'monitor_counts_size_0_to_4':counts,
    'orbit_counts_size_0_to_4':orbit_totals, 'successful_orbits':success,
    'jump_edges':4680, 'slide_edges':1920,
    'jump_degree_hist':dict(sorted(Counter(map(len,jump)).items())),
    'slide_degree_hist':dict(sorted(Counter(map(len,slide)).items())),
    'jump_distance_hist':dict(sorted(histj.items())),
    'slide_distance_hist':dict(sorted(hists.items())),
    'jump_eccentricity_hist':dict(sorted(eccj.items())),
    'slide_eccentricity_hist':dict(sorted(eccs.items())),
    'penalty_hist':dict(sorted(penalty.items())),
    'max_penalty_distance_types':{f'{a},{b}':v for (a,b),v in sorted(type_of_max.items())},
    'central_states':len(center)
}
print(json.dumps(summary, sort_keys=True))
