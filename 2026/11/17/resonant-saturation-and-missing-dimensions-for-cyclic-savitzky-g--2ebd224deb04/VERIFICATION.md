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

# Reproducibility and proof boundaries

Execute `python3 verify.py` with the standard Python library. The script reconstructs the quadratic center weights as integers, verifies their exact normalizations and quadratic reproduction, computes sharp two-column variation coefficients and binary-block equality witnesses, and checks the saturation criterion with exact rational arithmetic.

Its exhaustive exact-coefficient cases cover every radius from 2 through 20 and cycle lengths across both saturation boundaries. For radii 21 through 120, an independent support-disjointness implementation tests the integer-length classification, including the zero-coefficient radius 86. It checks the five-tap values and the thirteen-tap zero case. Successful completion prints `ALL_CYCLIC_SG_BV_EXACT_CHECKS_PASS`.

These finite calculations do not establish an assertion for infinitely many radii and lengths. The unrestricted theorem is proved by the support geometry and interval-sum argument in `RESULT.md`, while the asymptotic conclusions follow from explicit sign thresholds and a Riemann-sum calculation. No independent audit or external mathematical validation has occurred.
