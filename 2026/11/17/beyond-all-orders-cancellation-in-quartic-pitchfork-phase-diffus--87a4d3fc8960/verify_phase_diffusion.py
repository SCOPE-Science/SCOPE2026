"""Reproduce finite checks for quartic pitchfork phase diffusion.

The complete asymptotic assertion requires the analytic proof, not this script.
Python >=3.9, NumPy and SciPy required.
"""
from fractions import Fraction
from math import comb, factorial, pi, sqrt, exp
import numpy as np
from scipy.integrate import quad
from scipy.special import erfcx


def saddle_coeff(k):
    return Fraction(factorial(4*k), 16**k * factorial(2*k) * factorial(k))


def partition_coeff(k):
    # Gaussian expansion of (1+2*z/lambda)^(-1/2).
    b = Fraction(comb(4*k, 2*k), 4**(2*k))
    z_moment = Fraction(factorial(2*k), 4**k * factorial(k))
    return b * (2**(2*k)) * z_moment


def phase_rate(rho):
    def potential(x):
        return x**4 / 4 - rho * x*x / 2

    z = 2 * quad(lambda x: np.exp(-potential(x)), 0, 10,
                 epsabs=1.e-10, epsrel=1.e-11, limit=300)[0]
    # Equivalent stable formula: J(x) = sqrt(pi)/2*exp(-V(x))*erfcx((x^2-rho)/2).
    e = 2 * quad(lambda x: np.exp(-potential(x)) * erfcx((x*x-rho)/2)**2,
                 0, 10, epsabs=1.e-9, epsrel=1.e-10, limit=300)[0]
    return pi * e / (2*z)


def main():
    for k in range(6):
        assert saddle_coeff(k) == partition_coeff(k), k
    assert saddle_coeff(0) == 1
    assert saddle_coeff(1) == Fraction(3, 4)
    assert saddle_coeff(2) == Fraction(105, 32)
    ratios = []
    for x in (3., 4., 5., 6.):
        f = phase_rate(x)
        ratio = f / (sqrt(2)*pi*exp(x*x/4))
        assert 0.85 < ratio < 1.01, (x, ratio)
        ratios.append(ratio)
    deviations = [abs(1-x) for x in ratios]
    assert all(deviations[j+1] < deviations[j] for j in range(3)), deviations
    crit = phase_rate(0)
    assert abs(crit-0.9749909888) < 1e-6, crit
    print('QUARTIC_PHASE_ALL_ORDER_CHECK_OK exact_saddle_coeffs=6 '
          'finite_barriers=4 critical_value_checked=1')
    print('positive_barrier_ratios:', [round(x, 9) for x in ratios])


if __name__ == '__main__':
    main()
