#!/usr/bin/env python3
"""Numerical crosschecks of an analytic two-term spherical-kernel asymptotic.

Uses only published special-function definitions and independent circle integration;
finite checks are not a proof of the large-degree theorem.
"""
from math import comb
from mpmath import mp

mp.dps = 65
checks = 0

def near(a, b, tolerance, description):
    global checks
    assert abs(a-b) <= tolerance, (description, mp.nstr(a, 16), mp.nstr(b, 16))
    checks += 1

# Hypergeometric transform: the first two algebraic residues.
for lam, mu, eps in ((mp.mpf('2.5'), mp.mpf('6'), mp.mpf('.5')),
                     (mp.mpf('3'), mp.mpf('7'), mp.mpf('.75'))):
    b, c = lam+mu/2, lam+(mu+1)/2
    a0 = mp.gamma(b)*mp.gamma(c)/(mp.gamma(b-lam)*mp.gamma(c-lam))*(2*eps)**(2*lam)
    second = -lam*(mu-1)*(mu-2)*eps**2
    for z in (mp.mpf(40), mp.mpf(80)):
        f = mp.hyper([lam], [b,c], -(z/(2*eps))**2)
        recovered = (f*z**(2*lam)/a0-1)*z*z
        near(recovered, second, mp.mpf('.55'), 'Euclidean second residue')

# Exact Weber-Schafheitlin Bessel moments and gamma ratios.
for nu, rho in ((4, mp.mpf('2.5')), (7, mp.mpf('3'))):
    numeric = mp.quad(lambda z: z**(1-2*rho)*mp.besselj(nu,z)**2,
                      [0,2,8,20,100,500,mp.inf])
    formula = mp.gamma(rho-mp.mpf('.5'))*mp.gamma(nu+1-rho)/(
        2*mp.sqrt(mp.pi)*mp.gamma(rho)*mp.gamma(nu+rho))
    near(numeric/formula, 1, mp.mpf('2e-9'), 'Bessel Mellin integral')
for lam in (mp.mpf('2.5'), mp.mpf('3'), mp.mpf('3.4')):
    predicted = lam*(lam-mp.mpf('.5'))*(lam-1)/3
    for nu in (150,350):
        ratio = mp.gamma(nu+1-lam)/mp.gamma(nu+lam)*nu**(2*lam-1)
        measured = (ratio-1)*nu*nu
        near(measured, predicted, mp.mpf('.008'), 'gamma ratio second coefficient')

# Direct circular Fourier coefficients. In dimension d=2 with alpha=1, mu=6,
# the radial function has the exact elementary antiderivative below.
mu = 6
lam = mp.mpf('2.5')
for eps in (mp.mpf('.5'), mp.mpf('.25')):
    def f(theta):
        s = 2*eps*mp.sin(theta/2)
        return (mp.mpf(1)/((mu+1)*(mu+2))
            - sum((-1)**j*comb(mu,j)*s**(j+2)/(j+2) for j in range(mu+1)))
    constant = 4*mu*eps**3
    predicted = lam*(lam-mp.mpf('.5'))*(lam-1)/3 - (lam-mp.mpf('.5'))*(mu-1)*(mu-2)*eps**2
    for degree in (40,80,120):
        eig = 2*mp.quadgl(lambda t: f(t)*mp.cos(degree*t),
                          [0,mp.pi], degree=max(500,3*degree))
        measured = (eig*degree**4/constant - 1)*degree**2
        near(measured, predicted, mp.mpf('.045'), 'direct circle second coefficient')
        if eps == mp.mpf('.25'):
            near(predicted, 0, mp.mpf('1e-30'), 'unique calibrated scale')
print('WENDLAND_SECOND_ORDER_CHECKS_PASS', checks)
