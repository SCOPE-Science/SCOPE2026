"""Reproducible checks for octahedral shadow circumradius and silhouette type.

Requires Python 3, numpy and scipy; checks are finite diagnostics, not proofs.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.spatial import ConvexHull

PI = math.pi
M = 1 / math.sqrt(3)
C = 1 / math.sqrt(6)
RMIN = math.sqrt(2 / 3)
R4MIN = math.sqrt(5 / 6)


def phi_min(c):
    return math.asin(c / math.sqrt(1 - c*c))


def phi_boundary(c):
    return math.acos(c / math.sqrt(2 * (1 - c*c))) - PI/4


def l4(c):
    return max(0.0, phi_boundary(c) - phi_min(c)) if c < C else 0.0


def l6(c):
    return PI/4 - phi_min(c) - l4(c)


def joint_cdf4(r):
    if r <= R4MIN:
        return 0.0
    if r >= 1:
        return p4
    t = math.sqrt(1 - r*r)
    return (12/PI) * quad(l4, t, C, epsabs=2e-12, epsrel=2e-12)[0]


def survival_min(c):
    if c <= 0:
        return 1.0
    if c >= M:
        return 0.0
    return 1-3*c + (12/PI) * (
        c*phi_min(c) + math.atan(math.sqrt(1-2*c*c)) - PI/4
    )


def joint_cdf6(r):
    if r <= RMIN:
        return 0.0
    if r >= 1:
        return p6
    return survival_min(math.sqrt(1-r*r)) - joint_cdf4(r)


p6 = 4 / PI * math.atan(math.sqrt(2)/5)
p4 = 1 - p6


def projection_vertices(u):
    u = u / np.linalg.norm(u)
    reference = np.eye(3)[int(np.argmin(np.abs(u)))]
    e = np.cross(u, reference)
    e /= np.linalg.norm(e)
    f = np.cross(u, e)
    return np.vstack((np.eye(3), -np.eye(3))) @ np.column_stack((e, f))


def main():
    rng = np.random.default_rng(20261107)
    # The exact silhouette criterion and radius formula are checked against
    # independently computed two-dimensional convex hulls.
    hull_checks = 2400
    for _ in range(hull_checks):
        u = rng.standard_normal(3)
        u /= np.linalg.norm(u)
        pts = projection_vertices(u)
        n = len(ConvexHull(pts).vertices)
        a, b, c = np.sort(np.abs(u))[::-1]
        predicted_n = 4 if a > b+c else 6
        assert n == predicted_n, (n, predicted_n, u)
        expected_radius = math.sqrt(1-c*c)
        actual_radius = float(np.max(np.linalg.norm(pts, axis=1)))
        assert abs(actual_radius-expected_radius) < 1e-13

    # Compare quadrature to an independently parameterized spherical sample.
    sample_count = 600000
    u = rng.standard_normal(size=(sample_count, 3))
    u /= np.linalg.norm(u, axis=1)[:, None]
    ordered = np.sort(np.abs(u), axis=1)
    m = ordered[:, 0]
    R = np.sqrt(1-m*m)
    is4 = ordered[:, 2] >= ordered[:, 1] + ordered[:, 0]
    assert abs(is4.mean()-p4) < 0.003
    assert abs(np.mean(R*R) - (2/3 + 2/PI*(1-1/math.sqrt(3)))) < 0.003
    for r in (0.825, 0.85, 0.875, R4MIN, 0.93, 0.95, 0.97, 0.985, 0.997):
        err4 = abs(np.mean(is4 & (R <= r)) - joint_cdf4(r))
        err6 = abs(np.mean(~is4 & (R <= r)) - joint_cdf6(r))
        assert err4 < 0.003 and err6 < 0.003, (r, err4, err6)
    # Global law, numerical volume and monotone conditional comparison.
    q4 = (12/PI) * quad(l4, 0, C, epsabs=2e-13)[0]
    assert abs(q4-p4) < 1e-12, (q4, p4)
    assert abs(survival_min(0)-1) < 1e-14
    assert abs(survival_min(M)) < 1e-14
    rvals = np.linspace(RMIN+0.001, 0.999, 48)
    for r in rvals:
        f4 = joint_cdf4(r)
        f6 = joint_cdf6(r)
        assert -1e-11 <= f4 <= p4+1e-11
        assert -1e-11 <= f6 <= p6+1e-11
        assert f4/p4 < f6/p6
    # Four distinct boundary constants, not estimated from random sampling.
    k4low = 30*math.sqrt(6)/PI
    k6low = 18*math.sqrt(3)/PI
    k4top = 3*math.sqrt(2)
    k6top = 6*math.sqrt(2)/PI
    for eps in (2e-3, 5e-4, 1e-4):
        lower4 = joint_cdf4(R4MIN+eps)/eps**2
        lower6 = joint_cdf6(RMIN+eps)/eps**2
        upper4 = (p4-joint_cdf4(1-eps))/math.sqrt(eps)
        upper6 = (p6-joint_cdf6(1-eps))/eps
        assert abs(lower4/k4low-1) < 0.03
        assert abs(lower6/k6low-1) < 0.03
        assert abs(upper4/k4top-1) < 0.12
        assert abs(upper6/k6top-1) < 0.002
    print('OCTAHEDRON_SHADOW_RADIUS_SILHOUETTE_LAW_OK', sample_count, hull_checks, len(rvals))


if __name__ == '__main__':
    main()
