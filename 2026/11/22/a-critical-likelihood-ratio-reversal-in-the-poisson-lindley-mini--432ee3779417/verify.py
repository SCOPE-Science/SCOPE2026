#!/usr/bin/env python3
"""Standalone exact-algebra checks for the Poisson-Lindley minification theorem.

Requires Python 3 and SymPy. This checks finite polynomial/rational identities,
not the infinite-index inference, which is proved in RESULT.md.
"""
import sympy as sp

a, t = sp.symbols('a t', positive=True)
q, r = a/(1+a), 1/(1+a)
lambda_ = a*(t+1)+t
S = lambda k: (t*k+(t+1)**2)/(t+1)**(k+2)
SN = lambda k: a**k*(t+1)**(k-2)/lambda_**(k+1) * (t*(k+(t+1)**2)+a*(t+1)**3)
U, V = (sp.factor(S(k)/SN(k)) for k in (1,2))
s, z = 1/(t+1), a/(a+1-1/(t+1))
c, d = s*(1-s), s**2*(1-z)
gamma = s/z
for k in (0,1,2,3):
    assert sp.simplify(S(k)/SN(k) - gamma**k*(1+c*k)/(1+d*k)) == 0

# Admissibility is exactly 1-U >= 0; the positive root is the given a_critical.
F = (t+1)**2*(t+2)*a**2+(t+1)*(t+2)*(t-1)*a-(t**2+3*t+1)
D = a*(t+1)**2*(a*(t+1)**3+t**3+2*t**2+2*t)
assert sp.simplify((1-U)*D - t**2*F) == 0
assert sp.factor(F.subs(a,1/(t+1))) == -t-1
root = (1-t)/(2*(1+t)) + sp.sqrt((t*t+3*t+6)/((t+1)*(t+2)))/2
assert sp.simplify(F.subs(a,root)) == 0

# The boundary sign B(0) < 0 has a globally positive-coefficient certificate.
P = [
  t*(t**8+7*t**7+21*t**6+44*t**5+66*t**4+64*t**3+45*t**2+19*t+3),
  (t+1)*(3*t**8+19*t**7+47*t**6+78*t**5+92*t**4+60*t**3+29*t**2+9*t+1),
  t**2*(t+1)**2*(3*t**5+17*t**4+32*t**3+35*t**2+29*t+6),
  t**2*(t+1)**3*(t**4+5*t**3+6*t**2+t+1),
]
assert all(all(c>=0 for c in sp.Poly(p,t).all_coeffs()) for p in P)
Q = sum(a**i*p for i,p in enumerate(P))
D2 = a*(a+1)**2*(t+1)**6*(a*(t+1)**3+t**3+2*t**2+2*t)*(a*(t+1)**3+t**3+2*t**2+3*t)
N = U*(1+V*q**2)-2*q*V
assert sp.simplify(N - lambda_**2*Q/D2) == 0

# Verify exact adjacent determinant formula at two symbolic indices (it follows
# for arbitrary indices from the affine-in-y, geometric-tail formulas in the proof).
def K(y,x):
    survival_yx = lambda k: 1-r**(y+1)*sum(sp.binomial(y+j,j)*q**j for j in range(k))
    return sp.factor((S(x)/SN(x))*survival_yx(x)-(S(x+1)/SN(x+1))*survival_yx(x+1))

def B(y):
    return q*V*(1-U)*y+U*V*(2*r-1)-U+2*q*V-U*V*r**(y+2)

for y in (0,1,3,4):
    Delta = K(y,0)*K(y+1,1)-K(y+1,0)*K(y,1)
    assert sp.simplify(Delta + q*r**(y+1)*B(y)) == 0

example = {a:sp.Integer(1),t:sp.Integer(1)}
assert U.subs(example) == sp.Rational(45,52)
assert V.subs(example) == sp.Rational(81,112)
assert sp.factor((-q*r**4*B(3)).subs(example)) == sp.Rational(225,458752)
assert sp.factor((-q*r**5*B(4)).subs(example)) == -sp.Rational(2277,3407872)
print('PASS: exact survival identities, admissibility, coefficient positivity, minors, and rational example')
