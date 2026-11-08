---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

The Weierstrass discriminant \(\Delta=-(t^3+27)\) follows by substituting \(a_1=t\), \(a_3=-1\), and all remaining Weierstrass coefficients zero into the standard discriminant formula. The order-three point \((0,0)\) has triple tangent intersection \(y=0\). In the smooth model, adjunction and the height formula identify exactly twelve negative curves.

The independent finite tests in `verify_chambers.py` construct the complete twelve-curve integral intersection matrix and exhaustively check each of its \(4096\) principal subsets. One test uses exact Schur complements in `fractions.Fraction`; the other checks avoidance of the ten explicitly constructed minimal singular subgraphs. The two agree on every subset. A third check independently recomputes the inclusion-minimal excluded supports and verifies that there are exactly ten. Their ranks and polynomial counts reproduce the included `verification_output.txt` verbatim.

The finite verifier cannot establish the geometric claim that these are all negative irreducible curves; that is proved separately using the fiber geometry, adjunction and section group. The rank and graph premises are independent of floating-point arithmetic. No formal proof-assistant certification or external independent audit was performed.
