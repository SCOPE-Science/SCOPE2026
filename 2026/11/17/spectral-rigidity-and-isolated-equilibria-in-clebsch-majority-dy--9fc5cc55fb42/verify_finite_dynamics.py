#!/usr/bin/env python3
"""Exhaustive functional digraph certificate for majority on the 5-regular folded 5-cube."""
import json
from collections import Counter, deque

N = 16
TOTAL = 1 << N
SHIFTS = (1, 2, 4, 8, 15)
NEIGHBOR_MASKS = [sum(1 << (v ^ s) for s in SHIFTS) for v in range(N)]
assert all(mask.bit_count() == 5 for mask in NEIGHBOR_MASKS)

# Independent of any group-classification data: exactly the majority rule.
def update(state):
    result = 0
    for v in range(N):
        if (state & NEIGHBOR_MASKS[v]).bit_count() >= 3:
            result |= 1 << v
    return result

next_state = [update(x) for x in range(TOTAL)]
indegree = [0] * TOTAL
for y in next_state:
    indegree[y] += 1
queue = deque(x for x in range(TOTAL) if not indegree[x])
removed = []
while queue:
    x = queue.popleft()
    removed.append(x)
    y = next_state[x]
    indegree[y] -= 1
    if indegree[y] == 0:
        queue.append(y)
# Remaining states form disjoint directed cycles.
period = [0] * TOTAL
entry = [-1] * TOTAL
root = [-1] * TOTAL
cycles = []
for start in range(TOTAL):
    if indegree[start] <= 0 or period[start]:
        continue
    orbit = []
    y = start
    while not period[y]:
        orbit.append(y)
        period[y] = -1
        y = next_state[y]
    assert y == start
    L = len(orbit)
    rep = min(orbit)
    cycles.append(orbit)
    for z in orbit:
        period[z] = L
        entry[z] = 0
        root[z] = rep
for x in reversed(removed):
    y = next_state[x]
    assert entry[y] >= 0
    entry[x] = entry[y] + 1
    period[x] = period[y]
    root[x] = root[y]
assert all(0 <= e <= 4 for e in entry)
assert set(period) == {1, 2}
assert len(removed) + sum(map(len, cycles)) == TOTAL
assert all(next_state[next_state[next_state[next_state[next_state[next_state[x]]]]]] == next_state[next_state[next_state[next_state[x]]]] for x in range(TOTAL))
periodic_orbits = Counter(len(o) for o in cycles)
layer_census = Counter((entry[x], period[x]) for x in range(TOTAL))
basin_size = Counter(root)
basin_spectrum = Counter((period[r], n) for r, n in basin_size.items())
flips = Counter((next_state[o[0]] ^ o[0]).bit_count() for o in cycles if len(o) == 2)
fixed_weights = Counter(o[0].bit_count() for o in cycles if len(o) == 1)
result = {
    'graph': 'Clebsch graph, F_2^4 with generator set {1,2,4,8,15}',
    'vertices': 16, 'states_exhaustively_checked': TOTAL,
    'periodic_orbits': dict(sorted(periodic_orbits.items())),
    'first_entry_by_eventual_period': [
       [t, p, layer_census[(t,p)]] for t in range(5) for p in (1,2)
    ],
    'attractor_basin_sizes': [[p,b,n] for (p,b),n in sorted(basin_spectrum.items())],
    'primitive_two_cycle_flip_sizes': dict(sorted(flips.items())),
    'fixed_weight_histogram': dict(sorted(fixed_weights.items())),
    'max_first_entry': max(entry),
    'periodic_states': sum(len(o) for o in cycles),
}
assert periodic_orbits == {1: 142, 2: 1165}
assert layer_census == {(0,1):142,(0,2):2330,(1,1):2616,(1,2):14720,
                         (2,1):11264,(2,2):23680,(3,1):8864,(4,1):1920}
assert basin_spectrum == {(1,1):140,(1,12333):2,(2,2):40,(2,4):240,(2,8):480,
                          (2,10):120,(2,42):240,(2,462):40,(2,1218):5}
assert flips == {8:160,10:240,12:720,16:45}
assert fixed_weights == {0:1,8:140,16:1}
print(json.dumps(result, sort_keys=True, indent=2))
