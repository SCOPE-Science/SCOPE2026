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

The proof uses the scalar Schwarz–Pick lemma, the exact numerical-radius formula for two-by-two off-diagonal matrices, and an explicit rational interpolant with a constant boundary envelope. Reproduce finite numerical diagnostics with `python verify_asymmetric.py` after installing `mpmath`; the checker reports `ASYMMETRIC_NUMERICAL_RADIUS_EXACT_OK 480`. Its finite tests verify selected parameters and boundary points only and do not establish the all-parameter assertion. The analytic argument covers all positive unequal amplitudes and two distinct interior nodes. The equal-strength case is cited only as a known limit. Independent mathematical audit has not been performed.
