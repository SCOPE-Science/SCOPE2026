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

The analytic proof of global strict concavity uses a positive cubic-division remainder, and the endpoint coefficients follow from exact rational expansions. Independently, `python3 verification/check_inverse.py` passed 485 exact-rational parameter cases, checking determinant substitution, positivity, two algebraically different curvature formulas, and limiting constants. The check is finite and supplements rather than replaces the universally quantified proof. It uses only Python's standard library and no external packages.

All numerical examples concern the parameters of the specified two-state stationary-tail model. No measurement-noise or finite-sample identification theorem is asserted. Independent mathematical audit has not been performed.
