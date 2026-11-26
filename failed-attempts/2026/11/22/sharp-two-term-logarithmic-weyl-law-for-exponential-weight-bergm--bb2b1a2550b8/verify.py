"""Finite numerical diagnostics for exponential-weight Bergman Toeplitz spectra.

Requires Python 3, scipy and numpy. The infinite-dimensional theorem is proved
analytically; this file checks finite moment calculations and asymptotic scaling.
"""
from math import sqrt, log, exp, comb, factorial
import numpy as np
from scipy.integrate import quad


def log_moment(n, a):
    """Compute log integral_0^1 t^n exp(-a/(1-t)) dt stably."""
    assert n >= 1 and a > 0
    u0 = min(sqrt(a / n), 0.9)
    scale = 2 * sqrt(a * n) + a / 2
    def f(u):
        if u <= 0 or u >= 1:
            return 0.0
        return exp(n * np.log1p(-u) - a / u + scale)
    val, err = quad(f, 0.0, 1.0, points=[u0], epsabs=1e-10,
                    epsrel=1e-10, limit=300)
    assert val > 0 and err < max(val * 1e-7, 1e-10)
    return log(val) - scale


def log_eigen(n, d, a, b):
    m = n + d - 1
    return log_moment(m, a + b) - log_moment(m, a)


def test():
    cases = [(1, 1.0, 1.0), (2, 0.4, 0.2), (3, 2.0, 3.0),
             (4, 1.3, 0.5)]
    count = 0
    reports = []
    for d, a, b in cases:
        kappa = 2.0 * (sqrt(a+b)-sqrt(a))
        c = 0.25*log((a+b)/a) - 0.5*b
        errors = []
        for n in (80, 320, 1280, 5120):
            q = log_eigen(n, d, a, b)
            approximation = -kappa * sqrt(n) + c
            errors.append(abs(q-approximation) * sqrt(n))
            assert abs(q-approximation) * sqrt(n) < 40
            assert q < 0
            count += 3
            # This threshold lies strictly between two consecutive degree eigenvalues.
            q_next = log_eigen(n+1, d, a, b)
            assert q_next < q
            threshold_log = (q + q_next) / 2
            L = -threshold_log
            exact_N = comb(n+d, d)
            central = ((L+c)/kappa)**(2*d) / factorial(d)
            # The remainder must have the predicted order, without asserting a
            # universal numerical constant for all parameters.
            scaled = (exact_N-central) / (L**(2*d-2))
            assert np.isfinite(scaled) and abs(scaled) < 1e5
            count += 3
        reports.append((d, a, b, kappa, c, max(errors)))
    print('finite diagnostics passed:', count)
    for d, a, b, kap, c, err in reports:
        print('d=%d a=%.2f b=%.2f kappa=%.10f c=%.10f '
              'max_root_n_scaled_log_error=%.6f' % (d,a,b,kap,c,err))

if __name__=='__main__':
    test()
