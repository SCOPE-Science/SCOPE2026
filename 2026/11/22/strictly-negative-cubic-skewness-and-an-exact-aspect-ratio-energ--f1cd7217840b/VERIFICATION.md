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

# Reproduction and limits

Execute `python3 verify.py` from the directory containing `RESULT.md`. The test uses standard-library Gaussian directions normalized to a Haar-uniform unit vector. Five positive boxes, including a cube, are checked against two algebraically distinct formulas for the population cubic central moment, and their first three raw moments are compared to 300,000 simulated directions each. A separately implemented planar convex-hull algorithm computes areas of 360 projected eight-vertex boxes and checks the brightness formula. The saved program completed with `BOX_SHADOW_CUBIC_SKEWNESS_CHECKS_OK` and `BOX_SHADOW_HULL_GEOMETRY_CHECKS_OK`; the maximum normalized diagnostic raw-moment discrepancy was below 0.003.

The proof itself is symbolic: the exact Dirichlet sphere-moment formula, central-moment algebra, and a sum of nonnegative aspect-ratio squares. Random tests do not establish universal statements or publication priority. The older cuboid distribution exists, and no independent mathematical audit is asserted.
