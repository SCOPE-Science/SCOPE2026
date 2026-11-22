#!/usr/bin/env python3
"""Exact six-point Frobenius counts of negative supports on an A1 weak cubic del Pezzo surface.

Only Python's standard library is required.  The 21 (-1)-curves are 6 point
exceptionals and 15 secant transforms; the conic root has self-intersection -2.
"""
from itertools import combinations
from collections import Counter

N = 6
pairs = list(combinations(range(N), 2))
# For distinct (-1) curves, adjacency here means meeting positively.
meet = [0] * 21
for i in range(21):
    for j in range(i + 1, 21):
        if i < 6 and j >= 6:
            intersects = i in pairs[j - 6]
        elif i >= 6 and j >= 6:
            intersects = set(pairs[i - 6]).isdisjoint(pairs[j - 6])
        else:
            intersects = False
        if intersects:
            meet[i] |= 1 << j
            meet[j] |= 1 << i

# Recursive independent-set enumeration, from direct intersection constraints.
independent = []
def visit(i, chosen):
    if i == 21:
        independent.append(chosen)
        return
    visit(i + 1, chosen)
    if not chosen & meet[i]:
        visit(i + 1, chosen | (1 << i))
visit(0, 0)
supports = independent + [m | (1 << 21) for m in independent if (m & 63).bit_count() <= 1]
assert len(set(supports)) == len(supports)

def permutation(partition):
    p = list(range(6))
    start = 0
    for length in partition:
        for k in range(length):
            p[start + k] = start + (k + 1) % length
        start += length
    assert start == 6
    return p

def curve_permutation(partition):
    p = permutation(partition)
    return p + [6 + pairs.index(tuple(sorted((p[i], p[j])))) for i, j in pairs] + [21]

def orbit_masks(mapping):
    unseen = set(range(22))
    out = []
    while unseen:
        k = min(unseen)
        j = k
        orbit = 0
        while j in unseen:
            unseen.remove(j)
            orbit |= 1 << j
            j = mapping[j]
        assert j == k
        out.append(orbit)
    return out

def admissible(mask):
    if mask & (1 << 21) and (mask & 63).bit_count() > 1:
        return False
    for i in range(21):
        if mask & (1 << i) and (meet[i] & mask):
            return False
    return True

def by_independent_sets(mapping):
    answer = Counter()
    for mask in supports:
        image = sum(1 << mapping[i] for i in range(22) if mask & (1 << i))
        if image == mask:
            answer[(mask.bit_count(), int(bool(mask & (1 << 21))))] += 1
    return answer

def by_orbits(mapping):
    # A different algorithm: a Galois-stable support is a union of whole
    # geometric-curve cycles.  Use constrained backtracking on orbit masks,
    # rather than applying Frobenius to a precomputed support catalogue.
    orbits = orbit_masks(mapping)
    answer = Counter()
    def rec(i, mask):
        if i == len(orbits):
            answer[(mask.bit_count(), int(bool(mask & (1 << 21))))] += 1
            return
        rec(i + 1, mask)
        joined = mask | orbits[i]
        if admissible(joined):
            rec(i + 1, joined)
    rec(0, 0)
    return answer

parts = [
    (1,1,1,1,1,1), (2,1,1,1,1), (2,2,1,1), (2,2,2),
    (3,1,1,1), (3,2,1), (3,3), (4,1,1), (4,2), (5,1), (6,)
]
results = []
for part in parts:
    mapping = curve_permutation(part)
    a = by_independent_sets(mapping)
    b = by_orbits(mapping)
    assert a == b, (part, a, b)
    n = sum(a.values())
    root = sum(v for (sz,r),v in a.items() if r == 1)
    rec = {"partition":list(part), "total":n, "root":root,
           "support_size_counts":[sum(v for (s,r),v in a.items() if s==z) for z in range(7)],
           "root_size_counts":[a.get((z,1),0) for z in range(7)]}
    results.append(rec)
    print("partition",part,"stable",n,"with_root",root)
assert len(set((x['total'],x['root']) for x in results)) == 11
assert len(set(x['total'] for x in results)) == 10
assert results[0]['total'] == 1898 and results[0]['root'] == 648
assert results[0]['support_size_counts'] == [1,22,156,490,725,447,57]
assert results[8]['total'] == results[9]['total'] == 8
assert (results[8]['root'],results[9]['root']) == (2,3)
print('ARITHMETIC_CHAMBER_CLASSIFICATION_OK')
