"""Numerical, independently integrated checks for a short-chord asymptotic theorem.

Requires numpy; scipy is not required. No empirical check is used as a proof.
"""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss

L = 2.0 * math.pi

def chord_prob(n: int, eps: float, r: float, samples: int = 640) -> float:
    """Independent chord integration, bisection and midpoint average.

    gamma'(s)=exp(i(s+eps*sin(n*s)/n)); each secant is integrated
    with 40-point Gauss-Legendre quadrature, not its Taylor series.
    """
    abscissae, weights = leggauss(40)
    mids = (np.arange(samples) + .5) * L / samples
    lo = np.zeros(samples)
    hi = np.full(samples, 2.0*r)
    for _ in range(43):
        h = (hi + lo)*.5
        s = mids[:, None] + h[:, None]*abscissae[None, :]/2.0
        theta = s + eps*np.sin(n*s)/n
        real = h*np.sum(weights[None, :]*np.cos(theta), axis=1)/2.0
        imag = h*np.sum(weights[None, :]*np.sin(theta), axis=1)/2.0
        length = np.hypot(real, imag)
        lo = np.where(length < r, h, lo)
        hi = np.where(length >= r, h, hi)
    return 2.0*np.mean((lo + hi)/2.0)/L

def coefficients(n: int, eps: float):
    k0 = 2*math.pi/L
    int_k2 = L*k0**2*(1 + eps**2/2)
    int_k4 = L*k0**4*(1 + 3*eps**2 + 3*eps**4/8)
    int_kp2 = L*k0**4*eps**2*n**2/2
    return 2/L, int_k2/(12*L**2), (3*int_k4/320-int_kp2/360)/L**2

def main():
    nchecks = 0
    for n, eps in [(2, 0.0), (2, .3), (4, .3), (12, .3)]:
        c1, c3, c5 = coefficients(n, eps)
        for r in [.06, .10, .12]:
            direct = chord_prob(n, eps, r)
            series = c1*r+c3*r**3+c5*r**5
            error = abs(direct-series)
            assert error < 2.5e-8, (n,eps,r,direct,series,error)
            nchecks += 1
            if eps==0:
                exact_circle = 2.0/math.pi*math.asin(r/2)
                assert abs(direct-exact_circle)<3e-12, (r,direct,exact_circle)
    c5_n2 = coefficients(2,.3)[2]
    c5_n12 = coefficients(12,.3)[2]
    assert c5_n2 > 0 > c5_n12
    # The same L, curvature minimum/maximum and integral kappa^2 apply
    # to every integer n>=2 in this curvature family.
    assert coefficients(2,.3)[1] == coefficients(12,.3)[1]
    print('VERIFY_CHORD_OK',f'direct_integrals={nchecks}',f'fifth_coeff_n2={c5_n2:.12g}',f'fifth_coeff_n12={c5_n12:.12g}')

if __name__=='__main__':
    main()
