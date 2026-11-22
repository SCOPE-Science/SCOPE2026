"""Exact 18-spin ground-state census for the two Blanusa cubic graphs.

Run with Python 3 (standard library only). Both independent enumerators
inspect all 2**18 subsets, not a random sample.
"""
from collections import defaultdict

FIRST = [(0, 5), (1, 17), (2, 14), (3, 8), (4, 17),
         (6, 11), (7, 17), (9, 13), (10, 15), (12, 16)] + [
         (i, i + 1) for i in range(16)] + [(0, 16)]
SECOND = [(0, 1), (0, 2), (0, 14), (1, 5), (1, 11), (2, 3),
          (2, 6), (3, 4), (3, 9), (4, 5), (4, 7), (5, 6),
          (6, 8), (7, 8), (7, 17), (8, 9), (9, 15),
          (10, 11), (10, 14), (10, 16), (11, 12), (12, 13),
          (12, 17), (13, 14), (13, 15), (15, 16), (16, 17)]
EXPECTED = (
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
     [1, 18, 126, 438, 801, 748, 316, 46, 1, 20]),
    ([0, 0, 0, 0, 0, 0, 0, 0, 1, 2],
     [1, 18, 126, 438, 801, 746, 307, 36, 42, 4]),
)

def direct(edges):
    minima = [100] * 10
    counts = [0] * 10
    for mask in range(1 << 18):
        k = mask.bit_count()
        if k > 9:
            continue
        induced = sum(((mask >> u) & 1) & ((mask >> v) & 1)
                      for u, v in edges)
        if induced < minima[k]:
            minima[k], counts[k] = induced, 1
        elif induced == minima[k]:
            counts[k] += 1
    return minima, counts

def incremental(edges):
    neighbors = [0] * 18
    degrees = [0] * 18
    assert len(set(tuple(sorted(e)) for e in edges)) == 27
    for u, v in edges:
        assert 0 <= u < 18 and 0 <= v < 18 and u != v
        neighbors[u] |= 1 << v
        neighbors[v] |= 1 << u
        degrees[u] += 1
        degrees[v] += 1
    assert degrees == [3] * 18
    induced = [0] * (1 << 18)
    counts = [0] * 10
    minima = [100] * 10
    for mask in range(1 << 18):
        if mask:
            low = mask & -mask
            v = low.bit_length() - 1
            rest = mask - low
            induced[mask] = induced[rest] + (rest & neighbors[v]).bit_count()
        k = mask.bit_count()
        if k > 9:
            continue
        e = induced[mask]
        if e < minima[k]:
            minima[k], counts[k] = e, 1
        elif e == minima[k]:
            counts[k] += 1
    return minima, counts

def critical_counts(minima, counts, h):
    vals = [(27 - 6*k + 4*minima[k] - h*(18-2*k), counts[k])
            for k in range(10)]
    energy = min(x for x, y in vals)
    return energy, {18-2*k: y for k, (x, y) in enumerate(vals) if x == energy}

for name, edges, expected in zip(('first', 'second'), (FIRST, SECOND), EXPECTED):
    a = direct(edges)
    b = incremental(edges)
    assert a == b == (list(expected[0]), list(expected[1])), (name, a, b)
    print(name, 'min induced edges', a[0], 'sector counts', a[1])
    for h in (0, 1, 2, 3, 4):
        # At zero field, include mirror states with positive magnetization.
        energy, counts = critical_counts(*a, h)
        print(' h/J', h, 'E/J', energy, 'nonnegative M:', critical_counts(*a, h)[1])
    assert critical_counts(*a, 3)[1] == (
        {18:1,16:18,14:126,12:438,10:801,8:748,6:316,4:46,2:1}
        if name == 'first' else
        {18:1,16:18,14:126,12:438,10:801,8:746,6:307,4:36})
    assert (sum(critical_counts(*a, 3)[1].values()) ==
            (2495 if name == 'first' else 2473))
    if name == 'second':
        assert critical_counts(*a, 1)[1] == {4:36, 2:42, 0:4}
print('ALL_EXHAUSTIVE_CHECKS_PASSED')
