#!/usr/bin/env python3
"""Exact enumeration of Loday-associahedron vertex radii.

The combinatorial identity and all-dimensional theorem are proved in RESULT.md.
This standalone calculation is an independent finite-range check.
"""
from collections import Counter
from functools import lru_cache
from math import comb

@lru_cache(maxsize=None)
def profiles(internal_nodes):
    """Return (coordinate tuple, sum of local branching penalties) for every plane binary tree."""
    if internal_nodes == 0:
        return (((), 0),)
    out = []
    for left_nodes in range(internal_nodes):
        right_nodes = internal_nodes - 1 - left_nodes
        left_leaves, right_leaves = left_nodes + 1, right_nodes + 1
        local_penalty = left_leaves * right_leaves * left_nodes * right_nodes
        for left_coordinates, left_penalty in profiles(left_nodes):
            for right_coordinates, right_penalty in profiles(right_nodes):
                coordinates = left_coordinates + (left_leaves * right_leaves,) + right_coordinates
                out.append((coordinates, left_penalty + right_penalty + local_penalty))
    return tuple(out)

def catalan(n):
    return comb(2*n, n)//(n+1)

checked = 0
for n in range(1, 12):
    rows = profiles(n)
    assert len(rows) == catalan(n), (n,len(rows))
    baseline = n*(n+1)*(2*n+1)//6
    counts = Counter()
    for x, penalty in rows:
        assert len(x) == n
        assert sum(x) == n*(n+1)//2
        assert sum(v*v for v in x) - baseline == penalty
        assert penalty >= 0 and penalty % 4 == 0
        # Double-center with integer numerator: 4*||x-(n+1)/2||^2.
        direct_radius_fourfold = sum((2*v-(n+1))**2 for v in x)
        predicted_radius_fourfold = n*(n*n-1)//3 + 4*penalty
        assert direct_radius_fourfold == predicted_radius_fourfold
        counts[penalty] += 1
        checked += 1
    assert counts[0] == 2**(n-1)
    if n >= 3:
        assert min(i for i in counts if i > 0) == 4
        assert counts[4] == 2**(n-3)
    else:
        assert list(counts) == [0]
    print(f"n={n} vertices={len(rows)} min={counts[0]} next={counts.get(4, 0)} shells={len(counts)}")

for a in range(1, 50):
    for b in range(1, 50):
        n=a+b-1
        s=lambda k:k*(k+1)*(2*k+1)//6
        assert a*a*b*b+s(a-1)+s(b-1)-s(n) == a*b*(a-1)*(b-1)
print(f"LODAY_RADIAL_QUANTIZATION_CHECKS_PASSED profiles={checked} dimensions=11 algebraic_pairs=2401")
