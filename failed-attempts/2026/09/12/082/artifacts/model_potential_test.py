"""Bounded recovery test: model disk potential for monotone dP5-type fibre.

Toric dP5 has 5 boundary divisors -> 5-term Laurent potential (up to GL(2,Z)
+ node smoothings for the Vianna triangle). This script checks that a generic
5-term + one smoothing term model admits nondegenerate critical points, i.e.
that the SELF-Floer part HF(L,L;rho)!=0 is plausible, isolating the block to
the MIXED L-S strip differential (which needs explicit embeddings + J data).
Uses exact Groebner elimination for y, then back-substitution for x.
"""
import sympy as sp

x, y = sp.symbols('x y')
W = x + y + 1/x + 1/y + x/y + sp.Rational(1, 3)*x*y
Wx = sp.diff(W, x)
Wy = sp.diff(W, y)
print("W =", W)
f1 = sp.expand((Wx * x**2).as_numer_denom()[0])
f2 = sp.expand((Wy * y**2).as_numer_denom()[0])
print("f1 =", f1)
print("f2 =", f2)
G = sp.groebner([f1, f2], x, y, order='lex')
polys = list(G.polys)
print("Groebner basis:", [str(p.as_expr()) for p in polys])
# univariate elimination polynomial in y
uni = [p for p in polys if set(p.free_symbols) == {y}]
assert uni, "no univariate elimination polynomial"
py = uni[0].as_expr()
print("elim poly:", sp.expand(py))
yroots = sp.nroots(py)
print(f"{len(yroots)} y-roots (counted with multiplicity in degree)")
sols = []
for yr in yroots:
    xv = sp.solve(f2.subs(y, yr), x)
    for r in xv:
        try:
            xvN = complex(r.evalf())
            yvN = complex(yr.evalf())
            if abs(xvN) < 1e-8 or abs(yvN) < 1e-8:
                continue
            if abs(complex(Wx.subs({x: xvN, y: yvN}).evalf())) > 1e-6:
                continue
            if abs(complex(Wy.subs({x: xvN, y: yvN}).evalf())) > 1e-6:
                continue
            sols.append((xvN, yvN))
        except Exception:
            pass
print(f"verified critical points in (C*)^2: {len(sols)}")
H = sp.Matrix([[sp.diff(Wx, x), sp.diff(Wx, y)],
               [sp.diff(Wy, x), sp.diff(Wy, y)]])
nondeg = 0
for (a, b) in sols:
    det = complex(H.det().subs({x: a, y: b}).evalf())
    ok = abs(det) > 1e-8
    nondeg += ok
    print(f"  x={a:.4f} y={b:.4f} detHess={det:.4f} nondeg={ok}")
assert sols, "no critical point found"
print(f"RESULT: {'PASS' if nondeg else 'DEGENERATE'} - model potential has "
      f"{nondeg} nondegenerate critical point(s); self-Floer side viable, "
      "mixed L-S differential remains the blocker.")
