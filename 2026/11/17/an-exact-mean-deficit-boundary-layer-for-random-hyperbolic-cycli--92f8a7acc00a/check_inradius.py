"""Numerical corroboration of a boundary-layer inradius asymptotic.

Run: python check_inradius.py
Uses numpy and scipy. Numerical tests do not substitute for the analytic proof.
"""
import math
import numpy as np
from scipy.integrate import quad

R_STAR = math.atanh(0.5)
I_EXACT = math.pi - 4/math.sqrt(3)*math.atanh(1/math.sqrt(3))
C_EXACT = 3*I_EXACT/math.pi


def inradius_from_sides(R, gaps):
    gaps = np.asarray(gaps, dtype=float)
    sides = 2*np.arcsinh(np.sinh(R)*np.sin(gaps/2))
    s = sides.sum(axis=-1)/2
    u = np.exp(2*(sides - s[..., None]))
    q = np.prod(1-u, axis=-1)/(1-np.prod(u, axis=-1))
    return np.arctanh(0.5*np.sqrt(np.clip(q, 0, 1)))


def inradius_from_minkowski(R, angles):
    """Independent geodesic-normal computation in the hyperboloid model."""
    pts = np.column_stack((np.full(3, np.cosh(R)),
                           np.sinh(R)*np.cos(angles),
                           np.sinh(R)*np.sin(angles)))
    J = np.diag([-1.0, 1.0, 1.0])
    normals = []
    for i in range(3):
        j, k = (i+1)%3, (i+2)%3
        normal = J @ np.cross(pts[j], pts[k])
        normal /= math.sqrt(normal @ J @ normal)
        if normal @ J @ pts[i] < 0:
            normal = -normal
        normals.append(normal @ J)
    v = np.linalg.solve(np.array(normals), np.ones(3))
    return math.asinh(1/math.sqrt(-v @ J @ v))


def boundary_deficit(x):
    z = np.exp(-2*np.arcsinh(np.asarray(x)/4))
    return 0.5*np.log(3*(1+z)/(3-z))


if __name__ == '__main__':
    for R in [0.5, 1.0, 2.0, 3.0, 4.0]:
        for g1, g2 in [(.3, 1.4), (1.1, 2.2), (2.0, .05)]:
            gaps = np.array([g1, g2, 2*np.pi-g1-g2])
            alt = inradius_from_minkowski(R, np.array([0,g1,g1+g2]))
            side = inradius_from_sides(R, gaps)
            assert abs(alt-side) < 2e-9, (R, gaps, alt, side)
    print('Independent hyperboloid and side-length inradii: OK')

    for x in [0.1, 0.5, 1., 2., 5., 12.]:
        for R in [8, 10]:
            g = np.array([x*np.exp(-R), 2., 2*np.pi-2.-x*np.exp(-R)])
            d = R_STAR - inradius_from_sides(R, g)
            assert abs(d-boundary_deficit(x)) < 1e-5, (x, R, d)
    print('Rare-angular-gap boundary profile: OK')

    I_QUAD = quad(lambda z: 8*(1-z*z)/((1+z*z)*(3-z*z)),
                  0., 1., epsabs=1e-12)[0]
    assert abs(I_QUAD-I_EXACT) < 1e-11
    I_PROFILE = quad(lambda x: boundary_deficit(x), 0., np.inf, epsabs=1e-10)[0]
    assert abs(I_PROFILE-I_EXACT) < 1e-8
    print('Two independent boundary-integral calculations: OK')

    rng = np.random.default_rng(20261113)
    gaps = rng.dirichlet([1., 1., 1.], 1200000)*2*np.pi
    for R in [4., 5., 6., 7.]:
        sample_mean = np.exp(R)*np.mean(R_STAR-inradius_from_sides(R, gaps))
        print('R=',R,'scaled deficit mean=',float(sample_mean))
        assert abs(sample_mean-C_EXACT) < 0.085
    print('Predicted exact constant:',repr(C_EXACT))
    print('HYPERBOLIC_INRADIUS_BOUNDARY_CHECKS_OK')
