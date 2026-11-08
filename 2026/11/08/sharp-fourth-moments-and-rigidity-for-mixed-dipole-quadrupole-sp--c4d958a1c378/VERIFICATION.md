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

The self-contained standard-library checker `verify_mixed_sphere.py` was run with `python3 verify_mixed_sphere.py`. Its exact rational spherical-monomial integrations agreed with the invariant fourth-moment formula for 150 deterministic rational coefficient configurations. It checked both rational endpoint values and independent direct grid integrations of the two equality witnesses.

The universal identities and inequalities are established by the analytic Gaussian–spherical moment calculation and the two explicit sum-of-squares deficit expressions in RESULT.md. Sampling is not claimed as an exhaustive proof. The code uses only the Python standard library and requires no input data or external files.

Independent mathematical audit: not performed. The scientific limitations are recorded in RESULT.md and REVIEW.md.
