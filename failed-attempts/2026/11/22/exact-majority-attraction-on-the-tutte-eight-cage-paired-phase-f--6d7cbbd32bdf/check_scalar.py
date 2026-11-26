#!/usr/bin/env python3
"""Alternative scalar bit-by-bit census for the 30-vertex cubic girth-eight graph.

Builds all perfect matchings from permutations, then evaluates majority by
integer neighbor counts, not the bitwise formula of the other certificate.
"""
from collections import Counter
from itertools import combinations, permutations
import json

N = 1 << 15
EDGES = sorted(combinations(range(6), 2))
E_INDEX = {edge: i for i, edge in enumerate(EDGES)}
SYNTHEMES = sorted({tuple(sorted(tuple(sorted(p[i:i + 2])) for i in (0, 2, 4))) for p in permutations(range(6))})
assert len(EDGES) == len(SYNTHEMES) == 15
L_NEIGH = [[E_INDEX[e] for e in m] for m in SYNTHEMES]
P_NEIGH = [[j for j, m in enumerate(SYNTHEMES) if e in m] for e in EDGES]
assert sum(map(len, L_NEIGH)) == sum(map(len, P_NEIGH)) == 45


def majority(source_bits, destinations):
    out = 0
    for position, neighbours in enumerate(destinations):
        votes = sum((source_bits >> j) % 2 for j in neighbours)
        if votes > len(neighbours) // 2:
            out += 1 << position
    return out


# All 32,768 line-to-point and point-to-line majority maps are evaluated
# directly from graph incidence, without any vectorization or imported data.
A = [majority(v, P_NEIGH) for v in range(N)]
B = [majority(v, L_NEIGH) for v in range(N)]
T = [A[B[v]] for v in range(N)]
S = [B[A[v]] for v in range(N)]
assert all(T[T[T[v]]] == T[T[v]] and S[S[S[v]]] == S[S[v]] for v in range(N))

pt_end = [T[T[v]] for v in range(N)]
ln_end = [S[S[v]] for v in range(N)]
count_pt = Counter(pt_end)
count_ln = Counter(ln_end)
assert len(count_pt) == len(count_ln) == 2386
paired = Counter((count_pt[phase], count_ln[B[phase]]) for phase in count_pt)
assert paired == {
    (1, 1): 144, (3, 3): 720, (5, 5): 720, (6, 6): 360,
    (22, 38): 120, (38, 22): 120, (42, 42): 180,
    (58, 58): 20, (4392, 4392): 2,
}

# An alternative way to obtain basin counts is to traverse the actual fixed
# point phase labels and accumulate exact pairwise orbit weights.
fixed = Counter(count_pt[p] * count_ln[B[p]] for p in count_pt)
cyclic = Counter()
phases = sorted(count_pt)
for pos, a in enumerate(phases):
    for b in phases[pos+1:]:
        cyclic[count_pt[a] * count_ln[B[b]] + count_pt[b] * count_ln[B[a]]] += 1
assert len(fixed) == 8 and len(cyclic) == 36
assert sum(fixed.values()) == 2386
assert sum(cyclic.values()) == 2845305
assert sum(k * n for k, n in fixed.items()) + sum(k * n for k, n in cyclic.items()) == N*N

# Separable one-step transformation: generate the actual F^t coordinate
# functions as lists of maps on a single shore, then count their possible
# periodic images; no enumeration of the 2^30 pairs is required.
ximage = list(range(N)); yimage = list(range(N))
by_time = []
for t in range(5):
    already_x = sum(T[v] == v for v in ximage)
    already_y = sum(S[v] == v for v in yimage)
    by_time.append(already_x * already_y)
    ximage, yimage = [A[v] for v in yimage], [B[v] for v in ximage]
assert by_time == [5692996, 282508864, 635443264, 816130624, 1073741824]

# Direct full-graph trajectories of selected states verify the phase-level
# interpretation, including a state attaining sharp entry time four.
def step(state):
    p, l = state
    return A[l], B[p]
def entry_time(state):
    for t in range(5):
        next1 = step(state)
        if step(next1) == state:
            return t
        state = next1
    raise AssertionError('no periodic entry by four')
assert entry_time((106, 0)) == 4
for j in range(0, N, 73):
    assert entry_time((j, (j * 117 + 19) % N)) <= 4
print(json.dumps({'phase_count':len(count_pt),'paired_fiber_types':sorted([list(k)+[v] for k,v in paired.items()]), 'fixed_basin_types':len(fixed),'two_basin_types':len(cyclic),'fixed_orbits':sum(fixed.values()),'two_orbits':sum(cyclic.values()),'periodic_by_update':by_time,'witness': [106,0]},indent=2))
