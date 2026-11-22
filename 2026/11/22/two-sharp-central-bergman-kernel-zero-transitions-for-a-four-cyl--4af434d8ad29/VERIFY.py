"""Standalone symbolic checks for the four-cylinder central Bergman-kernel theorem.

Requires Python 3 and SymPy. Run: python VERIFY.py
"""
import sympy as s

p, t, u, w, n = s.symbols('p t u w n', real=True)
P = s.expand(s.prod(n + 1 + j*p for j in range(5)))
fac = [s.prod(n-j for j in range(k)) for k in range(6)]
a = s.symbols('a0:6')
sol = s.solve(s.Poly(P-sum(a[k]*fac[k] for k in range(6)),n).coeffs(),a)
S = sum(sol[a[k]]*s.factorial(k)*t**k/(1-t)**(k+1) for k in range(6))
Q = s.cancel(S*(1-t)**6)
expected_coefficients = [
    (p+1)*(2*p+1)*(3*p+1)*(4*p+1),
    -2*(p-1)*(p+1)*(2*p+1)*(24*p+13),
    6*(p-1)*(p+1)*(24*p**2-11),
    -2*(p-1)*(p+1)*(2*p-1)*(24*p-13),
    (p-1)*(2*p-1)*(3*p-1)*(4*p-1),
]
for j, v in enumerate(expected_coefficients):
    assert s.simplify(s.Poly(Q,t).nth(j)-v) == 0
H = s.cancel((u+1)**4*Q.subs(t, (u-1)/(u+1)))
H_expected = (120*u**4 + 480*p*u**3 + 120*(7*p**2-1)*u**2
              +160*p*(5*p**2-2)*u + 8*(16*p**2-1)*(3*p**2-2))
assert s.simplify(H-H_expected) == 0
# Routh first-column identities for a quartic au^4+bu^3+cu^2+du+e.
a4,b3,c2,d1,e0=[s.Poly(H,u).nth(j) for j in (4,3,2,1,0)]
b1=s.cancel((b3*c2-a4*d1)/b3)
c1=s.cancel((b1*d1-b3*e0)/b1)
assert s.simplify(b1-40*(16*p**2-1))==0
assert s.simplify(c1-128*p*(4*p**2-1))==0
assert s.simplify(e0-8*(16*p**2-1)*(3*p**2-2))==0
assert s.simplify(s.im(H.subs(u,s.I*w))-160*p*w*(5*p**2-3*w**2-2))==0
assert s.simplify(s.re(H.subs(u,s.I*w)).subs(w**2,(5*p**2-2)/3)+s.Rational(32,3)*(4*p**2-1)*(16*p**2-1))==0
assert s.simplify(Q.subs(t,-1)-8*(16*p**2-1)*(3*p**2-2))==0
assert s.diff(Q,t).subs({p:s.Rational(1,4),t:-1}) == -s.Rational(135,4)
assert s.simplify(s.diff(Q,t).subs({p:s.sqrt(s.Rational(2,3)),t:-1})-320*s.sqrt(6)/9)==0
# The three distinct sign-change counts from representatives of each region.
for pp, expected in [(s.Rational(1,10),2),(s.Rational(2,5),1),(s.Integer(1),0)]:
    seq=[a4,b3,b1,c1,e0]
    signs=[s.sign(v.subs(p,pp)) for v in seq]
    assert all(v in (-1,1) for v in signs)
    assert sum(signs[j]!=signs[j+1] for j in range(4))==expected
print('PASS: generating-function numerator, Cayley polynomial, Routh identities,')
print('imaginary-axis exclusion, simple boundary crossings and region counts')
