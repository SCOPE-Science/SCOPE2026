"""Reproducible exact identities and finite numerical checks for Ludwig cusp dynamics.

Requires Python 3 and SymPy. Analytical arguments in RESULT.md establish the
infinite-time statement; this script does not certify infinite trajectories.
"""
import math
import sympy as sp

x, z, tau, r, k = sp.symbols('x z tau r k', real=True, positive=True)
s = sp.sqrt(3)
rc = 3*s/8
kc = 3*s
H = r*x/k + x/(1 + x*x)
assert sp.simplify(H - x*sp.diff(H, x) - 2*x**3/(1+x*x)**2) == 0
assert sp.simplify((H-r).subs({r:rc,k:kc}) - (x-s)**3/(8*(1+x*x))) == 0
T = x*(1+tau*r)/(1+tau*H)
assert sp.simplify(sp.diff(T,x) - (1+tau*r)*(1+2*tau*x**3/(1+x*x)**2)/(1+tau*H)**2) == 0
f = sp.factor((T-x).subs({r:rc,k:kc,x:s+z}), extension=s)
D = 32 + 12*s*tau
exact = -tau*z**3*(s+z)/(D*(1+s*z/2+z*z/4)+tau*z**3)
assert sp.simplify(f - exact) == 0
jet = sp.series(f, z, 0, 6).removeO().expand()
c = sp.simplify(tau*s/D)
d = sp.simplify(tau/(2*D))
assert sp.simplify(jet.coeff(z,3)+c)==0
assert sp.simplify(jet.coeff(z,4)-d)==0
assert sp.simplify(jet.coeff(z,5))==0
acoef = sp.simplify(2*c)
ell = sp.simplify(3*c/2 - d**2/c**2)
ell_expected = (tau - 16*s/9)/(24*(tau+8*s/9))
assert sp.simplify(ell-ell_expected)==0
assert sp.simplify(acoef.subs(tau,16*s/9)-sp.Rational(1,9))==0
assert sp.simplify(sp.limit(acoef,tau,sp.oo)-sp.Rational(1,6))==0
assert sp.simplify(sp.limit(ell,tau,sp.oo)-sp.Rational(1,24))==0
print('EXACT_IDENTITIES map_derivative=1 cusp_factor=1 cubic_jet=3 log_cancellation=1 infinite_step=2')

# Finite orbit checks for positivity, strict order and approach toward equilibria.
# Cusp cases test approach on either side for various finite step sizes.
ss=math.sqrt(3.)
rr=3*ss/8
kk=3*ss
params = [0.5, 1.0, 16*ss/9, 7.0, math.inf]
finite_cases = 0
for t in params:
    alpha = (t*rr)/(1+t*rr) if math.isfinite(t) else 1.
    aa = alpha*ss/16
    for initial in (0.7, 2.8):
        y = initial
        previous = abs(y-ss)
        for i in range(12000):
            if math.isinf(t):
                next_y = rr/(rr/kk + 1/(1+y*y))
            else:
                next_y = y*(1+t*rr)/(1+t*(rr*y/kk+y/(1+y*y)))
            assert (next_y-ss)*(initial-ss)>0
            assert abs(next_y-ss) < previous + 5e-14
            previous=abs(next_y-ss)
            y = next_y
        # Avoid claiming asymptotic accuracy from the finite computation.
        assert previous < abs(initial-ss)
        finite_cases += 1
print('FINITE_ORBIT_SCENARIOS', finite_cases)
print('VERIFY_OK exact_algebra_plus_finite_checks; asymptotics_require_analytic_proof')
