"""Finite numerical diagnostics for a four-point thin homothetic shell law.

Analytic asymptotics require the accompanying proof; these finite tests are not
an infinite-asymptotic certificate. Dependencies: Python 3 and NumPy.
"""
import math
import numpy as np


def local_geometry(epsilon, theta):
    h = 1 + epsilon * np.cos(3 * theta)
    hprime = -3 * epsilon * np.sin(3 * theta)
    p = np.stack((h * np.cos(theta) - hprime * np.sin(theta),
                  h * np.sin(theta) + hprime * np.cos(theta)), axis=-1)
    return p


def coefficient(epsilon):
    z = epsilon * epsilon
    return (8 + 24*z + 963*z*z + 160*z*z*z) / (4 * math.pi**2 * (1 - 4*z)**3)


def sample_shell(rng, count, delta, epsilon):
    u = rng.random((count, 4))
    if epsilon:
        grid = np.linspace(0, 2*math.pi, 20001)
        h = 1 + epsilon * np.cos(3*grid)
        rho = 1 - 8*epsilon * np.cos(3*grid)
        weight = h * rho
        cdf = np.r_[0, np.cumsum((weight[:-1]+weight[1:])*np.diff(grid)/2)]
        cdf /= cdf[-1]
        theta = np.interp(u, cdf, grid)
    else:
        theta = 2*math.pi*u
    # The two random factors below are independent. Area measure has radial
    # density proportional to lambda on [1-delta, 1].
    radius = np.sqrt(1 - (2*delta-delta**2)*rng.random((count, 4)))
    return radius[..., None] * local_geometry(epsilon, theta)


def cross(a, b):
    return a[..., 0]*b[..., 1] - a[..., 1]*b[..., 0]


def nonconvex(points):
    n = len(points)
    contained = np.zeros(n, dtype=bool)
    for k in range(4):
        other = [j for j in range(4) if j != k]
        a, b, c = (points[:, j] for j in other)
        p = points[:, k]
        x = cross(b-a, p-a)
        y = cross(c-b, p-b)
        z = cross(a-c, p-c)
        contained |= ((x>0) & (y>0) & (z>0)) | ((x<0) & (y<0) & (z<0))
    return contained


def exact_polynomial_check():
    # Normalized angular average of (1+e cos(3theta))^4
    # (1-8e cos(3theta))^2 has coefficients 1, 3, 963/8, 20.
    from fractions import Fraction
    from math import comb
    coeff = [0]*7
    for i in range(5):
        for j in range(3):
            coeff[i+j] += comb(4,i)*comb(2,j)*(-8)**j
    avg = [Fraction(coeff[2*k]*comb(2*k,k),4**k) for k in range(4)]
    assert avg == [Fraction(1),Fraction(3),Fraction(963,8),Fraction(20)]
    assert abs(coefficient(0)-2/math.pi**2) < 1e-14
    assert coefficient(.1)>coefficient(0)
    print('EXACT_SUPPORT_INTEGRAL_OK', avg)


def monte_carlo():
    rng = np.random.default_rng(20261104)
    for e in (0.0,0.10):
        c = coefficient(e)
        previous = None
        for delta in (.02,.005,.001):
            n = 900000
            count = 0
            for _ in range(3):
                p = sample_shell(rng, n//3, delta, e)
                count += int(nonconvex(p).sum())
            prob = count/n
            ratio = prob/(delta*math.log(1/delta))
            print('TEST', 'epsilon',e,'delta',delta,'nonconvex',count,'/',n,
                  'normalized',round(ratio,6),'limit',round(c,6))
            # Deliberately broad check: convergence is logarithmically slow.
            assert abs(ratio-c)<.09
            if previous is not None:
                assert ratio < previous + .035
            previous=ratio
    print('THIN_SHELL_NUMERICS_OK')

if __name__ == '__main__':
    exact_polynomial_check()
    monte_carlo()
