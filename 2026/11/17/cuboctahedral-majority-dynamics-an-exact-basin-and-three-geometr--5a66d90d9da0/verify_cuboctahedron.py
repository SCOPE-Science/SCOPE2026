#!/usr/bin/env python3
"""Complete, dependency-free binary majority census on the cuboctahedral graph L(Q3)."""
from collections import Counter
from itertools import permutations

EDGES = tuple((v, v ^ (1 << j)) for v in range(8) for j in range(3) if v < (v ^ (1 << j)))
assert len(EDGES) == 12 and len(set(EDGES)) == 12
NEIGHBORS = tuple(tuple(j for j, f in enumerate(EDGES) if i != j and len(set(e) & set(f)) == 1) for i, e in enumerate(EDGES))
assert all(len(n) == 4 for n in NEIGHBORS)

def update(x):
    out = 0
    for i, ns in enumerate(NEIGHBORS):
        s = sum((x >> j) & 1 for j in ns)
        if s >= 3 or (s == 2 and (x & (1 << i))):
            out |= 1 << i
    return out

SIZE = 1 << 12
F = tuple(update(x) for x in range(SIZE))
assert all(update(x) == F[x] for x in range(SIZE))
assert all(F[F[F[F[F[F[x]]]]]] == F[F[F[F[x]]]] for x in range(SIZE))
PERIODIC = frozenset(x for x in range(SIZE) if F[F[x]] == x)
FIXED = frozenset(x for x in PERIODIC if F[x] == x)
TWOCYCLES = frozenset(tuple(sorted((x, F[x]))) for x in PERIODIC if F[x] != x)
assert len(FIXED) == 146 and len(TWOCYCLES) == 20 and len(PERIODIC) == 186
INDEGREE = Counter(F)
assert all(INDEGREE[x] == 1 for x in PERIODIC if F[x] != x)

entry = Counter()
period_entry = Counter()
basins = Counter()
first_max = None
for x in range(SIZE):
    v = x
    for t in range(5):
        if v in PERIODIC:
            length = 1 if v in FIXED else 2
            orbit = (v,) if length == 1 else tuple(sorted((v, F[v])))
            entry[t] += 1
            period_entry[(t, length)] += 1
            basins[orbit] += 1
            if t == 4 and first_max is None:
                first_max = x
            break
        v = F[v]
    else:
        raise AssertionError('Unclassified state: ' + str(x))
assert entry == {0: 186, 1: 1606, 2: 1200, 3: 1008, 4: 96}
assert all(basins[o] == 2 for o in TWOCYCLES)
assert Counter(basins[(x,)] for x in FIXED) == {1: 8, 5: 12, 6: 24, 8: 48, 10: 24, 11: 12, 64: 16, 1032: 2}

# Every automorphism of the cube is a translation followed by a coordinate permutation.
EDGE_INDEX = {e: i for i, e in enumerate(EDGES)}
AUT = set()
for perm in permutations(range(3)):
    for shift in range(8):
        def vertex_image(v):
            return shift ^ sum(((v >> j) & 1) << perm[j] for j in range(3))
        p = tuple(EDGE_INDEX[tuple(sorted((vertex_image(a), vertex_image(b))))] for a, b in EDGES)
        assert all(set(p[j] for j in ns) == set(NEIGHBORS[p[i]]) for i, ns in enumerate(NEIGHBORS))
        AUT.add(p)
assert len(AUT) == 48

def image(x, p):
    return sum(1 << p[i] for i in range(12) if x & (1 << i))

def classes(things, action):
    todo = set(things)
    output = []
    while todo:
        a = min(todo)
        orbit = set(action(a, p) for p in AUT)
        assert orbit <= todo
        output.append((a, len(orbit)))
        todo -= orbit
    return output

fclasses = classes(FIXED, lambda x, p: image(x, p))
cclasses = classes(TWOCYCLES, lambda pair, p: tuple(sorted((image(pair[0], p), image(pair[1], p)))))
assert len(fclasses) == 14 and len(cclasses) == 3
assert sorted(n for _, n in cclasses) == [6, 6, 8]
assert Counter((x ^ y).bit_count() for x, y in TWOCYCLES) == {6: 8, 8: 12}
assert all(x.bit_count() == 6 and y.bit_count() == 6 for x, y in TWOCYCLES)
assert first_max == 348

print('GRAPH=L(Q3) V=12 E=24 DEGREE=4 CUBE_EDGES=' + repr(EDGES))
print('STATE_SPACE=4096 EXACT_ALL_STATES=YES')
print('FIXED=146 PRIMITIVE_TWO_CYCLES=20 RECURRENT_STATES=186')
print('ENTRY_BY_TIME=' + repr(sorted(entry.items())))
print('ENTRY_BY_TIME_AND_PERIOD=' + repr(sorted(period_entry.items())))
print('FIXED_BASIN_SIZE_COUNTS=' + repr(sorted(Counter(basins[(x,)] for x in FIXED).items())))
print('TWO_CYCLE_BASIN_SIZE_COUNTS=' + repr(sorted(Counter(basins[o] for o in TWOCYCLES).items())))
print('TWO_CYCLE_FLIPS=' + repr(sorted(Counter((x ^ y).bit_count() for x, y in TWOCYCLES).items())))
print('ALL_40_TWO_CYCLE_STATES_HAVE_EXACTLY_ONE_INCOMING_EDGE=YES')
print('AUTOMORPHISM_GROUP_SIZE=48 FIXED_GEOMETRIC_CLASSES=14 TWO_CYCLE_GEOMETRIC_CLASSES=3')
print('FIXED_CLASS_REPRESENTATIVES_AND_SIZES=' + repr(fclasses))
print('TWO_CYCLE_CLASS_REPRESENTATIVES_AND_SIZES=' + repr(cclasses))
print('F6_EQUALS_F4=YES SHARP_FIRST_ENTRY_TIME=4 WITNESS=348')
print('CENSUS_VALIDATED=YES')
