"""Orientation audit (stdlib only). Run: python3 output/artifacts/refute_fallback.py

RESULT: the earlier 'refutation' targeted the WRONG fibration and is WITHDRAWN.

Anderson setup: Phi(x;y), |x|=2 object (Jacobian point), |y|=modulus (parameter).
Fallback clause (i) counts types S^Phi(B) over n MODULI. The C(n,5)/C(n,7) count
realizes types over n POINTS by moduli = PRIMAL direction (density of Phi^* with
5-/7-dim object). By Anderson Prop 8 that lower-bounds distal density of the DUAL
family (>= 5), not of Psi_2 itself. It does not refute clause (i).

Sanity for the correct orientation: two distinct monic quintics differ in degree
<= 5, so share <= 5 x-values (<= 10 affine points); pair-meeting patterns over n
moduli are ~C(n,2) = Theta(n^2), consistent with (not fatal to) the fallback.
KST: the incidence graph is K_{2,11}-free, so Theta(n^2) EDGES would be impossible;
clause (ii) 'intersections' must mean realized patterns, which pair-meetings supply.
No falsity of the fallback is established by this artifact.
"""
from math import comb
for n in (10, 20):
    print(f"n={n}: C(n,2)={comb(n,2)} pair-patterns; C(n,5)={comb(n,5)} is the DUAL count (irrelevant to clause i)")
print("ORIENTATION_AUDIT_OK: prior refutation withdrawn; fallback unrefuted by this route")
