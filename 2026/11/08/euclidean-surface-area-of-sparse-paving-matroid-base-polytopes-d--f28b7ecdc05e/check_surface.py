"""Numerical checks of intrinsic Euclidean boundary measure for selected sparse-paving base polytopes.

Python 3 with NumPy and SciPy. All geometry is computed in an orthonormal
basis of the affine hyperplane, not using lattice-normalized face volumes.
"""
import itertools
import math
import random
import numpy as np
from scipy.linalg import null_space
from scipy.spatial import ConvexHull


def eulerian(m, k):
    if k < 0 or k >= m:
        return 0
    a = [1]
    for j in range(2, m + 1):
        b = [0] * j
        for i in range(j):
            b[i] = (i + 1) * (a[i] if i < len(a) else 0) + (j - i) * (a[i - 1] if i else 0)
        a = b
    return a[k]


def correction(n, r):
    t = n - r
    denominator = math.factorial(r - 1) * math.factorial(t - 1)
    return (math.sqrt(n - 1) * (r * (r - 1) + t * (t - 1)) / (n - 2)
            - math.sqrt(r * t)) / denominator


def baseline(n, r):
    return (n * math.sqrt(n - 1) / math.factorial(n - 2)
            * (eulerian(n - 2, r - 1) + eulerian(n - 2, r - 2)))


def area_from_vertices(n, r, excluded):
    basis = null_space(np.ones((1, n)))
    exclusions = set(map(tuple, excluded))
    vertices = np.array([
        [int(i in subset) for i in range(n)]
        for comb in itertools.combinations(range(n), r)
        if (subset := frozenset(comb)) and tuple(sorted(subset)) not in exclusions
    ], dtype=float)
    return ConvexHull(vertices @ basis).area


def valid(circuits, r):
    return all(len(set(a) & set(b)) <= r - 2
               for a, b in itertools.combinations(circuits, 2))


def main():
    rng = random.Random(28473)
    cases = 0
    for n in range(4, 8):
        for r in range(2, n - 1):
            all_r = list(itertools.combinations(range(n), r))
            collections = [[all_r[0]]]
            for _ in range(7):
                chosen = []
                for h in rng.sample(all_r, len(all_r)):
                    if all(len(set(h) & set(other)) <= r - 2 for other in chosen):
                        chosen.append(h)
                    if len(chosen) == 3:
                        break
                if len(chosen) >= 2:
                    if n == 4 and r == 2 and len(chosen) == 2:
                        continue  # two parallel classes give a lower-dimensional direct sum
                    collections.append(chosen)
            for hs in collections:
                assert valid(hs, r)
                computed = area_from_vertices(n, r, hs)
                expected = baseline(n, r) - len(hs) * correction(n, r)
                assert abs(computed - expected) < 5e-6, (n, r, hs, computed, expected)
                cases += 1
    for n in range(4, 80):
        ds = [correction(n, r) for r in range(2, n - 1)]
        assert all(x > 0 for x in ds)
        assert all(ds[i + 1] > ds[i] for i in range((len(ds) - 1) // 2))
        assert np.allclose(ds, ds[::-1], rtol=1e-10, atol=1e-15)
    a = [(0, 1, 2), (3, 4, 5)]
    b = [(0, 1, 2), (0, 3, 4)]
    assert valid(a, 3) and valid(b, 3)
    assert abs(area_from_vertices(6, 3, a) - area_from_vertices(6, 3, b)) < 1e-7
    print("SPARSE_PAVING_EUCLIDEAN_AREA_CHECKS_PASSED", cases, "and_rank_profiles", 76)


if __name__ == '__main__':
    main()
