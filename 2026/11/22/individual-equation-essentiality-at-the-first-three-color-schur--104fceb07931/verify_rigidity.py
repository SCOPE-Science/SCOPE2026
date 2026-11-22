#!/usr/bin/env python3
"""Independent exhaustive check of the three Schur-free [1,13] partitions."""
from itertools import product
T = [(a,b,a+b) for a in range(1,14) for b in range(a,14) if a+b <= 13]
C = []
for word in product(range(3), repeat=12):
    colors = (-1,) + (0,) + word
    if all(not (colors[a] == colors[b] == colors[z]) for a,b,z in T):
        C.append(colors)
assert len(C) == 6  # normalized color of integer 1 equals 0
fixed = [{1,4,10,13}, {2,3,11,12}, {5,6,8,9}]
for c in C:
    classes = [set(v for v in range(1,14) if c[v] == h) for h in range(3)]
    assert all(any(D == A or D == A | {7} for D in classes) for A in fixed)
    assert 7 in (classes[0] | classes[1] | classes[2])
    for h in range(3):
        col14 = c + (h,)
        count14 = sum(col14[a] == h and col14[b] == h for a in range(1,8) for b in [14-a])
        assert count14 >= 2
print('PASS [1,13] rigidity: 6 normalized configurations; each hue for 14 creates at least two sum-14 violations')
