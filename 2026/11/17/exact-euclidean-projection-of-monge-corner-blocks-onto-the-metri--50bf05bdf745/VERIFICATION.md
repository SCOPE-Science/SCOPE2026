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

# Reproducible verification and limits

Run `python3 check_projection.py` from the same extracted directory. The script relies only on the Python standard library and uses exact rational arithmetic. On the saved version it printed:

`MONGE_METRIC_FACE_PROJECTION_PASS exact_cases=15179 matrix_checks=1438 n=3..45`

The checks compute independent full symmetric matrix entries in the smaller cases and compare their Frobenius inner products with the closed Gram formulas. Across all checked corner sizes, the explicit two-cut convex coefficients sum to one, all active-cut gradients agree, all other cut gradients are no lower, the squared nearest-point distance agrees with the theorem, and the designated corner block is the unique vertex of maximum distance.

This is a finite exact-arithmetic test, not an infinite-dimensional or all-parameter certificate. The proof in `RESULT.md` establishes the formulas for every integer \(n\ge3\). The claims do not include arbitrary Monge-matrix projection, independently audited originality, or attainment by a genuine metric when a projection lies on the boundary of the metric face.
