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

# Reproducibility

Run `python artifacts/verify.py` using Python 3 with no third-party packages. The exact-rational test script prints `PASS 375 exact-rational assertions`. It checks independent piecewise integration of jump-phase risks, nested covariance identities, Romberg interpolation conditions, and finite-depth sign/strictness tests.

The analytic proof in RESULT.md, not these bounded tests, establishes every positive integer refinement factor and unbounded extrapolation depth. The stated infinite-limit decimal was computed from the convergent expression; it is not independently certified. Independent scientific audit has not been performed.
