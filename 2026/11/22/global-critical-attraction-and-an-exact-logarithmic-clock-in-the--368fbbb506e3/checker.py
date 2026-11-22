"""Exact symbolic checks of the T-system's critical center jet and drift clock."""
import sympy as sp

s, n, m = sp.symbols('s n m', real=True, nonzero=True)
A, B, C = sp.symbols('A B C')
x, y, z = sp.symbols('x y z', real=True)
F = sp.Matrix([y-x, m*x-x*z, -n*z+x*y])
V_negative = -m*x*x+y*y+z*z
V_critical = y*y+z*z
assert sp.simplify(sp.Matrix([sp.diff(V_negative,t) for t in (x,y,z)]).dot(F) - (2*m*x*x-2*n*z*z)) == 0
assert sp.simplify(sp.Matrix([sp.diff(V_critical,t) for t in (x,y,z)]).dot(F.subs(m,0)) + 2*n*z*z) == 0
h = s + A*s**3 + B*s**5
k = s**2/n + C*s**4
red = -h*k
hx = sp.expand(sp.diff(h,s)*red - (s-h))
kx = sp.expand(sp.diff(k,s)*red - (-n*k+s*h))
eqns = [hx.coeff(s,3), hx.coeff(s,5), kx.coeff(s,4)]
sol = sp.solve(eqns, (A,B,C), dict=True)
assert len(sol) == 1
expected = {A:1/n, B:(5*n+2)/n**3, C:(n+2)/n**3}
assert all(sp.simplify(sol[0][u]-v)==0 for u,v in expected.items())
reduced = sp.expand(red.subs(expected))
assert sp.simplify(reduced.coeff(s,3)+1/n)==0
b = 2/n**2+2/n**3
assert sp.simplify(reduced.coeff(s,5)+b)==0
assert sp.simplify(b/(1/n) - (2/n+2/n**2))==0
for q in [sp.Rational(1,2), sp.Integer(1),sp.Integer(2),sp.Rational(7,3)]:
 assert all(sp.simplify(expr.subs(n,q))==0 for expr in [u.subs(expected) for u in eqns])
print('PASS: Lyapunov identities, center jets, scalar quintic term, logarithmic coefficient.')
