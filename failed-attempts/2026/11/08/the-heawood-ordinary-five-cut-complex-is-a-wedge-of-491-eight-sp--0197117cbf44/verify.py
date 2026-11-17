#!/usr/bin/env python3
"""Standalone finite certificate for a five-cut complex of the Fano Levi graph.

Run with Python 3 and no nonstandard dependencies. All simplices and cover
relations are exhausted; the matching is generated deterministically.
"""
from collections import Counter, deque
from itertools import combinations
import hashlib
import struct

N, K = 14, 5
FULL = (1 << N) - 1
DIFFERENCES = (0, 1, 3)
EDGES = sorted((p, 7 + ((p + d) % 7)) for p in range(7) for d in DIFFERENCES)
NEIGHBORS = [0] * N
for a, b in EDGES:
    NEIGHBORS[a] |= 1 << b
    NEIGHBORS[b] |= 1 << a
assert len(EDGES) == 21
assert sorted(m.bit_count() for m in NEIGHBORS) == [3] * 14


def mask_of(vertices):
    return sum(1 << v for v in vertices)


def vertices(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def induced_edges(mask):
    return sum((NEIGHBORS[v] & mask).bit_count() for v in vertices(mask)) // 2


def is_connected(mask):
    if not mask:
        return False
    reached = mask & -mask
    while True:
        nxt = reached
        for v in vertices(reached):
            nxt |= NEIGHBORS[v] & mask
        if nxt == reached:
            return reached == mask
        reached = nxt


# Enumerate connected and disconnected five-sets two independent ways.
FIVE_SETS = [mask_of(c) for c in combinations(range(N), K)]
CONNECTED = [a for a in FIVE_SETS if is_connected(a)]
DISCONNECTED = [a for a in FIVE_SETS if not is_connected(a)]
assert set(CONNECTED) == {a for a in FIVE_SETS if induced_edges(a) == 4}
assert len(CONNECTED) == 252 and len(DISCONNECTED) == 1750
# Independently count 5-vertex induced paths (unique center) and the
# degree-(3,2,1,1,1) trees (unique branch vertex).
PATHS_5 = set()
BRANCHED_5 = set()
for center in range(N):
    around = list(vertices(NEIGHBORS[center]))
    for u, v in combinations(around, 2):
        for a in vertices(NEIGHBORS[u] ^ (1 << center)):
            for b in vertices(NEIGHBORS[v] ^ (1 << center)):
                PATHS_5.add(mask_of([center, u, v, a, b]))
    for arm in around:
        for tip in vertices(NEIGHBORS[arm] ^ (1 << center)):
            BRANCHED_5.add(mask_of([center, *around, tip]))
assert len(PATHS_5) == 168 and len(BRANCHED_5) == 84
assert PATHS_5.isdisjoint(BRANCHED_5) and PATHS_5 | BRANCHED_5 == set(CONNECTED)

# Full closure of facets, obtained independently of the face membership test.
FACETS = [FULL ^ a for a in DISCONNECTED]
FACES = {0}
for f in FACETS:
    sub = f
    while sub:
        FACES.add(sub)
        sub = (sub - 1) & f
assert len(FACES) == 14633

# Independent face test: the complement contains a disconnected five-set.
FIVE_DISCONNECTED = set(DISCONNECTED)
for s in range(1 << N):
    complement = FULL ^ s
    has_disconnected_five = False
    if complement.bit_count() >= K:
        vs = list(vertices(complement))
        for c in combinations(vs, K):
            if mask_of(c) in FIVE_DISCONNECTED:
                has_disconnected_five = True
                break
    assert (s in FACES) == has_disconnected_five, ('face mismatch', s)

F_VECTOR = tuple(Counter(s.bit_count() - 1 for s in FACES)[i] for i in range(-1, 9))
assert F_VECTOR == (1, 14, 91, 364, 1001, 2002, 3003, 3432, 2975, 1750)
assert all(s in FACES for s in range(1 << N) if s.bit_count() <= 7)

# The only missing eight-vertex faces are complements of induced six-cycles.
MISSING_EIGHT = {s for s in range(1 << N) if s.bit_count() == 8 and s not in FACES}
SIX_CYCLES = {
    s for s in range(1 << N) if s.bit_count() == 6 and is_connected(s)
    and induced_edges(s) == 6
    and all((NEIGHBORS[v] & s).bit_count() == 2 for v in vertices(s))
}
assert len(MISSING_EIGHT) == len(SIX_CYCLES) == 28
# A six-cycle corresponds to a noncollinear point triple of the Fano plane.
FANO_LINES = [{(i - d) % 7 for d in DIFFERENCES} for i in range(7)]
assert len(FANO_LINES) == 7
assert all(len(a & b) == 1 for a, b in combinations(FANO_LINES, 2))
assert all(sum(x in line and y in line for line in FANO_LINES) == 1
           for x, y in combinations(range(7), 2))
assert len([t for t in combinations(range(7), 3) if set(t) not in FANO_LINES]) == 28
assert MISSING_EIGHT == {FULL ^ s for s in SIX_CYCLES}
assert {s for s in range(1 << N) if s.bit_count() == 9 and s not in FACES} == set(FULL ^ a for a in CONNECTED)

# Staged elementary toggle matching, on NONEMPTY faces. Earlier stages
# remove matched pairs. Forman patchwork gives acyclicity; verified below
# without relying on the patchwork theorem.
remaining = set(FACES) - {0}
PAIRS = []
STAGES = []
for v in range(N):
    bit = 1 << v
    stage = [(s, s | bit) for s in sorted(remaining) if not (s & bit) and (s | bit) in remaining]
    assert all(a.bit_count() + 1 == b.bit_count() for a, b in stage)
    for a, b in stage:
        remaining.remove(a)
        remaining.remove(b)
    PAIRS.extend(stage)
    STAGES.append(len(stage))
assert len(PAIRS) == 7070
assert Counter(s.bit_count() - 1 for s in remaining) == Counter({0: 1, 8: 491})
assert remaining & {(1 << v) for v in range(N)} == {1}
assert sum(STAGES) == len(PAIRS)

# Independently check the ENTIRE directed Hasse graph: every normal cover
# upper -> lower, every paired cover lower -> upper. A topological order of
# all nodes is a complete acyclicity witness, not a time-limited search.
NONEMPTY = sorted(FACES - {0})
IDS = {s: i for i, s in enumerate(NONEMPTY)}
out = [[] for _ in NONEMPTY]
indeg = [0] * len(NONEMPTY)
paired = set(PAIRS)
covers = 0
for high in NONEMPTY:
    if high.bit_count() == 1:
        continue
    for v in vertices(high):
        low = high ^ (1 << v)
        assert low in IDS
        if (low, high) in paired:
            src, dst = IDS[low], IDS[high]
        else:
            src, dst = IDS[high], IDS[low]
        out[src].append(dst)
        indeg[dst] += 1
        covers += 1
queue = deque(i for i, d in enumerate(indeg) if d == 0)
processed = 0
while queue:
    u = queue.popleft()
    processed += 1
    for w in out[u]:
        indeg[w] -= 1
        if not indeg[w]:
            queue.append(w)
assert processed == len(NONEMPTY)
assert covers == sum((i + 1) * F_VECTOR[i + 1] for i in range(1, 9))

# Euler characteristic independently fixes sphere multiplicity.
reduced_euler = sum((-1 if i == 0 else (1 if (i - 1) % 2 == 0 else -1)) * f for i, f in enumerate(F_VECTOR))
assert reduced_euler == 491
matching_digest = hashlib.sha256(b''.join(struct.pack('<HH', a, b) for a, b in PAIRS)).hexdigest()
print('GRAPH vertices=14 edges=21 degree=3 incidence_difference_set=0,1,3')
print('FIVE_SETS connected=252 (paths=168, branched=84), disconnected=1750')
print('SIX_CYCLES 28; MISSING_EIGHT 28, exact complement correspondence')
print('FACE_VECTOR including_empty=', F_VECTOR)
print('FACES nonempty=14632, facets=1750')
print('TOGGLE_STAGES=', tuple(STAGES))
print('MORSE matched_pairs=7070 critical_0=1 critical_8=491 other=0')
print('HASSE incidences=', covers, 'acyclic_nodes=', processed)
print('REDUCED_EULER=', reduced_euler)
print('MATCHING_SHA256=', matching_digest)
print('VERIFY_OK HEAWOOD_FIVE_CUT_TOP_SPHERE_WEDGE')
