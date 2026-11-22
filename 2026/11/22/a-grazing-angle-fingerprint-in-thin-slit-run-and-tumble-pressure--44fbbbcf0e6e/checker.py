"""Reproducibility checks for narrow-slit pressure response.

Dependencies: Python 3, numpy, scipy. Run: python checker.py
Numerical matrix comparisons corroborate but do not replace the proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.linalg import solve
from scipy.special import exp1, k0, k1, modstruve

GAMMA_E = 0.5772156649015328606
checks = 0


def check(statement, message):
    global checks
    assert statement, message
    checks += 1


def H(z, dimension):
    z = np.asarray(z, dtype=float)
    t = np.maximum(z, 1e-150)
    if dimension == 1:
        return -0.5 * np.expm1(-z)
    if dimension == 2:
        return 0.5 * z * (k0(t) * modstruve(-1, t)
                           + k1(t) * modstruve(0, t))
    if dimension == 3:
        return 0.5 * (z * exp1(t) - np.expm1(-z))
    raise ValueError('dimension must be 1, 2, or 3')


def angular_density(u, dimension):
    if dimension == 1:
        raise ValueError('discrete headings')
    if dimension == 2:
        return 1.0 / (math.pi * math.sqrt(1.0-u*u))
    if dimension == 3:
        return 0.5
    raise ValueError


def wall_integral(z, dimension):
    # Independent quadrature of W(z) = E[U_+ exp(-z/U_+)].
    if dimension == 1:
        return 0.5*math.exp(-z)
    if dimension == 2:
        return quad(lambda theta: math.cos(theta) *
                    math.exp(-z/math.cos(theta))/math.pi,
                    0, math.pi/2, epsabs=1e-12)[0]
    return 0.5*quad(lambda u: u*math.exp(-z/u),0,1,
                    epsabs=1e-12)[0]


def stationary_pressure(s, dimension, n=192):
    edges = np.linspace(0, s, n+1)
    x = 0.5*(edges[:-1]+edges[1:])
    low = edges[:-1][None,:]-x[:,None]
    high = edges[1:][None,:]-x[:,None]
    # K_{ij} is exact transition probability into cell j, starting at x_i.
    K = np.where(high < 0, H(-low,dimension)-H(-high,dimension),
            np.where(low > 0, H(high,dimension)-H(low,dimension),
                  H(np.maximum(-low,0),dimension)+H(np.maximum(high,0),dimension)))
    cumulative = solve(np.eye(n)-K, 0.5-H(s-x,dimension))
    m = {1:0.5, 2:1/math.pi, 3:0.25}[dimension]
    pressure = m-s/4+s*np.mean(cumulative * H(s-x,dimension))
    return pressure, cumulative, x, K


def asymptotic(s,dimension):
    if dimension == 1:
        return 0.5-s/4+s*s/8
    c = {2:1/math.pi, 3:0.5}[dimension]
    m = {2:1/math.pi,3:0.25}[dimension]
    I_over_c = {2:math.log(2),3:0.0}[dimension]
    return m-s/4+c*s*s/4*(math.log(1/s)+1.5-GAMMA_E+I_over_c)


for dimension in (1,2,3):
    for s in (0.16, 0.08, 0.04, 0.02):
        pressure, cumulative, x, K = stationary_pressure(s, dimension)
        check(np.all((cumulative >= -1e-11)&(cumulative<=1+1e-11)),
              'stationary cumulative distribution bounds')
        check(np.max(np.abs(cumulative+cumulative[::-1]-1))<3e-10,
              'mirror symmetry')
        check(np.max(np.abs((np.eye(len(x))-K)@cumulative-
                    (0.5-H(s-x,dimension))))<5e-12,
              'resolvent residual')
        check(pressure > 0, 'positive pressure')
        m={1:0.5, 2:1/math.pi, 3:0.25}[dimension]
        check(pressure>m-s/4, 'positive curvature correction')
        # Independent Euler-renewal reward quadrature averaged over
        # approximate reconstructed stationary probability masses.
        n=len(x)
        interior=np.diff(np.r_[0.,cumulative,1.])
        masses=np.r_[interior[0],interior[1:-1],interior[-1]]
        points=np.r_[0., 0.5*(x[1:]+x[:-1]),s]
        check(abs(sum(wall_integral(s-y,dimension)*w for y,w in zip(points,masses))
                  -pressure)<0.005, 'independent wall-impulse comparison')
        if dimension==1:
            check(abs(pressure-1/(2+s))<1e-7,'exact one-dimensional solution')
        else:
            deviation=abs(pressure-asymptotic(s,dimension))
            check(deviation<0.9*s**3*(1+math.log(1/s)**2),
                  'explicit logarithmic second-order asymptotic')
        print(f'dimension={dimension} width={s:.3f} '
              f'pressure={pressure:.11f} expansion={asymptotic(s,dimension):.11f}')

# The three-dimensional flux kernel can be integrated without special functions.
for s in (0.001,0.005,0.03,0.1,0.3,1.0):
    direct=0.5*quad(lambda u: 1-math.exp(-s/u),0,1,
                    epsabs=1e-13)[0]
    check(abs(H(s,3)-direct)<1e-11,'H3 independent integration')
for s in (0.001,0.01,0.1,0.5):
    direct=quad(lambda theta: (1-math.exp(-s/math.cos(theta)))/math.pi,
                0,math.pi/2,epsabs=1e-12)[0]
    check(abs(H(s,2)-direct)<1e-11,'H2 independent integration')

# Independent angular-integral quadrature for singular/vanishing grazing densities.
# The exact continuum estimate identifies the first nonlinear term with
# B(s) = 0.5 * integral_0^s H(t) dt; the stationary correction is higher order.
for alpha, scales in ((-0.5, (0.003,0.001)), (0.5,(0.003,0.001))):
    c=(alpha+1)/2
    for s in scales:
        B=0.5*quad(lambda u: c*u**alpha *
                   (s+u*math.expm1(-s/u)),0,1,epsabs=1e-12)[0]
        if alpha<0:
            prediction=c*math.gamma(-alpha)*s**(alpha+2)/(
                2*(alpha+1)*(alpha+2))
        else:
            prediction=c/alpha*s*s/4
        check(abs(B/prediction-1)<0.06,
              'grazing-density fractional/regular coefficient')

print(f'PASS: {checks} reproducible deterministic assertions')
