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

The standalone `check_fractional_multipartite.py` script (Python 3 with NumPy and SciPy) tests the finite identities independently: numerical halfspace intersection on small graph instances produces all relaxation vertices, direct coordinate-space quadratic optimization checks the predicted Hausdorff projection, and exact rational arithmetic checks the threshold, three-class formula, four-class transition, and finite majorization extrema.

Observed run: `MULTIPARTITE_HAUSDORFF_PASS numerical_projections=17 independent_halfspace_vertices=230 exact_majorization_profiles=274`.

The abstract proof, not any finite test, supplies the all-order result. Finite floating-point optimization has tolerance and is not exhaustive in graph order. The normal cone / priority questions were not independently audited. Independent audit remains not performed.
