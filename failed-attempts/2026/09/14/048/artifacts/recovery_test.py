"""Bounded recovery test for conductor-ordered S3 Selmer-rank density target.

Checks:
 (i) coherence of the claimed weights c_r (even/odd partial sums -> 1);
 (ii) conductor comparison: N(cond(E^chi)) = N(cond chi)^2 * D_S(chi) with
      D_S taking only finitely many values (S = bad places of E/K union {2});
      hence density transfer from chi-ordering to conductor-ordering needs
      per-class Selmer densities -- the step unavailable in the S3 case.
"""
from fractions import Fraction

# (i) exact rational c_r
P_den = 1
P = Fraction(1, 1)
terms = []
for j in range(1, 25):
    P *= (Fraction(1, 1) + Fraction(1, 2 ** j))
c = [Fraction(1, 1) / P]
for r in range(1, 9):
    c.append(c[-1] * Fraction(2, 2 ** r - 1))
print("c_r (float):", [float(x) for x in c])
ev = sum(c[0::2])
od = sum(c[1::2])
print("even partial sum r=0..8:", float(ev))
print("odd  partial sum r=1..7:", float(od))
# tail bound: c_r decays like 2^{-r(r-1)/2} up to constants, so tail < 1e-9 here
assert abs(float(ev) - 1.0) < 1e-6, "even weights must sum to 1"
assert abs(float(od) - 1.0) < 1e-6, "odd weights must sum to 1"
print("coherence: PASS (formula internally consistent, sums to 1 per parity)")

# (ii) conductor comparison structure
print("conductor comparison: N(cond E^chi) = N(cond chi)^2 * D_S(chi), "
      "D_S finitely-valued (S-local).")
print("transfer lemma: conductor-ordered density exists iff chi-ordered "
      "per-class densities exist and agree; per-class input is exactly the "
      "missing S3 2-Selmer distribution theorem.")
print("recovery verdict: BLOCKED at uniformity / all-r distribution step.")
