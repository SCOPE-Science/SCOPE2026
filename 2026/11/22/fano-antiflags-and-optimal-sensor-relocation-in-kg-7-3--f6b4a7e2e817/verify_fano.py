#!/usr/bin/env python3
"""Independent Steiner-design realization of minimum sensor configurations."""
from itertools import combinations, permutations

POINTS = frozenset(range(7))
VERTICES = tuple(frozenset(c) for c in combinations(range(7), 3))
INDEX = {v: i for i, v in enumerate(VERTICES)}
BASE = frozenset(map(frozenset, [(0,1,2),(0,3,4),(0,5,6),
                                   (1,3,5),(1,4,6),(2,3,6),(2,4,5)]))
assert len(BASE) == 7
for pair in combinations(range(7), 2):
    assert sum(frozenset(pair) <= block for block in BASE) == 1
planes = set()
for p in permutations(range(7)):
    planes.add(frozenset(frozenset(p[t] for t in block) for block in BASE))
assert len(planes) == 30
seen = {}
for plane in planes:
    for point in POINTS:
        pencil = [block for block in plane if point in block]
        assert len(pencil) == 3
        for other in plane:
            if point not in other:
                config = frozenset(pencil + [other])
                assert config not in seen, 'Fano completion not unique'
                seen[config] = (plane, point, other)
assert len(seen) == 840

# Verify the intrinsic pencil/transversal property without using graph algorithms.
for config, (_, center, transversal) in seen.items():
    pencil = [block for block in config if center in block]
    assert len(pencil) == 3 and all(len((pencil[i] & pencil[j])) == 1
                                         for i in range(3) for j in range(i+1,3))
    assert all(len(block & transversal) == 1 for block in pencil)

# Complementary transversals determine different Fano planes but the same pencil.
for config, (plane, center, transversal) in seen.items():
    pencil = frozenset(block for block in config if center in block)
    complement = POINTS.difference({center}).difference(transversal)
    other_config = frozenset(pencil | {complement})
    assert other_config in seen
    other_plane, same_center, other_line = seen[other_config]
    assert plane != other_plane and center == same_center
    assert other_line == complement
    assert frozenset(block for block in other_config if center in block) == pencil
print('PASS: 30 labelled Fano planes and 840 unique antiflags')
print('PASS: each optimum configuration has unique Fano completion')
print('PASS: complementary-transversal slide switches Fano plane, fixes pencil')
