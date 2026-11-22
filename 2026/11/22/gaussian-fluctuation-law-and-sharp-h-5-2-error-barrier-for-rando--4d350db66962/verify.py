"""Exact symbolic checks for the randomized two-stage SDIRK fluctuation law.

Run with: python verify.py
Requires sympy. Symbolic finite checks support, but do not replace, the
analytic uniform Taylor expansion and the martingale functional CLT.
"""
import sympy as sp

h, x, z = sp.symbols('h x z', real=True)
a, b, c, d = sp.symbols('a b c d', real=True)
F = lambda v: a + b*v + c*v**2/sp.Integer(2) + d*v**3/sp.Integer(6)
trunc = lambda expr, order=4: sp.series(expr, h, 0, order).removeO().expand()

# At base point y=0, solve two implicit-stage equations as formal power series.
k1 = sp.Integer(0)
for _ in range(4):
    k1 = trunc(F(h*x*k1))
k2 = sp.Integer(0)
for _ in range(4):
    k2 = trunc(F(h*((1-2*x)*k1+x*k2)))
step = trunc(h*(k1+k2)/2)
exact = h*a + h**2*b*a/2 + h**3*(b*b*a+c*a*a)/6

g = x*(1-x)
delta = g-sp.Rational(1,6)
H = b*b*a - c*a*a/2
assert sp.simplify(sp.expand(step-exact-h**3*delta*H).coeff(h,3)) == 0
assert sp.simplify(sp.expand(step-exact).coeff(h,1)) == 0
assert sp.simplify(sp.expand(step-exact).coeff(h,2)) == 0

# Also verify the order-three Butcher coefficients directly.
A = sp.Matrix([[x,0],[1-2*x,x]])
beta = sp.Matrix([sp.Rational(1,2),sp.Rational(1,2)])
cc = A*sp.ones(2,1)
assert sp.simplify((beta.T*A*cc)[0] - g) == 0
assert sp.simplify((beta.T*sp.Matrix([j*j for j in cc]))[0]-(sp.Rational(1,2)-g))==0

Eg = 2*sp.integrate(g,(x,sp.Rational(1,2),1))
Eg2 = 2*sp.integrate(g*g,(x,sp.Rational(1,2),1))
assert Eg == sp.Rational(1,6)
assert Eg2 == sp.Rational(1,30)
assert Eg2-Eg**2 == sp.Rational(1,180)

# Check scalar stability multiplier and leading random fluctuation exactly.
R = (1+(1-2*x)*z+(x*x-2*x+sp.Rational(1,2))*z*z)/(1-x*z)**2
rr = sp.series(R,z,0,7).removeO().expand()
assert sp.simplify(rr.coeff(z,3)-g) == 0
assert sp.simplify(rr.coeff(z,0)-1) == 0
assert sp.simplify(rr.coeff(z,1)-1) == 0
assert sp.simplify(rr.coeff(z,2)-sp.Rational(1,2)) == 0
mean = sp.expand(2*sp.integrate(rr,(x,sp.Rational(1,2),1)))
second = sp.expand(2*sp.integrate(sp.series(R**2,z,0,7).removeO(),(x,sp.Rational(1,2),1)))
variance = sp.series(second-mean**2,z,0,7).removeO().expand()
assert all(sp.simplify(variance.coeff(z,k))==0 for k in range(6))
assert sp.simplify(variance.coeff(z,6)-sp.Rational(1,180))==0
assert all(sp.simplify(mean.coeff(z,k)-sp.Rational(1,sp.factorial(k)))==0 for k in range(4))

# Scalar degeneracy identity is an algebraic differential identity.
y = sp.symbols('y',real=True)
ff = sp.Function('f')(y)
Hf = ff*sp.diff(ff,y)**2 - ff**2*sp.diff(ff,y,2)/2
assert sp.simplify(Hf - ff**4*sp.diff(1/ff,y,2)/2)==0

print('PASS: 2-stage third-order B-series jet, uniform moment 1/180,')
print('      scalar one-step variance coefficient, and reciprocal-field identity')
