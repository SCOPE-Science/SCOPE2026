"""Reproducible exact and high-precision checks of the intermittent-trap response law.

Requires sympy and mpmath. Run with: python check_fdt.py
"""
import sympy as S
import mpmath as mp
from fractions import Fraction

k, s, D = S.symbols('k s D', positive=True)
A = S.Matrix([[-k-s, s], [s, -s]])
q = S.Matrix([[D/k, D/k + D/s]])
u = S.Matrix([1, 1])
assert S.simplify(q*A + S.Matrix([[0, D]])) == S.zeros(1, 2)
assert S.simplify((q*u)[0] - (2*D/k + D/s)) == 0
assert S.simplify(A.charpoly().as_expr() - (S.Symbol('lambda')**2 + (k+2*s)*S.Symbol('lambda') + k*s)) == 0
assert S.simplify((A*u)[0]+k) == 0
assert S.simplify((A*u)[1]) == 0
# The two-dimensional backward system also gives the exact Taylor
# coefficients of both response and covariance at every order.
for n in range(0, 16):
    p = A**n*u
    f = S.simplify((p[0]+p[1])/2)
    lhs = S.simplify((-q*A**(n+1)*u/D)[0])
    assert S.simplify(lhs-p[1]) == 0
    assert S.simplify(lhs-f-(p[1]-p[0])/2) == 0

mp.mp.dps = 65
checks = 0
for k0,s0,D0 in [(1, 1, 1), (3, 2, 5), (5, 6, 2), (7, 1, 3), (1, 7, 11), (12, 13, 3), (2, 11, 5)]:
    km, sm, dm = map(mp.mpf, (k0, s0, D0))
    Om = mp.sqrt(km*km+4*sm*sm)
    lp = (km+2*sm+Om)/2
    lm = (km+2*sm-Om)/2
    assert lp > lm > 0
    assert abs(lp*lm-km*sm) < mp.mpf('1e-58')
    A_mp = mp.matrix([[-km-sm,sm],[sm,-sm]])
    q_mp = mp.matrix([[dm/km, dm/km+dm/sm]])
    unit = mp.matrix([1,1])
    for t0 in [0, mp.mpf('0.01'),mp.mpf('0.1'),mp.mpf('0.5'),1,2,5,10]:
        z = mp.expm(A_mp*t0)*unit
        phi1,phi0 = z[0],z[1]
        R = (phi1+phi0)/2
        expected = km/(2*Om)*(mp.exp(-lm*t0)-mp.exp(-lp*t0))
        observed = phi0-R
        Cprime = (q_mp*A_mp*mp.expm(A_mp*t0)*unit)[0]
        assert abs(observed-expected) < mp.mpf('1e-50')
        assert abs(-Cprime/dm-phi0) < mp.mpf('1e-50')
        assert abs(phi0-phi1-2*expected) < mp.mpf('1e-50')
        if t0>0:
            assert expected>0
        checks += 3
    total_gap=km/(2*Om)*(1/lm-1/lp)
    assert abs(total_gap-1/(2*sm)) < mp.mpf('1e-50')
    assert abs(km/(2*Om)*(lp-lm)-km/2) < mp.mpf('1e-50')
    tstar=mp.log(lp/lm)/Om
    maximum = km/(2*lp)*(lm/lp)**(lm/Om)
    direct=km/(2*Om)*(mp.exp(-lm*tstar)-mp.exp(-lp*tstar))
    assert abs(maximum-direct)<mp.mpf('1e-50')
    for ratio in [mp.mpf('0.1'),mp.mpf('0.5'),mp.mpf('0.9'),mp.mpf('1.1'),mp.mpf('1.5'),mp.mpf('10')]:
        z=ratio*tstar
        val=km/(2*Om)*(mp.exp(-lm*z)-mp.exp(-lp*z))
        assert val < direct
        checks += 1
# An entirely rational eigenvalue example: k=3, s=2, D=5.
t=S.symbols('t',real=True,nonnegative=True)
psi0=(6*S.exp(-t)-S.exp(-6*t))/5
psi1=(3*S.exp(-t)+2*S.exp(-6*t))/5
C=6*S.exp(-t)-S.exp(-6*t)/6
R=(9*S.exp(-t)+S.exp(-6*t))/10
G=S.Rational(3,10)*(S.exp(-t)-S.exp(-6*t))
assert S.simplify(-S.diff(C,t)/5-psi0)==0
assert S.simplify(psi0-psi1-2*G)==0
assert S.simplify((psi0+psi1)/2-R)==0
assert S.simplify(C.subs(t,0)-S.Rational(35,6))==0
assert S.simplify(G.subs(t,0))==0
assert S.simplify(S.diff(G,t).subs(t,S.log(6)/5))==0
print('PASS: exact generator identities, 16 Taylor orders, 168 matrix-exponential comparisons, 14 sum-rule/onset checks, 42 strict-max comparisons, and rational closed-form checks.')
