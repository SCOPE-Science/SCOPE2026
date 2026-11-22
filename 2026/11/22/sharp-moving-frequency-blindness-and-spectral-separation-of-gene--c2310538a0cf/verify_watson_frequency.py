"""Standalone numerical checks for the Fourier representation and oscillatory alternatives.

Requires numpy and scipy. These computations supplement, but do not replace,
the finite-variance, triangular-array central-limit and tail-bound arguments.
"""
import math
import numpy as np
from scipy.special import zeta

EPS = 0.6
RNG = np.random.default_rng(19750409)
checks = 0

def near(a, b, tol=1e-9):
    global checks
    assert abs(a-b) <= tol, (a,b,tol)
    checks += 1

def kernel(z, m):
    z = np.asarray(z)
    if m == 1:
        return (z*z-z)/2+1/12
    if m == 2:
        return (1/720-z*z/24+z**3/12-z**4/24)
    raise ValueError('Only m=1 or 2 used in direct polynomial check')

def pair_stat(x, m):
    z = np.abs(np.subtract.outer(x, x))
    return kernel(z, m).sum()/len(x)

def spectral_stat(x, m, cutoff):
    freqs = np.arange(1, cutoff+1, dtype=float)
    phase = np.exp(2j*np.pi*np.outer(freqs, x))
    return 2*len(x)*np.sum(np.abs(phase.mean(axis=1))**2/(2*np.pi*freqs)**(2*m))

# Compare distinct finite-sample expressions, and verify exact circular invariance.
for m in (1,2):
    for n in (3,6,11):
        x = RNG.random(n)
        p = pair_stat(x,m)
        near(p, pair_stat((x+0.371)%1, m), 2e-12)
        s = spectral_stat(x, m, 2048 if m==1 else 384)
        near(p,s,0.00017 if m==1 else 1e-10)

# Analytical Fourier coefficient calculation is independently checked by quadrature.
from scipy.integrate import quad
for k in (3,7,17):
    for j in (1,k,2*k):
        real = quad(lambda x: math.cos(2*math.pi*j*x)*(1+EPS*math.cos(2*math.pi*k*x)),0,1,epsabs=2e-11,limit=1000)[0]
        imag = quad(lambda x: math.sin(2*math.pi*j*x)*(1+EPS*math.cos(2*math.pi*k*x)),0,1,epsabs=2e-11,limit=1000)[0]
        near(real, EPS/2 if j==k else 0, 2e-10)
        near(imag,0,2e-10)

# Verify exact expectation derived from E|n^{-1}sum e^{2piijX}|^2.
for m in (1,2,3):
    for n,k in ((101,4),(300,7),(2300,11)):
        baseline = 2*zeta(2*m,1)/(2*math.pi)**(2*m)
        signal = (n-1)*EPS*EPS/(2*(2*math.pi*k)**(2*m))
        decomposition = baseline+signal
        alternative = 2*sum(1/(2*math.pi*j)**(2*m) for j in range(1,50000)) + signal
        near(decomposition,alternative,2e-6)

# Exact threshold exponent: m=1 diverges and all m>=2 vanish for k_n=floor(n^(1/3)).
for n in (10**6,10**9,10**12,10**15):
    k = int(n**(1/3))
    assert n/k**2 >= 100 if n>=10**9 else n/k**2 >= 1
    checks += 1
    near((n/k**4)/(n/k**2),1/k**2,2e-12)

# Critical deterministic shift and its normalization.
for m in (1,2,3):
    for t in (0.6,1.1,2.0):
        n = 10**8
        k = int(t*n**(1/(2*m)))
        if k == 0: continue
        shift_exact = n*EPS**2/(2*(2*math.pi*k)**(2*m))
        shift_formula = EPS**2/(2*(2*math.pi)**(2*m)*(k/n**(1/(2*m)))**(2*m))
        near(shift_exact,shift_formula,2e-10)

print('PASS:',checks,'deterministic checks')
print('Null means m=1,2:',*[2*zeta(2*m,1)/(2*math.pi)**(2*m) for m in (1,2)])
print('Critical shift formula: epsilon^2 * s / (2*(2*pi)^(2*m))')
