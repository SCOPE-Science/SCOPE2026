"""Numerical checks for Pareto-reset Brownian first passage.

Requires Python 3, NumPy, and SciPy. Run: python VERIFY.py
These are finite checks, not substitutes for the analytic proof.
"""
from math import exp, gamma, pi, sqrt

import numpy as np
from scipy.fft import irfft, next_fast_len, rfft
from scipy.integrate import quad
from scipy.special import erf, gammainc, gammaincc

CHECKS = 0


def check(condition, description):
    global CHECKS
    if not condition:
        raise AssertionError(description)
    CHECKS += 1


def success_probability(beta, a=1., D=1., tau=1.):
    z = a*a/(4*D*tau)
    return (gammaincc(.5, z)
            + z**(-beta)*gamma(beta+.5)*gammainc(beta+.5, z)/sqrt(pi))


def first_hit_density(t, a=1., D=1.):
    return a*exp(-a*a/(4*D*t))/sqrt(4*pi*D*t**3)


def base_survival(t, a=1., D=1.):
    return erf(a/sqrt(4*D*t))


for beta in (.2, .5, .75, 1., 1.5, 2., 4.):
    p = success_probability(beta)
    p_integrated = (quad(first_hit_density, 0, 1, epsabs=2e-12)[0]
                    + quad(lambda s: first_hit_density(s)*s**(-beta),
                           1, np.inf, epsabs=2e-12)[0])
    q_integrated = quad(lambda s: beta*s**(-beta-1)*base_survival(s),
                        1, np.inf, epsabs=2e-12)[0]
    check(0 < p < 1, 'Single-attempt success must be nondegenerate')
    check(abs(p-p_integrated) < 3e-10, 'Incomplete-gamma success probability')
    check(abs(1-p-q_integrated) < 3e-10, 'Defective-reset kernel mass')

# Independent time-discretized solution of S = h + k*S by Fourier inversion.
# The half-grid boundary correction accounts for the jump in the reset density.
dt = .05
size = 120000
times = np.arange(size, dtype=float)*dt
times[0] = 1.0  # The t=0 values below are set explicitly.
T = times[1:]
L = next_fast_len(2*size)
for beta in (.3, .5, .75, 1., 2.):
    h = np.empty(size, dtype=float)
    h[0] = 1.0
    h[1:] = erf(1/np.sqrt(4*T))*np.where(T < 1, 1, T**(-beta))
    k = np.zeros(size, dtype=float)
    mask = T >= 1
    k[1:][mask] = beta*T[mask]**(-beta-1)*erf(1/np.sqrt(4*T[mask]))
    k[int(round(1/dt))] *= .5
    survival = irfft(rfft(h, L)/(1-rfft(dt*k, L)), L)[:size]
    constant = 1/(sqrt(pi)*success_probability(beta))
    errors = []
    for target in (1000., 3000., 5000.):
        j = int(round(target/dt))
        prediction = constant*target**(-beta-.5)
        discrepancy = abs(survival[j]/prediction-1.)
        errors.append(discrepancy)
        check(discrepancy < .035, 'Algebraic survival coefficient at large times')
    check(errors[-1] < errors[0], 'Improvement with increasing observation time')

# Absorbing heat kernel and its normalized large-time one-excursion limit.
for t in (1000., 10000.):
    eps = 1/sqrt(t)
    norm = erf(eps/2)
    def conditional_scaled_density(y):
        return (exp(-(y-eps)**2/4)-exp(-(y+eps)**2/4))/(sqrt(4*pi)*norm)
    check(abs(quad(conditional_scaled_density,0,np.inf)[0]-1.)<1e-10,
          'Surviving Brownian kernel normalization')
    for z in (.5, 1., 2., 3., 5.):
        cdf = quad(conditional_scaled_density, 0, z)[0]
        rayleigh_cdf = 1-exp(-z*z/4)
        check(abs(cdf-rayleigh_cdf)<.006,
              'Rayleigh endpoint distribution')

print('PASS:', CHECKS, 'independent numerical assertions')
