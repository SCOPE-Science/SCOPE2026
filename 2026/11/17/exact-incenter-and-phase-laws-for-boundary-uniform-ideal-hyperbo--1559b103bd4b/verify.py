#!/usr/bin/env python3
"""Independent numerical checks for ideal-triangle hyperbolic incenter laws.

Requires NumPy and SciPy. All samples are generated directly as boundary triples.
The incenter is reconstructed through a generic fractional-linear interpolation,
not from the analytic density or Jacobian used in the proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.stats import kstest

PI = math.pi
SQ3 = math.sqrt(3)


def radial_cdf(radius):
    radius = np.asarray(radius)
    return (6 / PI) * (np.arctan((1 + 2 * radius ** 2) / SQ3) - PI / 6)


def density(x, y):
    q = x*x + y*y
    return 3 * SQ3 / (PI * PI * (1 + q + q*q))


def direct_incenters(theta):
    # Sort boundary points and match them to the 3 cubic roots in positive order.
    theta = np.sort(theta, axis=1)
    points = np.exp(1j * theta)
    w = np.exp(2j * PI * np.arange(3) / 3)
    m = np.empty((len(theta), 3, 3), dtype=complex)
    m[:, :, 0] = w
    m[:, :, 1] = 1
    m[:, :, 2] = -points * w
    # Fractional linear map (A*w+B)/(C*w+1) agrees at all three vertices;
    # as the triples have the same cyclic order, it is a disk automorphism.
    a_b_c = np.linalg.solve(m, points[:, :, None])[:, :, 0]
    z = a_b_c[:, 1]
    return z, points


def map_angles(x, y, t):
    z = complex(x, y)
    w = np.exp(1j * (t + 2*PI*np.arange(3)/3))
    v = (z + w)/(1 + np.conjugate(z)*w)
    return np.angle(v)


def check_jacobian():
    h = 2e-6
    rng = np.random.default_rng(310)
    for _ in range(12):
        x, y = rng.uniform(-0.55, 0.55, size=2)
        t = rng.uniform(-PI, PI)
        z = complex(x, y)
        if abs(z) >= 0.9:
            continue
        jac = np.zeros((3,3))
        for j, (dx,dy,dt) in enumerate(((h,0,0),(0,h,0),(0,0,h))):
            ap = map_angles(x+dx,y+dy,t+dt)
            am = map_angles(x-dx,y-dy,t-dt)
            jac[:,j] = np.angle(np.exp(1j*(ap-am)))/(2*h)
        got = abs(np.linalg.det(jac))
        target = 6*SQ3*(1-abs(z)**2)/abs(1+(np.conjugate(z)*np.exp(1j*t))**3)**2
        assert abs(got/target - 1) < 2e-7, (got,target)
    print('JACOBIAN_FINITE_DIFFERENCES_OK')


def check_radial():
    val = quad(lambda u: (3*SQ3/PI)/(1+u+u*u), 0, 1,
               epsabs=1e-13, epsrel=1e-13)[0]
    assert abs(val-1) < 1e-12
    for r in (0.1,0.35,0.6,0.9):
        direct = quad(lambda q: 2*PI*q*density(q,0), 0, r)[0]
        assert abs(direct-radial_cdf(r)) < 1e-12
    expected_q = 3*SQ3*math.log(3)/(2*PI)-0.5
    mean = quad(lambda u: (3*SQ3/PI)*u/(1+u+u*u), 0, 1)[0]
    assert abs(mean-expected_q)<1e-12
    for T in (8,10,12):
        tail = 1-radial_cdf(math.tanh(T/2))
        asympt = (4*SQ3/PI)*math.exp(-T)
        assert abs(tail/asympt-1)<2.5e-3
    print('NORMALIZATION_MOMENT_HYPERBOLIC_TAIL_OK')


def check_sampling():
    rng = np.random.default_rng(91427)
    n = 120000
    theta = rng.uniform(0, 2*PI, (n,3))
    centers, points = direct_incenters(theta)
    radius = np.abs(centers)
    assert (radius<1).all()
    d,p = kstest(radius, radial_cdf)
    assert d < 0.013, (d,p)
    for a in (0.25,0.5,0.75,0.9):
        discrepancy = abs(np.mean(radius<=a)-radial_cdf(a))
        assert discrepancy < 0.009, (a,discrepancy)
    # Conditional phase is a Poisson kernel with Fourier coefficient -|z|^3.
    phase = (points[:,0]-centers)/(1-np.conjugate(centers)*points[:,0])
    t = np.angle(phase)
    residue = np.exp(3j*(t-np.angle(centers)))+radius**3
    assert abs(residue.mean()) < 0.012, residue.mean()
    for lo,hi in ((0.,.4),(.4,.7),(.7,.9),(.9,1.)):
        mask=(radius>=lo)&(radius<hi)
        assert abs(residue[mask].mean()) < 0.025, (lo,hi)
    print('CARTESIAN_MOBIUS_INVERSION_AND_POISSON_PHASE_OK',
          'sample_size',n,'ks_distance',round(d,6),
          'sample_mean_squared_radius',round(float(np.mean(radius**2)),6))


if __name__ == '__main__':
    check_jacobian()
    check_radial()
    check_sampling()
    print('IDEAL_HYPERBOLIC_INCENTER_CHECKS_OK')
