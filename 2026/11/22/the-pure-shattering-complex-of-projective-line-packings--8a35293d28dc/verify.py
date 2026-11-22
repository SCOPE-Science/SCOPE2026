"""Self-contained exact check of the binary projective packing shattering theorem.

Run: python3 verify.py. Standard Python library only.
"""
from collections import Counter
from itertools import combinations

# Projective points are the fifteen nonzero vectors of F_2^4.
points = range(1, 16)
lines = sorted({tuple(sorted((a, b, a ^ b))) for a, b in combinations(points, 2)})
assert len(lines) == 35
line_point_masks = [sum(1 << p for p in l) for l in lines]

# Enumerate all unordered exact covers of the 15 points by five lines.
spreads = []
def spread_cover(remaining, selected):
    if remaining == 0:
        spreads.append(tuple(sorted(selected)))
        return
    p = (remaining & -remaining).bit_length() - 1
    for i, mask in enumerate(line_point_masks):
        if (mask & (1 << p)) and (mask & remaining) == mask:
            spread_cover(remaining ^ mask, selected + [i])
spread_cover(sum(1 << p for p in points), [])
spreads = sorted(set(spreads))
assert len(spreads) == 56 and all(len(s) == 5 for s in spreads)
spread_line_masks = [sum(1 << i for i in s) for s in spreads]
through_line = [tuple(i for i, s in enumerate(spread_line_masks)
                      if (s >> l) & 1) for l in range(35)]

# Enumerate all unordered exact covers of 35 lines by seven spreads.
packings = []
def packing_cover(remaining, selected):
    if remaining == 0:
        packings.append(tuple(sorted(selected)))
        return
    l = (remaining & -remaining).bit_length() - 1
    for i in through_line[l]:
        mask = spread_line_masks[i]
        if (mask & remaining) == mask:
            packing_cover(remaining ^ mask, selected + [i])
packing_cover((1 << 35) - 1, [])
packings = sorted(set(packings))
assert len(packings) == 240 and all(len(p) == 7 for p in packings)

# Count, without assuming transitivity, extensions of each compatible support.
incidence = [Counter() for _ in range(6)]
for packing in packings:
    for k in range(1, 6):
        incidence[k].update(combinations(packing, k))
assert [len(incidence[k]) for k in range(1, 6)] == [56, 840, 4200, 7560, 5040]
assert Counter(incidence[1].values()) == {30: 56}
assert Counter(incidence[2].values()) == {6: 840}
assert Counter(incidence[3].values()) == {2: 4200}
assert Counter(incidence[4].values()) == {1: 6720, 2: 840}
assert Counter(incidence[5].values()) == {1: 5040}

# Recompute traces from Boolean observations, independently of incidence counts.
concepts = [sum(1 << s for s in p) for p in packings]
def shattered(support):
    traces = set()
    for p in concepts:
        traces.add(sum(1 << j for j, q in enumerate(support) if p & (1 << q)))
    return len(traces) == (1 << len(support))
for k in range(1, 5):
    expected = {s for s, m in incidence[k].items() if k < 4 or m == 1}
    for s in incidence[k]:
        assert shattered(s) == (s in expected), (k, s)
    if k == 2:
        assert not shattered(next(s for s in combinations(range(56), 2)
                                   if s not in incidence[2]))
assert not any(shattered(s) for s in incidence[5])
assert 6720 == sum(m == 1 for m in incidence[4].values())
# An arbitrary shattered five-support would have a shattered four-subset.
# Every four-subset of a five-set in one packing has its all-positive trace
# only in that same packing if shattered, so its required 4/1 trace fails.
print('PACKING_SHATTER_PASS lines=35 spreads=56 packings=240')
print('FACE_POLYNOMIAL 1+56z+840z^2+4200z^3+6720z^4')
print('QUARTETS unique=6720 double=840; each triple has two extensions')
