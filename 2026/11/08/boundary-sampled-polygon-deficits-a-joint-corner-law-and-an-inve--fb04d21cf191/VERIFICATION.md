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
# Verification record

The accompanying `check_corner_law.py` is executable with Python's standard library. It builds actual convex hulls from uniformly sampled polygonal boundaries and compares the missing area and missing perimeter to the two exact geometric corner formulas. The finite-sample integral for the expected area deficit is separately checked, and simulated limiting exponential-product samples are compared to the analytical first two moments for three convex polygons. It checks the angular Jensen inequality and the triangle sine correspondence.

Observed output: `BOUNDARY_POLYGON_CORNER_LAW_CHECKS_PASSED`. The sampling studies are diagnostic only and do not establish the limiting statements. The analytical proof rests on disjoint boundary-strip survival probabilities, uniform exponential tails, direct integral evaluation, and a gamma-product tail sandwich. No independent audit or external certification has occurred.
