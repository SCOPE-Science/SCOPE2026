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

Run `python checker.py` after installing the SciPy dependency. The numerical implementation computes convolution integrals using an independent endpoint-weighted quadrature; it reports sixteen checks against the exact beta-curvature and boundary coefficients, with additional monotonicity, normalization and drift-cancellation checks. Successful finite diagnostics corroborate the formulas but do not prove the continuum-rate theorem. The proof in RESULT.md establishes that theorem. No independent scientific audit or external certification has been performed.
