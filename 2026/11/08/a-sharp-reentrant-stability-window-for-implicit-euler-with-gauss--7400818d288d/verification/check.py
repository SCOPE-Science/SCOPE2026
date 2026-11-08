"""Numerical consistency checks for a Gaussian-denominator Euler model.

Requires Python 3, NumPy and SciPy. The finite checks supplement the analytic proof.
Run: python verification/check.py
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import dawsn

COUNT = 0

def check(cond, message):
    global COUNT
    assert cond, message
    COUNT += 1

GAMMA = 0.577215664901532860606512090082
H0 = -(GAMMA + math.log(2.0)) / 2.0

def w(t):
    return math.sqrt(2.0) * float(dawsn(t / math.sqrt(2.0)))

def H(t):
    # H(0)+integral_0^t H'(x)dx, independent of Gaussian-log quadrature.
    return H0 + quad(w, 0.0, t, epsabs=5e-13, epsrel=5e-13)[0]

def F(a, s):
    return math.log(s) + H(a / s)

def direct_log_expectation(t):
    # Transform X=Z+t and split at the integrable logarithmic singularity X=0.
    pdf = lambda x: math.exp(-0.5*(x-t)**2) / math.sqrt(2.0*math.pi)
    left = quad(lambda x: math.log(-x)*pdf(x), -23.0, 0.0, epsabs=2e-10, epsrel=2e-10)[0]
    right = quad(lambda x: math.log(x)*pdf(x), 0.0, 23.0, epsabs=2e-10, epsrel=2e-10)[0]
    return left + right

root = brentq(lambda t: t*w(t)-1.0, 0.1, 4.0, xtol=1e-14)
critical_a = root * math.exp(-H(root))
check(abs(root - 1.306929727719276) < 2e-12, 'Dawson crossing')
check(abs(critical_a - 1.2780775875261037) < 2e-12, 'critical damping')
check(abs(root*w(root) - 1.0) < 1e-12, 'stationarity')

for t in np.linspace(0.0, 4.8, 61):
    check(abs(H(t) - direct_log_expectation(t)) < 3e-9, 'Gaussian log potential')
    check(abs((w(t+1e-5)-w(t-1e-5))/(2e-5) - (1.0-t*w(t))) < 2e-8, 'Gaussian ODE')

for a in (1.01, 1.05, 1.1, 1.2, 1.25, critical_a, 1.3, 1.6, 4.0):
    sstar = a/root
    check(abs(F(a,sstar)-math.log(a/critical_a)) < 2e-11, 'minimum identity')
    for scale in np.geomspace(0.06, 12, 67):
        s = sstar * scale
        check(F(a,s) >= F(a,sstar) - 1e-10, 'unimodality')
    for s in (0.06, 0.19, 0.5, 0.9, 1.5, 2.6):
        delta = s*1e-5
        empirical = (F(a,s+delta)-F(a,s-delta))/(2*delta)
        analytic = (1-(a/s)*w(a/s))/s
        check(abs(empirical-analytic) < 2e-7, 'slope formula')

for a in (1.01, 1.05, 1.1, 1.2, 1.25):
    sstar = a / root
    small_root = brentq(lambda s: F(a,s), 0.002, sstar)
    large_root = brentq(lambda s: F(a,s), sstar, 5.0)
    check(small_root < sstar < large_root, 'two roots ordering')
    for s, expected in ((small_root/2,+1),(math.sqrt(small_root*sstar),-1),
                        (math.sqrt(sstar*large_root),-1),(2*large_root,+1)):
        check((F(a,s)>0) == (expected>0), 'reentrant signs')

# Reproducible finite-sample log increments. This does not prove the SLLN or LIL.
rng = np.random.default_rng(20261105)
z = rng.standard_normal(300000)
for a,s in ((1.1,0.25),(1.1,0.7),(1.1,1.8),(1.3,1.0)):
    check(abs(np.log(np.abs(a+s*z)).mean()-F(a,s))<0.011, 'sample log increment')

# Finite near-pole integral lower bounds for the first reciprocal moment.
a,s = 1.1,0.7
normal_density_at_pole = math.exp(-0.5*(a/s)**2)/(s*math.sqrt(2*math.pi))
for epsilon in (0.2,0.05,0.01,0.002):
    # For p>=1, integrating c/|x|^p in any neighborhood of x=0 diverges.
    lower_density = min(math.exp(-0.5*((x-a)/s)**2)/(s*math.sqrt(2*math.pi)) for x in (-epsilon,epsilon))
    check(lower_density > 0 and normal_density_at_pole > 0, 'strict pole density')

print(f'CHECKS_OK {COUNT}; crossing={root:.15f}; acrit={critical_a:.15f}')
