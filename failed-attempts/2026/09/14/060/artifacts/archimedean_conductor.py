"""CONDITIONAL exponent bookkeeping + conductor/AFE checks (honest version).

Nothing here proves an off-diagonal bound. It only records:
 (a) conductor exponent 4 -> AFE length exponent 2 (verified from gamma shifts);
 (b) IF off-diagonal OD <= T^A Δ^{-B} + T^C (all +eps), THEN the Delta-threshold
     exponent needed for OD <= ΔT is max((A-1)/(1+B), C-1). For the TARGETED
     shape (A,B,C)=(6/5,3/2-? ...) this gives 1/5 — but (A,B,C) are TARGETS
     of the analysis, NOT established facts.
Run: python3 archimedean_conductor.py
"""

def threshold(A, B, C):
    from fractions import Fraction
    t1 = (A - 1) / (1 + B)
    t2 = (C - 1)
    return t1, t2, max(t1, t2)

# (a) conductor: 6 gamma shifts for sym^2(u)xphi at s=1/2:
# sym^2 params {2it,0,-2it} + phi params {+s0,-s0} (s0 fixed) give shifts:
# +/-2it +/- s0 (4 shifts, each ~2T) and +/-s0 (2 shifts, O(1)).
# Q = prod (1+|shift|) ~ T^4. AFE length Q^{1/2} ~ T^2.
print("conductor exponent: 4 (4 large shifts x T^1 each); AFE length exponent: 2")

# Hecke index: AFE n <= T^2, lambda(n^2)-type coeffs -> Kuznetsov index m <= T^4.
print("Kuznetsov index exponent after Hecke: 4")

# (b) conditional thresholds for candidate shapes (LABELS, not claims):
for label, (A, B, C) in {
    "candidate-shape-1": (6/5, 3/2, 6/5),
    "candidate-shape-2": (5/4, 1/4, 6/5),
}.items():
    t1, t2, t = threshold(A, B, C)
    print(f"{label}: A={A} B={B} C={C} -> need d >= max({t1:.4f},{t2:.4f}) = {t:.4f}")

# check: d=1/5 suffices under candidate-shape-1
A, B, C, d = 6/5, 3/2, 6/5, 1/5
assert A - B*d <= d + 1 + 1e-12 and C <= d + 1 + 1e-12
print("CONDITIONAL check passed: under candidate shape, d>=1/5 suffices. QED-conditional.")
print("NOTE: proving the candidate shape is the remaining open core of the target.")
