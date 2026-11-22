#!/usr/bin/env python3
"""Exhaustive check for optimal power domination and its exchange metrics on GP(12,5)."""
from collections import Counter, deque
from itertools import combinations
import json

N = 24
U = (1 << N) - 1
nbr = [0] * N

def link(a, b):
    nbr[a] |= 1 << b
    nbr[b] |= 1 << a

for i in range(12):
    link(i, (i + 1) % 12)
    link(i, 12 + i)
    link(12 + i, 12 + ((i + 5) % 12))
assert all(x.bit_count() == 3 for x in nbr)
assert sum(x.bit_count() for x in nbr) // 2 == 36

def dominates(mask):
    observed = mask
    bits = mask
    while bits:
        p = bits & -bits
        bits -= p
        observed |= nbr[p.bit_length() - 1]
    while observed != U:
        forced = 0
        bits = observed
        while bits:
            p = bits & -bits
            bits -= p
            unknown = nbr[p.bit_length() - 1] & (~observed)
            if unknown and (unknown & (unknown - 1)) == 0:
                forced |= unknown
        if not (forced & (~observed)):
            break
        observed |= forced
    return observed == U

small = []
for k in (1, 2, 3):
    good = []
    for c in combinations(range(N), k):
        m = sum(1 << v for v in c)
        if dominates(m):
            good.append(m)
    small.append(len(good))
    if good:
        break
assert small == [0, 0, 576], small
optima = good
index = {m: i for i, m in enumerate(optima)}
assert len(index) == 576

def exchange(slide):
    edge_list = set()
    for i, m in enumerate(optima):
        s = m
        while s:
            bit = s & -s
            s -= bit
            v = bit.bit_length() - 1
            choices = (nbr[v] if slide else U) & ~m
            while choices:
                b = choices & -choices
                choices -= b
                nxt = m ^ bit ^ b
                j = index.get(nxt)
                if j is not None:
                    edge_list.add((min(i, j), max(i, j)))
    adj = [[] for _ in optima]
    for i, j in sorted(edge_list):
        adj[i].append(j)
        adj[j].append(i)
    return adj, edge_list

slide, sedges = exchange(True)
jump, jedges = exchange(False)
assert len(sedges) == 1152 and len(jedges) == 6660
assert set(sedges) <= set(jedges)
assert Counter(map(len, slide)) == {4: 576}

def all_distances(graph):
    pair_dist = {}
    eccentricities = Counter()
    profile = Counter()
    for start in range(len(graph)):
        seen = [-1] * len(graph)
        seen[start] = 0
        que = deque((start,))
        while que:
            cur = que.popleft()
            for nxt in graph[cur]:
                if seen[nxt] < 0:
                    seen[nxt] = seen[cur] + 1
                    que.append(nxt)
        assert -1 not in seen
        eccentricities[max(seen)] += 1
        for target in range(start + 1, len(graph)):
            d = seen[target]
            pair_dist[start, target] = d
            profile[d] += 1
    assert len(pair_dist) == 576 * 575 // 2
    return pair_dist, dict(sorted(profile.items())), dict(sorted(eccentricities.items()))

d_slide, p_slide, ecc_slide = all_distances(slide)
d_jump, p_jump, ecc_jump = all_distances(jump)
assert ecc_slide == {9: 432, 10: 144}
assert ecc_jump == {4: 576}
assert p_slide == {1:1152,2:3456,3:8856,4:19368,5:32472,6:40464,7:37116,8:19296,9:3348,10:72}
assert p_jump == {1:6660,2:46800,3:110844,4:1296}
penalty = Counter(d_slide[pair] - d_jump[pair] for pair in d_slide)
assert dict(sorted(penalty.items())) == {0:7416,1:15192,2:30528,3:39312,4:43164,5:22860,6:6732,7:396}
assert sum(d_jump[p] == 3 for p in d_slide if d_slide[p] == 10) == 72
assert Counter((d_slide[p], d_jump[p]) for p in d_slide if d_slide[p]-d_jump[p]==7) == {(8,1):324,(10,3):72}
# Since GP(12,5) is bipartite, every slide reverses parity of occupied vertices in one part.
colors = [-1] * N
colors[0] = 0
queue = deque([0])
while queue:
    v = queue.popleft()
    bits = nbr[v]
    while bits:
        bit = bits & -bits
        bits -= bit
        w = bit.bit_length() - 1
        if colors[w] == -1:
            colors[w] = colors[v] ^ 1
            queue.append(w)
        else:
            assert colors[w] != colors[v]
assert -1 not in colors
part = sum(1 << v for v in range(N) if colors[v] == 1)
for a, b in sedges:
    assert ((optima[a] & part).bit_count() - (optima[b] & part).bit_count()) % 2 == 1
res = {
    'model': 'generalized_petersen_GP_12_5',
    'vertices': N, 'underlying_edges': 36,
    'successes_by_sensor_count_1_2_3': small, 'optimal_sets': len(optima),
    'jump_edges': len(jedges), 'jump_distance_counts': p_jump, 'jump_eccentricities': ecc_jump,
    'slide_edges': len(sedges), 'slide_distance_counts': p_slide, 'slide_eccentricities': ecc_slide,
    'slide_minus_jump_counts': dict(sorted(penalty.items())), 'max_slide_penalty': max(penalty),
    'slide_diameter_pairs': p_slide[10],
    'maximum_penalty_pair_types': {'eight_slides_one_jump':324,'ten_slides_three_jumps':72},
}
print(json.dumps(res, sort_keys=True, separators=(',', ':')))
