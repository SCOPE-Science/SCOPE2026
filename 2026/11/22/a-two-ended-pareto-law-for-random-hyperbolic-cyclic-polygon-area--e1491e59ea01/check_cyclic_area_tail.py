"""Numerical consistency tests for a hyperbolic cyclic-polygon area-deficit law.

These tests are finite diagnostics, not proofs of distributional limits.
Requires Python 3 and NumPy.
"""
import math
import numpy as np


def area_from_edges(gaps, radius):
    z = math.tanh(radius / 2.0) ** 2
    return float(np.sum(2.0 * np.arctan2(z * np.sin(gaps),
                                          1.0 - z * np.cos(gaps))))


def area_from_angles(gaps, radius):
    scale = 1.0 / math.cosh(radius)
    f = np.arctan(scale / np.tan(gaps / 2.0))
    return float((len(gaps) - 2) * math.pi - 2.0 * np.sum(f))


def limit_variable(gaps):
    n = len(gaps)
    return float(4.0 * np.sum(1.0 / np.tan(gaps / 2.0))
                 - 4.0 * n / math.tan(math.pi / n))


def near_regular_coefficient(n):
    s, c = math.sin(math.pi/n), math.cos(math.pi/n)
    h = c / (s ** 3)
    k = (math.factorial(n - 1) * math.pi ** ((n - 1)/2.0)
         / ((2.0 * math.pi) ** (n - 1)
            * math.gamma((n + 1)/2.0) * math.sqrt(n) * h ** ((n - 1)/2.0)))
    return h, k


def run():
    rng = np.random.default_rng(20261120)
    counts = 0
    for n in (3, 4, 5, 7):
        reg = np.full(n, 2.0 * math.pi / n)
        for _ in range(40):
            g = rng.dirichlet(np.ones(n)) * 2.0 * math.pi
            for R in (0.3, 1.2, 3.1, 9.0):
                a = area_from_edges(g, R)
                b = area_from_angles(g, R)
                assert abs(a-b) < 1e-9, (n, R, a, b)
                assert a > 0 and a <= area_from_edges(reg, R) + 2e-13
                counts += 2
        for R in (5., 9., 13.):
            g = rng.dirichlet(np.ones(n)) * 2.0 * math.pi
            exact = math.exp(R)*(area_from_edges(reg, R)-area_from_edges(g, R))
            lim = limit_variable(g)
            rel = abs(exact - lim) / max(1.0, lim)
            assert rel < 20.0*math.exp(-R), (n,R,rel)
            counts += 1
        h, k = near_regular_coefficient(n)
        for eps in (1e-4, 1e-3, 4e-3):
            u = rng.normal(size=n)
            u -= np.mean(u)
            g = reg + eps * u
            z = limit_variable(g)
            quad = h*np.sum((eps*u)**2)
            assert abs(z/quad-1.0) < 0.05, (n,eps,z,quad)
            counts += 1
        assert h > 0 and k > 0
    # Independently sample Dirichlet gaps and estimate the sharp tail coefficient.
    # The threshold is moderate enough to observe thousands of rare events.
    for n in (3, 4, 5):
        samples = rng.dirichlet(np.ones(n), size=1_500_000) * 2.0*math.pi
        z = (4.0*np.sum(1.0/np.tan(samples/2.0),axis=1)
             - 4.0*n/math.tan(math.pi/n))
        t = 1800.0
        est = t * float(np.mean(z>t))
        predicted = 4.0*n*(n-1)/math.pi
        assert abs(est/predicted-1.0) < 0.11, (n,est,predicted)
        # Conditioning on an extreme event gives a uniform rescaled shortest gap.
        indices = np.where(z > t)[0]
        marks = t*np.min(samples[indices],axis=1)/8.0
        assert abs(float(np.mean(marks)) - 0.5) < 0.045
        counts += 2
    print(f'HYPERBOLIC_CYCLIC_PARETO_CHECK_OK ({counts} deterministic checks)')


if __name__ == '__main__':
    run()
