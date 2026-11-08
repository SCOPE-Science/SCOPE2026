"""Independent finite checks of Matérn Fourier-tail identities and bounds.

Run with: python verify.py
All checks are finite; the analytic theorem supplies the infinite-series proof.
"""
from __future__ import annotations
import cmath
import itertools
import math

COUNT = 0

def check(condition, context):
    global COUNT
    COUNT += 1
    if not condition:
        raise AssertionError(context)

def spectral(xi, d, nu, ell):
    norm_sq = sum(float(t) ** 2 for t in xi)
    C = (2 ** d * math.pi ** (d / 2) * (2 * nu) ** nu
         * math.gamma(nu + d / 2) / math.gamma(nu))
    return C * ell ** d / (2 * nu + 4 * math.pi ** 2 * ell ** 2 * norm_sq) ** (nu + d / 2)

def B(d, nu):
    return (math.gamma(nu + d / 2) / math.gamma(nu)
            / math.pi ** (d / 2) * (nu / (2 * math.pi ** 2)) ** nu)

def C(d, nu):
    return B(d, nu) * math.sqrt(2 ** (d + 1) * d * 5 ** (d - 1) / (4 * nu + d))

# Spectral normalization independently checked against the elementary
# exponential and exponential-times-linear Matérn transforms.
for ell in (.07, .2, .8):
    for xi in (0., .25, 1.3, 4.):
        f05 = 2 * ell / (1 + (2 * math.pi * ell * xi) ** 2)
        f15 = (4 * ell / math.sqrt(3)) / (1 + (2 * math.pi * ell * xi) ** 2 / 3) ** 2
        check(math.isclose(spectral((xi,), 1, .5, ell), f05, rel_tol=2e-14), 'nu=1/2 Fourier transform')
        check(math.isclose(spectral((xi,), 1, 1.5, ell), f15, rel_tol=2e-14), 'nu=3/2 Fourier transform')

# Every individual nonzero Fourier coefficient obeys the asserted power envelope.
for d, nu in itertools.product((1, 2, 3), (.5, 1.5, 2.5)):
    for ell, h in ((.08, .3), (.25, .7), (.7, 1.0)):
        for r in (1, 2, 3, 7, 11):
            xi = (h * r,) + (0.,) * (d - 1)
            lhs = spectral(xi, d, nu, ell)
            rhs = B(d, nu) * ell ** (-2 * nu) * (h * r) ** (-2 * nu - d)
            check(lhs <= rhs * (1 + 1e-12), 'spectral power envelope')

# Periodic Parseval geometry, using finite sums of genuinely nontrivial waves.
# Integrate over [-1,1] by midpoint rule; every period's exact mass is known.
for d in (1, 2):
    for h in (.25, .5, 1.):
        terms = [((1,) + (0,) * (d - 1), complex(.4, .1)),
                 ((-1,) + (0,) * (d - 1), complex(.4, -.1)),
                 ((2,) + (0,) * (d - 1), complex(-.2, .25)),
                 ((-2,) + (0,) * (d - 1), complex(-.2, -.25))]
        if d == 2:
            terms += [((0, 1), complex(.15, 0)), ((0, -1), complex(.15, 0))]
        s2 = sum(abs(c) ** 2 for _, c in terms)
        count = 256 if d == 1 else 42
        total = 0.
        for indices in itertools.product(range(count), repeat=d):
            z = tuple(-1 + 2 * (i + .5) / count for i in indices)
            f = sum(c * cmath.exp(2j * math.pi * h * sum(j[k] * z[k] for k in range(d))) for j, c in terms)
            total += abs(f) ** 2
        integral = total * (2. / count) ** d
        bound = 2 ** d * h ** (-d) * s2
        check(integral <= bound * (1 + 1e-9), 'periodic Parseval finite wave inequality')

# Explicit covariance combinatorics: exact expectation includes the diagonal.
for n in (2, 3, 4):
    for err0, err1 in ((1., .3), (.15, -.8)):
        # two-point iid distribution, symmetric error values e(0), e(+/-distance)
        q2 = .5 * err0 ** 2 + .5 * err1 ** 2
        formula = n * (n - 1) * q2 + n * err0 ** 2
        direct = 0.
        for config in itertools.product((0, 1), repeat=n):
            sumsq = sum((err0 if a == b else err1) ** 2 for a in config for b in config)
            direct += sumsq / (2 ** n)
        check(math.isclose(direct, formula, abs_tol=1e-12), 'diagonal correction identity')

print(f'PASS: {COUNT} supplementary finite checks; no infinite proof is inferred from them.')
