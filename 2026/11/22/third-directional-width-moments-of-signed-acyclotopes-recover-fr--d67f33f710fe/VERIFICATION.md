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

## Checks performed
The standalone `CHECKER.py` re-evaluates the one-dimensional Gaussian formula, the strict symbolic positivity bound, and a dimension-three signed-triangle example using fixed-seed Sobol Gaussian samples. The exact formula is proved without relying on the numerical comparison. The check does not claim exhaustive validation across arbitrary graph sizes.

## Scientific limits
The moment identity uses ambient spherical directions. The absolute-product formula is sensitive to the sign product of triangles but not the locations of individual frustrated edges. The observed numerical agreement is a reproducibility check, not a substitute for the all-graph argument. Independent validation has not been performed.
