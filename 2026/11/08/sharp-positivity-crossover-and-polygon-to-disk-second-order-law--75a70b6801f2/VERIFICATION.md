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

The standard-library checker `check_polygon.py` was executed directly and certified the strict cap-integral comparison against one half for each regular polygon with three through eleven sides, using rational intervals rather than floating-point sampling. It also certified a rational upper bound below one half for the unit-disk comparison at eleven sides; monotonicity extends this bound to all larger polygons. The full infinite-dimensional-index theorem additionally relies on the proved kernel reduction, radial expansion, and exact analytical integrals in `RESULT.md`. Neither finite checking nor an independent external audit is claimed to establish those analytic arguments.
