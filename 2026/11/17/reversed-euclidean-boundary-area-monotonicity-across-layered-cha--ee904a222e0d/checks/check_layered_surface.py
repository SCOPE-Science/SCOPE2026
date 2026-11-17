"""Reproduce Euclidean volume and boundary-area identities for layered chain-order polytopes.

Requires Python 3, numpy, scipy. Independently enumerates feasible Boolean vertices,
forms their Euclidean convex hull, and compares its volume/surface with the closed formula.
This is a finite-dimensional computational check, not a proof for all dimensions.
"""

from itertools import product
from math import factorial, prod, sqrt, isclose
import numpy as np
from scipy.spatial import ConvexHull


def ordered_compositions(n):
    for breaks in product((0, 1), repeat=n - 1):
        parts = []
        a = 1
        for bit in breaks:
            if bit:
                parts.append(a)
                a = 1
            else:
                a += 1
        yield tuple(parts + [a])


def facets(level_sizes, k):
    n = sum(level_sizes)
    r = len(level_sizes)
    levels = []
    pos = 0
    for a in level_sizes:
        levels.append(tuple(range(pos, pos + a)))
        pos += a
    inequalities = []

    def add(pos, neg, bound, family):
        normal = np.zeros(n)
        for j in pos:
            normal[j] += 1
        for j in neg:
            normal[j] -= 1
        inequalities.append((normal, bound, family))

    for i in range(k):
        for a in levels[i]:
            add([], [a], 0, "zero")
    for i in range(k + 1, r):
        for a in levels[i - 1]:
            for b in levels[i]:
                add([a], [b], 0, "order")
    if k < r:
        for choices in product(*levels[: k + 1]):
            add(choices[:k], [choices[-1]], 0, "mixed")
        for a in levels[-1]:
            add([a], [], 1, "top")
    else:
        for choices in product(*levels):
            add(choices, [], 1, "maximal")
    return inequalities


def exact_volume_and_surface(level_sizes, k):
    n = sum(level_sizes)
    r = len(level_sizes)
    volume = prod(factorial(x) for x in level_sizes) / factorial(n)
    if k < r:
        coefficient = k + 1 + sqrt(k + 1) + (r - k - 1) * sqrt(2)
    else:
        coefficient = r + sqrt(r)
    return volume, n * volume * coefficient


def verify(level_sizes, k):
    n = sum(level_sizes)
    inequalities = facets(level_sizes, k)
    vertices = np.array([
        binary for binary in product((0.0, 1.0), repeat=n)
        if all(np.dot(normal, binary) <= bound + 1e-12
               for normal, bound, _ in inequalities)
    ])
    polytope = ConvexHull(vertices)
    predicted_vol, predicted_surface = exact_volume_and_surface(level_sizes, k)
    assert isclose(polytope.volume, predicted_vol, rel_tol=2e-10, abs_tol=1e-11), (
        "volume", level_sizes, k, polytope.volume, predicted_vol
    )
    assert isclose(polytope.area, predicted_surface, rel_tol=2e-10, abs_tol=1e-11), (
        "area", level_sizes, k, polytope.area, predicted_surface
    )
    # Each listed hyperplane must contain dimension-(n-1) affine vertices.
    # This also checks facet completeness in small finite cases.
    for normal, bound, category in inequalities:
        face = vertices[np.abs(vertices @ normal - bound) < 1e-11]
        assert np.linalg.matrix_rank(face[1:] - face[0], tol=1e-10) == n - 1, (
            "facet rank", level_sizes, k, category
        )
    return len(inequalities)


def main():
    count = 0
    facet_checks = 0
    for n in range(2, 7):
        for profile in ordered_compositions(n):
            for k in range(len(profile) + 1):
                facet_checks += verify(profile, k)
                count += 1
    print(f"LAYERED_SURFACE_PASS hull_cases={count} facet_rank_checks={facet_checks} n=2..6")


if __name__ == "__main__":
    main()
