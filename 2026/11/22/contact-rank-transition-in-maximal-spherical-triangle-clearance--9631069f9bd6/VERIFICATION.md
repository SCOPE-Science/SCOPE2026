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

# Verification notes
The proof's analytic ingredients are the convex-projection maximum identity, the exact Gram inequality, spherical normal-coordinate expansions, bounded convergence in the rescaled tangent domains, and explicit Euclidean areas of the triangular and parabolic limits. Run `python verify.py` with Python 3, numpy, scipy and mpmath. Its three normal triples cover strict-three, critical two-positive/three-tight, and strict-two cases. Its check compares finite-deficit spherical area computations with the claimed leading coefficients; convergence is slow at the critical case and is not used as a proof. This is self-review only; no independent audit was performed.
