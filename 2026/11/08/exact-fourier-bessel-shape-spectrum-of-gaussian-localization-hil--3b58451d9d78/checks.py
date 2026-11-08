"""Independent quadrature and special-function checks for a disk Gaussian energy.

Requires numpy and scipy. Run: python checks.py
The finite checks are not a proof of the infinite Fourier expansion.
"""
import math
import numpy as np
from scipy.special import ive
from numpy.polynomial.legendre import leggauss

checks = 0

def verify(value, message):
    global checks
    if not bool(value):
        raise AssertionError(message)
    checks += 1


def multiplier(area, degree):
    return ive(1, 2*area) - ive(degree, 2*area)


def gaussian_energy(area, amplitude, degree, n_angles=64, n_radial=32):
    """Independent tensor-product quadrature of the original fourfold integral.

    Squared radius is area + amplitude*cos(degree*angle), with area preserved.
    """
    roots, weights = leggauss(n_radial)
    angles = np.arange(n_angles) * (2*math.pi/n_angles)
    upper = area + amplitude*np.cos(degree*angles)
    t = (upper[:, None]*(roots[None, :]+1)/2).ravel()
    w = (upper[:, None]*np.broadcast_to(weights[None, :], (n_angles,n_radial))/2/n_angles).ravel()
    theta = np.repeat(angles, n_radial)
    energy = 0.
    for start in range(0, len(t), 64):
        s = slice(start, start+64)
        cross_angle = theta[s,None] - theta[None,:]
        exponent = -t[s,None]-t[None,:]+2*np.sqrt(t[s,None]*t[None,:])*np.cos(cross_angle)
        energy += np.sum(np.exp(exponent)*w[s,None]*w[None,:])
    return float(energy)


# Strictly ascending positive deficit curvatures, and exact translation null modes.
for area in (0.001, 0.01, 0.1, 0.4, 1., 1.5, 2.3, 10., 100.):
    verify(abs(multiplier(area, 1)) < 1e-13, 'translation null mode')
    degrees = range(1, 7 if area < 0.1 else (10 if area < 1 else 16))
    values = [ive(k, 2*area) for k in degrees]
    verify(all(x > y for x,y in zip(values, values[1:])), 'Bessel coefficient ordering')
    verify(all(multiplier(area,k) > 0 for k in degrees if k>=2), 'positive higher-mode curvature')

# Direct fourfold Gaussian integral versus the analytical second variation.
for area in (0.75, 1.3, 2.0):
    center = gaussian_energy(area, 0., 0.)
    for degree in (2,3,4,5):
        expected = multiplier(area, degree)/2 # cos(k*theta) has squared Fourier mass 1/2
        observed = (2*center-gaussian_energy(area,0.02,degree)
                    -gaussian_energy(area,-0.02,degree))/(2*0.02**2)
        verify(abs(observed-expected) < 0.001*expected, 'energy curvature')

# The semigroup Fourier coefficients converge to their high-area Gaussian-perimeter law.
for area in (100., 300., 1000.):
    coeff = multiplier(area, 2)
    asymptotic = 3/(8*math.sqrt(math.pi)*area**1.5)
    verify(abs(coeff/asymptotic-1) < 0.004, 'large-area coefficient')

# Small-area asymptotics, and the next angular mode separating from the elliptic mode.
for area in (0.0001, 0.001, 0.01):
    verify(abs(multiplier(area,2)/area-1) < 0.03, 'small-area coefficient')
    verify(multiplier(area,3)>multiplier(area,2), 'mode 3 more costly')

print(f'GAUSSIAN_HS_SHAPE_CHECKS_PASS {checks}')
