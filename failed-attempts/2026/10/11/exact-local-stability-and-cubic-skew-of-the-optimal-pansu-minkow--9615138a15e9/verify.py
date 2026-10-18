import sympy as sp

u, d = sp.symbols("u d", real=True)
pi = sp.pi
ell = pi/2 + u
A = sp.sin(ell) - ell*sp.cos(ell)
B = 3*sp.sin(ell) + sp.sin(3*ell)/3 - 4*ell*sp.cos(ell)
Q = 4*(2*pi)**sp.Rational(1,3) * A / B**sp.Rational(2,3)
Qmin = (18*pi)**sp.Rational(1,3)
q = sp.simplify(Q/Qmin)

assert sp.simplify(q.subs(u,0)-1) == 0

q_u = sp.series(q, u, 0, 4).removeO().expand()
c2u = sp.simplify(q_u.coeff(u,2))
c3u = sp.simplify(q_u.coeff(u,3))
assert sp.simplify(c2u - (pi**2-8)/16) == 0
assert sp.simplify(c3u - pi*(48-5*pi**2)/96) == 0

# Canonical parameter relation: d = sin(u)/4.
# Its inverse through cubic order is u = 4d + (32/3)d^3 + O(d^5).
u_of_d = 4*d + sp.Rational(32,3)*d**3
q_d = sp.series(q_u.subs(u,u_of_d), d, 0, 4).removeO().expand()
c2d = sp.simplify(q_d.coeff(d,2))
c3d = sp.simplify(q_d.coeff(d,3))
assert sp.simplify(c2d - (pi**2-8)) == 0
assert sp.simplify(c3d - sp.Rational(2,3)*pi*(48-5*pi**2)) == 0

# Rigorous sign checks from classical rational bounds 333/106 < pi < 22/7.
# Lower bound proves pi^2 > 8 and 5*pi^2 > 48.
assert sp.Rational(333,106)**2 > 8
assert 5*sp.Rational(333,106)**2 > 48

print("VERIFY_OK")
print("normalized_quadratic_coefficient=pi^2-8")
print("normalized_cubic_coefficient=(2*pi/3)*(48-5*pi^2)")
print("quadratic_positive=true")
print("cubic_negative=true")
