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

Execute `python3 verify_prism_brightness.py` with Python 3 and no third-party packages. The script directly projects all vertices of several unrelated right polygonal prisms and independently computes the planar convex hull and its area. It compares these against the analytic shadow-area identity at 57,600 seeded random viewing directions, and it compares measured moments with the formula using numerical angular integration of the planar widths. It checks multiple heights, the universal optimizer, and the distinct equilateral optimizers. The actual completed run printed `ALL_CONVEX_POLYGON_PRISM_SHADOW_CHECKS_PASSED` and `TRIANGLE_TWO_DISTINCT_OPTIMAL_HEIGHTS_PASSED`.

The complete proof covers all compact convex planar bases; finite numerical experiments do not verify uncountably many bodies or all view directions. The mathematical proof uses a direct area identity, exact one-dimensional spherical integrals, a differentiable rational optimization, and equality in Jensen's inequality. No independent audit has been performed.
