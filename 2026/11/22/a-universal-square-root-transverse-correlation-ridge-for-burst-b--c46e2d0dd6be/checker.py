"""Reproducible tests for the all-order equal-distance correlation ridge.

Requires Python 3 with NumPy, SciPy and mpmath.
"""
import math
import numpy as np
from scipy.special import kve
from scipy.integrate import quad

D, delta, burst_rate, mean_k = 1.25, 0.8, 2.3, 2.0
alpha = math.sqrt(delta / D)


def log_phi(j, positions):
    s = sum(float(x)**2 for x in positions)
    assert j >= 1 and s > 0
    nu = 1.0 - j / 2.0
    z = alpha * math.sqrt(j * s)
    return (math.log(2.) - (j / 2.) * math.log(4. * math.pi * D)
            + (nu / 2.) * math.log(s / (4. * j * delta * D))
            + math.log(float(kve(nu, z))) - z)


def log_g(j, positions):
    assert len(positions) == j
    # The burst factorial moment multiplies g by a spatially constant factor.
    # It cancels in all normalized geometric ratios tested here.
    return log_phi(j, positions) + alpha * sum(abs(x) for x in positions)


# Independent numerical time quadrature of the common-age cluster kernel.
for j, coords in [(3, [-1.1, 0.7, 1.8]), (4, [0.4, -1.4, 2.2, -0.7]),
                  (5, [1.4, -0.8, 0.5, -0.1, 2.2])]:
    s = sum(x*x for x in coords)
    integral, e = quad(lambda t: (4*math.pi*D*t)**(-j/2.) *
                       math.exp(-j*delta*t - s/(4*D*t)), 0, math.inf,
                       epsabs=1e-13, epsrel=1e-12, limit=400)
    exact = math.exp(log_phi(j, coords))
    assert abs(integral / exact-1) < 5e-10, (j, integral, exact)

# Special three-particle closed form: Phi_3(S)=exp(-sqrt(3*delta*S/D))/(4*pi*D*sqrt(S)).
for s in [.25, 1., 6., 30.]:
    x = [math.sqrt(s), 0., 0.]
    closed = math.exp(-math.sqrt(3 * delta * s / D))/(4*math.pi*D*math.sqrt(s))
    assert abs(math.exp(log_phi(3,x))/closed-1) < 3e-14

# Exact far-field large-deviation exponent for normalized connected factorial cumulants.
for u in [[1.,2.,3.], [1.,1.,1.], [2.,-3.,1.,4.]]:
    j = len(u)
    target = -alpha * (math.sqrt(j * sum(x*x for x in u))-sum(abs(x) for x in u))
    for radius in [1000., 6000.]:
        actual = log_g(j, [radius*x for x in u])/radius
        assert abs(actual-target) < 0.035, (u,radius,actual,target)

# The relative transverse profile at the sharp sqrt(radius) scale.
for v in [[-1.,0.,1.], [-1.,0.,.4,1.2]]:
    j = len(v)
    predicted = -.5*alpha * sum((x-sum(v)/j)**2 for x in v)
    for radius in [300., 2000., 15000.]:
        x = [radius + x*math.sqrt(radius) for x in v]
        observed = log_g(j,x)-log_g(j,[radius]*j)
        assert abs(observed-predicted) < 0.12, (v,radius,observed,predicted)

# Three geometrically distinct scaling regimes for transverse offsets.
v = [-.5, .2, .9]
expected = -.5*alpha*sum((x-sum(v)/len(v))**2 for x in v)
for gamma in [0.25,0.5,0.75]:
    radius=1e5
    observed = log_g(3,[radius+x*radius**gamma for x in v])-log_g(3,[radius]*3)
    if gamma < 0.5:
        assert abs(observed)<0.05, (gamma,observed)
    elif gamma == 0.5:
        assert abs(observed-expected)<0.06, (gamma,observed,expected)
    else:
        assert observed < -5., (gamma,observed)

print('PASS: 3 independent quadratures; 4 exact triplet checks; 6 far-field exponent comparisons; 6 Gaussian shell comparisons; 3 transverse scaling regimes')
