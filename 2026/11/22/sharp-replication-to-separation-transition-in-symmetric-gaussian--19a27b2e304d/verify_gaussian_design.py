"""Independent numerical checks of the exact Gaussian-kernel mirror-design theorem.

Run with Python 3.10+; no third-party dependencies. Numerical comparisons
illustrate, but do not replace, the analytical proof in RESULT.md.
"""
import math
import random


def selected_parameters(ell, tau, budget):
    threshold = ell * ell / (tau * tau)
    alpha = 1.0 + 2.0 * tau * tau / (ell * ell)
    nugget = 1.0 + 2.0 / budget
    if budget <= threshold:
        return 0.0, threshold
    return math.sqrt(0.5 * ell * ell * math.log(alpha / nugget)), threshold


def explained_closed(ell, tau, budget, a, p):
    """Closed expression from analytic conditioning; p is left precision."""
    q = budget - p
    s = ell * ell + tau * tau
    mu2 = ell * ell / s * math.exp(-a * a / s)
    k = math.exp(-2.0 * a * a / (ell * ell))
    z = p * q
    return mu2 * (budget + 2.0 * (1.0 - k) * z) / (
        1.0 + budget + (1.0 - k * k) * z
    )


def explained_direct(ell, tau, budget, a, p):
    """Direct inversion of the raw covariance for two independent noisy readings."""
    q = budget - p
    s = ell * ell + tau * tau
    mu = ell / math.sqrt(s) * math.exp(-a * a / (2.0 * s))
    if p == 0.0 or q == 0.0:
        return mu * mu * budget / (1.0 + budget)
    k = math.exp(-2.0 * a * a / (ell * ell))
    aa = 1.0 + 1.0 / p
    bb = 1.0 + 1.0 / q
    determinant = aa * bb - k * k
    return mu * mu * (aa + bb - 2.0 * k) / determinant


def optimum_risk(ell, tau, budget):
    a, _ = selected_parameters(ell, tau, budget)
    prior = 1.0 / math.sqrt(1.0 + 2.0 * tau * tau / (ell * ell))
    return prior - explained_closed(ell, tau, budget, a, budget / 2.0)


def run():
    rng = random.Random(14012026)
    checks = 0
    for _ in range(16000):
        ell = math.exp(rng.uniform(-1.3, 1.3))
        tau = math.exp(rng.uniform(-1.3, 1.3))
        budget = math.exp(rng.uniform(-2.5, 3.0))
        a_star, threshold = selected_parameters(ell, tau, budget)
        a = 0.0 if rng.random() < 0.08 else rng.uniform(0.0, 3.5 * ell + 2.0 * tau)
        p = budget * rng.random()
        closed = explained_closed(ell, tau, budget, a, p)
        direct = explained_direct(ell, tau, budget, a, p)
        assert math.isclose(closed, direct, rel_tol=4e-11, abs_tol=2e-13), (ell, tau, budget, a, p, closed, direct)
        checks += 1
        best = explained_closed(ell, tau, budget, a_star, budget / 2.0)
        assert closed <= best + 2e-12, (ell, tau, budget, a_star, a, p, best, closed)
        checks += 1
        assert optimum_risk(ell, tau, budget) >= -3e-12
        checks += 1
        if a > 1e-5 and 0 < p < budget:
            assert closed <= explained_closed(ell, tau, budget, a, budget / 2.0) + 2e-12
            checks += 1
        if budget <= threshold:
            assert a_star == 0.0
        else:
            assert a_star > 0.0
        checks += 1
    ell, tau = 1.0, 1.0
    for budget in [0.1, 0.25, 0.5, 0.99, 1.0, 1.01, 1.4, 2, 10, 100]:
        a, threshold = selected_parameters(ell, tau, budget)
        assert threshold == 1.0
        if budget <= 1.0:
            assert a == 0.0
            for p in [0.0, budget / 4.0, budget / 2.0, budget]:
                assert math.isclose(explained_closed(ell, tau, budget, a, p), 0.5 * budget / (budget + 1.0), abs_tol=1e-13)
                checks += 1
        else:
            expected = math.sqrt(0.5 * math.log(3.0 / (1.0 + 2.0 / budget)))
            assert math.isclose(a, expected, abs_tol=1e-14)
            checks += 1
    for ell, tau in [(0.5, 1.0), (1.0, 0.5), (1.0, 1.0), (2.0, 1.0)]:
        pc = ell * ell / (tau * tau)
        for delta in [1e-4, 1e-5, 1e-6]:
            a, _ = selected_parameters(ell, tau, pc + delta)
            coefficient = tau * tau / math.sqrt(ell * ell + 2.0 * tau * tau)
            assert abs(a / math.sqrt(delta) / coefficient - 1) < 5e-3
            checks += 1
    print(f'PASS: {checks} independent numerical formula/competitor/boundary checks')
    print('Example ell=tau=1: critical budget P=1, noiseless half-gap=sqrt(log(3)/2)')
    print('Example P=10: optimal half-gap', selected_parameters(1, 1, 10)[0])


if __name__ == '__main__':
    run()
