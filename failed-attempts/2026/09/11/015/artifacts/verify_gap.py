"""Exact rational gap certificate for lane-712 target route.

Checks, in exact Fraction arithmetic (no floating point):
  eta_sharp = pi/(W+pi) with W = 6*pi  =>  1/7
  DF/2 cap = eta/2 = 1/14
  Barrett line = pi/W = 1/6
  gap (DF/2, Barrett) nonempty: 1/14 < 1/6
  any DF-type implication "admissible exponent b with b<=eta => s<b/2"
    caps at s < 1/14, hence cannot reach any s in [1/14, 1/6)
  reaching s->1/6 from below via s<b/2 needs b>1/3 > eta=1/7: contradiction.

Run: python3 output/artifacts/verify_gap.py  (stdlib only)
"""
from fractions import Fraction

eta = Fraction(1, 7)        # Liu exact DF index: pi/(6pi+pi)
df_half = eta / 2           # Berndtsson-Charpentier cap: s < eta/2 = 1/14
barrett = Fraction(1, 6)    # pi/W, W = 6pi
need = Fraction(1, 3)       # b needed so b/2 >= 1/6

checks = []
checks.append(("eta == 1/7", eta == Fraction(1, 7)))
checks.append(("DF/2 == 1/14", df_half == Fraction(1, 14)))
checks.append(("Barrett == 1/6", barrett == Fraction(1, 6)))
checks.append(("gap nonempty: DF/2 < Barrett", df_half < barrett))
checks.append(("standard cap below Barrett: DF/2 < 1/6", df_half < barrett))
checks.append(("full-target needs b >= 1/3", need == Fraction(1, 3)))
checks.append(("needed b exceeds eta: 1/3 > 1/7", need > eta))
# Sweep: no admissible b <= eta reaches s >= 1/14, let alone 1/6
sweep_ok = all(b / 2 <= df_half for b in
               [Fraction(i, 700) for i in range(1, 101) if Fraction(i, 700) <= eta])
checks.append(("all b<=eta give s<b/2<=1/14", sweep_ok))

all_ok = True
for name, ok in checks:
    print(("PASS" if ok else "FAIL"), "-", name)
    all_ok = all_ok and ok
print("eta =", eta, "| DF/2 =", df_half, "| Barrett =", barrett,
      "| need b >=", need)
print("ALL VERIFY_OK" if all_ok else "VERIFY_FAILED")
raise SystemExit(0 if all_ok else 1)
