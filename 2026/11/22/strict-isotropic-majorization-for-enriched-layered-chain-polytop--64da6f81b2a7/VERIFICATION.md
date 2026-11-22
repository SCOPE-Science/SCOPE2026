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

The mathematical proof is self-contained: it derives the radial Dirichlet law and exact covariance, proves strict positivity of every discrete second difference of the isotropic potential using explicit elementary logarithmic inequalities, then applies finite majorization transfers. No computational extrapolation is used to prove the universal claim.

The standalone `verification/verify.py` uses Python standard-library exact fractions and integer arithmetic, plus NumPy and SciPy for convex-hull candidate identification. It checks 798 discrete convexity inequalities, all 31,161 relevant ordered positive layer-size compositions through total size 18, and 11 low-dimensional hull-triangulation cases with exact rational volumes and second moments. The hull identification uses floating-point geometry, but the determinant and moment comparison is exact after identification.

The remaining limitation is historical: known Hanner covariance recursions cover the numerical formula, while this theorem's strict fixed-layer majorization assertion is not identified in the sources inspected. The absence of a retrieved equivalent is not proof of novelty. Independent mathematical audit: not performed.
