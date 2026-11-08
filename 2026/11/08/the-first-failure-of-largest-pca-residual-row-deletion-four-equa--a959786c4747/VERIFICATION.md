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

# Verification

Execute `python verify.py` with Python 3, SymPy, and NumPy. The checker verifies the displayed rational witness row norms, Gram matrix and characteristic polynomials, isolates the leading eigenvalue, checks exact adjugate comparisons, and certifies a strictly better refitted deletion. It symbolically reconstructs the equal-diagonal three-by-three cofactor identities. Its deterministic numerical cross-check comprises 2,625 examples of the planar and three-row cases, plus a floating-point rendering of the rational witness.

The finite tests are supplemental, not a proof of the infinitely many cases. The universal planar and three-row assertions follow from the doubled-angle identity and the three-by-three eigenprojector formula proved in `RESULT.md`. The counterexample uses exact rational identities and a strict interval inequality; it does not depend on floating-point rounding. Proof completeness, priority against unindexed literature, and application to more general algorithms have not been independently audited.
