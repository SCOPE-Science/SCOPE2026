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
# Verification of the orthotope small-section theorem

The proof in `RESULT.md` is analytic and applies to all integers \(d\ge2\) and every fixed positive side vector. The following reproducible computational checks are **supplementary** and do not prove any all-dimensional statement.

Use Python 3 with NumPy, SciPy and mpmath installed, and execute `python verify.py` in the directory containing the script. It evaluates the explicit gamma formula in dimensions 2–8, the exact planar value, and the scale law under unequal side lengths; computes three-dimensional box-slice areas from an inclusion–exclusion formula; integrates by deterministic spherical Sobol quadrature with bisection for three small-area thresholds; and tests two weighted normal-coordinate moments against their Dirichlet targets for dimensions three and four. The Sobol seed and 43 bisection iterations are explicit in the source. All implemented assertions passed in the recorded execution, printing `PASS; exact gamma identities, box-spline tests, weighted angular moments`.

The separate box-spline computation avoids using the asymptotic simplex formula to compute its numerical section-area inputs. Numerical tolerance does not certify the limiting order or uniqueness for all shapes. The proof's crucial uniform domination, beta integrals and conditional weak convergence must be assessed from the written argument. Independent external mathematical audit has not been performed.
