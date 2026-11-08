#!/usr/bin/env python3
"""Exact rational algebra for four-site open exclusion reentrant rectification.
Requires Python 3.10+ and sympy. Run: python verify.py in this directory.
No simulations, external datasets, or internet services are used.
"""
import json
from pathlib import Path
import sympy as sp

c, d, r, h, u = sp.symbols('c d r h u')

def generator(c, d, left=sp.Integer(1), right=sp.Integer(0)):
    rates = (sp.Integer(1), c, d, sp.Integer(1))
    q = sp.zeros(16, 16)  # columns are source configurations
    for state in range(16):
        def transition(target, rate):
            q[target, state] += rate
            q[state, state] -= rate
        for i in range(3):
            ni, nj = (state >> i) & 1, (state >> (i+1)) & 1
            if ni and not nj:
                transition(state ^ (3 << i), rates[i])
            elif nj and not ni:
                transition(state ^ (3 << i), rates[i+1])
        if state & 1:
            transition(state & ~1, 1-left)
        else:
            transition(state | 1, left)
        if state & 8:
            transition(state & ~8, 1-right)
        else:
            transition(state | 8, right)
    assert all(v == 0 for v in [sum(q[:, i]) for i in range(16)])
    return q

def current(c, d):
    q = generator(c, d)
    matrix = q[:15, :].col_join(sp.ones(1, 16))
    rhs = sp.zeros(16, 1)
    rhs[15] = 1
    p = matrix.inv(method='DM')*rhs
    return sp.factor(1 - sum(p[s] for s in range(16) if s & 1))

J = current(c, d)
JN, V = sp.fraction(J)
assert all(co > 0 for co in sp.Poly(V, c, d).coeffs())
assert sp.Poly(V, c, d).total_degree() >= 2
swapped = J.xreplace({c:d, d:c})
D = sp.factor(J-swapped)
N, Den = sp.fraction(D)
assert sp.expand(Den - V*V.xreplace({c:d, d:c})) == 0
Pcd = sp.cancel(-N/(c*d*(c-d)))
assert Pcd.is_polynomial(c, d)
P = sp.expand(Pcd.subs({c:r*h, d:h}))
coefficients = [[int(x) for x in reversed(sp.Poly(co, r).all_coeffs())]
                for co in reversed(sp.Poly(P, h).all_coeffs())]
expected = json.loads(Path(__file__).with_name('COEFFICIENTS.json').read_text('utf-8'))
assert expected['coefficients_h_ascending_r_ascending'] == coefficients
assert len(coefficients) == 17
assert all(all(z > 0 for z in coefficients[k]) for k in range(4))
assert all(all(z <= 0 for z in coefficients[k]) and any(z < 0 for z in coefficients[k]) for k in range(4,11))
assert all(all(z >= 0 for z in coefficients[k]) and any(z > 0 for z in coefficients[k]) for k in range(13,17))
A = (150*r**8+3776*r**7+11771*r**6-9379*r**5-39888*r**4
     -9379*r**3+11771*r**2+3776*r+150)
B = (141*r**8-333*r**7-13951*r**6-54997*r**5-83115*r**4
     -54997*r**3-13951*r**2-333*r+141)
assert sp.expand(sp.Poly(P,h).nth(11) + r*(r+1)*A) == 0
assert sp.expand(sp.Poly(P,h).nth(12) + r**2*B) == 0
assert all(i > 0 for i in sp.Poly(sp.expand(A.subs(r, 2+u)), u).all_coeffs())
T = (75600*r**9+1221480*r**8+4461570*r**7+7402041*r**6
     +6829195*r**5+3800385*r**4+1306816*r**3+271698*r**2
     +31285*r+1530)
assert sp.factor(P.subs(h, 1/r) + 2*T/r**9) == 0
assert sp.Poly(P,h).nth(0) == 11664
assert sp.factor(sp.Poly(P,h).nth(16)-3*r**6*(r+1)**4) == 0
# An explicit denominator with positive coefficients after the h substitution.
Q = sp.cancel(V.subs({c:r*h,d:h})*V.subs({c:h,d:r*h})/h**2)
assert sp.expand(Q*(-sp.cancel(D.subs({c:r*h,d:h}))) - r*(r-1)*h*P) == 0
# Exact finite-chain stationary solves independent of the symbolic current formula.
for k in [sp.Rational(1,5), sp.Integer(1), sp.Integer(3)]:
    x1 = current(2*k, k)
    x2 = current(k, 2*k)
    diff = x1-x2
    assert sp.sign(diff) == (1 if k == 1 else -1)
    assert sp.sign(sp.expand(P.subs({r:2,h:k}))) == -sp.sign(diff)
# The r=2 polynomial has exactly two positive roots, bracketed by rational endpoints.
P2 = sp.Poly(P.subs(r,2),h)
assert sp.sign(P2.eval(sp.Rational(1,4))) == 1
assert sp.sign(P2.eval(sp.Rational(1,3))) == -1
assert sp.sign(P2.eval(2)) == -1
assert sp.sign(P2.eval(sp.Rational(5,2))) == 1
print('PASS: exact 16-state stationary solution, 17 coefficients, positive denominator,')
print('      exceptional sign polynomials, intermediate witness and rational reversals.')
print('r=2: h roots approximately 0.251206144606 and 2.113641039357.')
