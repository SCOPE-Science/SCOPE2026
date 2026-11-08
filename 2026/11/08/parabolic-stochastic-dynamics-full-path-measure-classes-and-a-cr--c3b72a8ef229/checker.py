"""Finite exact and numerical checks for parabolic stochastic-map path laws."""
from fractions import Fraction
from math import exp, log, sqrt


def h(gamma, x):
    return (x ** (-gamma) + 1.0) ** (-1.0 / gamma) if x else 0.0


def pn(gamma, x, n):
    return (x ** (-gamma) + n) ** (-1.0 / gamma)


def assert_close(x, y, tol=1e-11):
    assert abs(x - y) <= tol * max(1.0, abs(x), abs(y)), (x, y)


# (1) Exact parabolic iterate for gamma=1, all rational arithmetic.
for s in [Fraction(1, 6), Fraction(2, 3), Fraction(1)]:
    t = s
    for n in range(1, 300):
        t = t / (1 + t)
        assert t == s / (1 + n * s)
print('PARABOLIC_EXACT_ITERATE_RATIONAL_OK')

# (2) The B_n coupling errors have a summable O(n^(-1-1/gamma)) envelope.
for gamma in [0.6, 1.0, 1.75, 3.0]:
    alpha = 1.0 / gamma
    for x in [0.12, 0.54, 1.0]:
        a = x ** (-gamma)
        upper = alpha * (a - 1.0)
        for n in [1, 2, 3, 10, 100, 1000, 100000]:
            d = abs(pn(gamma, x, n) - (n + 1) ** (-alpha))
            assert d <= upper * (n + 1) ** (-alpha - 1) * (1 + 1e-12)
print('FINITE_DEFECT_COUPLING_BOUND_OK')

# (3) Conditional Bernoulli row chi-square identity and its summable asymptotic.
for gamma in [0.75, 1.0, 2.0]:
    alpha = 1.0 / gamma
    for n in [5, 10, 100, 1000, 10000]:
        p, q = pn(gamma, 0.4, n), (n + 1) ** (-alpha)
        chisq = p*p/q + (1-p)*(1-p)/(1-q) - 1
        ref = (p-q)**2/(q*(1-q))
        assert_close(chisq, ref, 1e-10)
        assert ref * n**(2 + alpha) < 500.0
print('LIKELIHOOD_SECOND_MOMENT_BOUND_OK')

# (4) Exact independent comparison means, variances and critical-window integral.
for u in [-2.0, -0.5, 0, 0.75, 3.0]:
    ell = exp(u) - 1
    ell = ell/u if u else 1.0
    for N in [30000, 100000, 300000]:
        alpha = 1/(1 + u/log(N))
        mean = sum((n+1)**(-alpha) for n in range(1, N+1))
        variance = sum(((n+1)**(-alpha))*(1 - (n+1)**(-alpha)) for n in range(1, N+1))
        # A nonasymptotic O(1) deviation, with generous allowance for u=3.
        assert abs(mean - ell*log(N)) < 100.0, (u,N,mean,ell*log(N))
        assert abs(mean-variance)<5.0, (u,N,mean,variance)
print('TRIANGULAR_CRITICAL_WINDOW_MEAN_VARIANCE_OK')
print('PARABOLIC_MARKOV_PATH_CHECK_OK')
