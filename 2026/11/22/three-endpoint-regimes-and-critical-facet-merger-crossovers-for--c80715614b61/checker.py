"""Numerical checks of an exact spherical-sector boundary-clearance law.

Requires Python 3, NumPy, SciPy. These computations check finite thresholds;
they do not replace the analytic limiting and measure-theoretic arguments.
"""
import math
import numpy as np
from scipy.special import roots_legendre
from scipy.integrate import quad

N = 520
X, W = roots_legendre(N)

def exact_tail(alpha, beta, h):
    A, B = math.sin(alpha / 2), math.sin(beta / 2)
    rho = math.asin(A * B / math.hypot(A, B))
    t = rho - h
    u = alpha * (X + 1) / 4
    v = beta * (X + 1) / 4
    s = math.sin(t) ** 2
    integrand = np.maximum(0.0, 1 - s * (1 / np.sin(u[:, None]) ** 2 + 1 / np.sin(v[None, :]) ** 2))
    return float(np.einsum('i,ij,j->', W, integrand, W) / 4)

def endpoint_coefficient(alpha, beta):
    a, b = alpha / 2, beta / 2
    A, B = math.sin(a), math.sin(b)
    q = (A * B) ** 2 / (A * A + B * B)
    rho = math.asin(math.sqrt(q))
    H = 2 / math.tan(rho)
    ca = 2 * q * math.cos(a) / A ** 3
    cb = 2 * q * math.cos(b) / B ** 3
    if abs(ca) < 1e-13 and abs(cb) < 1e-13:
        return 2., 4 / math.pi
    if abs(ca) < 1e-13:
        return 2.5, 16 * H ** 2.5 / (15 * alpha * beta * cb * math.sqrt(q))
    if abs(cb) < 1e-13:
        return 2.5, 16 * H ** 2.5 / (15 * alpha * beta * ca * math.sqrt(q))
    return 3., 2 * H ** 3 / (3 * alpha * beta * ca * cb)

def critical_one(beta, lam):
    B = math.sin(beta / 2)
    q = B * B / (1 + B * B)
    H = 2 / math.tan(math.asin(math.sqrt(q)))
    c = 2 * q * math.cos(beta / 2) / B ** 3
    L = (math.sqrt(lam * lam + 4 * H / q) - lam) / 2
    z = quad(lambda x: (H - q * (lam * x + x * x)) ** 2, 0, L, epsabs=1e-12)[0]
    return 2 * z / (math.pi * beta * c)

def critical_double(lam, mu):
    # Integrating the second coordinate analytically leaves a finite 1D integral.
    def f(x):
        r = max(0., 2 - (x*x + lam*x) / 2)
        L = (math.sqrt(mu*mu + 8*r) - mu) / 2
        return r*L - mu*L*L/4 - L**3/6
    Lx = (math.sqrt(lam*lam+16)-lam)/2
    return 4 / math.pi**2 * quad(f, 0, Lx, epsabs=1e-11)[0]

def close_relative(observed, expected, tolerance):
    assert expected > 0, expected
    assert abs(observed/expected-1) < tolerance, (observed, expected, tolerance)

for a, b in [(1.3, 1.7), (math.pi, 1.7), (math.pi, math.pi)]:
    p, c = endpoint_coefficient(a, b)
    close_relative(exact_tail(a, b, 0.012), c * .012 ** p, .05)
    assert abs(exact_tail(a,b,.03)-exact_tail(b,a,.03)) < 2e-9

for t in (.1, .3, .6):
    exact = 1 - 4*t/math.pi - 2*math.sin(2*t)/math.pi + 4*math.sin(t)**2/math.pi
    close_relative(exact_tail(math.pi, math.pi, math.pi/4-t), exact, .0001)

for beta, lam in [(1.5, 0.), (1.5, 1.), (2.5, 2.)]:
    h = .004
    close_relative(exact_tail(math.pi-lam*math.sqrt(h),beta,h),critical_one(beta,lam)*h**2.5,.055)

for lam, mu in [(0.,0.), (1.,0.), (1.,2.)]:
    h=.002
    close_relative(exact_tail(math.pi-lam*math.sqrt(h), math.pi-mu*math.sqrt(h),h),critical_double(lam,mu)*h**2,.075)

assert abs(critical_double(0.,0.)-4/math.pi) < 1e-10
assert abs(critical_one(1.7,0.)-endpoint_coefficient(math.pi,1.7)[1])<1e-11
print('ALL_CHECKS_PASSED')
