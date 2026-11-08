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

# Reproducibility and analytical boundaries

Run `python bipyramid_santalo_check.py` with Python 3 and the packages SymPy, NumPy, and SciPy. It was run successfully using the packaged code and printed:

`ASYMMETRIC_BIPYRAMID_CHECKS_PASSED 18 18 128 8 25 9`

The six numbers count exact-fraction polar-volume expansions, symbolic derivative/limit identities, exact-rational centroid and midpoint sign comparisons, symbolic quadratic expansion checks, numerical optimizer comparisons, and convex-hull/polar-volume comparisons, respectively.

The proof of the all-dimensional statements is in RESULT.md. No finite range of dimensions or optimizer sampling can establish universal uniqueness, strict inequalities, or exact asymptotic coefficients. The relevant independent analytical steps are the polar section calculation, the positive derivative of the centroid comparison function, the opposite sign at the apex midpoint, envelope differentiation, and the second-order Taylor calculation. The code supplies reproducible regression checks of these steps; independent mathematical validation has not been performed.
