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

## Reproduction

Run `python3 verify.py` with Python 3. The checker uses only standard-library exact fractions and integer binomial coefficients. It verifies the Gram matrix and its inverse for every integer pair \(2\le m\le16\), \(1\le r\le m\) (135 pairs), evaluates the nonnegative kernel integral independently by polynomial integration, tests the old full-volume endpoint, and checks additional finite ambient-rank monotonicity and limiting diagnostics. The final line is `ALL_SIMPLEX_SKELETON_CHECKS_PASSED`.

## Analytical coverage and limits

All-dimensional validity, precise norming-point classification, strict upper bound, and both limits are proved in `RESULT.md` using the explicit kernel, the beta survival integral, and a derivative identity. The finite checker is not an exhaustive proof of the infinite parameter ranges. No independent audit has been performed.
