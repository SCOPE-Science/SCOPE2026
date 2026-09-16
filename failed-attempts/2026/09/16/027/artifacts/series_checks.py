"""Reproducible symbolic checks for quoted HIMW steps (HIMW orientation (1.3)).

Check 1: radial tip curvature. Eq (1.3) radially:
  upp + (n-1)*up*(1+up^2)/r + (1+up^2) = 0.
  Ansatz u = a2 r^2 + a4 r^4 + a6 r^6 gives 2*a2*n + 1 = 0, i.e. u_rr(0) = -1/n.
Check 2: Thm 9.2 Taylor identity:
  (x1 D2 - x2 D1)(-k1 x1^2 - k2 x2^2) = 2 (k1 - k2) x1 x2.
"""
import sympy as sp

r = sp.symbols('r')
n = sp.symbols('n', integer=True, positive=True)
a2, a4, a6 = sp.symbols('a2 a4 a6')
u = a2*r**2 + a4*r**4 + a6*r**6
up = sp.diff(u, r); upp = sp.diff(up, r)
expr = (upp + (n-1)*up*(1+up**2)/r + (1+up**2)).expand()
s = sp.series(expr, r, 0, 6).removeO()
c0 = sp.expand(s).coeff(r, 0)
assert c0 == 2*a2*n + 1, c0
a2sol = sp.solve(c0, a2)[0]
assert a2sol == -1/(2*n), a2sol
print("Check 1 passed: 2*a2*n + 1 = 0 -> u_rr(0) = 2*a2 =", a2sol*2)

x1, x2, k1, k2 = sp.symbols('x1 x2 k1 k2')
q = -k1*x1**2 - k2*x2**2
f = sp.expand(x1*sp.diff(q, x2) - x2*sp.diff(q, x1))
assert sp.expand(f - 2*(k1-k2)*x1*x2) == 0, f
print("Check 2 passed: (x1 D2 - x2 D1) q =", f)
