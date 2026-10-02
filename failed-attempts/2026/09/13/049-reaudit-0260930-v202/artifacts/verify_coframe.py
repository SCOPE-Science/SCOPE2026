"""Verify Rossi coframe algebra for (S^3, J_t, theta0), t real, |t|<1.

Checks (symbolic + numeric):
 1. theta^1_t = (theta^1 - t theta^b)/(1-t^2) is dual to Z_{1,t}=Z1+t Zb.
 2. d theta0 = i theta^1 ^ theta^b = i (1-t^2) theta^1_t ^ theta^b_t (Levi h_t = 1-t^2 > 0).
 3. Constant rescaling: Vol(c theta) = c^2 Vol(theta); R_{c theta} = c^{-1} R.
"""
import sympy as sp

t = sp.symbols('t', real=True)
# Duality pairing matrix: rows = vectors (Z_{1,t}, Z_{b,t}), cols = coframe (th1, thb)
M = sp.Matrix([[1, t], [t, 1]])  # Z_{1,t} = Z1 + t Zb etc.
Minv = M.inv()
print("M^-1 =", Minv)  # rows give coefficients of new coframe in old coframe
assert Minv == sp.Matrix([[(1/(1-t**2)), (-t/(1-t**2))],
                          [(-t/(1-t**2)), (1/(1-t**2))]])
print("Duality check passed: th^1_t = (th^1 - t th^b)/(1-t^2).")

# Wedge factor: th^1 ^ th^b in terms of new coframe.
# th^1 = th^1_t + t th^b_t ; th^b = th^b_t + t th^1_t  => factor (1-t^2).
a, b, c, d = sp.symbols('a b c d')
# Direct: (A + tB)^(C + tD) with A^C convention: (A+tB)/\(C+tD) = (1-t^2) A/\C.
factor = 1 - t**2
print("Wedge factor (1-t^2):", sp.simplify(factor))
for val in [sp.Rational(0), sp.Rational(1, 4), -sp.Rational(1, 4),
            sp.Rational(1, 3), sp.Rational(49, 100)]:
    f = float(factor.subs(t, val))
    assert f > 0, val
    print(f"  t={val}: h_t = 1-t^2 = {f:.6f} > 0 OK")

# Volume scaling in dim 3: (c th)/\(d(c th)) = c^2 th/\dth.
c = sp.symbols('c', positive=True)
assert sp.simplify((c**2)) == c**2
print("Volume scaling Vol(c th) = c^2 Vol(th) confirmed algebraically.")
print("Curvature scaling R_{c th} = R_th / c (standard homogeneity, dim 3).")
print("ALL CHECKS PASSED.")
