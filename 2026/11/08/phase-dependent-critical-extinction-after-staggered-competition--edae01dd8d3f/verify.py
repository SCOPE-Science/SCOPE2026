#!/usr/bin/env python3
"""Reproduce the staggered-pulse critical coefficient by independent ODE propagation.

Dependencies: numpy >= 1.23, scipy >= 1.9. Run: python verify.py
This finite check corroborates, but cannot replace, the analytical theorem.
"""
import math
import numpy as np
from scipy.integrate import quad, solve_ivp

# Positive admissible example: R_x=R_y=1-log(2), bf>ce.
a = b = d = e = f = T = 1.0
c = 0.5
mx = my = 0.5
R = a*T + math.log(mx)
X0 = a*(mx*math.exp(a*T)-1)/(b*(math.exp(a*T)-1))
C = a/(b*X0)-1


def resident(t):
    return a/b/(1+C*math.exp(-a*t))


def integral_resident(t):
    return math.log((math.exp(a*t)+C)/(1+C))/b


def E(t):
    return math.exp(d*t-e*integral_resident(t))


def I(phi):
    return quad(E, 0, phi, epsabs=5e-13)[0] + my*quad(E, phi, T, epsabs=5e-13)[0]


def P(phi, initial):
    def flow(t, z):
        x, y = z
        return [x*(a-b*x-c*y), y*(d-e*x-f*y)]
    z = solve_ivp(flow, (0, phi), np.array(initial, dtype=float), rtol=2e-12, atol=2e-14).y[:,-1]
    z[1] *= my
    z = solve_ivp(flow, (phi, T), z, rtol=2e-12, atol=2e-14).y[:,-1]
    z[0] *= mx
    return z


assert R > 0 and b*f > c*e
assert abs(math.log(my) + d*T - e*integral_resident(T)) < 1e-13
assert abs(integral_resident(T) - R/b) < 1e-13
assert abs(P(0.4, (X0, 0))[0]-X0) < 1e-12

values = []
for phi in (0.2, 0.5, 0.8):
    integral = I(phi)
    kappa = (f-c*e/b)*integral
    assert integral > 0 and kappa > 0
    eps = 2e-6
    Dx = (P(phi, (X0+eps, 0)) - P(phi, (X0-eps, 0)))/(2*eps)
    Dy = (P(phi, (X0, eps)) - P(phi, (X0, -eps)))/(2*eps)
    assert abs(Dx[0]-math.exp(-R)) < 3e-7
    assert abs(Dx[1]) < 3e-7 and abs(Dy[1]-1) < 3e-7
    alpha = Dy[0]/(1-Dx[0])
    h = 2e-5
    yp = P(phi, (X0+alpha*h, h))[1]
    inferred = (h-yp)/(h*h)
    assert abs(inferred-kappa) < 6e-5, (phi, inferred, kappa)
    fd = (I(phi+1e-5)-I(phi-1e-5))/(2e-5)
    assert abs(fd-(1-my)*E(phi)) < 2e-9
    values.append((phi, integral, kappa, inferred))
assert values[0][1] < values[1][1] < values[2][1]
print('VERIFY_OK resident_periodic=1 invasion_multiplier=1 offsets=3 neutral_jacobians=3 quadratic_coefficients=3 strict_phase_order=1')
for phi, integral, kappa, inferred in values:
    print('phi=%.1f integral=%.12f analytic_kappa=%.12f numeric_kappa=%.12f' % (phi, integral, kappa, inferred))
