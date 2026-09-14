"""Bounded recovery test for F_{8,2x1/2(1,1,1)} delta stratification.

Question: can the valuative sign beta(E) = A(E) - S(E) for the Kawamata
divisor over a 1/2(1,1,1) point be decided without the explicit
twisted-cubic model (Mori cone / nef & pseudoeffective thresholds of the
Kawamata blowup)?

Part 1 calibrates model-free numerics: (-K)^3 = 15, A(E) = 1/2.
Part 2 shows the *nef-only* estimate S_nef already swings widely as the
unknown cubic coefficient c = E^3 (stack-vs-coarse convention / normal
bundle, plausibly 4..8) and the unknown nef threshold t0 vary — and,
crucially, the true S(E) needs the divisorial Zariski decomposition past
t0, i.e. the second extremal ray of the Kawamata blowup Y, which is pure
hidden geometry (lines through the singular point, flops). Hence no robust
valuative conclusion is available pre-geometry. Recorded as BLOCKED signal.
"""
import json
import numpy as np

# Part 1: degree calibration (Reid orbifold RR; model-free)
g = 8
h0 = g + 2
basket_corr = 2 * (1 * (2 - 1) / 2)
deg = 2 * g - 2 + basket_corr
A_E = (1 + 1 + 1) / 2 - 1
print(f"h0(-K) = {h0}, (-K)^3 = {deg}, A(E) = {A_E}")
assert h0 == 10 and abs(deg - 15.0) < 1e-9 and abs(A_E - 0.5) < 1e-9

# Part 2: nef-only volume vol(t) = deg - c*t^3 on [0, t0]; S_nef = integral/deg.
# t0 ranges over plausible nef thresholds; c over convention uncertainty.
def S_nef(c, t0, deg=15.0):
    return (deg * t0 - c * t0 ** 4 / 4) / deg

rows = []
for c in [2.0, 4.0, 8.0]:
    for t0 in [0.3, 0.5, 0.8, 1.0, 1.2, 1.55]:
        S = S_nef(c, t0)
        rows.append({"c": c, "t0": t0, "S_nef": round(S, 4),
                     "beta_nef": round(A_E - S, 4)})
S_vals = [r["S_nef"] for r in rows]
print(f"nef-only S(E) ranges over [{min(S_vals):.3f}, {max(S_vals):.3f}] "
      f"across plausible (c, t0); A(E) = {A_E}")
for r in rows:
    print(r)
spread = max(S_vals) - min(S_vals)
print(f"spread = {spread:.3f} (> 2*A(E) = {2*A_E}); "
      "true S needs Zariski decomposition past t0 (second ray: UNKNOWN)")

with open("sensitivity_table.json", "w") as f:
    json.dump({"degree": deg, "A_E": A_E, "S_spread": round(spread, 4),
               "rows": rows,
               "verdict": "S(E) estimate swings by more than 2*A(E) across "
                          "plausible hidden-geometry inputs; true volume "
                          "function needs Mori cone of Kawamata blowup: BLOCKED"},
              f, indent=2)
print("VERDICT: valuative sign underdetermined pre-geometry -> target blocked.")
