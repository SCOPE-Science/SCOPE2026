"""Independent numerical checks for the bounded-switching diffusivity reset model.

Requires Python, NumPy and SciPy. Execute: python verify_reset_edge.py
The exact spectral representation and its Fourier resolvent are evaluated
using distinct quadrature formulas; finite checks complement the analytic proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import gamma
from scipy.special import hyp2f1

NU = 0.5
LAM = 1.0
RC = LAM / NU
C = NU + 1.0


def w(d):
    return C * (1 - d) ** NU


def Q(z, a):
    return quad(lambda d: w(d) / (a + z*d), 0, 1,
                epsabs=3e-12, epsrel=3e-12)[0]


def root_and_residue(r):
    a = r+LAM
    if r >= RC:
        return None
    s = brentq(lambda s: LAM*Q(-s, a)-1,
               1e-12, a*(1-1e-5), xtol=5e-14)
    c = quad(lambda d: d*w(d)/(a-s*d)**2,
             0, 1, epsabs=3e-12)[0]
    return s, r/(LAM*LAM*c)


def boundary_q(s, a):
    """Analytic beta(1,3/2) Cauchy transform on the branch."""
    v = math.sqrt(1-a/s)
    pv = 3/s*(1-v*np.arctanh(v))
    imag_mag = 3*math.pi*v/(2*s)
    return complex(pv, -imag_mag)


def spectral_rho(s, r):
    a = r+LAM
    if s <= a:
        return 0.0
    qq = boundary_q(s, a)
    return r*w(a/s)/(s*abs(1-LAM*qq)**2)


def transform_by_renewal(k, r):
    a = r+LAM
    val = Q(k*k, a)
    return r*val/(1-LAM*val)


def transform_by_spectrum(k, r):
    a = r+LAM
    cont = quad(lambda v: 2*v*spectral_rho(a+v*v, r)/(a+v*v+k*k),
                0, np.inf, epsabs=1e-10, epsrel=2e-10,
                limit=450)[0]
    pole = root_and_residue(r)
    return cont+(pole[1]/(pole[0]+k*k) if pole else 0)


def density_by_spectrum(x, r):
    a = r+LAM
    cont = quad(lambda v: spectral_rho(a+v*v, r)*v/
                math.sqrt(a+v*v)*math.exp(-math.sqrt(a+v*v)*x),
                0, 25, epsabs=2e-14, epsrel=1e-10,
                limit=400)[0]
    pole = root_and_residue(r)
    return cont+(pole[1]/(2*math.sqrt(pole[0]))*
                 math.exp(-math.sqrt(pole[0])*x) if pole else 0)


def asymptotic(x, r):
    a = r+LAM
    pole = root_and_residue(r)
    if pole:
        s, res = pole
        return res/(2*math.sqrt(s))*math.exp(-math.sqrt(s)*x)
    if r == RC:
        k = (r*a**(1+NU/2)*math.sin(math.pi*NU)**2*gamma(1-NU)/
             (2**NU*LAM**2*C*math.pi**2))
        return k*x**(NU-1)*math.exp(-math.sqrt(a)*x)
    delta = (r-RC)/a
    k = r*C*2**NU*gamma(NU+1)/(a**(1+NU/2)*delta**2)
    return k*x**(-NU-1)*math.exp(-math.sqrt(a)*x)


# Normalization, spectral decomposition, and both positions of the pole.
for r in [1.0, 2.0, 3.0]:
    assert abs(transform_by_renewal(0, r)-1) < 2e-12
    for k in [0.0, 0.2, 1.0, 2.0]:
        x = transform_by_renewal(k, r)
        y = transform_by_spectrum(k, r)
        assert abs(x-y) < 5e-9, (r,k,x,y)
    pole = root_and_residue(r)
    assert (pole is not None) == (r < RC)
    if pole:
        assert 0 < pole[0] < r+LAM and pole[1] > 0
    for x in [8.0, 16.0, 32.0]:
        assert density_by_spectrum(x, r) > 0

# The endpoint exponential moment is finite only in the supercritical case.
r=3.0
a=r+LAM
H=(NU+1)/NU
predicted = r*H/(r-RC)
edge_moment=quad(lambda v: (2*v*spectral_rho(a+v*v,r)/(v*v)
                           if v > 0 else 0),
                 0, np.inf, epsabs=1e-9, limit=600)[0]
assert abs(edge_moment-predicted) < 3e-6, (edge_moment,predicted)

# The large-position ratios tend to one in all three regimes.
for r in [1.0, 2.0]:
    ratio=density_by_spectrum(32.0,r)/asymptotic(32.0,r)
    assert 0.97 < ratio < 1.03,(r,ratio)
ratio = density_by_spectrum(128.0,3.0)/asymptotic(128.0,3.0)
assert 0.65 < ratio < 1.05,ratio

# Edge power in the critical transform for two other laws W_nu.
# This independently verifies the coefficient used in the branch analysis.
for nu in [0.25, 0.75]:
    a=1+1/nu # lambda=1, r=1/nu at the threshold
    H=(nu+1)/nu
    for e in [2e-5, 1e-6]:
        q=float(hyp2f1(1, 1, nu+2, 1-e/a))/a
        predicted=(nu+1)*math.pi/(a**(nu+1)*math.sin(math.pi*nu))*e**nu
        ratio=(H/a-q)/predicted
        assert abs(ratio-1) < (0.12 if nu==0.75 else 0.03), (nu,e,ratio)
print("PASS: stationary normalization; 12 independent spectral-resolvent comparisons; ")
print("      pole/continuum selection; three tail regimes; edge exponential moment;")
print("      4 independent general-edge coefficient checks.")
