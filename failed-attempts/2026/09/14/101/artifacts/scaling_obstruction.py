"""Quantify the three scaling obstructions for bounded-Gamma ancient Liouville without periodicity.

Route A (Harnack/oscillation decay): Harnack constant for -dT + b.grad with |b|<=M0
on Q_R scales like exp(C*R*M0). No uniform-in-R decay => ancient Liouville open.
Route B (energy/Caccioppoli): cutoff remainder on B_R scales like volume*|grad phi|
~ R^3/R = R^2 -> infinity for L^\infty data; no global gradient vanishing.
Route C (axis singularity): |Gamma| <= C2 r^2 near axis (smoothness) forces any
sup-maximizing sequence with M>0 to stay at r_k >= sqrt(M/(2*C2)) or escape to
r_k -> infinity; the r_k->infinity limit is self-consistent (constant-Gamma
drift-diffusion limit with vanishing swirl), so no contradiction without
periodicity/decay.
"""
import math, json

M0 = 1.0   # sup|b| bound (representative)
C = 1.0
print("R | Harnack factor exp(C*R*M0) | energy remainder ~R^2")
for R in [1, 2, 5, 10, 20, 50]:
    print(f"{R:4d} | {math.exp(C*R*M0):.3e} | {R**2}")

# Axis smallness: |Gamma| <= C2 r^2; given M>0, maximizing seq needs r_k >= sqrt(M/(2C2))
C2 = 2.0
for M in [0.1, 0.5, 1.0]:
    print(f"M={M}: r_k lower bound sqrt(M/2C2) = {math.sqrt(M/(2*C2)):.4f} (or r_k -> inf)")

# Singular drift magnitude 2/r at sample radii
print("r | 2/r")
for r in [1.0, 0.1, 0.01, 0.001]:
    print(f"{r}: {2.0/r}")

summary = {
    "M0": M0,
    "harnack_growth": "exp(C*R*M0), non-uniform as R->inf",
    "energy_remainder": "O(R^2) diverges for L_inf data",
    "axis_conclusion": "r_k->infinity case self-consistent; periodicity needed to compactify",
}
with open("obstruction_summary.json", "w") as f:
    json.dump(summary, f, indent=2)
print("wrote obstruction_summary.json")
