"""Standalone finite numerical diagnostics for the bivariate Lindley strong-coupling theorem.

Requires numpy and scipy; these checks supplement, but do not establish, the limits.
Run: python check.py
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import exp1, lambertw
from scipy.stats import kendalltau, spearmanr


def inverse_hazard(y, theta):
    """Inverse of H_theta(x)=theta*x-log(1+theta*x/(theta+1))."""
    z = -(theta + 1.0) * np.exp(-theta - 1.0 - np.asarray(y))
    x = (-lambertw(z, -1).real - theta - 1.0) / theta
    return np.maximum(x, 0.0)


def coefficients(theta, rate):
    def integrand(y, power):
        if y == 0:
            return 0.0
        return float(inverse_hazard(y, theta) ** power * np.exp(-rate*y) / y)
    a = quad(lambda y: integrand(y, 1), 0, 100, epsabs=1e-10)[0]
    b = quad(lambda y: integrand(y, 2), 0, 100, epsabs=1e-10)[0]
    return a, b


def moments(k, theta=1.0, a1=1.0, a2=1.0):
    z = np.exp(a1*a2/k)*exp1(a1*a2/k)/k
    def mean(power):
        def integrand(y):
            return float(inverse_hazard(y, theta)**power*np.exp(-a1*y)/(a2+k*y))
        return quad(integrand, 0, 100, points=[1/k], epsabs=1e-11)[0]/z
    return mean(1),mean(2)


def simulate(k, n, seed=391):
    rng = np.random.default_rng(seed)
    low = np.exp(-max(30, np.log(k)+18))
    grid = np.exp(np.linspace(np.log(low), np.log(35.0), 110000))
    cdf = 1-exp1(grid+1/k)/exp1(1/k)
    y1 = np.interp(rng.random(n), cdf, grid)
    y2 = rng.exponential(size=n)/(1+k*y1)
    x1 = inverse_hazard(y1, 1.0)
    x2 = inverse_hazard(y2, 1.0)
    return float(np.corrcoef(x1,x2)[0,1]),float(kendalltau(x1[:4000],x2[:4000]).statistic),float(spearmanr(x1,x2).statistic)


def main():
    aa, bb = coefficients(1.0, 1.0)
    assert abs(aa-1.65845197625151)<1e-5, aa
    assert abs(bb-2.27068611250048)<1e-5, bb
    coefficient = aa*aa/bb
    print('Symmetric Lindley moment constants A,B and Pearson coefficient:',aa,bb,coefficient)
    for k in [1e4,1e8]:
        mu,second = moments(k)
        print('k, log(k)*mean, log(k)*second moment:',k,np.log(k)*mu,np.log(k)*second)
        assert 0.85 < np.log(k)*mu/aa < 1.20
        assert 0.85 < np.log(k)*second/bb < 1.20
    for k in [1e4,1e8]:
        pearson,tau,spear = simulate(k,12000,seed=391)
        print('k, Pearson, Kendall tau, Spearman rho:',k,pearson,tau,spear)
        assert pearson < 0 and tau < 0 and spear < 0
        if k == 1e8:
            assert pearson > -0.16 and tau < -0.75 and spear < -0.90
    print('Numerical diagnostics PASS (not a proof).')

if __name__ == '__main__':
    main()
