#!/usr/bin/env python3
"""Independent finite checks of exact period-average identities and weak-forcing response.

Requires numpy, scipy and sympy. All model parameters are explicit below.
These tests corroborate, but do not replace, the analytic infinite-family proof.
"""
import math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import root

r0, K, a, b, m = 1.2, 6.0, 1.1, 0.32, 0.45
Ns = m / (a * b)
Ps = r0 * (1 - Ns / K) / a
gamma = r0 * Ns / K
Omega2 = a*a*b*Ns*Ps
assert Ns > 1.0 and Ps > 0.7

# Check two key coboundary identities as polynomial identities.
n, p, r = sp.symbols('n p r', positive=True)
R, KK, aa, bb, mm = sp.symbols('R K a b m', positive=True)
nstar = mm/(aa*bb)
pstar = R*(1-nstar/KK)/aa
f = n*(r*(1-n/KK)-aa*p)
h = p*(bb*aa*n-mm)
Vdot = sp.expand(bb*(1-nstar/n)*f+(1-pstar/p)*h)
expected = bb*(n-nstar)*((r-R)*(1-nstar/KK)-r*(n-nstar)/KK)
assert sp.simplify(Vdot-expected) == 0

z, gam, om2 = sp.symbols('z gam om2', positive=True)
D = (om2-z)**2 + gam**2*z
# The unique frequency optimum of z/D occurs at z=om2.
assert sp.simplify(sp.diff(z/D, z) - (om2**2-z**2)/D**2) == 0


def periodic_orbit(A, omega):
    T = 2 * math.pi / omega
    def rhs(t, state):
        N, P = state[:2]
        rho = r0 + A*math.cos(omega*t)
        dN = N*(rho*(1-N/K)-a*P)
        dP = P*(a*b*N-m)
        if len(state)==2:
            return [dN, dP]
        return [dN, dP, N, P, rho*N, rho*(N-Ns)**2]
    def period_map(x):
        sol = solve_ivp(rhs, (0,T), x, method='DOP853',
                        rtol=1e-11, atol=1e-13)
        assert sol.success
        return sol.y[:,-1]
    sol = root(lambda x:period_map(x)-x, [Ns, Ps], tol=1e-10)
    assert sol.success or np.linalg.norm(period_map(sol.x)-sol.x) < 1e-10
    assert np.linalg.norm(period_map(sol.x)-sol.x) < 2e-10
    y0 = list(sol.x) + [0.0]*4
    q = solve_ivp(rhs, (0,T), y0, method='DOP853',
                  rtol=2e-12,atol=1e-14, dense_output=True)
    assert q.success
    grid = q.sol(np.linspace(0,T,241))
    assert np.min(grid[0])>1.0 and np.min(grid[1])>0.7
    meanN, meanP, mean_rhoN, weighted_var = q.y[2:,-1]/T
    delta = Ps-meanP
    c1 = (mean_rhoN-r0*Ns)/(a*K)
    c2 = weighted_var/(a*K*K*(1-Ns/K))
    assert abs(meanN-Ns) < 2e-9, (A,omega,meanN,Ns)
    assert abs(delta-c1) < 2e-9, (A,omega,delta,c1)
    assert abs(delta-c2) < 2e-9, (A,omega,delta,c2)
    assert delta>0
    predicted_frac = A*A/(2*r0*r0) * (gamma*gamma*omega*omega)/((Omega2-omega*omega)**2+gamma*gamma*omega*omega)
    return delta/Ps, predicted_frac

for A in [0.001, 0.01, 0.03, 0.05]:
    for freq in [0.4, math.sqrt(Omega2), 0.8, 1.2]:
        actual, predicted = periodic_orbit(A, freq)
        if A<=0.01:
            assert abs(actual-predicted) < 0.0002*A*A
        print('PASS', f'A={A:.3f}',f'omega={freq:.6f}',
              f'fractional_deficit={actual:.11g}',
              f'quadratic={predicted:.11g}')
print('PASS: 2 symbolic identities and 16 periodic shooting/integration cases')
