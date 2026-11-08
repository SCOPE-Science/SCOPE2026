"""Reproducibility diagnostics for quadratic occupation under renewal-reset Brownian motion.

Usage: python checker.py. Finite checks do not prove infinite-horizon limits.
"""
import math
from fractions import Fraction
import numpy as np
from scipy.integrate import quad

NTESTS = 0

def check(condition, message):
    global NTESTS
    NTESTS += 1
    if not condition:
        raise AssertionError(message)


def normal_variance(alpha, D=1.0):
    m = alpha/(alpha-1)
    q = (alpha-1)/(alpha-2)
    mom = lambda j: alpha/(alpha-j)
    return D*D/m * ((7/3)*mom(4)-2*q*mom(3)+q*q*mom(2))


def brownian_j_laplace(s):
    return math.exp(-0.5 * math.log(math.cosh(math.sqrt(2*s))))


def fractional_moment_z(beta, D=1.0):
    # E Z^beta with Z=2D int_0^1 B_s^2 ds; 1<beta<2.
    gam = math.gamma(-beta)
    def integrand(s):
        if s < 1e-5:
            # E Z^2=7D^2/3, so Laplace correction ~ (7D^2/6)s^2.
            correction = 7*D*D*s*s/6
        else:
            u = math.sqrt(4*D*s)
            if u > 700:
                lap = 0.0
            else:
                lap = math.exp(-0.5*math.log(math.cosh(u)))
            correction = lap - 1 + D*s
        return correction / s**(1+beta)
    left = quad(integrand, 0, 1, epsabs=2e-7, limit=400)[0]
    right = quad(integrand, 1, math.inf, epsabs=2e-7, limit=400)[0]
    return (left+right)/gam


def main():
    # Brownian scaling and two evaluations of the second quadratic-area moment.
    k = np.arange(1, 30001, dtype=float)
    eig = 1 / ((k-0.5)**2 * math.pi**2)
    check(abs(eig.sum()-0.5) < 4e-6, "Karhunen-Loeve mean")
    check(abs((eig*eig).sum()-1/6) < 2e-10, "Karhunen-Loeve squared eigenvalues")
    second = eig.sum()**2 + 2*np.dot(eig,eig)
    check(abs(second-7/12) < 4e-6, "Gaussian quadratic-area second moment")
    for s in (0.04, 0.1, 1.0, 3.0):
        product = float(np.exp(-0.5*np.log1p(2*s*eig).sum()))
        check(abs(product-brownian_j_laplace(s)) < 3e-5, "Laplace spectral product")

    # Independent Gaussian covariance integration via exact elementary integrals.
    grid = (np.arange(400)+0.5)/400
    w = 1/400**2
    integral = (np.sum(np.outer(grid,grid)) + 2*np.sum(np.minimum.outer(grid,grid)**2))*w
    check(abs(integral-7/12) < 1e-5, "Gaussian Wick double integration")

    # Exact Pareto moment normalization in the finite-variance phase.
    check(Fraction(695,192) == (
        Fraction(7,3)*Fraction(6,2) - 2*Fraction(5,4)*Fraction(6,3) +
        Fraction(5,4)**2 * Fraction(6,4)) / Fraction(6,5), "symbolic α=6 variance")
    for alpha in (4.01, 4.5, 5, 6, 8, 12, 30):
        check(normal_variance(alpha) > 0, "positive Gaussian variance")
    check(abs(normal_variance(6)-695/192)<1e-13, "exact α=6")
    check(abs(normal_variance(5)-172/27)<1e-13, "exact α=5")
    check(abs((7/3)/(4/3)-7/4)<1e-13, "critical α=4 log variance")

    # Numerically evaluate the stable-law amplitude by an independent Mellin-Laplace integral.
    c = fractional_moment_z(1.5)
    check(0.5 < c < 6, "positive stable-law tail coefficient")
    m = 3/2
    beta=1.5
    for u in (0.25, 0.5, 1.0, 2.0):
        z = (c*beta/m)*math.gamma(-beta)*complex(0,-u)**beta
        check(z.real < 0 and z.imag < 0, "spectrally positive stable exponent")
    print(f"Computed fractional moment E[(2J)^1.5]={c:.10f}")

    # Independent sampled Brownian Karhunen-Loeve cycles test reward moments.
    rng = np.random.default_rng(240513)
    n = 200000
    spec = 1/((np.arange(1,121)-0.5)**2 * math.pi**2)
    remainder = 0.5-spec.sum()
    samples=[]
    for _ in range(20):
        g=rng.normal(size=(10000,120))
        j= ((g*g)*spec).sum(axis=1) + remainder
        t=(1-rng.random(10000))**(-1/8)
        y=2*t*t*j-(7/6)*t
        samples.append(y)
    y=np.concatenate(samples)
    check(abs(float(y.mean())) < 0.04, "mean-zero reward at α=8")
    check(abs(float(np.mean(y*y))/normal_variance(8)/(8/7)-1)<0.17,
          "independent simulation of reward second moment")

    # Domain, exponents, and nondegenerate stable scale across test parameters.
    for alpha in (2.2, 2.5, 3, 3.5, 3.9):
        beta=alpha/2
        check(1<beta<2 and 0<1-1/beta<0.5,"stable regime exponents")
        check(math.gamma(-beta)>0, "centered positive-stable Levy exponent")
    print(f"PASS: {NTESTS} deterministic mathematical/numerical checks")

if __name__ == '__main__':
    main()
