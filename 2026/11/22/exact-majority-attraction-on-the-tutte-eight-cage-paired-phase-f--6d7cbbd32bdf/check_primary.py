#!/usr/bin/env python3
"""Exact phase and basin certificate for open-neighbor majority on the Tutte eight-cage.

Requires Python 3 standard library only. Enumerates all 2**15 configurations on
both incidence shores, not the infeasible 2**30 Cartesian product.
"""
from collections import Counter
from itertools import combinations
import json

SIDE = 15
SIZE = 1 << SIDE
PAIRS = tuple(combinations(range(6), 2))
PAIR_IDS = {p: k for k, p in enumerate(PAIRS)}


def matchings(remaining):
    if not remaining:
        yield ()
        return
    first, *rest = remaining
    for j, second in enumerate(rest):
        for tail in matchings(rest[:j] + rest[j + 1:]):
            yield ((first, second),) + tail


LINES = tuple(sorted(matchings(list(range(6)))))
assert len(PAIRS) == len(LINES) == 15
P_ADJ = tuple(tuple(j for j, line in enumerate(LINES) if pair in line) for pair in PAIRS)
L_ADJ = tuple(tuple(PAIR_IDS[pair] for pair in line) for line in LINES)
assert all(len(row) == 3 for row in P_ADJ + L_ADJ)


def table(adjacency):
    output = [0] * SIZE
    for s in range(SIZE):
        val = 0
        for i, (a, b, c) in enumerate(adjacency):
            abit = (s >> a) & 1
            bbit = (s >> b) & 1
            cbit = (s >> c) & 1
            val |= ((abit & bbit) | (abit & cbit) | (bbit & cbit)) << i
        output[s] = val
    return output


P = table(P_ADJ)  # fifteen line bits -> fifteen point bits
L = table(L_ADJ)  # fifteen point bits -> fifteen line bits
T = [P[L[s]] for s in range(SIZE)]
U = [L[P[s]] for s in range(SIZE)]
assert all(T[T[T[s]]] == T[T[s]] and U[U[U[s]]] == U[U[s]] for s in range(SIZE))
phase_p = [T[T[s]] for s in range(SIZE)]
phase_l = [U[U[s]] for s in range(SIZE)]
wp = Counter(phase_p)
wl = Counter(phase_l)
assert set(wp) == {s for s in range(SIZE) if T[s] == s}
assert set(wl) == {s for s in range(SIZE) if U[s] == s}
assert len(wp) == len(wl) == 2386
assert {L[s] for s in wp} == set(wl)
assert all(P[L[s]] == s for s in wp)
PAIR_TYPES = Counter((wp[s], wl[L[s]]) for s in wp)
EXPECTED = {
    (1, 1): 144, (3, 3): 720, (5, 5): 720, (6, 6): 360,
    (22, 38): 120, (38, 22): 120, (42, 42): 180,
    (58, 58): 20, (4392, 4392): 2,
}
assert PAIR_TYPES == EXPECTED, (PAIR_TYPES, EXPECTED)

# A two-cycle between distinct phase labels i,j has two F^2-fixed phases.
# Their preimage products add to a single orbit basin.
fixed_basins = Counter({a * b: 0 for a, b in PAIR_TYPES})
cycle_basins = Counter()
types = sorted(PAIR_TYPES.items())
for idx, ((a, b), n) in enumerate(types):
    fixed_basins[a * b] += n
    cycle_basins[2 * a * b] += n * (n - 1) // 2
    for (c, d), m in types[idx + 1:]:
        cycle_basins[a * d + c * b] += n * m

assert sum(fixed_basins.values()) == 2386
assert sum(cycle_basins.values()) == 2845305
assert sum(k * v for k, v in fixed_basins.items()) + sum(k * v for k, v in cycle_basins.items()) == SIZE ** 2
assert fixed_basins == {1: 144, 9: 720, 25: 720, 36: 360, 836: 240, 1764: 180, 3364: 20, 19289664: 2}
assert max(cycle_basins) == 38579328 and cycle_basins[38579328] == 1

# F^t has separated coordinates on the two shores. Even times give maps
# of their own initial shore; odd times exchange dependencies. The product
# below counts exact states already periodic after t updates.
point_map = list(range(SIZE))
line_map = list(range(SIZE))
periodic_by_t = []
for t in range(5):
    count_p = sum(T[v] == v for v in point_map)
    count_l = sum(U[v] == v for v in line_map)
    periodic_by_t.append(count_p * count_l)
    point_map, line_map = [P[v] for v in line_map], [L[v] for v in point_map]
assert periodic_by_t == [5692996, 282508864, 635443264, 816130624, 1073741824]
entries = [periodic_by_t[0]] + [periodic_by_t[i] - periodic_by_t[i - 1] for i in range(1, 5)]
assert entries == [5692996, 276815868, 352934400, 180687360, 257611200]

# An explicit labelled witness proves the fourth update is sometimes needed.
assert U[L[T[106]]] != L[T[106]]
assert T[T[106]] == 0

report = {
    'vertex_count': 30,
    'state_count': SIZE ** 2,
    'point_phase_count': len(wp),
    'line_phase_count': len(wl),
    'paired_fiber_types': [[a, b, PAIR_TYPES[a, b]] for a, b in sorted(PAIR_TYPES)],
    'fixed_orbits': sum(fixed_basins.values()),
    'two_orbits': sum(cycle_basins.values()),
    'fixed_basin_spectrum': [[k, v] for k, v in sorted(fixed_basins.items())],
    'two_basin_spectrum': [[k, v] for k, v in sorted(cycle_basins.items())],
    'periodic_by_update': periodic_by_t,
    'first_periodic_entry_counts': entries,
    'sharp_entry_time': 4,
    'explicit_four_step_witness': {'point_bits': 106, 'line_bits': 0},
}
print(json.dumps(report, sort_keys=True, indent=2))
