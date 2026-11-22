"""Independent finite computations for exponential-covariance quadrature design.

Run with Python 3, NumPy and SciPy. The mathematical global theorem
is proved in RESULT.md, not by the finite tests in this file.
"""
import numpy as np
from scipy.optimize import brentq, minimize


def solution(n, lam, precision):
    assert n >= 1 and lam > 0 and precision > 0
    if n == 1:
        gap, margin = 0.0, 0.5
    else:
        def equation(gap):
            margin = (1.0 - (n - 1) * gap) / 2
            tau = np.tanh(lam * gap / 2)
            return (-np.expm1(-lam * margin)) / (1 + n / precision) - tau / (1 + n * tau / precision)
        gap = brentq(equation, 0, 1 / (n - 1), xtol=3e-15)
        margin = (1 - (n - 1) * gap) / 2
    times = margin + gap * np.arange(n)
    weight = (2 / lam) * (-np.expm1(-lam * margin)) / (1 + n / precision)
    weights = np.full(n, weight)
    allocated_precision = np.full(n, precision / n)
    return times, weights, allocated_precision, gap, margin


def kernel_terms(times, lam):
    times = np.asarray(times)
    covariance = np.exp(-lam * np.abs(times[:, None] - times[None, :]))
    kernel_mean = (2 - np.exp(-lam * times) - np.exp(-lam * (1 - times))) / lam
    prior_integral_variance = 2 * (lam + np.expm1(-lam)) / lam**2
    return covariance, kernel_mean, prior_integral_variance


def posterior_risk(times, precisions, lam):
    covariance, kernel_mean, var = kernel_terms(times, lam)
    coeff = np.linalg.solve(covariance + np.diag(1 / precisions), kernel_mean)
    return var - kernel_mean @ coeff, coeff


def test_all():
    assertions = 0
    for lam in (0.2, 1., 2., 7.):
        for total_p in (0.05, 0.8, 3., 30.):
            for n in (1, 2, 3, 4, 5, 6):
                times, weights, p, gap, margin = solution(n, lam, total_p)
                posterior, coeff = posterior_risk(times, p, lam)
                cov, mean, var = kernel_terms(times, lam)
                formula = var - weights @ mean
                assert np.allclose(weights, coeff, atol=5e-11, rtol=2e-9)
                assert abs(posterior - formula) < 5e-11
                assertions += 2
                assert np.max(np.abs(times + times[::-1] - 1)) < 4e-12
                assertions += 1
                assert np.max(abs(p - total_p / n)) < 1e-12
                assertions += 1
                if n > 1:
                    tau = np.tanh(lam * gap / 2)
                    assert abs(weights[0] - (2 / lam) * tau / (1 + n * tau / total_p)) < 5e-11
                    assert abs(gap * (n - 1) + 2 * margin - 1) < 2e-12
                    assertions += 2
                    if total_p < n:
                        assert margin > gap
                    elif total_p > n:
                        assert margin < gap
                    else:
                        assert abs(margin - gap) < 1e-10
                    assertions += 1
    for lam in (0.1, 1., 3., 17.):
        for n in range(1, 9):
            times, _, _, gap, margin = solution(n, lam, n)
            assert np.max(np.abs(times - np.arange(1, n + 1) / (n + 1))) < 3e-12
            assertions += 1
    rng = np.random.default_rng(6127)
    comparisons = 0
    # Tests do not establish the global result: each compares finitely many designs.
    for lam in (0.6, 2.1, 5.2):
        for total_p in (0.4, 2.5, 8.):
            for n in (2, 3, 4, 5):
                times, _, p, _, _ = solution(n, lam, total_p)
                optimum, _ = posterior_risk(times, p, lam)
                for j in range(125):
                    trial_times = np.sort(rng.uniform(0, 1, size=n))
                    allocation = rng.dirichlet(np.ones(n)) * total_p
                    trial_risk, _ = posterior_risk(trial_times, allocation, lam)
                    assert trial_risk > optimum - 1e-9
                    comparisons += 1
                # Fix random times and minimize over all precision distributions.
                # The numerical optimizer is only a stress test.
                for j in range(8):
                    trial_times = np.sort(rng.uniform(0, 1, size=n))
                    def objective(z):
                        return posterior_risk(trial_times, z, lam)[0]
                    optimized = minimize(objective, np.full(n, total_p / n),
                        method='SLSQP', bounds=[(1e-8, total_p)] * n,
                        constraints=[{'type':'eq', 'fun':lambda z: z.sum() - total_p}],
                        options={'maxiter':350, 'ftol':1e-12})
                    assert optimized.fun > optimum - 1e-9
                    comparisons += 1
    print('PASS', assertions, 'formula and design assertions;', comparisons,
          'finite competitor comparisons')


if __name__ == '__main__':
    test_all()
