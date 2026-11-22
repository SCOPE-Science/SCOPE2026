#!/usr/bin/env python3
"""Finite numerical corroboration of weighted smooth-body projection stability.

This script is supplementary: the statements for all dimensions and convex bodies
follow from the analytic proof, not from the finite tests here.
"""
import math
import random


def project_ellipsoid(x, radii):
    assert len(x) == len(radii) and all(a > 0 for a in radii)
    if sum((xi / a) ** 2 for xi, a in zip(x, radii)) <= 1:
        return list(x)

    def residual(t):
        return sum((a * xi / (a * a + t)) ** 2
                   for xi, a in zip(x, radii)) - 1

    lo, hi = 0., 1.
    while residual(hi) > 0:
        hi *= 2
    for _ in range(90):
        mid = (lo + hi) / 2
        if residual(mid) > 0:
            lo = mid
        else:
            hi = mid
    t = (lo + hi) / 2
    return [a*a*xi/(a*a+t) for xi, a in zip(x, radii)]


def norm_infty(x, w):
    return max(abs(xi)/wi for xi, wi in zip(x, w))


def norm_one(x, w):
    return sum(abs(xi)*wi for xi, wi in zip(x, w))


def extremal_normal(w):
    n = len(w)
    i = min(range(n), key=lambda j: w[j])
    R = math.sqrt(sum(v*v for v in w))
    tau = (1-w[i]/R)/2
    v = [0.] * n
    v[i] = math.sqrt(tau)
    other = math.sqrt(sum(w[j]**2 for j in range(n) if j != i))
    for j in range(n):
        if j != i:
            v[j] = w[j] * math.sqrt(1-tau) / other
    h = [-q for q in w]
    h[i] = w[i]
    return v, h


def near_boundary_ratio(radii, w, eps, use_one=False):
    normal, h = extremal_normal(w)
    if use_one:
        i = min(range(len(w)), key=lambda j: w[j])
        h = [1. / w[i] if j == i else 0. for j in range(len(w))]
    scale = math.sqrt(sum((a*v)**2 for a, v in zip(radii, normal)))
    y = [a*a*v/scale for a, v in zip(radii, normal)]
    # Both inputs are on the exterior side of the limiting tangent hyperplane.
    shift = [10. * v for v in normal]
    x1 = [q+eps*(s+t) for q, s, t in zip(y, shift, h)]
    x0 = [q+eps*s for q, s in zip(y, shift)]
    p1 = project_ellipsoid(x1, radii)
    p0 = project_ellipsoid(x0, radii)
    diff = [a-b for a,b in zip(p1,p0)]
    if use_one:
        return norm_one(diff,w)/(eps*norm_one(h,w))
    return norm_infty(diff,w)/(eps*norm_infty(h,w))


def check():
    rng = random.Random(20261115)
    cases = [([1.,2.], [1.,1.]),
             ([.7,1.5,2.], [1.,1.,1.]),
             ([1.,3.,.5,2.], [1.,2.,3.,1.]),
             ([1.,2.,4.,.5,2.5], [.5,3.,1.,2.,1.3])]
    checked = 0
    for radii, w in cases:
        n = len(w)
        L = (1+math.sqrt(sum(v*v for v in w))/min(w))/2
        # Exact row-sum identity for the extremal limiting tangent projector.
        u, h = extremal_normal(w)
        projected = [h[j] - u[j]*sum(u[k]*h[k] for k in range(n)) for j in range(n)]
        assert math.isclose(norm_infty(projected,w), L, rel_tol=2e-14)
        checked += 1
        # Actual ellipsoidal projection has ratios approaching the sharp factor.
        r1 = near_boundary_ratio(radii,w,1e-4)
        r2 = near_boundary_ratio(radii,w,1e-6)
        assert r1 <= L+2e-7 and r2 <= L+2e-7
        assert 0 <= L-r2 < L-r1 and L-r2 < 0.0002
        # The dual weighted-sum norm has the same tangent sharpness.
        k = min(range(n),key=lambda j:w[j])
        e = [1./w[k] if j == k else 0. for j in range(n)]
        tangent_col = [e[j]-u[j]*sum(u[q]*e[q] for q in range(n)) for j in range(n)]
        assert math.isclose(norm_one(tangent_col,w),L,rel_tol=2e-14)
        r3 = near_boundary_ratio(radii,w,1e-4,True)
        r4 = near_boundary_ratio(radii,w,1e-6,True)
        assert r3 <= L+2e-7 and r4 <= L+2e-7
        assert 0 <= L-r4 < L-r3 and L-r4 < 0.0002
        checked += 6
        # Sample global two-input inequalities in dual weighted norms.
        for _ in range(300):
            x = [rng.uniform(-4.,4.) for _ in range(n)]
            y = [rng.uniform(-4.,4.) for _ in range(n)]
            p = project_ellipsoid(x,radii)
            q = project_ellipsoid(y,radii)
            d = [a-b for a,b in zip(p,q)]
            v = [a-b for a,b in zip(x,y)]
            assert norm_infty(d,w) <= L*norm_infty(v,w)+5e-10
            assert norm_one(d,w) <= L*norm_one(v,w)+5e-10
            checked += 2
    # Cube clamping has constant exactly one in both norms.
    for n in (2,3,5):
        w = [1.+j*.25 for j in range(n)]
        for _ in range(300):
            x = [rng.uniform(-3,3) for _ in range(n)]
            y = [rng.uniform(-3,3) for _ in range(n)]
            p = [max(-1,min(1,z)) for z in x]
            q = [max(-1,min(1,z)) for z in y]
            d = [a-b for a,b in zip(p,q)]
            v = [a-b for a,b in zip(x,y)]
            assert norm_infty(d,w) <= norm_infty(v,w)+1e-12
            assert norm_one(d,w) <= norm_one(v,w)+1e-12
            checked += 2
    print('PASS:',checked,'supplementary checks; proof is analytic')

if __name__ == '__main__':
    check()
