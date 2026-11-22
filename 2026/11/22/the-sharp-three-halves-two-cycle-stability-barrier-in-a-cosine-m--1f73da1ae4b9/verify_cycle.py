#!/usr/bin/env python3
"""Exact algebraic and independent high-precision diagnostics for the cosine-memristor two-cycle stability threshold."""
from fractions import Fraction
import sympy as sp
import mpmath as mp

k, t, B, b, p, q, s, T, z = sp.symbols('k t B b p q s T z', real=True)
J0 = sp.Matrix([[-1-t-k, 2*t-B], [1,1]])
J1 = sp.Matrix([[-1+t+k, -2*t-B], [1,1]])
M = sp.expand(J1*J0)
assert sp.simplify(sp.trace(M) - (2-2*B-(k+t)**2)) == 0
assert sp.simplify((sp.eye(2)-M).det()-(B**2-4*k*t-8*t*t)) == 0
# Directly reduce the two original first-coordinate equations and both phase Jacobians.
sph = 1-1/b
a_cos = b*q*p*p
phase0_x = a_cos+b*((q-p/2)**2-1)*p
phase1_x = a_cos+b*((q+p/2)**2-1)*(-p)
assert sp.simplify((phase0_x+p).expand().subs(q*q, sph-p*p/4)) == 0
assert sp.simplify((phase1_x-p).expand().subs(q*q, sph-p*p/4)) == 0
J0_11 = -k+b*((q-p/2)**2-1)
J1_11 = k+b*((q+p/2)**2-1)
assert sp.simplify((J0_11-(-1-b*p*q-k)).expand().subs(q*q,sph-p*p/4)) == 0
assert sp.simplify((J1_11-(-1+b*p*q+k)).expand().subs(q*q,sph-p*p/4)) == 0
# Reduced characteristic-polynomial values after t=b p q, k=t p tan(p), B=b p^2.
D = B**2-4*k*t-8*t*t
D_reduced = sp.expand(D.subs({B:b*p*p,t:b*p*q,k:b*p*p*q*T})/(b*b*p*p))
D_expected = 3*p*p-8*s-p*(4*s-p*p)*T
assert sp.simplify(D_reduced.subs(q*q, s-p*p/4)-D_expected) == 0
# The small-amplitude estimate in the range 0<z<=1, s>=1/3.
assert sp.simplify(sp.expand(z*z+(3-4*s)*z-8*s).subs(s,sp.Rational(1,3)) - (z-1)*(z+sp.Rational(8,3))) == 0
assert sp.Rational(3,2)*sp.Rational(49,9)/4 == sp.Rational(49,24) > 2
# Large-amplitude trace lower bound, with P^2=4(1-1/b) and Q=1+z+z^2/3.
P2 = 4*(1-1/b)
Q = 1+z+z*z/3
W = 2*b*z-4+b*b*z*(P2-z)*Q*Q/4
W_decomp = 4*(2*b-3)+b*(P2-z)*(b*z*Q*Q/4-2)
assert sp.simplify(W-W_decomp) == 0

mp.mp.dps = 70

def test_orbit(beta_text, relative_amplitude, should_sink):
    beta=mp.mpf(beta_text)
    P=2*mp.sqrt(1-1/beta)
    p0=P*mp.mpf(relative_amplitude)
    q0=mp.sqrt(1-1/beta-p0*p0/4)
    alpha=beta*p0*p0*q0/mp.cos(p0)
    state0=(p0,q0-p0/2)
    state1=(-p0,q0+p0/2)
    def F(x,y): return alpha*mp.cos(x)+beta*(y*y-1)*x, y+x
    for actual,expected in ((F(*state0),state1),(F(*state1),state0)):
        assert all(abs(actual[j]-expected[j]) < mp.mpf('1e-60') for j in range(2))
    def J(x,y):return mp.matrix([[-alpha*mp.sin(x)+beta*(y*y-1), 2*beta*y*x],[1,1]])
    monodromy=J(*state1)*J(*state0)
    tr=monodromy[0,0]+monodromy[1,1]
    det=mp.det(monodromy)
    roots=[(tr+mp.sqrt(tr*tr-4*det))/2,(tr-mp.sqrt(tr*tr-4*det))/2]
    radius=max(abs(root) for root in roots)
    assert (radius<1) is should_sink, (beta_text,relative_amplitude,radius,alpha)
    return {'beta':str(beta),'alpha':mp.nstr(alpha,20),'p':mp.nstr(p0,20),'spectral_radius':mp.nstr(radius,20),'sink':bool(radius<1)}

if __name__=='__main__':
    print('SYMBOLIC_IDENTITIES_OK')
    for v in [ ('1.05','0.99999',True),('1.2','0.9999',True),('1.4','0.9999',True),('1.5','0.9999',False),('1.7','0.9',False),('2','0.9',False) ]:
        print(test_orbit(*v))
    print('VERIFY_OK')
