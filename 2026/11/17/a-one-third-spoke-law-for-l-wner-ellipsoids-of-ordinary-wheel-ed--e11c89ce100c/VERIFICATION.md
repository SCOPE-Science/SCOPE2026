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
# Reproducible calculations

Execute `python3 wheel_unsigned_ellipsoid_verify.py` with the standard Python 3 library. The program constructs all \(2m\) incidence-vector vertices of the wheel, computes the orbit-weighted mean and covariance directly, and solves the covariance linear systems in the intrinsic sum-zero subspace. It checks the derived Mahalanobis contacts and the Fourier eigenvalues through rim order 24, the two exact orbit-contact equations through order 99, the exact small-order weights, and asymptotic samples through order 2000.

Observed final output begins `WHEEL_UNSIGNED_LOEWNER_PASS matrix_orders=3..24 orbit_checks=3..99`, and its largest finite matrix-contact residual was approximately \(2.13\cdot10^{-14}\). The checker uses floating-point arithmetic, with numerical tolerances explicitly present in the file; it is not an exact proof of the infinite theorem. The analytical proof in RESULT.md supplies the determinant maximization, exact all-vertex contacts, global ellipsoid inequality and asymptotic coefficient. Independent audit: not performed.
