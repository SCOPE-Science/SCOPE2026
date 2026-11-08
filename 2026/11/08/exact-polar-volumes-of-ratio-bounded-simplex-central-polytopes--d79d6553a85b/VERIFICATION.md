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

# Reproducibility and verification

The closed polar-volume theorem follows from the vertex characterization, explicit polar inequalities, facet product structure, and pyramid decomposition in `RESULT.md`. The beta-integral argument separately provides the primal volume, and symmetry determines the Santaló center.

Run `OPENBLAS_NUM_THREADS=1 python verify_polar_volume.py` under Python 3.10+ with NumPy and SciPy installed. The program performed 177,492 standard-library exact-rational support and identity assertions and 18 independent SciPy convex-hull volume comparisons. Checked dimensions were \(2\le m\le8\) for support certificates, \(2\le m\le15\) for the \(c=2\) primal identity, and \(2\le m\le7\) for geometric hull volumes. The latter test uses \(c\in\{3/2,2,3\}\).

These finite experiments do not establish the all-dimensional theorem or historical priority. The mathematical proof does not require floating-point convex hulls. Independent audit has not been performed.
