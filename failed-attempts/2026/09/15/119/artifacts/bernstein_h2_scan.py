"""Symbolic H-mean curvature of X1-intrinsic graphs in H^2.

Conventions: H^2 coords (x1,x2,y1,y2,t), group law with factor 2:
  X1 = dx1 + 2 y1 dt ; X2 = dx2 + 2 y2 dt
  Y1 = dy1 - 2 x1 dt ; Y2 = dy2 - 2 x2 dt ; T = dt.
W = {x1 = 0} with coords (x2,y1,y2,s=t).
Graph map: Phi(x2,y1,y2,s) = (phi, x2, y1, y2, s + 2 y1 phi).
Level fn: f = x1 - phi(x2,y1,y2,u), u = t - 2 y1 x1.
H-mean curvature numerator: Hnum = div_H(A)*S2 - 1/2 sum_Z A_Z Z(S2),
  A_Z = Z(f), S2 = sum A_Z^2.  Minimality <=> Hnum|_S = 0.
Restriction to S: x1 = phi0, t = s + 2 y1 phi0, phi0 = phi(x2,y1,y2,s).
"""
import sympy as sp

x1, x2, y1, y2, t, s = sp.symbols('x1 x2 y1 y2 t s')


def fields(g):
    gx1 = sp.diff(g, x1); gx2 = sp.diff(g, x2)
    gy1 = sp.diff(g, y1); gy2 = sp.diff(g, y2); gt = sp.diff(g, t)
    X1 = gx1 + 2*y1*gt
    X2 = gx2 + 2*y2*gt
    Y1 = gy1 - 2*x1*gt
    Y2 = gy2 - 2*x2*gt
    return [sp.expand(X1), sp.expand(X2), sp.expand(Y1), sp.expand(Y2)]


def hnum_on_graph(phi):
    """phi: sympy expr in (x2,y1,y2,s). Returns (sanity_X1eq1, Hnum restricted, S2 restricted)."""
    u = t - 2*y1*x1
    f = x1 - phi.subs({x2: x2, y1: y1, y2: y2, s: u})
    f = sp.expand(f)
    A = fields(f)
    sanity = sp.simplify(A[0] - 1)
    S2 = sum(a**2 for a in A)
    ZA = fields(A[0])[:1] + fields(A[1])[1:2] + fields(A[2])[2:3] + fields(A[3])[3:]
    # div = X1(A1)+X2(A2)+Y1(A3)+Y2(A4)
    div = sp.expand(fields(A[0])[0] + fields(A[1])[1] + fields(A[2])[2] + fields(A[3])[3])
    ZS2 = fields(S2)
    Hnum = sp.expand(div*S2 - sp.Rational(1, 2)*sum(A[i]*ZS2[i] for i in range(4)))
    phi0 = phi
    Hres = sp.expand(Hnum.subs({x1: phi0, t: s + 2*y1*phi0}))
    S2res = sp.expand(S2.subs({x1: phi0, t: s + 2*y1*phi0}))
    return sanity, Hres, S2res


def test(name, phi):
    sanity, Hres, S2res = hnum_on_graph(phi)
    ok_sanity = (sanity == 0)
    is_min = (Hres == 0)
    print(f"--- {name}: phi = {phi}")
    print(f"    X1(f)==1 identically: {ok_sanity}")
    print(f"    EXACTLY H-MINIMAL (Hnum|S == 0): {is_min}")
    if not is_min:
        P = sp.Poly(Hres, x2, y1, y2, s)
        print(f"    Hnum|S degree={P.total_degree()}, terms={len(P.terms())}")
    return is_min


results = {}
results['affine_t-indep'] = test('affine (vertical plane)', 1 + 2*x2 - 3*y1 + 4*y2)
results['quad_sum'] = test('quad sum', x2**2 + y1**2 + y2**2)
results['quad_diff'] = test('quad diff', x2**2 - y2**2)
results['cubic'] = test('cubic', x2**3 - 3*x2*y2**2)
results['lin_s'] = test('linear s', 3*s)
results['y1*s'] = test('y1*s', y1*s)
results['x2*s'] = test('x2*s', x2*s)
results['s^2'] = test('s^2', s**2)
results['x2^2+s'] = test('x2^2+s', x2**2 + s)
results['affine+s'] = test('affine+s', 1 + 2*x2 - 3*y1 + 4*y2 + s)
results['affine+2s'] = test('affine+2s', x2 + 2*s)
results['y2*s^2'] = test('y2*s^2', y2*s**2)
results['x2*y1+s'] = test('x2*y1+s', x2*y1 + s)
results['helicoid-like'] = test('x2*y1-s', x2*y1 - s)
print()
print("SUMMARY:", {k: ('MINIMAL' if v else 'not minimal') for k, v in results.items()})
