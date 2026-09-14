"""Numerology check for twisty-phase Kakeya target dim >= 49/20.

Verifies the dictionary between Hausdorff-dimension lower bound and
delta-tube union-volume exponent, and quantifies the wall-term gap that
must be closed by the quantitative coney-twisty hairbrush lemma.

No external data; pure arithmetic. Run: python3 check_numerology.py
"""
import math

DIM_TARGET = 49 / 20          # 2.45
AMBIENT = 3
VOL_EXP = AMBIENT - DIM_TARGET  # union volume |U T| ~ delta^{VOL_EXP}
WOLFF_STRAIGHT = 5 / 2        # straight-line Wolff hairbrush bound
GENERIC_C4 = 12 / 5           # qualitative recall: generic contact-order-4 bound ~2.4

print(f"target dim            = {DIM_TARGET:.4f} (49/20)")
print(f"required volume expon = {VOL_EXP:.4f} (11/20 = 0.55)")
assert abs(VOL_EXP - 11 / 20) < 1e-12

for d in [0.1, 0.01, 0.001]:
    print(f"delta={d:<6}: required |U T| ~= delta^0.55 = {d ** VOL_EXP:.3e}")

# Gap accounting: naive grain overlap counting.
# M ~ delta^{-2} tubes, each vol ~ delta^2, naive union lower bound via
# Cauchy-Schwarz needs L^2 overlap control sum_{T,T'} |T cap T'|.
# Inside a delta^{1/2}-grain, naive overlap per pair ~ delta^3 (full grain
# volume scale) vs twistiness-improved overlap ~ delta^{3+c} for some c>0.
# Required gain: fixed power of delta (not delta^{-eps}).
print()
print("gap accounting:")
print(f"  straight Wolff dim bound      = {WOLFF_STRAIGHT}")
print(f"  curvature loss to reach 49/20 = {WOLFF_STRAIGHT - DIM_TARGET:.4f}")
print(f"  margin above generic C4 ~2.4  = {DIM_TARGET - GENERIC_C4:.4f}")
print("  -> need quantitative (fixed-power) twistiness gain in wall term;")
print("     soft epsilon-removal cannot close it. Lemma unavailable locally.")

# Partitioning degree balance (schematic): cellular term ~ D^3 * (delta-cell bound),
# wall term ~ D * (hairbrush wall bound); optimizing D gives the exponent only
# if the wall bound carries the coney-twisty power gain. Placeholder scan:
print()
for D in [4, 8, 16, 32]:
    print(f"  D={D:3d}: wall factor D={D}, cellular factor D^3={D**3} (schematic; needs lemma)")
print("OK: numerology consistent; missing input = quantitative coney-twisty wall estimate.")
