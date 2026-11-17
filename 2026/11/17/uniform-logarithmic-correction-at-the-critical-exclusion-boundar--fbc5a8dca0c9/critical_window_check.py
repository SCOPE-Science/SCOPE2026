"""Independent numerical checks of a two-term reciprocal crossover for a quadratic map.

Finite tests do not certify the uniform asymptotic theorem, which has an analytic proof.
"""
from math import exp, expm1, log, isfinite


def reciprocals(n, r, gamma, tau, t):
    z, u = r, r + tau / n
    assert 0 < z < 1 and 0 < u < 1
    steps = int(n * t)
    for _ in range(steps):
        zn = z * (1 - gamma * u)
        un = u * (1 - gamma * z)
        z, u = zn, un
    return 1 / z, 1 / u, z, u


def leading(gamma, tau, t):
    return gamma * t if tau == 0 else expm1(gamma * tau * t) / tau


def test_exact_identity():
    for gamma in (0.14, 0.6, 0.92):
        for tau in (-2., -.6, 0., .6, 2.):
            n = 1000
            z, u = .37, .37 + tau / n
            for _ in range(500):
                old_difference = u - z
                z, u = z * (1 - gamma * u), u * (1 - gamma * z)
                assert abs((u - z) - old_difference) < 2e-13


def test_two_term_log_coefficient():
    # Differencing the residual at n and 10n eliminates the unknown O(1) term.
    for gamma in (.3, .6):
        for tau in (-3., -1., 0., 1., 4.):
            for t in (.25, .6, 1.):
                residuals = []
                for n in (10000, 100000):
                    w, v, z, u = reciprocals(n, .37, gamma, tau, t)
                    assert abs((u-z) - tau/n) < 2e-12
                    residuals.append(w - n * leading(gamma, tau, t))
                estimate = (residuals[1] - residuals[0]) / log(10)
                predicted = gamma * exp(gamma * tau * t)
                assert abs(estimate - predicted) < .12 + .05 * predicted, (gamma, tau, t, estimate, predicted)


if __name__ == '__main__':
    test_exact_identity()
    test_two_term_log_coefficient()
    print('BIPOP_RECIPROCAL_LOG_WINDOW_OK exact_symmetry=7500 cases=30')
