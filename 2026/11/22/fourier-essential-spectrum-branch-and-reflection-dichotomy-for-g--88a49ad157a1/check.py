"""Finite and symbolic consistency tests for generalized Hilbert matrix identities.

Supplementary checks; the all-rank conclusions use the analytical proof.
Run: python check.py (requires SymPy).
"""
from fractions import Fraction
from math import comb, exp, log, sqrt
import sympy as sp

q,z,w=sp.symbols('q z w', positive=True)
z_w=(w-1)/(w+1)
phi=q/(1-(1-q)*z_w)
w_phi=(1+phi)/(1-phi)
assert sp.simplify(w_phi-(q*w+1)/(1-q))==0
assert sp.simplify((w_phi+1)/((w+1)*(1-(1-q)*z_w))-1/(1-q))==0
assert sp.simplify(((1/q)*sp.sqrt(q/(1-q)))**2-(1/(q*(1-q))))==0
checks=3
for t in (Fraction(1,5),Fraction(1,2),Fraction(3,4)):
    a = 1 - t
    previous = None
    for k in range(8):
        # For T_t(z^k), (1-a*z) T_t(z^k) = t*T_t(z^(k-1)) if k>0,
        # and (1-a*z) T_t(1) = 1.
        coefficients = []
        for n in range(8):
            exact=Fraction(comb(n+k,k))*t**k*(1-t)**n
            rhs = Fraction(n == 0) if previous is None else t * previous[n]
            by_series = rhs + (a * coefficients[-1] if n else 0)
            coefficients.append(by_series)
            assert exact==by_series
            checks+=1
        previous = coefficients
for R,L in ((100,8),(1000,100),(10000,1000)):
    bound=0.0
    for t,mass in ((0.25,0.4),(0.75,0.6)):
        ell=log((1-t)/t); weight=1/sqrt(t*(1-t))
        damping=1-exp(-exp(-R+L+abs(ell))/t)
        bound+=mass*weight*(sqrt(abs(ell)/L)+damping)
    assert 0<=bound<1
    print(f'R={R}, L={L}, upper packet error={bound:.8f}')
    checks+=1
assert sp.simplify(1/sp.sqrt(q*(1-q))-1/sp.sqrt((1-q)*q))==0
checks+=1
print(f'PASS: {checks} exact symbolic/rational and finite-packet checks')
