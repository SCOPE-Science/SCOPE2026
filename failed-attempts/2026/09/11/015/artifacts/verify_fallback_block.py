"""Fallback-block certificate for lane-712: s_* = 13/126 needs b >= 13/63 > eta.

Exact rational checks (stdlib only):
  s_* = eta/2 + (1/6 - eta/2)/3 with eta=1/7  =>  13/126 ~ 0.10317
  eta/2 = 1/14 < s_* < 1/6 (strictly interior)
  any s<b/2-type DF/D'Angelo route needs b >= 2 s_* = 13/63 ~ 0.20635
  but admissible b <= eta = 1/7 = 9/63 < 13/63: contradiction.
  interpolation anchors {0} U [0,1/14) cap below s_*: convex combos stay < 1/14.

Run: python3 output/artifacts/verify_fallback_block.py
"""
from fractions import Fraction

eta = Fraction(1, 7)
df_half = eta / 2            # 1/14
barrett = Fraction(1, 6)
s_star = eta / 2 + (barrett - eta / 2) / 3
need = 2 * s_star

checks = []
checks.append(("s_* == 13/126", s_star == Fraction(13, 126)))
checks.append(("DF/2 == 1/14", df_half == Fraction(1, 14)))
checks.append(("s_* strictly interior: DF/2 < s_* < 1/6", df_half < s_star < barrett))
checks.append(("need b >= 2s_* == 13/63", need == Fraction(13, 63)))
checks.append(("need exceeds eta: 13/63 > 1/7=9/63", need > eta))
# interpolation: anchors below 1/14 cannot reach s_* by convexity
anchors_ok = all(
    (1 - t) * Fraction(0, 1) + t * a < s_star
    for a in [Fraction(0, 1), Fraction(1, 15), Fraction(1, 14) - Fraction(1, 1000)]
    for t in [Fraction(1, 2), Fraction(9, 10), Fraction(1, 1)]
)
checks.append(("L2 + sub-DF/2 anchors interpolate only below s_*", anchors_ok))

all_ok = True
for name, ok in checks:
    print(("PASS" if ok else "FAIL"), "-", name)
    all_ok = all_ok and ok
print("s_* =", s_star, "| 2s_* =", need, "| eta =", eta)
print("ALL VERIFY_OK" if all_ok else "VERIFY_FAILED")
raise SystemExit(0 if all_ok else 1)
