"""Finite cross-checks for the Euclidean geometry of biclique symmetric edge polytopes.

Requires numpy and scipy. All tolerance-sensitive checks are numerical diagnostics,
not replacements for the general proof.
"""
import itertools
import math

import numpy as np
from scipy.linalg import null_space
from scipy.optimize import linprog
from scipy.spatial import ConvexHull


def normals(p, q):
    n = p + q
    result = []
    for side in (0, 1):
        k = q if side == 0 else p
        for signs in itertools.product((-1.0, 1.0), repeat=k):
            v = np.zeros(n)
            if side == 0:
                v[p:] = signs
            else:
                v[:p] = signs
            v -= v.mean()
            if not any(np.allclose(v, w, atol=1e-12) for w in result):
                result.append(v)
    return np.asarray(result)


def theoretical(p, q):
    n = p + q
    a, b = sorted((p, q))
    max_squared = b - (b % 2) / n
    rad = 1 / math.sqrt(max_squared)
    if a < b:
        dim = a if b % 2 == 0 else a-1
        contacts = math.comb(b, b // 2) * (1 if b % 2 == 0 else 2)
    else:
        dim = 1 if b % 2 == 0 else 0
        contacts = 2 * math.comb(b, b // 2) * (1 if b % 2 == 0 else 2)
    return rad, dim, contacts


def edge_vertices(p, q):
    n = p + q
    a = []
    for i in range(p):
        for j in range(p, n):
            e = np.zeros(n)
            e[i] = 1
            e[j] = -1
            a.extend((e, -e))
    return np.asarray(a)


def check_one(p, q, do_hull):
    n = p + q
    verts = edge_vertices(p, q)
    facets = normals(p, q)
    rad, dim, contacts = theoretical(p, q)
    assert len(facets) == 2**p + 2**q - 2
    # All supporting hyperplanes actually support the edge hull.
    assert np.allclose((facets @ verts.T).max(axis=1), 1.0)
    norms = np.linalg.norm(facets, axis=1)
    assert abs(1 / norms.max() - rad) < 1e-12
    tangent = facets[np.isclose(norms, norms.max(), atol=1e-11)]
    assert len(tangent) == contacts
    rank = np.linalg.matrix_rank(tangent, tol=1e-9)
    assert n-1-rank == dim, (p, q, n-1-rank, dim)
    # A dual linear program, with genuine H coordinates, independently
    # maximizes the radius of an arbitrarily translated inscribed ball.
    basis = null_space(np.ones((1, n)))
    aa = np.column_stack((facets @ basis, norms))
    lp = linprog(np.r_[np.zeros(n-1), -1.0], A_ub=aa,
                 b_ub=np.ones(len(facets)), bounds=[(None, None)]*n,
                 method='highs')
    assert lp.success, (p, q, lp.message)
    assert abs(lp.x[-1] - rad) < 3e-8, (p, q, lp.x[-1], rad)
    # The nonzero tangent-orthogonal directions remain feasible near 0.
    null_tangent = null_space(np.vstack((tangent, np.ones((1, n)))))
    assert null_tangent.shape[1] == dim
    for k in range(dim):
        testx = null_tangent[:,k]
        margin = 1.0 - norms*rad
        loose = margin > 1e-10
        steps = margin[loose] / np.maximum(np.abs(facets[loose] @ testx), 1e-15)
        step = min(0.02, 0.1 * float(steps.min()))
        assert np.all(facets @ (step*testx) + norms*rad <= 1+1e-9)
        assert np.all(facets @ (-step*testx) + norms*rad <= 1+1e-9)
    # Independently recover facets via Euclidean convex hull, not the sign
    # enumeration. Triangulated hull facets are deduplicated by hyperplane.
    if do_hull:
        points = verts @ basis
        hull = ConvexHull(points)
        planes = []
        for plane in hull.equations:
            u = np.r_[plane[:-1], plane[-1]]
            if not any(np.linalg.norm(u-v) < 1e-7 for v in planes):
                planes.append(u)
        assert len(planes) == len(facets), (p,q,len(planes),len(facets))
        distances = sorted(-u[-1] for u in planes)
        predicted = sorted(1/norms)
        assert np.allclose(distances, predicted, atol=1e-7), (p,q)


if __name__ == '__main__':
    cases = 0
    for p in range(2, 6):
        for q in range(p, 8):
            if p+q > 11:
                continue
            check_one(p, q, do_hull=(p+q <= 6))
            cases += 1
    # Complete balanced-even center segment: verify both endpoints are
    # feasible, and any strictly larger parameter violates a facet.
    for m in (2, 4, 6):
        r, dim, touching = theoretical(m, m)
        assert dim == 1
        zmax = (1.0 - math.sqrt(1.0 - 2.0 / (m*m))) / 2.0
        vv = normals(m, m)
        nn = np.linalg.norm(vv, axis=1)
        for t in (-zmax, zmax):
            z = np.r_[np.full(m, t), np.full(m, -t)]
            lhs = vv @ z + r*nn
            assert lhs.max() <= 1 + 1e-11
            assert np.count_nonzero(np.isclose(lhs, 1, atol=1e-9)) == (
                touching + 2*math.comb(m, m//2-1) - (1 if m == 2 else 0))
        t = zmax + 0.01
        z = np.r_[np.full(m, t), np.full(m, -t)]
        assert (vv @ z + r*nn).max() > 1 + 1e-5
    print('BICLIQUE_INBALL_FACETS_CENTERS_CHECKS_PASSED', cases)
