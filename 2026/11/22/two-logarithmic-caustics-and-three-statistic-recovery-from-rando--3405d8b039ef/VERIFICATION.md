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

The mathematical proof in RESULT.md is analytic. Recompute the squared visible axes as eigenvalues of the compression of the diagonal form and use the exact joint density and Morse-saddle calculation; the separation of the two candidate higher-caustic coefficients is \(p\sqrt q>1\). The CDF endpoint coefficients are obtained from explicit integrable two-dimensional beta-simplex limits.

Run `python triaxial_shadow_check.py` with Python 3, NumPy and SciPy. The supplied checker passed 990 deterministic tests: 2D projection matrix eigenvalues versus the algebraic secular inversion; joint-law normalization and density quadratures; caustic amplitude estimates for multiple shapes including a coincident-level shape; both endpoint asymptotics; two-branch inverse candidates. Numerical quadrature and finite-precision checks are *diagnostic*, not an independent analytic proof.

Assumptions: one strictly triaxial ellipsoid, Haar-uniform normal directions, exact Euclidean orthographic projections. The exact density has two logarithmic singularity contributions, whose positions may coincide; each asymptotic is pointwise in fixed semiaxes. The method does not establish statistical robustness or recover an absolute scale from dimensionless aspect ratios. Independent mathematical audit has not been performed.
