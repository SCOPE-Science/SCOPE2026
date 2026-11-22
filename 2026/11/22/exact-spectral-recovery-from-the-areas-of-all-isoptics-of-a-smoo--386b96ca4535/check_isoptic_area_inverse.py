#!/usr/bin/env python3
"""Numerical and algebraic tests for isoptic-area spectral reconstruction.

Requires numpy only; does not load any external data or other files.
This is reproducibility testing, not a substitute for the analytic proof.
"""
import math
import numpy as np

R = 20.0
# Real trigonometric Fourier modes: (m, cosine coefficient, sine coefficient).
modes = [(2, 0.8, -0.4), (3, 0.3, 0.5), (4, -0.2, 0.3),
         (5, 0.15, -0.1), (7, 0.01, 0.04)]
q = {m: a*a + b*b for m, a, b in modes}


def support(t):
    p = R + np.zeros_like(t)
    dp = np.zeros_like(t)
    for m, a, b in modes:
        p = p + a*np.cos(m*t) + b*np.sin(m*t)
        dp = dp + m*(-a*np.sin(m*t) + b*np.cos(m*t))
    return p, dp


def normalized_area_formula(alpha):
    return 2*R*R*(1-np.cos(alpha)) + sum(
        qm*(1-np.cos(m*alpha)*np.cos(alpha) -
            m*np.sin(m*alpha)*np.sin(alpha)) for m, qm in q.items())


def isoptic_direct_area(alpha, n=32768):
    t = (2*np.pi/n)*np.arange(n)
    p, dp = support(t)
    pa, dpa = support(t+alpha)
    u = (pa-p*np.cos(alpha))/np.sin(alpha)
    du = (dpa-dp*np.cos(alpha))/np.sin(alpha)
    # x = p*n + u*tau; det(x,x')=p*(p+u')-u*(p'-u)
    det = p*(p+du) - u*(dp-u)
    return 0.5*(2*np.pi/n)*sum(det)


for alpha in (0.14, 0.37, 0.74, 1.25, 1.93, 2.55, 2.97):
    direct = isoptic_direct_area(alpha)
    predicted = np.pi*normalized_area_formula(alpha)/np.sin(alpha)**2
    assert math.isclose(direct, predicted, abs_tol=2e-7, rel_tol=2e-11), (alpha, direct, predicted)

# The analytic cosine coefficients c_k of H(alpha)=A(alpha) sin(alpha)^2 / pi.
c = {0: 2*R*R+sum(q.values()), 1: -2*R*R}
for m, qm in q.items():
    c[m-1] = c.get(m-1, 0) - (m+1)*qm/2
    c[m+1] = c.get(m+1, 0) + (m-1)*qm/2

# Recover the entire finite spectral family from the two parity recurrences.
for j in range(1, 8):
    even = 2*sum((2*l+1)*c.get(2*l+1, 0) for l in range(j, 20))/((2*j-1)*(2*j+1))
    odd = -sum(l*c.get(2*l, 0) for l in range(1,j+1))/(j*(j+1))
    assert abs(even-q.get(2*j,0)) < 2e-11, (2*j, even, q.get(2*j,0))
    assert abs(odd-q.get(2*j+1,0)) < 2e-11, (2*j+1, odd, q.get(2*j+1,0))
R2 = -0.5*sum((2*l+1)*c.get(2*l+1,0) for l in range(20))
assert abs(R2-R*R) < 1e-10

# Recover coefficients directly from sampled areas, without using the analytic coefficients c.
alpha = np.linspace(0, np.pi, 65537)
h = normalized_area_formula(alpha)
for k in range(0, 10):
    coeff = np.trapezoid(h*np.cos(k*alpha), alpha)/np.pi*(1 if k==0 else 2)
    assert abs(coeff-c.get(k, 0)) < 2e-10, (k, coeff, c.get(k,0))

# Phase-twisted Fourier example: identical Green-computed areas, noncongruent ovals.
def direct_example_area(alpha, phase):
    n = 32768
    t = 2*np.pi*np.arange(n)/n
    def pp(t):
        # p(t)=20+cos(2t)+cos(3t+phase), its curvature radius is at least 9.
        return (20+np.cos(2*t)+np.cos(3*t+phase),
                -2*np.sin(2*t)-3*np.sin(3*t+phase))
    p,dp = pp(t)
    pa,dpa = pp(t+alpha)
    u = (pa-p*np.cos(alpha))/np.sin(alpha)
    du = (dpa-dp*np.cos(alpha))/np.sin(alpha)
    return .5*(2*np.pi/n)*sum(p*(p+du)-u*(dp-u))

for alpha in (.31, .9, 1.4, 2.4):
    direct1 = direct_example_area(alpha, 0.0)
    direct2 = direct_example_area(alpha, -np.pi/2)
    assert abs(direct1-direct2) < 2e-9, (alpha,direct1,direct2)
# The second harmonic fixes the admissible rigid phases modulo pi,
# whereas a third-harmonic sine is not a signed cosine under these phases.
assert 20-3-8>0
print('ISOPTIC_AREA_SPECTRAL_INVERSE_CHECKS_OK')
