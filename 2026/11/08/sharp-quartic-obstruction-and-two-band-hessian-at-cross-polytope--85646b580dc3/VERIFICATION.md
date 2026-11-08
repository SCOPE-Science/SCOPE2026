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

# Reproduction and limits

The self-contained `checker.py` is bundled beside the written result. It uses standard Python, NumPy and SymPy. Running `python3 checker.py` returned `CROSSPOLYTOPE_EXACT_CHECKS_PASS 1110` on the packaged source after extraction. The reported checks construct the Hessian from the moment Jacobians, compare eigenvalues numerically against explicit integer formulas for dimensions 3 through 10, verify ranks exactly for dimensions 3 through 6, test rational second-jet elimination in dimensions 3 through 8, verify the explicit squared-flow imbalance and symbolically verify the exact three-dimensional quartic curve. These finite checks cannot establish a theorem for all dimensions; the written algebraic argument does.

The analytical verification uses only unit-vector Taylor expansions through second order, orthogonal splitting of tangent vectors, symmetric matrix coordinates, and the exact normalized analytic paths stated in the proof. Every equality of limiting fourth-order coefficients is established by direct cancellation of residual jets. The stated absence of a complete integration classification is deliberate. Verification is a self-review, not independent certification.
