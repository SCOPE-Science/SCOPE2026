"""Independent symbolic identities and numerical diagnostics for the stated ODE.

Requires: Python 3, sympy, scipy, numpy.  Run: python verify.py
Finite integrations are diagnostics; the accompanying mathematical proof is decisive.
"""
from fractions import Fraction
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

E, G, x = sp.symbols('E G x', positive=True)
s, i = sp.symbols('s i', positive=True)
lam_sym = (G+E)/(1-E)
sig_sym = 1-G*(1-E)/(G+E)
v = 1-s-i
s_original = -E*s-(1-E)*lam_sym*s*i+G*i
i_original = (1-E)*lam_sym*s*i+(1-sig_sym)*lam_sym*v*i-G*i
s_reduced = -E*s+G*i-(G+E)*s*i
i_reduced = E*s*i-G*i*i
assert sp.simplify(s_original-s_reduced) == 0
assert sp.simplify(i_original-i_reduced) == 0
r_rhs = G-E*s/i-E*i*(s/i)*(s/i+1)
assert sp.simplify((s_reduced*i-s*i_reduced)/i**2-r_rhs) == 0
R = G/E
p = R*(R+1)
b = p*(2*R+1)
r = R-p*x+b*x**2
f = G-E*r-E*x*r*(r+1)
g = E*x*x*(r-R)
assert sp.simplify(sp.series(sp.diff(r, x)*g-f, x, 0, 3).removeO()) == 0
K = sp.factor(E*p)
L = sp.factor(E*b)
assert sp.simplify(K-G*(G+E)/E) == 0
assert sp.simplify(L/(2*K*K)-(2*G+E)/(2*G*(G+E))) == 0

e = Fraction(1, 10)
gam = Fraction(7, 100)
lam = (gam+e)/(1-e)
sigma = 1-gam*(1-e)/(gam+e)
assert lam == Fraction(17, 90)
assert sigma == Fraction(107, 170)
assert 0 < lam < 1 and 0 < sigma < 1
k = float((gam*(gam+e))/e)
c0 = (2*k)**(-0.5)
c1 = float((2*gam+e)/(2*gam*(gam+e)))
assert abs(c0-(500/119)**.5)<1e-12
assert abs(c1-1200/119)<1e-12

Ef, Gf = float(e), float(gam)
def ode(t, y):
    s, i = y
    return [-Ef*s+Gf*i-(Ef+Gf)*s*i, Ef*s*i-Gf*i*i]

for s0, i0, peak_expected in [(0., 1., False), (.18, .02, True), (.05, .25, False)]:
    sol = solve_ivp(ode, (0, 1_000_000), [s0, i0], method='LSODA',
                    rtol=2e-11, atol=1e-13, dense_output=True)
    assert sol.success, sol.message
    assert min(sol.y[0]) > -1e-10 and min(sol.y[1]) > 0
    sample = sol.sol(np.array([0., 1., 10., 100., 1_000., 1_000_000.]))
    si, ii = sample
    assert np.all(ii > 0)
    assert ii[-1] < .005 and si[-1] < .005
    r0 = s0/i0
    if peak_expected:
        assert r0 > Gf/Ef
        assert np.max(sol.y[1]) > i0*1.001
    else:
        assert r0 < Gf/Ef
        assert np.max(sol.y[1]) <= i0*1.00000001
    t = 1_000_000.
    observed = t*(ii[-1]-c0/t**.5)
    if not peak_expected:  # near-critical slow convergence depends on initial transient
        assert abs(observed-c1)/c1 < .04, (observed, c1)

print('VERIFY_OK')
