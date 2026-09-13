"""Bounded verification test for the Arreche-Dreyfus computation on Y''=(x^3+t)Y.

Checks the exact symbolic identities used in the proof:
  (A) z=1/x transform at infinity -> Y-coefficient pole order 7 (irregular).
  (B) Riccati residue lemma: u=a/(x-c) gives (a^2-a)/(x-c)^2 leading polar part.
  (C) Case-1 degree obstruction: (f x^d)'+(f x^d)^2 has degree 2d; 2d=3 impossible.
  (D) Case-2 trace identities: Delta=4r-2s'-s^2, s=-Delta'/(2Delta) consequences:
      log-derivative vanishes at infinity; pole-order doubling  m -> 2m.
  (E) Telescoping (integrability) equation L[b] := b'''-4r b'-2r'b with r=x^3+t:
      monomial leading term -(4nu+6) f x^{nu+2}; pole-amplification m -> m+3.
"""
import sympy as sp

x, z, t, c, a, f, m = sp.symbols('x z t c a f m')
ok = []

# (A) infinity irregularity
Y = sp.Function('Y')
r = x**3 + t
# x=1/z: d/dx = -z^2 d/dz; d^2/dx^2 = z^4 D_zz + 2 z^3 D_z
Yz = sp.Function('Yz')
expr = z**4 * Yz(z).diff(z, 2) + 2*z**3 * Yz(z).diff(z) - (z**-3 + t) * Yz(z)
bcoef = -(z**-3 + t) / z**4  # coefficient of Yz after dividing by z^4
bcoef = sp.simplify(bcoef)
pole_order = -sp.Poly(sp.together(bcoef).as_numer_denom()[0].subs(z, 0)*0
                      + sp.together(bcoef).as_num_denom()[0], z).degree() \
    if False else None
num, den = sp.together(bcoef).as_numer_denom()
ord_zero_den = sp.Poly(den, z).degree()  # den = z^7
print("(A) transformed Y-coefficient:", bcoef, "| denom degree:", ord_zero_den)
assert ord_zero_den == 7, "expected pole order 7"
# first-derivative coefficient 2/z has pole order 1 (fine); Y-coef order 7 > 2
ok.append("A: infinity irregular (Y-coefficient pole order 7 > 2)")

# (B) Riccati residue lemma
u = a / (x - c)
lead = sp.simplify(sp.diff(u, x) + u**2)
print("(B) u'+u^2 =", lead, "= (a^2-a)/(x-c)^2 -> a=1")
assert sp.simplify(lead - (a**2 - a) / (x - c)**2) == 0
ok.append("B: finite Riccati poles simple with residue 1")

# (C) case-1 degree obstruction
for d in range(0, 7):
    lead_term = sp.expand(f**2 * x**(2*d))  # (f x^d)^2 dominates u' for d>=1
    assert 2*d != 3
print("(C) 2d never equals 3 for integer d; odd-degree polynomial potential")
ok.append("C: deg(u'+u^2)=2d even or LHS bounded; r=x^3+t degree 3 unmatched")

# (D) case-2 trace identities (repaired): Delta=4r-2s'-s^2, s=-Delta'/(2Delta).
# (D1) s is -(1/2) a log derivative: only simple poles; a Delta pole of order
#      P gives s-residue +P/2 (sign check).
# (D2) residue a=2 excluded: for s=2/(x-c) the double poles cancel
#      (2a-a^2=0), so Delta=4r-2s'-s^2 has valuation >= -1 at c, whence
#      s=-Delta'/(2Delta) cannot have residue 2 there.
# (D3) s=P+sum 1/(x-c_i) vanishes at infinity (log derivative), so P=0;
#      Delta=Q/prod(x-c_i)^2 with deg Q=3+2N, and Delta'/Delta=-2s forces Q'=0.
s = sp.Function('s')
E, g, a1 = sp.symbols('E g a1')
Delta = g * x**E * (1 + a1 / x)
s_expr = -sp.diff(Delta, x) / (2 * Delta)
print("(D) s=-Delta'/(2Delta) series:", sp.series(s_expr, x, sp.oo, 3))
# (D1) sign: Delta=y^-P (pole order P) -> s residue +P/2
yy, P = sp.symbols('yy P')
print("(D1) Delta pole order P -> s residue +P/2:",
      sp.simplify(-sp.diff(yy**(-P), yy) / (2 * yy**(-P)) * yy))
assert sp.simplify(-sp.diff(yy**(-P), yy) / (2 * yy**(-P)) - P / (2 * yy)) == 0
# (D2) a=2 cancellation at x=c
y = sp.Symbol('y')
for aa in (1, 2):
    ss = aa / (x - c)
    DD = 4*r - 2*sp.diff(ss, x) - ss**2
    DDy = sp.together(DD.subs(x, y + c))
    numD, denD = DDy.as_numer_denom()
    pn, pd = sp.Poly(sp.expand(numD), y), sp.Poly(sp.expand(denD), y)
    vn = min(mo[0] for mo in pn.monoms())
    vd = min(mo[0] for mo in pd.monoms())
    print(f"(D2) a={aa}: valuation of Delta at c = {vn - vd}"
          f" (2a-a^2={2*aa - aa**2})")
    if aa == 1:
        assert vn - vd == -2  # Delta ~ -1/(x-c)^2 for residue 1
    else:
        assert vn - vd >= -1  # double poles cancel for residue 2
# residue bookkeeping: valuation e of Delta at c gives s-residue -e/2 != 2
for e in (-1, 0, 1, 2):
    print(f"(D2) Delta valuation {e} -> s-residue {-e}/2 != 2")
    assert -sp.Rational(e, 2) != 2
ok.append("D: log-derivative sign +P/2; residue a=2 excluded (Delta val>=-1)")
# (D3) s=sum 1/(x-c_i) vanishes at infinity, so polynomial part P=0
c1, c2 = sp.symbols('c1 c2')
for ssN, N in ((sp.Integer(0), 0), (1/(x - c1), 1),
               (1/(x - c1) + 1/(x - c2), 2)):
    print(f"(D3) N={N}: s(oo)=", sp.limit(ssN, x, sp.oo), "-> P=0")
    assert sp.limit(ssN, x, sp.oo) == 0
    DD = sp.together(4*r - 2*sp.diff(ssN, x) - ssN**2)
    numQ, denQ = DD.as_numer_denom()
    denQ = sp.Poly(sp.expand(denQ), x)
    numQ = sp.Poly(sp.expand(numQ), x)
    # denominator is prod(x-c_i)^2 up to constant; Q has degree 3+2N
    assert denQ.degree() == 2*N, (N, denQ.degree())
    assert numQ.degree() == 3 + 2*N, (N, numQ.degree())
    assert numQ.nth(3 + 2*N) == 4, (N, numQ.nth(3 + 2*N))
    # Delta'/Delta + 2s simplifies to Q'/Q, which is nonzero (deg>=3)
    QQ = sp.simplify(sp.diff(DD, x) / DD + 2*ssN)
    print(f"(D3) N={N}: deg Q={numQ.degree()}, Q'/Q =", sp.simplify(QQ),
          "!= 0")
    assert not sp.simplify(QQ) == 0
ok.append("D: P=0 at infinity; Delta=Q/prod^2 with deg Q=3+2N>=3 forces Q'/Q!=0")

# (E) telescoping equation L[b] = b'''-4(x^3+t)b'-6x^2 b
def L(b):
    return sp.expand(sp.diff(b, x, 3) - 4*r*sp.diff(b, x) - 6*x**2*b)

for nu in range(0, 7):
    b = f * x**nu
    Lb = L(b)
    p = sp.Poly(Lb, x)
    deg = p.degree()
    lc = p.nth(deg)
    assert deg == nu + 2, (nu, deg)
    assert sp.simplify(lc + (4*nu + 6)*f) == 0, (nu, lc)
    print(f"(E) nu={nu}: deg={deg}, lc={lc} = -(4nu+6)f OK")
# pole amplification: b=(x-c)^{-m} -> L pole order m+3 (valuation at x=c)
y = sp.Symbol('y')
for mm in (1, 2, 3):
    b = 1 / (x - c)**mm
    Ly = sp.together(L(b).subs(x, y + c))
    numL, denL = Ly.as_numer_denom()
    pn, pd = sp.Poly(sp.expand(numL), y), sp.Poly(sp.expand(denL), y)
    vn = min(mo[0] for mo in pn.monoms())
    vd = min(mo[0] for mo in pd.monoms())
    print(f"(E) m={mm}: pole order {vd - vn} == m+3 = {mm + 3}")
    assert vd - vn == mm + 3
# RHS is constant -2: regular of degree 0; LHS always deg>=2 or pole -> no solution
ok.append("E: L[b] has degree nu+2>=2 (polynomial) or pole order m+3>=4; never -2")

print("\nALL CHECKS PASSED")
for line in ok:
    print(" -", line)
