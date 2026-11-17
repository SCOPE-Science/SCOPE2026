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

The analytic identities are proved in RESULT.md. The supplemental standard-library program `verify.py` was executed for positive parameters satisfying the focus inequality, including points close to the large-area edge, and returned `CROSSING_AREA_AND_PERIOD_EDGE_CHECK_OK`.

The program compares the Green-integral quadrature, the velocity-energy expression, the explicit hyperbolic formula, and the sharp asymptotic constant. Its finite checks do not certify the infinite-domain, uniqueness, or limiting statements; those follow from the analytic argument. The nontransverse switching point is excluded. No independent external validation has been performed.
