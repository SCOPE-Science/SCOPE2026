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

The analytic argument proves the exact inequality and the complete equality cases for every nondegenerate trirectangular tetrahedron, not just those with rational legs or sampled directions.

Run `python verify.py` with `numpy`, `scipy`, `sympy`, and `mpmath`. The verifier recomputes the exact degree-nine Sturm variations (5 at \(1/3\), 4 at \(1\)), the rational strict boundary comparison, and the numerical root of the scalar stationarity equation. A seeded simulation checks 130,000 positive triples against the claimed sharp inequality and calculates convex-hull shadow counts for 54,000 independent random orientations.

Actual execution:

`VERIFY_OK sturm=(5,4) sharp_constant= 0.586187019691207749 optimizer= 0.784991151151295253 random_simplex_tests= 130000 geometric_projection_trials= 54000 max_projection_error= 0.002235`

Finite tests are cross-checks only; the universal inequality and uniqueness are established by differentiation, compactness, exact rational comparisons and Sturm's theorem. Computed decimal values are not claimed as independently certified numerical intervals. The mathematical priority assessment is provisional. Independent audit has not been performed.
