"""Verify the two structural obstructions to the stated P^1 family.

Obstruction A (filtration axiom): Fil^{i+1} must be contained in Fil^i.
For lines in a 2-plane this forces equality; the stated pairs of lines
are distinct, hence not nested.

Obstruction B (weak admissibility): phi-stable line span(e1) has
t_N = 2 < t_H = 2 + 2 = 4.
"""
import itertools

P = 11

# --- Obstruction A: line distinctness via 2x2 determinants ---
# Work over F_11 (3 != 0 mod 11 implies 3 != 0 in Qbar_11 by residue).
def det2(a1, a2, b1, b2):
    return (a1 * b2 - a2 * b1) % P

# sigma_1 pair: e1=(1,0), e1+3e2=(1,3)
d1 = det2(1, 0, 1, 3)
print(f"det[e1, e1+3e2] mod 11 = {d1} (nonzero => distinct lines)")
assert d1 == 3 and d1 != 0

# sigma_0 generic pair: e1=(1,0), e1+t e2=(1,t) for t in F_11
bad = []
for t in range(P):
    d = det2(1, 0, 1, t)
    if d == 0:
        bad.append(t)
print(f"t in F_11 with span(e1)==span(e1+t e2): {bad} (only t=0)")
assert bad == [0]

# t = infinity: span(e2)=(0,1) vs span(e1)=(1,0)
dinf = det2(1, 0, 0, 1)
print(f"det[e1, e2] mod 11 = {dinf} (nonzero => distinct)")
assert dinf != 0

# Lift to Qbar_11: equality of lines e1 ~ e1+3e2 would imply 3=0 in residue,
# impossible since 3 is a unit (|3|_11 = 1). Determinant 3 is a unit.
print("3 mod 11 =", 3 % P, "=> 3 is a unit in Z_11, so lines stay distinct over Qbar_11.")

# --- Obstruction B: Newton vs Hodge numbers ---
# phi = diag(11^2 zeta1, 11^2 zeta2), zeta_i Teichmuller (valuation 0).
v_p_eig1 = 2
v_p_eig2 = 2
tN_D = v_p_eig1 + v_p_eig2
# Labelled weights claimed {0,2}+{0,2}; whole-module Hodge number:
tH_D = (0 + 2) + (0 + 2)
print(f"t_N(D) = {tN_D}, t_H(D) = {tH_D} (numerically equal, so whole-module test passes)")
assert tN_D == tH_D == 4

# Subobject D' = span(e1), phi-stable, rank 1 over K0.
tN_Dprime = v_p_eig1
# e1 lies in Fil^2 at both embeddings (Fil^2_0 = Fil^2_1 = span(e1)),
# so Hodge contribution 2 per embedding:
tH_Dprime = 2 + 2
print(f"t_N(span e1) = {tN_Dprime}, t_H(span e1) = {tH_Dprime} => violates t_H <= t_N: {tH_Dprime > tN_Dprime}")
assert tH_Dprime > tN_Dprime

print("RESULT: no t gives a valid filtration; and span(e1) violates weak admissibility at every t.")
