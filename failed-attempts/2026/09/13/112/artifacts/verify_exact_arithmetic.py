"""Exact rational verification for lane-1728 (S3 vacuous-truth proof).

Checks, with Fractions (no floating point):
  t0, partial barycenters A' = B' = 9/16 I, traces 27/16,
  mass bounds lam >= 9/16, 1-lam >= 9/20, sum 81/80 > 1 (contradiction).
"""
from fractions import Fraction

alpha = Fraction(5, 4)
t0 = (1 + alpha) / 2
assert t0 == Fraction(9, 8), t0

# Cofactor/barycenter linear system: A' + B' = t0 I ; A' + alpha B' = t0^2 I
diff = t0 * t0 - t0          # (t0^2 - t0) = 9/64
assert diff == Fraction(9, 64), diff
Bcoeff = diff / (alpha - 1)  # B' coefficient -> 9/16
Acoeff = t0 - Bcoeff         # A' coefficient -> 9/16
assert Bcoeff == Fraction(9, 16), Bcoeff
assert Acoeff == Fraction(9, 16), Acoeff

# Traces of the partial barycenters
trA = 3 * Acoeff
trB = 3 * Bcoeff
assert trA == Fraction(27, 16) and trB == Fraction(27, 16), (trA, trB)

# Mass lower bounds from tr(R) <= 3, tr(alpha Q) <= 3 alpha
lam_lo = trA / 3            # lam >= 9/16
omu_lo = trB / (3 * alpha)  # (1-lam) >= 9/20
assert lam_lo == Fraction(9, 16), lam_lo
assert omu_lo == Fraction(9, 20), omu_lo

total_lo = lam_lo + omu_lo
assert total_lo == Fraction(81, 80), total_lo
assert total_lo > 1

print("alpha =", alpha)
print("t0 =", t0)
print("t0^2 - t0 =", diff)
print("B' coeff =", Bcoeff, " A' coeff =", Acoeff)
print("trace =", trA)
print("lam >= ", lam_lo, " (1-lam) >= ", omu_lo)
print("sum lower bound =", total_lo, "> 1 -> contradiction. OK")
