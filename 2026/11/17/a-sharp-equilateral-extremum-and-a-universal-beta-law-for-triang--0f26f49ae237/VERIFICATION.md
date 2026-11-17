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

# Mathematical verification

The primary exact argument is in `RESULT.md`. It identifies the translation fibers, the stochastic trace inequalities, the equality configurations, and the gauge-integral identity without reliance on floating-point computation.

The bundled script `verify.py` uses `numpy` and `scipy`, independently constructs the nine linear inequalities for the inclusion of one triangle in itself, and obtains the four-dimensional polytope volume using `HalfspaceIntersection` and `ConvexHull`. A second path computes the projection footprint, its support-gauge integral, and the predicted volume. Five specified triangles and 120 deterministic pseudorandom triangles were tested. There were 382 passed assertions, with no failures. The script checks the sharp equilateral value and several moments of the \(\operatorname{Beta}(2,3)\) distribution.

Numerical tolerances are stated in the script. The numerical evidence does not certify the unrestricted theorem, does not establish historical priority, and is not an independent mathematical audit. The exact proof applies to all nondegenerate real triangles.
