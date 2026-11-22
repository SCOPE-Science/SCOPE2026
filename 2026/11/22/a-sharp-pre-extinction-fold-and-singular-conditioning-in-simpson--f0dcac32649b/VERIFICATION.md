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

The exact claims rely on the algebraic quadratic reduction, positivity criterion, strict monotonicity, Simpson fourth-derivative sign, and factorization of the scalar residual. Numerical checks are auxiliary. Running `python3 checker.py` in the extracted package requires only the Python standard library and checks representative pre-fold and post-fold values, root normalization, the physical branch's sign bias, the critical constant, the Jacobian identity, and the sphere energy identity.

The decimal root and asymptotic coefficients are reproducible from the implicit equation and its derivative. The numbers are high-precision evaluations rather than a formally certified interval-arithmetic enclosure. The result does not certify the fully coupled geometric BDF solver, predictor accuracy, spatial errors, general non-circular curves, or finite precision Newton convergence. No independent audit is asserted.
