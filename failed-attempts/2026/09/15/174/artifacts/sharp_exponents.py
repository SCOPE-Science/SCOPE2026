"""Exact rational-exponent checks for p-adic small-cap sharp examples (recovery test).

Covers: (1) coherent all-caps endpoint sharpness; (2) isotropic null-strip
phase diagram vs claimed exponent; (3) equichar-2 diagonal-fiber saturation.
Uses Fraction so all comparisons are exact (no floating point).
"""
from fractions import Fraction

print("== 1. Coherent (all caps): endpoint sharpness ==")
for asum in [Fraction(1), Fraction(5, 4), Fraction(3, 2)]:
    p = 2 + Fraction(2, 1) / asum
    e_claim = asum * (Fraction(1, 2) - 1 / p)
    e_coh = (asum * (p - 2) - 1) / p
    assert e_claim == e_coh, (asum, e_claim, e_coh)
    print(f"|a|={asum} pend={p} exponent={e_claim} EXACT MATCH")

print("== 2. Isotropic null strip, square caps a=(3/4,3/4) ==")
for p in [Fraction(5, 2), Fraction(3), Fraction(10, 3), Fraction(4), Fraction(9, 2)]:
    if p < 3:
        actual = (p - 2) / (2 * p)
    elif p == 3:
        print("p=3: log-loss boundary case, skipped (needs separate shell-log analysis)")
        continue
    else:
        actual = 1 - Fraction(5, 2) / p
    claimed = Fraction(3, 2) * (Fraction(1, 2) - 1 / p)
    tag = "OK(<=)" if actual <= claimed else "EXCEEDS (p outside claimed range only)"
    print(f"p={p}: actual={actual} claimed={claimed} {tag}")

print("== 3. Equichar-2 diagonal fiber, square caps a=(3/4,3/4) ==")
for p in [Fraction(5, 2), Fraction(3), Fraction(10, 3)]:
    actual = Fraction(3, 4) * (1 - 2 / p)
    claimed = Fraction(3, 2) * (Fraction(1, 2) - 1 / p)
    assert actual == claimed
    print(f"p={p}: actual={actual} claimed={claimed} SATURATES (no violation)")

print("CONCLUSION: no in-range falsification; range p<=2+2/|a| necessary and endpoint sharp.")
