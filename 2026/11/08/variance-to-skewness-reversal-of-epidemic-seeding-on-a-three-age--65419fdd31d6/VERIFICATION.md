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

# Reproducibility and verification

Run `python3 verify.py` (Python 3.10+, Python standard library only). The verifier checks the full multivariate polynomial mean recurrence, all three pair-difference identities and Jacobians, all exact diagonal equilibria for three rational recovery rates, two nonzero quadratic curvature certificates, and the exact cubic curvature cancellation coefficient. It additionally runs four finite original-map trajectory diagnostics. Expected exit output:

`VERIFY_OK 72 exact identities/certificates and finite trajectory diagnostics`

The polynomial coefficients are checked over exact rational arithmetic, not tolerance-based floating point. The four numerical diagnostics are a stress test only; no finite iteration count proves an infinite-time limit or an all-small-parameter theorem. The proof in RESULT.md uses the positive difference multiplier, monotone scalar recursion, smooth stable-manifold invariance, and ordering to establish its unlimited-time conclusions. Public-source comparison and publication-priority risks are recorded separately in REVIEW.md and AUDIT.json.
