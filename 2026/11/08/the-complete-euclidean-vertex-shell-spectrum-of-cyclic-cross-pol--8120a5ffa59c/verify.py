"""Finite independent checks of cyclic coordinate-diamond Minkowski sums.

Requires NumPy and SciPy. The mathematical proof is given separately.
"""
from collections import Counter
from itertools import product
from math import comb
import numpy as np
from scipy.spatial import ConvexHull

for n in range(3, 8):
    sums = set()
    for choices in product(range(4), repeat=n):
        vector = [0] * n
        for i, choice in enumerate(choices):
            endpoint = i if choice < 2 else (i + 1) % n
            sign = 1 if choice % 2 == 0 else -1
            vector[endpoint] += sign
        sums.add(tuple(vector))
    squared_norm_counts = Counter(sum(x * x for x in point) for point in sums)
    outer_squared_radius = n + 2 * (n // 2)
    expected_contacts = 2 ** (n - n // 2 + 1) * comb(n, 2 * (n // 2))
    assert max(squared_norm_counts) == outer_squared_radius
    assert squared_norm_counts[outer_squared_radius] == expected_contacts

    if n <= 5:
        candidates = np.asarray(sorted(sums), dtype=np.float64)
        hull = ConvexHull(candidates)
        vertex_shells = Counter(
            int(sum(round(float(x * x)) for x in candidates[j]))
            for j in hull.vertices
        )
        predicted = Counter({
            n + 2 * k: 2 ** (n - k + 1) * comb(n, 2 * k)
            for k in range(1, n // 2 + 1)
        })
        assert vertex_shells == predicted, (n, vertex_shells, predicted)
    print(f"n={n} checked; distinct endpoint sums={len(sums)}")
print("PASS")
