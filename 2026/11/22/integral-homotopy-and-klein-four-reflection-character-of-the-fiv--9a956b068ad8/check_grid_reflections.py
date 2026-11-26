#!/usr/bin/env python3
"""Exact grid reflection character and replay of lexicographic dual matching."""
from collections import Counter
from itertools import combinations

N = 20
vertices = range(N)
points = [divmod(v, 5) for v in vertices]
size = 1 << N
full = size - 1
dual = bytearray(size)
facets = 0
for face in combinations(vertices, 5):
    if all(sum(abs(x - y) for x, y in zip(points[i], points[j])) != 1
           for i, j in combinations(face, 2)):
        dual[full ^ sum(1 << v for v in face)] = 1
        facets += 1
assert facets == 1998

for v in vertices:
    bit = 1 << v
    for base in range(0, size, 2 * bit):
        for m in range(base, base + bit):
            if dual[m | bit]:
                dual[m] = 1
assert sum(dual) == 976007

live = dual[:]
assert live[0] and live[1]  # The first pivot pairs the empty face and {0}.
for v in vertices:
    bit = 1 << v
    for base in range(0, size, 2 * bit):
        for m in range(base, base + bit):
            if live[m] and live[m | bit]:
                live[m] = live[m | bit] = 0
critical = Counter(m.bit_count() - 1 for m, present in enumerate(live) if present)
assert critical == {10: 489}
print('dual faces including empty:', sum(dual), 'critical:', sorted(critical.items()))

def fixed_trace(reverse_rows, reverse_cols):
    orbit_masks = []
    for v, (r, c) in enumerate(points):
        image_r = 3 - r if reverse_rows else r
        image_c = 4 - c if reverse_cols else c
        w = 5 * image_r + image_c
        if v <= w:
            orbit_masks.append((1 << v) | (1 << w))
    unions = [0] * (1 << len(orbit_masks))
    fixed = lefschetz = 0
    for i in range(1, len(unions)):
        low = i & -i
        unions[i] = unions[i - low] | orbit_masks[low.bit_length() - 1]
        if not dual[full ^ unions[i]]:
            fixed += 1
            lefschetz += 1 if i.bit_count() % 2 else -1
    return fixed, lefschetz, 1 - lefschetz

data = [fixed_trace(*g) for g in ((0, 0), (1, 0), (0, 1), (1, 1))]
assert data == [(72568, -488, 489), (252, -30, 31), (444, -12, 13), (212, -14, 15)]
char = [row[2] for row in data]
numerators = [char[0] + a * char[1] + b * char[2] + a * b * char[3]
              for a in (1, -1) for b in (1, -1)]
assert all(x % 4 == 0 for x in numerators)
mult = [x // 4 for x in numerators]
assert mult == [137, 123, 114, 115]
print('fixed, Lefschetz, H7 trace:', data)
print('rational sign multiplicities:', mult)
