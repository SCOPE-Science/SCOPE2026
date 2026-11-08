"""Exact integer cross-check of the incidence obstruction in RESULT.md.

This checks arithmetic consequences, not the external geometric theorems.
Run: python3 verify_constraints.py
"""
from fractions import Fraction

candidates = []
stages = {"bezout_and_tjurina": 0, "conic_hirzebruch": 0,
          "conic_incidence": 0, "line_hirzebruch": 0}
for t in range(8):
    n = t - 1
    s = 12 - t
    h = 7 - t
    if n < 0:
        continue
    for u in range(s + 1):
        v = s - u
        assert n + 2*t + 3*s == 35
        assert n + 3*t + 4*s == 47
        stages["bezout_and_tjurina"] += 1
        if 8 + n + Fraction(3*s, 4) < 7 + Fraction(5*t, 2):
            continue
        stages["conic_hirzebruch"] += 1
        if v > h:
            continue
        stages["conic_incidence"] += 1
        line_double = 21 - 3*u - v
        if line_double < 0:
            continue
        if line_double + Fraction(3*u, 4) < 7:
            continue
        stages["line_hirzebruch"] += 1
        candidates.append((n, t, s, u, v))
assert not candidates, candidates
assert stages == {"bezout_and_tjurina": 63, "conic_hirzebruch": 42,
                  "conic_incidence": 22, "line_hirzebruch": 0}, stages
print("DEGREE9_ONE_CONIC_SEVEN_LINES_NO_NEARLY_FREE_PASS", stages)
