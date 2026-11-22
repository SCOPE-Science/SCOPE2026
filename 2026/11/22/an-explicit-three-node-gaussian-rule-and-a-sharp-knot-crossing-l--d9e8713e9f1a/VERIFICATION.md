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

The symbolic calculations and 100-sample high-precision checks can be rerun with `python verify.py` (requires SymPy). The script checks 1,130 assertions for residual moment identities, quadratic coefficients, endpoint test-polynomial factorizations, symmetric-grid moments, and one-sided derivatives. The mathematical argument in RESULT.md proves sign positivity, uniqueness, and minimality for all real \(0<s<1\); finite checks cannot replace the analytic proof.

The published symmetric-case construction and homotopy continuation framework were inspected for overlap. An unindexed earlier equivalent closed-form quadrature remains possible. Independent mathematical review or external certification has not been performed.
