"""Numerical cross-checks for the two-concentric-circle mixed-radius Sylvester profile.

Run with: python mixed_circle_check.py
Requires numpy and scipy. All claims of limits follow from the manuscript's proof,
not from these finite computations.
"""
import math
import numpy as np
from scipy.integrate import quad

PI = math.pi


def exact_profile(r):
    if not 0 <= r <= 1:
        raise ValueError('radius ratio must lie in [0,1]')
    a = lambda x: math.asin(r * math.sin(x))
    i1 = quad(lambda x: x * a(x), 0, PI/2, epsabs=3e-13, epsrel=3e-13)[0]
    i2 = quad(lambda x: a(x)**2, 0, PI/2, epsabs=3e-13, epsrel=3e-13)[0]
    return .5 + (8*i1 + 4*i2)/PI**3


def cross(a, b):
    return a[..., 0]*b[..., 1] - a[..., 1]*b[..., 0]


def triangle_contains(z, a, b, c):
    determinant = cross(b-a, c-a)
    t = cross(b-a, z-a)/determinant
    u = cross(z-a, c-a)/determinant
    return (t > 0) & (u > 0) & (t + u < 1)


def simulate(r, count=900_000, seed=1307):
    rng = np.random.default_rng(seed)
    ang = rng.uniform(0, 2*PI, (count, 4))
    sites = np.stack((np.cos(ang), np.sin(ang)), axis=-1)
    sites[:, 2:, :] *= r
    # The two outer-radius points are always vertices. Only an inner site can
    # lie in the triangle spanned by the other three.
    trapped_2 = triangle_contains(sites[:, 2], sites[:, 0], sites[:, 1], sites[:, 3])
    trapped_3 = triangle_contains(sites[:, 3], sites[:, 0], sites[:, 1], sites[:, 2])
    if np.any(trapped_2 & trapped_3):
        raise AssertionError('two vertices cannot simultaneously be interior')
    return 1 - np.mean(trapped_2 | trapped_3)


def check():
    assert abs(exact_profile(0) - .5) < 1e-13
    assert abs(exact_profile(1) - 1) < 1e-13
    rs = (0.05, 0.2, 0.5, 0.75, 0.95)
    ps = [exact_profile(r) for r in rs]
    assert all(a < b for a, b in zip(ps, ps[1:]))
    for r, predicted in zip(rs, ps):
        empirical = simulate(r, count=500_000, seed=1307+int(1000*r))
        print(f'r={r:.3f} exact={predicted:.8f} direct={empirical:.8f} delta={empirical-predicted:+.7f}')
        assert abs(empirical-predicted) < .004
    for d in (1e-4, 1e-5, 1e-6):
        value = 1 - exact_profile(1-d)
        ratio = value/(d*math.log(1/d))
        print(f'boundary delta={d:.0e} ratio={ratio:.8f} target={4/PI**2:.8f}')
        assert abs(ratio-4/PI**2) < .06
    for r in (.001,.003,.01):
        approx = .5+8*r/PI**3 + r*r/PI**2 + (28/(27*PI**3))*r**3
        assert abs(exact_profile(r)-approx) < .04*r**4
    print('MIXED_CIRCLE_PROFILE_CHECKS_OK')


if __name__ == '__main__':
    check()
