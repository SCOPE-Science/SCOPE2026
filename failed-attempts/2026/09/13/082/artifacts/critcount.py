import sys
sys.path = [p for p in sys.path if p not in ('/tmp', '')]
import sympy as sp

def count_crit(W, x, y, label):
    Wx = sp.diff(W, x); Wy = sp.diff(W, y)
    # clear denominators: multiply by suitable monomial
    Fx = sp.together(Wx).as_numer_denom()[0]
    Fy = sp.together(Wy).as_numer_denom()[0]
    Fx = sp.Poly(Fx, x, y); Fy = sp.Poly(Fy, x, y)
    print("="*60)
    print(label, ": W =", W)
    print("  Fx =", Fx.as_expr(), " Fy =", Fy.as_expr())
    # resultant in y then solve
    try:
        resx = Fx.resultant(Fy, y)
        resx = sp.Poly(resx, x)
        print("  resultant_x degree:", resx.degree())
        # count nonzero roots with multiplicity via degree (generic)
        # now solve fully
        sols = sp.solve([Fx.as_expr(), Fy.as_expr()], [x, y], dict=True)
        # filter nonzero
        sols = [s for s in sols if (complex(s[x]).__abs__() if s[x].is_number else True) ]
        print("  nsols:", len(sols))
        for s in sols:
            print("   ", {str(k): complex(v.evalf()) for k,v in s.items()})
    except Exception as e:
        print("  failed:", type(e).__name__, str(e)[:500])

x, y = sp.symbols('x y')
cands = {
 "P2-Clifford": x + y + 1/(x*y),
 "P1xP1": x + y + 1/x + 1/y,
 "Bl2-pent": x + y + 1/(x*y) + 1/x + 1/y,
 "guess-Bl5-oct": x + y + 1/(x*y) + 1/x + 1/y + x/(y) + y/(x) + x*y,  # 8 terms?
 "guess-dP4-A": x + y + 1/x + 1/y + 1/(x*y) + x*y,
 "guess-dP4-B": x + y + 1/(x*y) + 2/x + 2/y,
}
for k,v in cands.items():
    count_crit(v, x, y, k)
