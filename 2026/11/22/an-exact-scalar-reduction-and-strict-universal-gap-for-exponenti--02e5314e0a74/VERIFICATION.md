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
The analytic proof in `RESULT.md` is the basis for the global statement. Reproduce the standalone supplementary check by running `python3 check.py` with Python 3 and the standard library. It checks the explicit smooth-branch input-output Jacobian against an independent matrix-inverse differentiation at 350 deterministic test points; it verifies the two row-norm formulas, a strict analytical lower-value benchmark numerically, and reports a noncertifying scalar grid survey.

The universal strict upper bound is proved through equality conditions of rank-one Euclidean projections and the limits of the two scalar functions, not through a mesh or finite computation. The exact scalar maximizers, which scalar branch dominates, and independently reviewed literature priority are not determined. Any numerical digits reported for unrestricted scalar optimization are exploratory and not part of the mathematical assertion.
