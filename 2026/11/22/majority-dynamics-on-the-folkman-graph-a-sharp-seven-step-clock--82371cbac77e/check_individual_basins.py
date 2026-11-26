"""Exact labelled attraction-basin census on the Folkman graph (Python 3, NumPy)."""

import csv
import sys
from collections import Counter
from itertools import combinations

import numpy as np


def individual_basins():
    pairs = list(combinations(range(5), 2))
    neighbors = [[10+k for k, p in enumerate(pairs) if v % 5 in p] for v in range(10)]
    neighbors += [[i, i+5, j, j+5] for i, j in pairs]
    assert len(neighbors) == 20 and all(len(ns) == 4 for ns in neighbors)
    assert all(i in neighbors[j] for i, ns in enumerate(neighbors) for j in ns)
    masks = np.arange(1 << 20, dtype=np.int32)
    bits = [((masks >> i) & 1).astype(np.uint8) for i in range(20)]
    f = np.zeros_like(masks)
    for i, ns in enumerate(neighbors):
        voters = ns + [i]
        f |= (sum(bits[j] for j in voters) >= 3).astype(np.int32) << i

    p = f[f] == masks
    roots = np.full_like(masks, -1)
    roots[p] = np.minimum(masks[p], f[p])
    while np.any(roots < 0):
        successors = roots[f]
        new = (roots < 0) & (successors >= 0)
        assert np.any(new), 'Unclassified cycle'
        roots[new] = successors[new]

    weights = np.bincount(roots, minlength=len(masks))
    assert weights[0] == weights[-1] == 207670 and f[0] == 0 and f[-1] == len(masks)-1
    return [(int(r), 1+int(f[r] != r), int(weights[r])) for r in np.flatnonzero(weights)]


def main():
    rows = individual_basins()
    fixed = {1:384,3:480,4:120,18:160,21:120,25:120,28:120,30:240,38:60,
             55:720,56:720,72:120,76:240,86:120,124:120,152:60,284:20,
             1368:60,4249:40,12190:10,207670:2}
    osc = {2:60,16:240,899:40,4038:10,8652:1}
    for period, expected in [(1, fixed), (2, osc)]:
        assert Counter(b for _, p, b in rows if p == period) == expected
    if len(sys.argv) > 1:
        with open(sys.argv[1], newline='', encoding='utf-8') as checked:
            reader = csv.reader(checked, delimiter='\t')
            assert next(reader) == ['periodic_representative', 'least_period', 'basin_size']
            assert sorted(tuple(map(int, row)) for row in reader) == rows
        print(f'Exact catalog agreement: {len(rows)} rows')
    for b in sorted(fixed.keys() | osc.keys()):
        print(b, fixed.get(b, 0), osc.get(b, 0))


if __name__ == '__main__':
    main()
