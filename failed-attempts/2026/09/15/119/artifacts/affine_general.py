"""General AFFINE phi: F = a*x2 + b*y1 + c*y2 + d*s + e.
Determine for which (a,b,c,d,e) the X1-graph is exactly H-minimal."""
import sympy as sp
from bernstein_h2_scan import hnum_on_graph

x2, y1, y2, s = sp.symbols('x2 y1 y2 s')
a, b, c, d, e = sp.symbols('a b c d e')
phi = a*x2 + b*y1 + c*y2 + d*s + e
sanity, Hres, S2res = hnum_on_graph(phi)
print("sanity (X1-1) =", sanity)
Hres = sp.expand(Hres)
print("Hnum|S =", Hres)
P = sp.Poly(Hres, x2, y1, y2, s)
print(f"degree={P.total_degree()}, nterms={len(P.terms())}")
for mon, coeff in sorted(P.as_dict().items()):
    print(f"  mon {mon}: {sp.factor(coeff)}")
# Solve coeff system == 0
sol = sp.solve(P.coeffs(), (a, b, c, d, e), dict=True)
print("solve over coeffs:", sol)
