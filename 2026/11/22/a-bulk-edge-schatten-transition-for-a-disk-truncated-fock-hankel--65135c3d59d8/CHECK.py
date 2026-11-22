"""Finite numerical checks for disk-truncated Gaussian Fock Hankel spectra.

Uses Python >=3.10, scipy >=1.9, numpy >=1.23. This is supplementary
finite evidence; the asymptotic theorems are analytic.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.stats import poisson, norm

checks = 0

def record(statement, label):
    global checks
    if not statement:
        raise AssertionError(label)
    checks += 1

def exact_modes(T, nmax):
    n = np.arange(nmax, dtype=int)
    q = poisson.sf(n, T)  # P{Poisson(T)>=n+1}
    mass = poisson.pmf(n+1, T)
    squares = q + n*q*(1-q) - (n+1)*mass
    record(bool(np.min(squares) > -1e-8), 'roundoff positivity')
    return n, np.sqrt(np.maximum(squares, 0)), squares

# Independently compare the exact formula with gamma-integral L2 and projection terms.
for T in (0.4, 2.2, 9.0, 20.0):
    n, s, square = exact_modes(T, 16)
    for j in range(16):
        norm_square, _ = quad(lambda t: t**(j+1)*math.exp(-t)/math.factorial(j),
                              0, T, epsabs=1e-10)
        proj_square = 0.0
        if j:
            coeff, _ = quad(lambda t: t**j*math.exp(-t) /
                            math.sqrt(math.factorial(j)*math.factorial(j-1)),
                            0, T, epsabs=1e-10)
            proj_square = coeff**2
        record(abs(square[j]-(norm_square-proj_square)) < 2e-8,
               f'exact mode T={T} n={j}')

I = {}
for p in (0.5, 1.0, 2.0, 3.0):
    I[p] = quad(lambda u: (norm.cdf(u)*norm.cdf(-u))**(p/2),
                -12, 12, epsabs=1e-11)[0]
record(abs(I[2.0]-1/math.sqrt(math.pi)) < 1e-11,
       'Gaussian integral at p=2')

for T in (400, 1600, 6400, 25600):
    nmax = int(T + 24*math.sqrt(T) + 200)
    n, sv, sq = exact_modes(T, nmax)
    record(abs(np.max(sv)/math.sqrt(T)-0.5) < 0.05, 'norm scale')
    record(abs(np.sum(sv**2)/T**1.5-I[2.0]) < 0.005, 'HS coefficient')
    record(abs(np.sum(sv**3)/T**2-I[3.0]) < 0.07, 'p=3 coefficient')
    record(1.05 < np.sum(np.sqrt(sv))/T < 1.75, 'p=1/2 bulk scale')
    record(2.15 < np.sum(sv)/T < 2.65, 'critical trace coexistence')
    if T >= 1600:
        for u in (-1.5, -0.75, 0, 0.8, 1.6):
            idx = round(T+u*math.sqrt(T))
            limit = math.sqrt(norm.cdf(u)*norm.cdf(-u))
            record(abs(sv[idx]/math.sqrt(T)-limit) < 0.035,
                   f'edge profile T={T} u={u}')
print('DISK_HANKEL_BULK_EDGE_DIAGNOSTIC_OK', checks)
