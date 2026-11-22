"""Reproducible numerical checks for a Gaussian-smoothed reset-phase law.
These checks illustrate, but do not prove, global mode uniqueness or asymptotics.
Requires numpy and scipy.
"""
import math
import numpy as np
from scipy.special import roots_legendre, ndtr, gamma, pbdv
from scipy.optimize import brentq, root

nodes, weights = roots_legendre(850)
theta = (nodes + 1) * math.pi / 2
base_weights = weights * math.pi / 2
z = np.cos(theta)

def phase_weights(lam):
    return base_weights * lam * np.cosh(lam * (math.pi - theta)) / np.sinh(lam * math.pi)

def density_derivatives(y, t, lam):
    w = phase_weights(lam)
    dif = y-z
    p = np.exp(-dif*dif/(2*t)) * w / math.sqrt(2*math.pi*t)
    return (np.sum(p), -np.sum(p*dif)/t,
            np.sum(p*(dif*dif/t-1))/t)

def roots_of_derivative(t, lam):
    grid = np.linspace(-1.25, 1.25, 300)
    vals = [density_derivatives(x,t,lam)[1] for x in grid]
    rr = []
    for i in range(len(grid)-1):
        if vals[i]*vals[i+1] < 0:
            rr.append(brentq(lambda x:density_derivatives(x,t,lam)[1],grid[i],grid[i+1],xtol=1e-13))
    return rr

assert abs(np.sum(phase_weights(0.5))-1) < 1e-12
assert abs(np.sum(phase_weights(1.0))-1) < 1e-12
expected = {0.5:(-0.4048951, 0.15783092),1.0:(-0.60306087, 0.0564606146)}
for lam,(exp_y,exp_t) in expected.items():
    rt = root(lambda q:density_derivatives(q[0],q[1],lam)[1:], [exp_y,exp_t],tol=1e-10)
    assert rt.success and np.linalg.norm(rt.fun)<1e-8 and abs(rt.x[0]-exp_y)<2e-6 and abs(rt.x[1]-exp_t)<2e-6
    assert len(roots_of_derivative(exp_t*.65,lam))==3
    assert len(roots_of_derivative(exp_t*1.4,lam))==1
    assert len(roots_of_derivative(1.2,lam))==1
for lam in (0.2, 0.5, 1.0):
    t=1e-7
    # universal boundary coordinate, obtained independently as a root of D_{1/2}
    q=0.7649508673897399
    assert abs(pbdv(0.5,-q)[0]) < 1e-10
    right = density_derivatives(1-q*math.sqrt(t),t,lam)[0]
    left = density_derivatives(-1+q*math.sqrt(t),t,lam)[0]
    assert abs(right/left/math.cosh(math.pi*lam)-1) < 0.05
    overshoot_right = np.sum(phase_weights(lam)*ndtr((z-1)/math.sqrt(t)))
    overshoot_left  = np.sum(phase_weights(lam)*ndtr((-1-z)/math.sqrt(t)))
    assert abs(overshoot_right/overshoot_left/math.cosh(math.pi*lam)-1) < 0.05
    Aplus=lam*math.cosh(math.pi*lam)/(math.sqrt(2)*math.sinh(math.pi*lam))
    C=2**0.25*gamma(.75)/math.sqrt(math.pi)
    assert abs(overshoot_right/(Aplus*(t**.25)*C)-1)<0.05
print('PASS: 2 numerical double-root thresholds, 6 mode counts, normalized phase law,')
print('3 peak ratios, 3 overshoot ratios, 3 overshoot constants; finite checks only.')
