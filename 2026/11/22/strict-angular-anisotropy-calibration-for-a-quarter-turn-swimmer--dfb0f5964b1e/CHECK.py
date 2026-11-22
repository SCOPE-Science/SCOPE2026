"""Numerical cross-checks for the fourfold positional-angle response.

Requires Python >=3.10, NumPy and SciPy. The infinite-parameter theorem
rests on the accompanying mathematical proof, not on these finite checks.
"""
import math
import numpy as np
from scipy.special import roots_jacobi
from scipy.stats import qmc, beta as beta_distribution


def jacobi_response(a: float, n: int = 420) -> float:
    """Tensor Gauss-Jacobi quadrature under two Beta(1/2,a) laws."""
    nodes, weights = roots_jacobi(n, a-1., -.5)
    t = (nodes + 1) / 2
    w = weights / np.sum(weights)
    ratio = t[:, None] * t[None, :] / (t[:, None] + t[None, :]) ** 2
    return float(-1 + 8 * np.sum(w[:, None] * w[None, :] * ratio))


def quasi_mc_responses(parameters, exponent: int = 19):
    """Independent bounded integrand representation using scrambled Sobol points."""
    uv = qmc.Sobol(d=2, scramble=True, seed=1729).random_base2(exponent)
    for a in parameters:
        x, y = beta_distribution.ppf(uv, .5, a).T
        yield a, float(np.mean(-1 + 8*x*y/(x+y)**2))


def exact_uniform_angle_response():
    """For a=1, integrate cos(4phi) against the uniform square's polar law."""
    # cos(4t) / cos(t)^2 = 8cos(t)^2 - 8 + sec(t)^2.
    integral = (math.pi + 2.) - 2*math.pi + 1.
    return -integral  # physical angle is rotated by 45 degrees


def main():
    checks = 0
    exact = math.pi - 3
    assert abs(exact_uniform_angle_response() - exact) < 1e-14
    checks += 1
    grid = [.125, .25, .5, 1., 2., 4.]
    quad = [(a, jacobi_response(a)) for a in grid]
    for a, value in quad:
        assert 0. < value < 1., (a, value)
        checks += 1
    for (_, x), (_, y) in zip(quad, quad[1:]):
        assert x > y, (x, y)
        checks += 1
    assert abs(jacobi_response(1.) - exact) < 1.3e-5
    checks += 1
    grid_all = [.125, .25, .5, 1., 2., 4., 10., 30., 100.]
    mc = list(quasi_mc_responses(grid_all))
    for a, value in mc:
        assert 0. < value < 1., (a, value)
        checks += 1
    for (_, x), (_, y) in zip(mc, mc[1:]):
        assert x > y, (x, y)
        checks += 1
    for (a, v1), (_, v2) in zip(quad, mc):
        assert abs(v1 - v2) < .0015, (a, v1, v2)
        checks += 1
    assert abs(dict(mc)[1.] - exact) < .001
    checks += 1
    assert abs(100 * dict(mc)[100.] - 1./8.) < .008
    checks += 1
    print(f'PASS: {checks} analytic-anchor, positivity, monotonicity, quadrature, and asymptotic checks')
    for a, response in mc:
        print(f'a={a:7g}, Q={response:.9f}')


if __name__ == '__main__':
    main()
