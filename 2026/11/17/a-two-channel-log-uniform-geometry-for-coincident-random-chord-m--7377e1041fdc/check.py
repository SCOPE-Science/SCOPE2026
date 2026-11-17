"""Reproducible numerical checks for near-colliding independently endpoint-uniform chord midpoints.
This script tests finite precision consequences; the limiting theorem uses analytic arguments.
Run with Python 3 and numpy.
"""
import math
import numpy as np

PI = math.pi
C_LOG = 3 / PI**2
C_CONST = (6 * math.log(2) + 1.5) / PI**2


def midpoint_density_radius(r):
    assert 0 < r < 1
    return 1.0 / (PI**2 * r * math.sqrt(1.0 - r*r))


def log_band_integral(lo, hi):
    # integral_{lo<|z|<hi} f(z)^2 dz; stable for the ranges tested
    F = lambda r: math.log(r) - .5 * math.log1p(-r*r)
    return 2.0 / PI**3 * (F(hi) - F(lo))


def check_log_band_coefficients():
    epsilon, a, b = 1.0e-12, .2, .8
    L = math.log(1.0 / epsilon)
    center = log_band_integral(epsilon**b, epsilon**a) / L
    rim = log_band_integral(1.0 - epsilon**a, 1.0 - epsilon**b) / L
    target_center = 2 * (b-a) / PI**3
    target_rim = (b-a) / PI**3
    assert abs(center / target_center - 1) < .01, (center, target_center)
    assert abs(rim / target_rim - 1) < .01, (rim, target_rim)
    print('SQUARED_DENSITY_TWO_SINGULARITIES_OK', center, rim)


def check_marked_density():
    # Exact density of (mechanism, log radius mark, midpoint angle, scaled difference),
    # divided by eps^2 log(1/eps). For a.e. 0<t<1 it tends to 1/pi^4
    # for near-center, 1/(2*pi^4) for near-boundary.
    for mechanism in (0, 1):
        target = 1 / (PI**4 * (1+mechanism))
        for t in (.2, .5, .8):
            eps = 1e-10
            radius = eps**t if mechanism == 0 else 1-eps**t
            y = radius - .4*eps  # relative displacement along the radial line
            jac_over_log = radius if mechanism == 0 else eps**t
            scaled = (midpoint_density_radius(radius)
                      * midpoint_density_radius(y) * radius * jac_over_log)
            assert abs(scaled/target-1) < .025, (mechanism,t,scaled,target)
    print('MARKED_DENSITY_LIMITS_OK')


def check_simulation():
    rng = np.random.default_rng(20261111)
    count = 4_000_000
    hit = np.zeros(2, dtype=np.int64)
    eps_values = np.array([.05, .02])
    for _ in range(8):
        angle = rng.uniform(0, 2 * PI, (4, count//8))
        x = (np.exp(1j*angle[0]) + np.exp(1j*angle[1]))/2
        y = (np.exp(1j*angle[2]) + np.exp(1j*angle[3]))/2
        distance = np.abs(y - x)
        hit += np.array([(distance < e).sum() for e in eps_values])
    for epsilon, number in zip(eps_values, hit):
        empirical = number / count
        prior_two_term = epsilon**2 * (C_LOG*math.log(1/epsilon)+C_CONST)
        assert abs(empirical-prior_two_term) < .09*prior_two_term, (epsilon,empirical,prior_two_term)
        print('FOUR_ENDPOINT_CARTESIAN_SIMULATION',epsilon,empirical,prior_two_term,int(number))
    print('NEAR_MIDPOINT_COLLISION_DIAGNOSTICS_OK')

if __name__ == '__main__':
    check_log_band_coefficients()
    check_marked_density()
    check_simulation()
