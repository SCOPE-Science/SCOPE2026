#!/usr/bin/env python3
"""Reproduce finite symbolic and numerical checks for the four-site quadrature ring.

Requirements: Python 3, sympy, numpy, scipy. These checks support, but do not
replace, the analytic proof in RESULT.md.
"""
import math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.special import ellipk

s, x, y = sp.symbols('s x y', real=True)
psi = [s+x, -s+y-sp.pi, s-x, -s-y+sp.pi]
rhs = [sp.cos(psi[(j+1)%4]) - sp.cos(psi[(j-1)%4]) for j in range(4)]
checks = [
    (rhs[0]+rhs[2])/2,
    (rhs[0]-rhs[2])/2+2*sp.sin(s)*sp.sin(y),
    (rhs[1]-rhs[3])/2-2*sp.sin(s)*sp.sin(x),
    sum(sp.sin(a) for a in psi)-2*sp.sin(s)*(sp.cos(x)+sp.cos(y)),
    sum(sp.cos(a) for a in psi)/2-sp.cos(s)*(sp.cos(x)-sp.cos(y)),
]
for expr in checks:
    assert sp.trigsimp(sp.expand_trig(expr)) == 0, expr


def full_rhs(t, theta):
    return np.cos(np.roll(theta, 1)-theta)+np.cos(np.roll(theta, -1)-theta)


def phase_rhs(t, z):
    return np.roll(np.cos(z), -1)-np.roll(np.cos(z), 1)


def make_phases(sv, hv):
    if hv > 0:
        xv, yv = math.acos(hv-1), 0.
    else:
        xv, yv = math.acos(hv+1), math.pi
    p = np.array([sv+xv, -sv+yv-math.pi, sv-xv, -sv-yv+math.pi])
    theta = np.r_[0.,np.cumsum(p[:3])]
    return p, theta


count = 0
max_theta_error = 0.
max_psi_error = 0.
max_half_period_distance = 0.
for sv in [-2.27, -1.12, -0.42, 0.29, 0.85, 1.45, 2.27]:
    for hv in [-1.9, -1.5, -0.9, -0.3, -0.1, 0.1, 0.3, 0.9, 1.5, 1.9]:
        phase, theta = make_phases(sv,hv)
        assert abs(sum(phase)) < 2e-15
        assert abs(sum(np.sin(phase))-2*math.sin(sv)*hv) < 2e-14
        T = 2./abs(math.sin(sv))*ellipk(1-hv*hv/4)
        zsol = solve_ivp(phase_rhs,(0.,T),phase,rtol=2e-12,atol=2e-13,method='DOP853',dense_output=True)
        tsol = solve_ivp(full_rhs,(0.,T),theta,rtol=2e-12,atol=2e-13,method='DOP853',dense_output=True)
        assert zsol.success and tsol.success
        zerr = max(abs(((zsol.y[:,-1]-phase+math.pi)%(2*math.pi))-math.pi))
        terr = max(abs(((tsol.y[:,-1]-theta+math.pi)%(2*math.pi))-math.pi))
        max_psi_error = max(max_psi_error, zerr)
        max_theta_error = max(max_theta_error, terr)
        assert zerr < 3e-9 and terr < 3e-9, (sv,hv,zerr,terr)
        half = tsol.sol(T/2)
        half_dist = max(abs(((half-theta+math.pi)%(2*math.pi))-math.pi))
        max_half_period_distance = max(max_half_period_distance,half_dist)
        assert half_dist > 1e-3, (sv,hv,half_dist)
        count += 1

# Strict period decrease in absolute energy, verified at a finite test grid.
for sv in [0.4, 1.1, 2.2]:
    old = math.inf
    for hv in np.linspace(0.05,1.95,35):
        T = 2./abs(math.sin(sv))*ellipk(1-hv*hv/4)
        assert T < old
        old = T

# The separatrix log constant and center limiting period are numerical sanity checks.
for sv in [0.4,1.1,2.2]:
    for hv in [1e-4,3e-5,1e-5]:
        T = 2./abs(math.sin(sv))*ellipk(1-hv*hv/4)
        asymp = 2./abs(math.sin(sv))*math.log(8./hv)
        assert abs(T-asymp) < 3e-6
    hc=2.-1e-7
    Tc=2./abs(math.sin(sv))*ellipk(1-hc*hc/4)
    assert abs(Tc-math.pi/abs(math.sin(sv))) < 1e-6

print('VERIFY_OK symbolic_identities=5 complete_orbits=%d max_full_phase_return_error=%.3g max_relative_return_error=%.3g min_half_period_displacement_exceeds=0.001' % (count,max_theta_error,max_psi_error))
