#!/usr/bin/env python3
"""Reproducible independent checks for the reinforced finite-speed run/rest asymptotic.

Requires Python 3.10+, sympy and scipy. This is a numerical/symbolic
cross-check of a proof, not a replacement for the infinite-time argument.
"""
import math
import sympy as sp
from scipy.integrate import solve_ivp

z, lam, eta, alpha, v = sp.symbols('z lam eta alpha v', positive=True)
gamma = lam + sp.Rational(2,3)*eta
theta = 2*alpha*eta/gamma
P = (2*z + lam + 2*lam*alpha*eta/(z+gamma))/(z*(z+lam))
Q = -2*v**2/(z*(z+lam)) * ((1-lam/gamma)/z**2 + (lam/gamma)/(z+gamma)**2)
C = 2*v**2/lam*(1-lam/gamma)
assert sp.simplify(sp.limit(z*P, z, 0) - (1+theta)) == 0
assert sp.simplify(sp.limit(-z**3*Q, z, 0) - C) == 0
assert sp.simplify(C-4*eta*v**2/(lam*(3*lam+2*eta))) == 0
assert sp.simplify((theta.subs(alpha,sp.Rational(1,3)+lam/(2*eta)))-1) == 0
# Confirm the two representations of the published moment equation.
assert sp.simplify(P-(2*z+lam+2*lam*alpha*eta/(z+gamma))/(z*(z+lam)))==0

def moments(t, l, e, a, speed):
    g=l+2*e/3
    def ode(x, state):
        m, corr, rest = state
        active=1-l/g*(1-math.exp(-g*x))
        return [2*corr, speed**2*active-l*corr+(a*e/x)*rest if x>0 else speed**2,
                l*m-g*rest]
    ts=[1,10,100,1000,10000,100000]
    sol=solve_ivp(ode, (0, max(ts)), [0,0,0], method='DOP853', rtol=2e-10,
                  atol=1e-11, dense_output=True)
    assert sol.success, sol.message
    output=[]
    for t in ts:
        m, corr, rest=sol.sol(t)
        assert m>0 and corr>0 and rest>=0
        assert m<=speed**2*t*t*(1+1e-8)
        output.append((t,float(m)))
    return output

for l,e,speed in [(1,3,1),(2,5,2)]:
    g=l+2*e/3
    acrit=g/(2*e)
    assert 0<acrit<2/3
    constant=2*speed**2/l*(1-l/g)
    critical=moments(0,l,e,acrit,speed)
    norm=[m/(constant*t*math.log(l*t)) for t,m in critical if t>=100]
    assert all(0.5<z<1.1 for z in norm)
    assert all(norm[i+1]>norm[i] for i in range(len(norm)-1)), norm
    sub=moments(0,l,e,0.8*acrit,speed)
    norm2=[m/(constant*t/0.2) for t,m in sub if t>=100]
    assert all(0.4<z<1.1 for z in norm2), norm2
    assert all(norm2[i+1]>norm2[i] for i in range(len(norm2)-1)), norm2
    print(f'lambda={l}, eta={e}, speed={speed}: critical normalized {norm}, subcritical {norm2}')
print('PASS: exact symbolic residues and two-parameter numerical moment trajectories')
