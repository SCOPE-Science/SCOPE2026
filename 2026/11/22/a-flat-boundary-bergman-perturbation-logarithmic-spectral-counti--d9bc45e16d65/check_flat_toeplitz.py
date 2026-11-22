"""Independent numerical checks for a flat-boundary Bergman Toeplitz perturbation.

Requires Python 3, numpy, scipy. Finite tests are not proofs of infinite claims.
Run: python check_flat_toeplitz.py
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigh_tridiagonal
from scipy.special import kv
from scipy.optimize import brentq


def radial_moment(a, k):
    return (k + 1) * quad(
        lambda t: (1 - t) ** k * math.exp(-a / t) if 0 < t < 1 else 0.,
        0, 1, epsabs=2e-12, epsrel=1e-10, limit=160
    )[0]


def jacobi_weight(a, k):
    def f(t):
        if t <= 0 or t >= 1:
            return 0.
        return math.exp((k + 1) * math.log1p(-t) - a / t) / t
    integ = quad(f, 0, 1, epsabs=1e-12, epsrel=1e-9, limit=180)[0]
    return a * (k + 1) * math.sqrt((k + 2) * (k + 3)) * integ


def jacobi_norm(a, n):
    bonds = np.array([jacobi_weight(a, k) for k in range(n)])
    return eigh_tridiagonal(
        np.zeros(n+1), bonds, select='i',
        select_range=(n,n), check_finite=False
    )[0][0]


checks = 0
for a in (0.13, 0.7, 1.9):
    for k in range(0, 13):
        b0, b1 = radial_moment(a, k), radial_moment(a, k+1)
        d0, d1 = 1/((k+1)*(k+2)), 1/((k+2)*(k+3))
        shift = math.sqrt((k+1)/(k+2))
        w = shift * (b0-b1) / math.sqrt(d0*d1)
        assert abs(w-jacobi_weight(a,k)) <= 2e-8 * max(1, abs(w))
        assert w > 0
        checks += 2

# Independently compute a finite Toeplitz commutator, avoiding its artificial last-row boundary.
a, c, n = 0.7, (0.37+0.21j), 24
S = np.zeros((n,n),dtype=complex)
S[1:,:-1] = np.diag(np.sqrt(np.arange(1,n) / np.arange(2,n+1)))
b = np.array([radial_moment(a,k) for k in range(n)])
D = np.diag(b)
V = S + c*D
H = V.conj().T@V - V@V.conj().T
scale = np.sqrt((np.arange(n-1)+1)*(np.arange(n-1)+2))
B = (scale[:,None]*H[:-1,:-1])*scale[None,:]
assert np.max(np.abs(B.diagonal()-1)) < 1e-10
checks += n-1
for k in range(n-2):
    assert abs(abs(B[k,k+1])-abs(c)*jacobi_weight(a,k)) < 1e-9
    checks += 1
assert np.max(np.abs(B-np.triu(np.tril(B,1),-1))) < 1e-10
checks += 1

# The Bessel constant is a strict interior maximum and the finite norm tends toward it.
y = brentq(lambda z: z*kv(1,z)-4*kv(0,z), 0.1, 15.0)
constant = y**4*kv(0,y)/4
assert abs(y-3.52827055203376)<1e-9
assert abs(constant-0.735349154218607)<1e-9
checks += 2
previous = 0.0
for a in (0.4,0.2,0.1,0.05):
    scaled = a * jacobi_norm(a, int(11/a)+100)
    assert 0 < scaled < constant
    assert scaled > previous
    previous = scaled
    checks += 2
assert abs(previous-constant)<0.025
checks += 1
print(f'PASS: {checks} numerical assertions; Bessel maximum y={y:.10f}, '
      f'small-parameter norm coefficient={constant:.10f}, '
      f'last finite scaled norm={previous:.10f}')
