"""Reproducibility checks for quartic half-integer Bessel moments.

Requires Python 3, scipy, numpy. Finite checks are not proof of
an all-order theorem or of the limiting asymptotic statement.
"""
from fractions import Fraction
from math import comb, pi
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import eval_legendre, jv
from scipy.integrate import quad


def rational_moment(k):
    # I_k = R_k/pi. Exact rational arithmetic.
    out = Fraction(0)
    for a in range(k + 1):
        aa = comb(k, a) * comb(k + a, a)
        for b in range(k + 1):
            bb = comb(k, b) * comb(k + b, b)
            out += Fraction((-1) ** (a + b) * aa * bb, 2 * (a + b) + 1)
    return out


expected = [Fraction(1), Fraction(7, 15), Fraction(11, 35), Fraction(3607, 15015)]
for k, target in enumerate(expected):
    assert rational_moment(k) == target, (k, rational_moment(k), target)
    x, w = leggauss(200)
    # u=1+x, mapped from [-1,1] to [0,2].
    u = 1 + x
    numerical_legendre = float(np.dot(w, eval_legendre(k, 1 - u*u/2) ** 2) / (2*pi))
    assert abs(numerical_legendre - float(target) / pi) < 2e-13
    # Truncate the Bessel integral only for numerical cross-check. Tail is O(1/R).
    numerical_bessel = quad(lambda t: jv(k+.5, t) ** 4, 0, 400, epsabs=1e-8,
                             limit=2000)[0]
    assert abs(numerical_bessel - float(target) / pi) < 5e-4, (k, numerical_bessel)

for k in [10, 50, 100, 250, 500]:
    x, w = leggauss(3*k + 60)
    u = 1+x
    moment = float(np.dot(w,eval_legendre(k,1-u*u/2)**2)/(2*pi))
    assert moment>0
    ratio = 2*pi*pi*k*moment/np.log(k)
    assert 1<ratio<3, (k,ratio)
print('SPHERICAL_MODAL_BESSEL_MOMENT_CHECKS_PASSED')
