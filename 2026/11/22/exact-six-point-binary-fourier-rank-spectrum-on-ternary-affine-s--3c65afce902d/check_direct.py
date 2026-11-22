#!/usr/bin/env python3
"""Independent direct integer convolution-rank census of all six-subsets."""
from itertools import combinations, product
from collections import Counter

points = list(product((0,1,2), repeat=3))
# Use all 26 nonzero Fourier vectors (rather than 13 projective directions).
frequency_vectors = points[1:]
phases = [tuple(sum(p[j]*v[j] for j in range(3)) % 3 for p in points)
          for v in frequency_vectors]
counts = Counter()
for S in combinations(range(27), 6):
    zeros = 0
    for phase in phases:
        a = sum(phase[i] == 0 for i in S)
        if a != 2:
            continue
        b = sum(phase[i] == 1 for i in S)
        if b == 2:  # remaining two have phase 2
            zeros += 1
    counts[27 - zeros] += 1
expected = {9:468, 15:10530, 21:78624, 23:113724,
            25:75816, 27:16848}
assert dict(counts) == expected, (counts, expected)
assert sum(counts.values()) == 296010
print('PASS: all 296010 subsets, 26 Fourier vectors, six exact rank strata.')
