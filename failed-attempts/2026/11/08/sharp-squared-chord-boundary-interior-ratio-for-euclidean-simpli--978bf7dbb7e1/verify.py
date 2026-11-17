#!/usr/bin/env python3
"""Supplementary checks for a sharp simplex boundary/interior squared-distance ratio.

Analytic proof is in RESULT.md. This checker independently computes facet areas
and squared-distance moments from their definitions, then checks the claimed closed
formula and two-cluster limit numerically. Requires Python 3 and numpy.
"""
import math
import numpy as np


def facet_weights(vertices):
    d = vertices.shape[1]
    areas = []
    for i in range(d + 1):
        facet = np.delete(vertices, i, axis=0)
        edge = (facet[1:] - facet[0]).T
        singular = np.linalg.svd(edge, compute_uv=False)
        areas.append(np.prod(singular) / math.factorial(d - 1))
    a = np.asarray(areas)
    assert np.min(a) > 0
    return a / np.sum(a)


def moments_from_barycentric_integrals(v, w):
    d = v.shape[1]
    n = d + 1
    # Interior barycentric vector has E(lambda_i lambda_j)=(1+delta_ij)/(n(n+1)).
    interior_second = 0.0
    interior_mean = np.mean(v, axis=0)
    for i in range(n):
        for j in range(n):
            interior_second += (1 + (i == j)) * np.dot(v[i], v[j]) / (n * (n + 1))
    interior_pair = 2 * (interior_second - np.dot(interior_mean, interior_mean))

    boundary_second = 0.0
    boundary_mean = np.zeros(d)
    for omitted in range(n):
        face = np.delete(v, omitted, axis=0)
        face_mean = np.mean(face, axis=0)
        second = 0.0
        for i in range(d):
            for j in range(d):
                second += (1 + (i == j)) * np.dot(face[i], face[j]) / (d * (d + 1))
        boundary_second += w[omitted] * second
        boundary_mean += w[omitted] * face_mean
    boundary_pair = 2 * (boundary_second - np.dot(boundary_mean, boundary_mean))
    return interior_pair, boundary_pair


def moments_from_formula(v, w):
    d = v.shape[1]
    g = np.mean(v, axis=0)
    s = float(np.sum((v - g)**2))
    incenter = np.sum(w[:, None] * v, axis=0)
    gap = float(np.sum((incenter - g)**2))
    inside = 2 * s / ((d + 1) * (d + 2))
    boundary = 2 * s / (d * (d + 1)) - 2 * gap / (d * d)
    return inside, boundary, gap/s


def collapse_family(d, t):
    v = np.zeros((d + 1, d), float)
    v[0, 0] = 1
    v[1, 0] = 1
    v[1, 1] = t * t
    v[2:, 0] = -1
    for i in range(3, d + 1):
        v[i, i-1] = t
    return v


def main():
    rng = np.random.default_rng(20261102)
    checks = 0
    for d in range(2, 9):
        for _ in range(40):
            v = rng.normal(size=(d + 1, d))
            v *= rng.uniform(0.5, 5.0, size=d)
            w = facet_weights(v)
            assert np.max(w) < 0.5 + 1e-10
            inside, boundary = moments_from_barycentric_integrals(v, w)
            inside2, boundary2, q = moments_from_formula(v, w)
            assert math.isclose(inside, inside2, rel_tol=2e-9, abs_tol=2e-9)
            assert math.isclose(boundary, boundary2, rel_tol=2e-9, abs_tol=2e-9)
            sharp = (d + 1) * (d + 2) / (2 * d * d)
            assert boundary / inside > sharp - 1e-10
            assert 0 <= q < (d-1) / (2 * (d+1)) + 1e-10
            checks += 4
    for d in range(2, 11):
        for t in (0.1, 0.01, 0.001):
            v = collapse_family(d, t)
            w = facet_weights(v)
            inside, boundary, q = moments_from_formula(v, w)
            sharp = (d + 1) * (d + 2) / (2 * d * d)
            assert boundary / inside > sharp - 1e-9
            assert np.linalg.norm(w[:2] - 0.5) < 2 * d * t
            assert np.max(w[2:]) < 3*d*t
            checks += 3
    # Independently sample the pair distances in a non-regular four-simplex.
    d = 4
    v = collapse_family(d, .01)
    w = facet_weights(v)
    inside, boundary, _ = moments_from_formula(v, w)
    assert boundary < inside
    N = 100000
    lx = rng.dirichlet(np.ones(d + 1), size=(2, N))
    x = lx @ v
    empirical_inside = np.mean(np.sum((x[0] - x[1])**2, axis=1))
    faces = rng.choice(d + 1, size=(2, N), p=w)
    lam = rng.dirichlet(np.ones(d), size=(2, N))
    y = np.zeros((2, N, d))
    for i in range(d + 1):
        verts = np.delete(v, i, axis=0)
        for side in range(2):
            inds = (faces[side] == i)
            y[side, inds] = lam[side, inds] @ verts
    empirical_boundary = np.mean(np.sum((y[0] - y[1])**2, axis=1))
    assert abs(empirical_inside-inside)/inside < 0.04
    assert abs(empirical_boundary-boundary)/boundary < 0.04
    checks += 3
    print('SIMPLEX_SURFACE_SECOND_MOMENT_OK', checks)
    print('DIM4_EXAMPLE_RATIO', boundary/inside)
    print('DIM4_SHARP_INFIMUM', (d+1)*(d+2)/(2*d*d))

if __name__ == '__main__':
    main()
