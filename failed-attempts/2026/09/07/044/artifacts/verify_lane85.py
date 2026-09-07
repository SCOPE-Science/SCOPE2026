"""Lane 85 verification script (stdlib + sympy only).
Checks:
 A. Symbolic divergence of B*X with B=(1+2x^2)^-2 exposes the y-term
    dropped by the audit plan.
 B. Exact-rational counterexample: div(BX)/B >> -1/20 at one point.
 C. B=1 blindness discriminants over the box (exact Fractions).
 D. Lyapunov rescue: V=(x^2+y^2)/2 gives V'<=-(1/10)x^2 uniformly on box.
 E. Audit-plan quartic at vertex (1.1,2.0) re-derived (certifies only the
    truncated, y-free function -- hence irrelevant to true divergence).
"""
import sympy as sp
from fractions import Fraction as Fr

x, y, a, b = sp.symbols('x y a b')
F = x**3 + b*x**2 + a*x
B = (1 + 2*x**2)**(-2)
X1 = y - F
X2 = -x
div = sp.diff(B*X1, x) + sp.diff(B*X2, y)
div_over_B = sp.simplify(div / B)
print("A. div(BX)/B =", div_over_B)
Fp = sp.diff(F, x)
BoverBp_term = sp.simplify(div_over_B - (-Fp))
print("   div/B - (-F') =", sp.simplify(BoverBp_term))
print("   factor in y:", sp.simplify(BoverBp_term / (y - F)), "(= B'/B)")
assert sp.simplify(div_over_B - (-Fp + (-8*x/(1+2*x**2))*(y - F))) == 0
print("   CONFIRMED: div/B = -F'(x) - 8x(y-F(x))/(1+2x^2); linear in y.\n")

# B. exact counterexample (a,b,x,y) = (1.1, 2.0, 1, -10)
fa, fb, fx, fy = Fr(11, 10), Fr(2), Fr(1), Fr(-10)
FF = fx**3 + fb*fx**2 + fa*fx          # 41/10
FFp = 3*fx**2 + 2*fb*fx + fa           # 81/10
val = -FFp + Fr(-8)*fx*(fy - FF) / (1 + 2*fx**2)
print(f"B. F={FF} ({float(FF)}), F'={FFp} ({float(FFp)}), div/B={val} = {float(val)}")
assert val == Fr(59, 2) and val > Fr(-1, 20)
print("   CONFIRMED: div/B = 59/2 > 0 > -1/20; uniform margin claim is FALSE.\n")

# C. B=1 blindness: F' discriminant 4(b^2-3a) over A=[1.1,1.2]x[1.9,2.0]
lo = Fr(19, 10)**2 - 3*Fr(12, 10)   # min b^2-3a at (a=1.2,b=1.9)
hi = Fr(20, 10)**2 - 3*Fr(11, 10)   # max at (a=1.1,b=2.0)
print(f"C. b^2-3a in [{lo}, {hi}] = [{float(lo)}, {float(hi)}]; disc=4x in [{4*lo}, {4*hi}]")
assert lo == Fr(1, 100) and hi == Fr(7, 10)
print("   CONFIRMED: discriminant in [0.04, 2.8] > 0, so -F' changes sign; B=1 inconclusive.\n")

# D. Lyapunov: min over box of (a - b^2/4)
m = Fr(11, 10) - Fr(20, 10)**2 / 4
print(f"D. min(a-b^2/4) = {m} = {float(m)} at (a,b)=(1.1,2.0)")
assert m == Fr(1, 10)
print("   x^2+bx+a = (x+b/2)^2 + (a-b^2/4) >= 1/10 on box => V' <= -(1/10)x^2 <= 0.")
print("   CONFIRMED rescue hypothesis.\n")

# E. vertex quartic at (a,b)=(1.1,2.0): audit-plan M has BOTH a dropped y-term
# AND a flipped sign (+8xF/D -> -8xF/D); reproduce its polynomial identity.
aa, bb = sp.Rational(11, 10), sp.Integer(2)
Aterm = -(aa + 2*bb*x + 3*x**2)
Bterm = -8*x*(aa*x + bb*x**2 + x**3)
Mc_audit = Aterm + Bterm/(1 + 2*x**2)
Pc = sp.expand(Aterm*(1 + 2*x**2) + Bterm)
print("E. P_(1.1,2.0)(x) =", Pc)
assert Pc == -14*x**4 - 24*x**3 - 14*x**2 - 4*x - sp.Rational(11, 10)
print("   matches audit plan; but it audits the WRONG function:")
print("   true y=0 slice is -F'+8xF/D, audit uses -F'-8xF/D (sign flip + y dropped).")
print("\nALL CHECKS PASSED")
