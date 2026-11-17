"""Reproducible analytic-identity and finite numerical consistency checks.

The assertions do not certify the infinite-energy limits; the latter are proved
by inverse-branch convolution estimates in RESULT.md.
"""
import math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


def sigmoid(t):
    return 1 / (1 + np.exp(-t))


def potential(t, c0, c1, c2):
    return c0*t + (c1+c2)*(np.logaddexp(0, t)-math.log(2)) - c2*(sigmoid(t)-0.5)


def exact_symbolic_checks():
    z, c0, c1, c2 = sp.symbols('z c0 c1 c2', real=True)
    x = 1/(1+sp.exp(-z))
    v = c0*z + (c1+c2)*(sp.log(1+sp.exp(z))-sp.log(2)) - c2*(x-sp.Rational(1, 2))
    assert sp.simplify(sp.diff(v,z)-(c0+c1*x+c2*x*x)) == 0
    p, q = sp.symbols('p q', real=True)
    xx, yy = 1/(1+sp.exp(-p)), 1/(1+sp.exp(-q))
    f0, f1, f2, g0, g1, g2 = sp.symbols('f0 f1 f2 g0 g1 g2', real=True)
    flow_p = f0+f1*yy+f2*yy**2
    flow_q = -g0-g1*xx-g2*xx**2
    # The canonical Hamiltonian is V(p)+W(q): V'=G(x), W'=F(y).
    assert sp.simplify((g0+g1*xx+g2*xx**2)*flow_p + (f0+f1*yy+f2*yy**2)*flow_q) == 0


def integration_check():
    f0, f1, f2 = -1., 3.5, -0.5
    g0, g1, g2 = -2., 5.2, -0.2
    F = lambda y: f0+f1*y+f2*y*y
    G = lambda x: g0+g1*x+g2*x*x
    a_minus, a_plus = -G(0), G(1)
    b_minus, b_plus = -F(0), F(1)
    A, C = 1/a_minus+1/a_plus, 1/b_minus+1/b_plus
    beta_vm = -(g1+g2)*math.log(2)+g2/2
    beta_vp = -(g1+g2)*math.log(2)-g2/2
    beta_wm = -(f1+f2)*math.log(2)+f2/2
    beta_wp = -(f1+f2)*math.log(2)-f2/2
    B = beta_vm/a_minus + beta_vp/a_plus
    D = beta_wm/b_minus + beta_wp/b_plus
    lead, offset = A*C, -B*C-A*D
    weights = np.outer([1/a_minus,1/a_plus],[1/b_minus,1/b_plus])/(A*C)
    assert np.isclose(np.sum(weights),1)
    ps = math.log(brentq(G,0,1)/(1-brentq(G,0,1)))
    qs = math.log(brentq(F,0,1)/(1-brentq(F,0,1)))
    V = lambda p: potential(p,g0,g1,g2)
    W = lambda q: potential(q,f0,f1,f2)
    prior_error = float('inf')
    for energy in [10.,25.,50.]:
        pmax=brentq(lambda p: V(p)+W(qs)-energy, ps, 3*energy+20)
        z0=[pmax,qs-1.e-8]
        def rhs(t,z):return [F(sigmoid(z[1])),-G(sigmoid(z[0]))]
        def down(t,z):return z[1]-qs
        down.direction=-1
        down.terminal=True
        sol=solve_ivp(rhs,(0,800),z0,events=down,max_step=0.14,rtol=1.e-11,atol=1.e-12,dense_output=True)
        assert len(sol.t_events[0]) == 1
        period=sol.t_events[0][0]
        error=abs(period-(lead*energy+offset))
        if energy>10: assert error < prior_error
        prior_error=error
        print(f'E={energy:g}: period={period:.10f}, two_term={lead*energy+offset:.10f}, absolute_error={error:.3g}')
        if energy==50:
            states=sol.sol(np.linspace(0,period,40001,endpoint=False))
            measured=np.array([[(np.logical_and(states[0]>0 if i else states[0]<0, states[1]>0 if j else states[1]<0)).mean() for j in range(2)] for i in range(2)])
            print('observed corner-proxy fractions (row x=0,1; column y=0,1):',measured.tolist())
            print('theoretical corner weights:',weights.tolist())
            assert np.max(np.abs(measured-weights)) < .01
    assert abs(lead-1.25) < 1e-13
    assert prior_error < 1e-6


if __name__ == '__main__':
    exact_symbolic_checks()
    integration_check()
    print('REPLICATOR_CORNER_PERIOD_CHECK_OK')
