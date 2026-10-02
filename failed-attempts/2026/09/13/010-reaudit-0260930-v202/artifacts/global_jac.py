# Global Jacobian Groebner check (sympy over QQ) + independent mod-p Buchberger count.
# Run: python3 global_jac.py  (requires sympy)
import sympy as sp
x, y, z = sp.symbols('x y z')
f = x**5 + y**6 + z**7 + x**3*y**2*z
fx, fy, fz = sp.diff(f, x), sp.diff(f, y), sp.diff(f, z)
G = sp.groebner([fx, fy, fz], x, y, z, order='grlex')
print('grlex len:', len(G.polys))
for p in G.polys:
    print('  ', sorted(sp.Poly(p.as_expr(), x, y, z).as_dict().items()))
Gl = sp.groebner([fx, fy, fz], x, y, z, order='lex')
print('lex len:', len(Gl.polys))
for p in Gl.polys:
    print('  ', sorted(sp.Poly(p.as_expr(), x, y, z).as_dict().items()))
