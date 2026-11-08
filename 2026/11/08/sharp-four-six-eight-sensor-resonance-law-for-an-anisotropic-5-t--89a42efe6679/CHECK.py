#!/usr/bin/env python3
"""Independent finite checks for the exact anisotropic torus theorem."""
import cmath
import itertools
import math
import numpy as np

P, Q = 5, 7
A = [math.cos(2 * math.pi * i / P) for i in range(3)]
B = [math.cos(2 * math.pi * j / Q) for j in range(4)]
ORBIT = [(i, j) for i in range(3) for j in range(4)]

def modes(i, j):
    return [(a, b) for a in ([0] if i == 0 else [i, -i])
                   for b in ([0] if j == 0 else [j, -j])]

def sampling(S, W):
    return np.array([[cmath.exp(2j * math.pi * (a * x / P + b * y / Q))
                      for a, b in W] for x, y in S])

def full_column_rank(S, W):
    v = np.linalg.svd(sampling(S, W), compute_uv=False)
    return len(S) >= len(W) and v[len(W)-1] > 1e-6

S4 = [(0, 0), (1, 0), (0, 1), (2, 1)]
S8 = [(x, y) for x in range(4) for y in range(2)]
records = []
for i, k in itertools.combinations(range(3), 2):
    for ell, j in itertools.combinations(range(4), 2):
        r = (B[ell] - B[j]) / (A[i] - A[k])
        if i > 0 and ell > 0:
            d, S = 8, S8
        elif i == 0 and ell == 0:
            d, S = 4, S4
        elif i == 0:
            d, S = 6, [(x, y) for x in range(3) for y in range(2)]
        else:
            d, S = 6, [(x, y) for x in range(2) for y in range(3)]
        merged = modes(i, j) + modes(k, ell)
        assert r > 0 and len(merged) == d
        assert full_column_rank(S, merged)
        for uv in ORBIT:
            if uv not in ((i, j), (k, ell)):
                assert full_column_rank(S, modes(*uv))
        records.append((r, i, j, k, ell, d, S))
assert len(records) == 18
assert sum(d == 4 for _, _, _, _, _, d, _ in records) == 6
assert sum(d == 6 for _, _, _, _, _, d, _ in records) == 9
assert sum(d == 8 for _, _, _, _, _, d, _ in records) == 3
ratios = sorted(row[0] for row in records)
assert min(v-u for u, v in zip(ratios, ratios[1:])) > 0.03

# Check that each coupling has exactly one collision among the 12 levels.
for r, i, j, k, ell, d, S in records:
    values = [r * A[u] + B[v] for u, v in ORBIT]
    gaps = sorted(abs(values[t] - values[s])
                  for t in range(12) for s in range(t + 1, 12))
    assert gaps[0] < 1e-13 and gaps[1] > 0.015

# Full observability test, independent of spectral block arguments.
def observation(r, S, K):
    W = [(a, b) for a in range(-2, 3) for b in range(-3, 4)]
    return np.array([[(r * A[abs(a)] + B[abs(b)]) ** t
                      * cmath.exp(2j * math.pi * (a*x/P + b*y/Q))
                      for a, b in W]
                     for t in range(K) for (x, y) in S])

for r, _, _, _, _, _, S in records:
    singular_values = np.linalg.svd(observation(r, S, 11), compute_uv=False)
    assert singular_values[-1] > 1e-8

regular = [(x, y) for x in range(2) for y in range(2)]
for ij in ORBIT:
    assert full_column_rank(regular, modes(*ij))
assert np.linalg.svd(observation(1.0, regular, 12), compute_uv=False)[-1] > 1e-8
print("ALL_ANISOTROPIC_5_BY_7_TORUS_CHECKS_PASSED")
