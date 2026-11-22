"""Finite diagnostics for the two-pulse Cesaro amplification theorem.

Usage: python verify.py
Requires Python 3 and numpy/scipy. No network or external data.
Finite tests are not substitutes for the infinite-dimensional proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import beta

count = 0

def check(cond, msg):
    global count
    assert cond, msg
    count += 1

def basis_constant(N, d):
    return (N ** (d - 1)) * sum(j ** (-d) for j in range(1, N + 1))

# Exact finite-pulse formula and direct iteration on weighted ell^p.
p, q, a = 2., 1., 0.4
r = a * p
for N in (30, 100, 210):
    for s in (0.4, 0.75, 0.95):
        for eps in (0.04, 0.18, 0.42):
            j = int(s * N)
            x = np.zeros(N)
            x[j - 1] = (eps ** (1 / p)) * j ** a
            x[N - 1] = ((1 - eps) ** (1 / p)) * N ** a
            weights = np.arange(1, N + 1, dtype=float) ** (-a * p)
            direct = 0.
            for k in range(N):
                direct += (np.dot(np.abs(x[k:]) ** p, weights[:N-k]) ** (q / p)) / N
            kk = np.arange(N)
            A = (N / (N - kk)) ** r
            B = np.zeros(N)
            mask = kk < j
            B[mask] = (j / (j - kk[mask])) ** r
            formula = np.mean(((1 - eps) * A + eps * B) ** (q / p))
            check(abs(direct - formula) < 3e-13, 'two-pulse formula')

for d in (0.1, 0.2, 0.4, 0.65):
    values = [basis_constant(N, d) for N in (4, 20, 100, 800, 5000)]
    check(all(v <= 1 / (1 - d) + 1e-12 for v in values), 'basis bound')
    check(all(values[i] < values[i+1] for i in range(len(values)-1)), 'basis trend')

# Explicit finite-horizon witness, exceeding the infinite single-coordinate supremum.
N = 200000
s = 0.95
eps = 0.25
j = int(s * N)
k = np.arange(N)
A = (N / (N - k)) ** r
B = np.zeros(N)
mask = k < j
B[mask] = (j / (j - k[mask])) ** r
observed = float(np.mean(((1 - eps) * A + eps * B) ** (q / p)))
check(observed > 1/(1 - a*q) + 0.02, 'finite two-pulse strict gain')

# Independently evaluate the beta-function coefficient through a split integral.
for p, q, a in ((2., 1., .4), (3., 1., .2), (2., .5, .15)):
    r = a*p
    b = a*(p-q)
    d = a*q
    coefficient = b * beta(1-r, d)/(1-d)
    check(coefficient > 0, 'positive beta coefficient')
    for delta in (1e-3, 1e-4, 1e-5):
        s = 1-delta
        eta = delta/s
        # Split at eta and use the algebraic singularity as a quadrature weight.
        integral, _ = quad(lambda u: (u+eta)**b, 0, 1, weight='alg', wvar=(-r, 0), epsabs=2e-11, epsrel=2e-11)
        I = (s**(1+b)) * integral
        excess = I - 1/(1-d)
        check(excess > 0, 'positive first variation')
        scaled = excess/(delta**(1-d))
        if delta <= 1e-5 and d >= .2:
            check(abs(scaled/coefficient - 1) < .15, 'beta boundary asymptotics')

print(f'PASS: {count} finite diagnostic assertions; explicit gain={observed - 1/(1-.4):.9f}')
