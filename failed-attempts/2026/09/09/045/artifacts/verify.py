"""Independent stdlib-only verifier: replays remainder_log.json.

Checks (from committed rational endpoints only + recomputed rigorous bounds):
  1. sqrt5/zeta enclosure consistency, zeta in (7,8).
  2. Ai(5), Ai'(5) boxes contain the high-precision reference values
     (as necessary-condition cross-check, not as proof).
  3. Picard self-mapping + contraction inequalities from log rationals.
  4. Recomputes the full rigorous chain from scratch (interval.py) and
     confirms the recomputed boxes are SUBSETS of the committed boxes.
Prints VERIFY_OK or raises.
"""
import json
import sys
from fractions import Fraction as F

ART = "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-382/output/artifacts"
sys.path.insert(0, ART)
from interval import I, exp_interval, isqrt, pi_interval

log = json.load(open(ART + "/remainder_log.json"))
Ai5 = I(F(log["Ai5"][0]), F(log["Ai5"][1]))
Api5 = I(F(log["Api5"][0]), F(log["Api5"][1]))
zeta = I(F(log["zeta"][0]), F(log["zeta"][1]))
h, M0, M1 = F(log["h"]), F(log["M0"]), F(log["M1"])
B2, L = F(log["B2"]), None

assert zeta.lo > 7 and zeta.hi < 8, "zeta range"
# reference cross-check (mpmath 80-digit: Ai(5)=1.08334428...e-4, Ai'(5)=-2.47413890...e-4)
assert Ai5.lo <= F("0.0001083444281360744") <= Ai5.hi, "Ai5 misses reference"
assert Api5.lo <= F("-0.0002474138908684624") <= Api5.hi, "Api5 misses reference"

# Picard inequalities from committed rationals
assert Ai5.hi + h * M1 <= M0, "w self-map upper"
assert Ai5.lo - h * M1 >= -M0, "w self-map lower"
assert Api5.hi + h * F(log["B2"]) <= M1, "v self-map upper"
assert Api5.lo - h * F(log["B2"]) >= -M1, "v self-map lower"
assert h * (6 * M0 * M0 + 5) < 1, "contraction"
assert F(log["B2"]) == 2 * M0**3 + 5 * M0, "B2 formula"

# Full recomputation from scratch; must land inside committed boxes
sq5 = isqrt(I(F(5)))
z2 = I(F(2, 3)) * I(F(5)) * sq5
assert z2.lo >= zeta.lo and z2.hi <= zeta.hi, "zeta not reproduced inside log box"
pi = pi_interval(K=12)
x4 = isqrt(isqrt(I(F(5))))
e_neg = exp_interval(-z2)
pre = e_neg / (I(2) * isqrt(pi) * x4)
pre2 = (x4 * e_neg) / (I(2) * isqrt(pi))
u1, u2 = F(5, 72), F(385, 10368)
v2 = F(-13, 11) * u2
A2 = pre * (I(1) + I(-(I(u1) / z2).hi, F(0)))
# fac2 = 1 + 7/(72z) + S2 with S2 in [v2/z^2,0]; reconstruct carefully:
c1 = I(F(7, 72)) / z2
S2 = I((I(v2) / (z2 * z2)).lo, F(0))
P2 = -(pre2 * (I(1) + c1 + S2))
assert A2.lo >= Ai5.lo and A2.hi <= Ai5.hi, (A2, Ai5)
assert P2.lo >= Api5.lo and P2.hi <= Api5.hi, (P2, Api5)
print("VERIFY_OK")
print("Ai5  =", float(Ai5.lo), float(Ai5.hi))
print("Api5 =", float(Api5.lo), float(Api5.hi))
print("hL   =", float(h * (6 * M0 * M0 + 5)))
