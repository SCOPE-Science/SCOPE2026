#!/usr/bin/env python3
"""Exhaustive independent implementation of the Clebsch strong-odd census.

Vertex labels are the even-weight integers 0..31; adjacency means
Hamming distance 4. No external packages are needed.
"""
from functools import lru_cache
from collections import Counter
from math import factorial

words = [v for v in range(32) if v.bit_count() % 2 == 0]
assert len(words) == 16
neighbors = [sum(1 << j for j, y in enumerate(words)
                 if (x ^ y).bit_count() == 4) for x in words]
assert all(m.bit_count() == 5 for m in neighbors)
assert sum(m.bit_count() for m in neighbors) == 80

classes = []
independent_classes = []
for mask in range(1, 1 << 16):
    if any(mask & (1 << i) and neighbors[i] & mask for i in range(16)):
        continue
    independent_classes.append(mask)
    if all((neighbors[i] & mask).bit_count() % 2 == 1 or
           (neighbors[i] & mask) == 0 for i in range(16)):
        classes.append(mask)

assert Counter(m.bit_count() for m in classes) == {1: 16, 4: 40}

@lru_cache(None)
def partition_counts(remaining):
    """Count unordered partitions into admissible classes, by block count."""
    if remaining == 0:
        return (1,) + (0,) * 16
    least = remaining & -remaining
    ans = [0] * 17
    for block in classes:
        if block & least and block & remaining == block:
            rest = partition_counts(remaining ^ block)
            for k in range(1, 17):
                ans[k] += rest[k - 1]
    return tuple(ans)

counts = partition_counts((1 << 16) - 1)
expected = {4: 70, 7: 360, 10: 300, 13: 40, 16: 1}
assert {k: x for k, x in enumerate(counts) if x} == expected

@lru_cache(None)
def ordinary_four(remaining, k):
    if remaining == 0:
        return int(k == 0)
    if k == 0:
        return 0
    least = remaining & -remaining
    return sum(ordinary_four(remaining ^ block, k - 1)
               for block in independent_classes
               if block & least and block & remaining == block)

proper_4_partitions = ordinary_four((1 << 16) - 1, 4)
assert proper_4_partitions == 1190
assert proper_4_partitions * factorial(4) == 28560

print('vertices=16 edges=40 odd_independent_classes=56')
print('odd_independent_size_counts={1:16,4:40}')
print('strong_odd_unlabelled_partition_polynomial=', expected)
print('strong_odd_chromatic_number=4 optimal_unlabelled=70 optimal_named=1680')
print('ordinary_proper_4_partitions=1190 named=28560 fraction_strong_odd=1/17')
