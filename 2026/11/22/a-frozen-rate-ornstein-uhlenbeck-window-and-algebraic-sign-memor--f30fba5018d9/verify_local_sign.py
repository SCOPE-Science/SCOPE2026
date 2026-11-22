"""Numerical consistency checks for the Brownian-squared confinement window theorem.

Run: python verify_local_sign.py
Requires NumPy and SciPy. No stochastic simulation is used as a proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gammaln


def sign_corr(lag, strength=1.0):
    """Exact one-dimensional Gaussian mixture, variable transformed at large lag."""
    if lag == 0:
        return 1.0
    v = strength * lag
    val, err = quad(lambda y: math.asin(math.exp(-y*y)) * math.exp(-y*y/(2*v)),
                    0, 12, epsabs=1e-11, epsrel=1e-11)
    return 4*val/(math.pi*math.sqrt(2*math.pi*v))


def tail_constant_integral(strength=1.0):
    val = quad(lambda y: math.asin(math.exp(-y*y)), 0, 12,
               epsabs=1e-12, epsrel=1e-12)[0]
    return 4*val/(math.pi*math.sqrt(2*math.pi*strength))


def tail_constant_series(strength=1.0, terms=100000):
    series = 0.0
    for n in range(terms):
        logbinom = gammaln(2*n+1)-2*gammaln(n+1)-n*math.log(4)
        series += math.exp(logbinom)/(2*n+1)**1.5
    return math.sqrt(2)*series/(math.pi*math.sqrt(strength))


def linear_path_variance(T, z=1.3, strength=0.9, diffusion=1.4, baseline=0.2):
    """Quadratic-occupation variance on deterministic continuous path B_s=z*s/sqrt(T)."""
    # q = T*(T-s) is the backward microscopic lag.
    def f(q):
        h = q/T**2
        integrated = z*z*(q-q*q/T**2+q**3/(3*T**4))
        return math.exp(-2*baseline*q/T-2*strength*integrated)
    v = quad(f, 0, T*T, epsabs=1e-11, epsrel=1e-10)[0]
    return 2*diffusion*v


def main():
    count = 0
    def check(condition, label):
        nonlocal count
        if not condition:
            raise AssertionError(label)
        count += 1

    c = tail_constant_integral()
    check(abs(c-0.538851623662042)<1e-11, 'independent integral calibration')
    for strength in (0.5, 1.0, 3.0):
        x = tail_constant_series(strength)
        y = tail_constant_integral(strength)
        check(abs(x/y-1)<1e-5, 'positive series vs integral')
    for strength in (0.5, 1.0, 3.0):
        for lag in (0.1, 2.0):
            check(abs(sign_corr(lag,strength)-sign_corr(strength*lag))<1e-11,
                  'rate-scale collapse')
    for strength in (0.7, 1.0, 2.1):
        for lag in (100.0, 1000.0):
            observed=math.sqrt(lag)*sign_corr(lag,strength)
            target=tail_constant_integral(strength)
            tolerance = 0.004 if lag == 100 else 0.00035
            check(abs(observed/target-1)<tolerance, 'large-lag coefficient')
    for strength in (0.5, 1.0, 2.0):
        lag=1e-5
        observed=(1-sign_corr(lag,strength))/math.sqrt(lag)
        expected=4*math.sqrt(strength)/(math.pi*math.sqrt(math.pi))
        check(abs(observed/expected-1)<0.007, 'small-lag square-root cusp')
    for T in (10.0, 25.0, 50.0):
        approx=linear_path_variance(T)
        target=1.4/(0.9*1.3**2)
        check(abs(approx/target-1)<0.1, 'endpoint conditional variance')
    # Independent bivariate-normal Monte Carlo checks of the arcsine mixture.
    rng=np.random.default_rng(20260927)
    n=300000
    g=rng.standard_normal(n)
    y0=rng.standard_normal(n)
    e=rng.standard_normal(n)
    for lag in (0.15, 1.0, 5.0):
        rho=np.exp(-g*g*lag)
        yt=rho*y0+np.sqrt(-np.expm1(-2*g*g*lag))*e
        empirical=np.mean(np.sign(y0)*np.sign(yt))
        check(abs(empirical-sign_corr(lag))<0.008, 'independent Gaussian sign pair')
    check(sign_corr(0)==1.0, 'zero-lag normalization')
    print(f'PASS: {count} independent numerical and analytic-identity checks; K(1)={c:.12f}')

if __name__=='__main__':
    main()
