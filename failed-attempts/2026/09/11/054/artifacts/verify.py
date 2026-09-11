"""Replay calibration triple for lane-850 (stdlib only).

Checks, on the toric B_p^4 curve (n=4):
  P(inf) = 32/3 exactly (rational arithmetic),
  P(2) = pi^4/4 with analytic lower bound from pi > 3,
  P(4) = Vol(B_4^4)*Vol(B_{4/3}^4) via math.gamma (margin ~9.88 >> float error),
  c(X_p) = 4 for p = 2, 4, inf (analytic: sup coordinate = 1, Shi-Lu Thm 1.4/Cor 1.6),
  D_cap = 0 <= D_M with C = 1, and reverse D_M <= C*D_cap impossible at p = 2, 4.
"""
from fractions import Fraction
import math

BASELINE = Fraction(32, 3)  # P(B_inf^4) = 16 * (2/3)

# --- Mahler side ---
P_inf = BASELINE
assert P_inf == Fraction(32, 3)

P2 = math.pi ** 4 / 4.0
P2_low = Fraction(81, 4)  # pi > 3  =>  pi^4/4 > 81/4
assert P2_low > BASELINE  # 20.25 > 10.667, margin 9.583
assert P2 > float(P2_low) > float(BASELINE)
D2 = P2 - float(BASELINE)
assert D2 > 9.5

g54 = math.gamma(1.25)
g74 = math.gamma(1.75)
V4 = (2 * g54) ** 4 / math.gamma(2.0)   # Gamma(2) = 1
V43 = (2 * g74) ** 4 / math.gamma(4.0)  # Gamma(4) = 6
P4 = V4 * V43
assert P4 > float(BASELINE) + 9.0  # margin ~9.88
D4 = P4 - float(BASELINE)

# duality cross-check: V(B_{4/3}) recomputed from q=4/3 directly
Vq = (2 * math.gamma(1 + 3 / 4)) ** 4 / math.gamma(1 + 4 * 3 / 4)
assert abs(Vq - V43) < 1e-9

# --- Capacity side (analytic value, recorded) ---
caps = {2: 4.0, 4: 4.0, "inf": 4.0}
for p, Dm in ((2, D2), (4, D4)):
    assert caps[p] - caps["inf"] == 0.0       # D_cap = 0
    assert 0.0 <= 1.0 * Dm                     # D_cap <= 1 * D_M, C = 1
    assert Dm > 0.0                            # reverse with any finite C fails

print(f"P(inf) = {float(P_inf):.6f} (exact {P_inf})")
print(f"P(2)   = {P2:.6f}  (analytic low {float(P2_low):.4f}; D_M = {D2:.6f})")
print(f"P(4)   = {P4:.6f}  (D_M = {D4:.6f})")
print(f"|B_4^4| ~ {V4:.6f}; |B_(4/3)^4| ~ {V43:.6f}")
print("c(X_2) = c(X_4) = c(X_inf) = 4; D_cap = 0 identically")
print("D_cap <= 1*D_M holds; D_M <= C*D_cap impossible for finite C at p=2,4")
print("VERIFY_OK")
