# Global Tjurina Groebner check (sympy over QQ): ideal (f, fx, fy, fz).
# Run: python3 global_tjurina.py  (requires sympy)
import sympy as sp
x, y, z = sp.symbols('x y z')
f = x**5 + y**6 + z**7 + x**3*y**2*z
fx, fy, fz = sp.diff(f, x), sp.diff(f, y), sp.diff(f, z)
for order in ['grlex', 'lex']:
    G = sp.groebner([f, fx, fy, fz], x, y, z, order=order)
    print(order, 'len:', len(G.polys))
    for p in G.polys:
        print('  ', sorted(sp.Poly(p.as_expr(), x, y, z).as_dict().items()))
