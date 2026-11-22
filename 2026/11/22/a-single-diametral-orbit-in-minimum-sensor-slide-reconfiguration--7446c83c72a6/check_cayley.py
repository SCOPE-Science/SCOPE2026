#!/usr/bin/env python3
"""Independent set-based exhaustive verifier using the S4 star-transposition Cayley graph."""
from itertools import combinations, permutations
from collections import defaultdict, Counter, deque
import json

vertices = tuple(permutations(range(4)))
lookup = {p: i for i, p in enumerate(vertices)}
assert len(vertices) == 24
neighbors = [set() for _ in vertices]
for i, p in enumerate(vertices):
    for j in (1, 2, 3):
        q = list(p)
        q[0], q[j] = q[j], q[0]
        neighbors[i].add(lookup[tuple(q)])
assert all(len(x) == 3 for x in neighbors)
assert all(i in neighbors[j] for i, a in enumerate(neighbors) for j in a)

# Verify explicit Cayley-to-GP isomorphism as an independent model-identity check.
iso = [0,18,22,8,4,14,12,6,10,20,16,2,17,7,11,13,21,3,5,19,23,1,9,15]
assert sorted(iso) == list(range(24))
gp_neighbors = [set() for _ in range(24)]
def connect(a, b):
    gp_neighbors[a].add(b)
    gp_neighbors[b].add(a)
for a in range(12):
    connect(a, (a + 1) % 12)
    connect(a, a + 12)
    connect(a + 12, ((a + 5) % 12) + 12)
assert all({iso[j] for j in neighbors[i]} == gp_neighbors[iso[i]] for i in range(24))

# Sequential closure: unlike the bit-mask checker, force exactly one vertex per iteration.
def successful(chosen):
    known = set(chosen)
    for x in chosen:
        known.update(neighbors[x])
    while True:
        v = next((z for x in sorted(known) for z in sorted(neighbors[x] - known)
                  if len(neighbors[x] - known) == 1), None)
        if v is None:
            return len(known) == 24
        known.add(v)

counts = []
opt = []
for size in (1, 2, 3):
    sets = [frozenset(c) for c in combinations(range(24), size) if successful(c)]
    counts.append(len(sets))
    if sets:
        opt = sets
        break
assert counts == [0, 0, 576]
M = len(opt)
# Explicit all-pair relation, instead of generating moves from local masks.
adj_jump = [set() for _ in opt]
adj_slide = [set() for _ in opt]
for i in range(M):
    for j in range(i + 1, M):
        old, new = opt[i] - opt[j], opt[j] - opt[i]
        if len(old) == len(new) == 1:
            adj_jump[i].add(j)
            adj_jump[j].add(i)
            if next(iter(new)) in neighbors[next(iter(old))]:
                adj_slide[i].add(j)
                adj_slide[j].add(i)

def metrics(graph):
    profile, eprofile = Counter(), Counter()
    dists = {}
    for i in range(M):
        dist = {i: 0}
        queue = deque([i])
        while queue:
            x = queue.popleft()
            for y in graph[x]:
                if y not in dist:
                    dist[y] = dist[x] + 1
                    queue.append(y)
        assert len(dist) == M
        eprofile[max(dist.values())] += 1
        for j in range(i + 1, M):
            dists[i, j] = dist[j]
            profile[dist[j]] += 1
    return dists, dict(sorted(profile.items())), dict(sorted(eprofile.items()))

jd, jp, je = metrics(adj_jump)
sd, sp, se = metrics(adj_slide)
gaps = dict(sorted(Counter(sd[x] - jd[x] for x in sd).items()))
assert len(jd) == M * (M - 1) // 2
assert len(sd) == len(jd)
assert sum(map(len, adj_slide)) // 2 == 1152
assert sum(map(len, adj_jump)) // 2 == 6660
assert Counter(map(len, adj_slide)) == {4: 576}
assert sp == {1:1152,2:3456,3:8856,4:19368,5:32472,6:40464,7:37116,8:19296,9:3348,10:72}
assert jp == {1:6660,2:46800,3:110844,4:1296}
assert se == {9:432,10:144}
assert je == {4:576}
assert gaps == {0:7416,1:15192,2:30528,3:39312,4:43164,5:22860,6:6732,7:396}
assert all(jd[x] == 3 for x in sd if sd[x] == 10)
assert Counter((sd[x], jd[x]) for x in sd if sd[x]-jd[x]==7) == {(8,1):324,(10,3):72}
print(json.dumps({'model':'Cayley_S4_star_transpositions','isomorphism':'verified',
                  'successes_by_sensor_count_1_2_3':counts,'optimal_sets':M,
                  'jump_edges':sum(map(len,adj_jump))//2,'jump_distance_counts':jp,
                  'jump_eccentricities':je,'slide_edges':sum(map(len,adj_slide))//2,
                  'slide_distance_counts':sp,'slide_eccentricities':se,
                  'slide_minus_jump_counts':gaps,'max_slide_penalty':max(gaps),
                  'slide_diameter_pairs':sp[10],
                  'maximum_penalty_pair_types': {'eight_slides_one_jump':324,'ten_slides_three_jumps':72}},sort_keys=True,separators=(',',':')))
