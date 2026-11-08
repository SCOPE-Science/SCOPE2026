"""Finite checks for expected-volume optimization under independent vertex retention.

Requires numpy and scipy. All geometric polytope volumes are computed
independently from the analytic pair-state formula.
"""
import itertools
import math
import numpy as np
from scipy.spatial import ConvexHull


def actual_hull_volume(vertices):
    if len(vertices) < vertices.shape[1] + 1:
        return 0.0
    if np.linalg.matrix_rank(vertices[1:] - vertices[0]) < vertices.shape[1]:
        return 0.0
    return float(ConvexHull(vertices).volume)


def exact_expected_from_all_masks(V, probabilities):
    n = V.shape[0]
    vv = np.vstack([V[:, i] for i in range(n)] + [-V[:, i] for i in range(n)])
    ans = 0.0
    for mask in itertools.product([0,1], repeat=2*n):
        prob = math.prod(float(probabilities[i]) if flag else (1-float(probabilities[i]))
                         for i,flag in enumerate(mask))
        if prob == 0.0:
            continue
        subset = vv[[i for i,flag in enumerate(mask) if flag]]
        if len(subset):
            ans += prob*actual_hull_volume(subset)
    return ans


def formula(V, probabilities):
    n = V.shape[0]
    pplus = np.asarray(probabilities[:n])
    pminus = np.asarray(probabilities[n:])
    sums = pplus+pminus
    singles = sums-2*pplus*pminus
    return abs(np.linalg.det(V))/math.factorial(n)*(float(np.prod(sums))-float(np.prod(singles)))

rng = np.random.default_rng(20261102)
for n in (2,3,4):
    for trial in range(3):
        V = rng.normal(size=(n,n))
        probabilities = rng.uniform(.08,.93,size=2*n)
        brute = exact_expected_from_all_masks(V,probabilities)
        closed = formula(V,probabilities)
        assert abs(brute-closed)<1e-9*(1+abs(closed)),(n,trial,brute,closed)

for n in range(2,13):
    for _ in range(2500):
        p = rng.uniform(.001,.999)
        s = rng.dirichlet(np.ones(2*n))*(2*n*p)
        # Skip allocations outside probability box
        if max(s)>1:
            continue
        V = np.eye(n)
        actual = formula(V,s)
        optimal = (2**n/math.factorial(n))*p**n*(1-(1-p)**n)
        assert actual <= optimal + 1e-12,(n,p,actual,optimal)
print('CROSSPOLY_HETEROGENEOUS_VOLUME_OPTIMIZATION_CHECKS_PASSED')
