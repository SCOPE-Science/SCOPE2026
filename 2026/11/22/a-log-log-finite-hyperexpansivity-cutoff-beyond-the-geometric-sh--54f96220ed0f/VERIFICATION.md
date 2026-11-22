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

Run `python3 check.py` beside this document. The checker uses standard-library exact `Fraction` arithmetic for coefficient recurrences and initial weight-product moments, then compares independently evaluated finite differences with the sign of a truncated convergent charge series in concrete rational instances. It also reports finite-order thresholds at five successively smaller distances to the boundary.

The checker uses a convergent numerical series truncated when coefficients become negligible in the test examples. It does **not** certify all infinite orders, any arbitrary parameters, or the asymptotic remainder. These follow from the analytic product recurrence, strict coefficient signs, global tail dominance, uniform geometric-product bounds and the two-sided saddle estimate in `RESULT.md`.

Self-review: passed. Independent audit: not yet performed.
