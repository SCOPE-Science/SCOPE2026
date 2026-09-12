"""Kovacic check for generic 4-punctured-sphere Schwarzian family.

Verifies, for a representative rational triple (the argument is uniform in the
punctures): pole structure of R_lambda, double-pole coefficients 1/2, behavior
at infinity, and that Kovacic Cases 1, 2, 3 all give d < 0, hence no Liouvillian
solutions, hence differential Galois group of u'' + (R/2) u = 0 is SL2(C).

The key point: all Kovacic data depend ONLY on the double-pole coefficients
(1/2, fixed by the parabolic/4-punctured-sphere normalization) and the pole
count (4), hence are INDEPENDENT of the accessory parameter lambda. The
conclusion SL2 therefore holds for every lambda, in particular generic lambda.
"""
import sympy as sp

s, lam = sp.symbols('s lam')
# Representative rational punctures; the computation is identical for any
# distinct rationals (only Vandermonde-type nonzero quantities change).
a1, a2, a3 = sp.Rational(0), sp.Rational(1), sp.Rational(2)
a = [a1, a2, a3]
P = (s - a1) * (s - a2) * (s - a3)

# Homogeneous direction: sum b_i = 0 and weighted sum b_i*a_i = 0.
b = [a2 - a3, a3 - a1, a1 - a2]
# Particular solution: sum c0_i = 0, weighted sum = -1.
c0 = [-sp.Integer(1) / (a1 - a2), sp.Integer(1) / (a1 - a2), sp.Rational(0)]
assert sum(c0) == 0
assert sum(c0[i] * a[i] for i in range(3)) == -1
assert sum(b) == 0
assert sum(b[i] * a[i] for i in range(3)) == 0

R = sum(sp.Rational(1, 2) / (s - a[i]) ** 2 + (c0[i] + lam * b[i]) / (s - a[i])
        for i in range(3))
R = sp.simplify(R)
print("R_lambda =", R)

num, den = sp.together(R).as_numer_denom()
N = sp.expand(num)
print("denominator:", sp.factor(den), " expected ", sp.factor(P**2))
ratio = sp.simplify(den / P**2)
print("den/P^2 =", ratio)
assert ratio.is_number and ratio != 0
dN = sp.Poly(N, s).degree()
print("deg numerator N:", dN, "(expect 4 for generic lam)")
assert dN == 4

lim_inf = sp.limit(s**2 * R, s, sp.oo)
print("s^2 R at oo:", lim_inf, "(expect 1/2)")
assert lim_inf == sp.Rational(1, 2)

def pp_coeff(expr, pt):
    """Principal-part double-pole coefficient via limit (avoids 0/0 at subs)."""
    return sp.simplify(sp.limit((s - pt) ** 2 * expr, s, pt))


for i in range(3):
    ai = a[i]
    bcoef = pp_coeff(R, ai)
    print(f"double-pole coeff at a{i + 1}={ai}:", bcoef, "(expect 1/2)")
    assert bcoef == sp.Rational(1, 2)
    Nai = sp.simplify(sp.Poly(N, s).eval(ai))
    assert Nai != 0  # exact double pole; overall scalar from together() is nonzero

# Equation u'' = r u with r = -R/2.
r = sp.simplify(-R / 2)
for i in range(3):
    ai = a[i]
    bc = pp_coeff(r, ai)
    print(f"b (r-coeff) at a{i + 1}:", bc, "(expect -1/4)")
    assert bc == sp.Rational(-1, 4)
bo = sp.limit(s**2 * r, s, sp.oo)
print("b_oo =", bo, "(expect -1/4)")
assert bo == sp.Rational(-1, 4)

# Kovacic Case 1: every pole (incl. oo) has sqrt(1+4b) = 0, alpha = 1/2.
# d = alpha_oo - sum over the 3 FINITE poles (oo counted once, not twice).
sqrt_disc = sp.sqrt(1 + 4 * sp.Rational(-1, 4))
assert sqrt_disc == 0
alp = sp.Rational(1, 2)
d1 = alp - 3 * alp
print("Case1 d =", d1, "(<0 => Case 1 impossible)")
assert d1 == -1 and d1 < 0

# Kovacic Case 2: E_c = {2} at every pole, d = (2 - 3*2)/2.
d2 = sp.Rational(2 - 3 * 2, 2)
print("Case2 d =", d2, "(<0 => Case 2 impossible)")
assert d2 < 0

# Kovacic Case 3: E_c = {6} at every pole; d = (6-18)/m < 0 for m = 4, 6, 12.
for m in [4, 6, 12]:
    d3 = sp.Rational(6 - 3 * 6, m)
    print(f"Case3 m={m} d =", d3, "(<0 => impossible)")
    assert d3 < 0

print("CONCLUSION: no Liouvillian solutions for any lam; "
      "differential Galois group is SL2(C).")
print("Hence by Casale-Freitag-Nagloo, the Schwarzian X_lam is strongly "
      "minimal.")
