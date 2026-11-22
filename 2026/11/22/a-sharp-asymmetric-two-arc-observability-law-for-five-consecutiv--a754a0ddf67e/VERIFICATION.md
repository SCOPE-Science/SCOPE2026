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

# Reproducibility and scientific limits

Run `python checks/verify_five_mode.py` after installing the two packages in `requirements.txt`. The direct high-precision Fourier Gram integration is compared against independent quadrature of each of the twenty-five entries. Symbolic operations check the antipodal polynomial, coefficient norm, derivative-sign factorization, and exact Legendre residual norm. Multiple small-aperture designs demonstrate the direction of the spectral gain and its approach to the sharp coefficient. The successfully executed checker prints `TWO_ARC_FIVE_MODE_CHECKS_PASS 55`.

The universal result is proved by analytic Hermite interpolation, Legendre orthogonal projection, the colliding-center trial bound, and compactness of normalized polynomial coefficients. Numerical testing confirms examples and normalization but cannot prove the universal limit or originality. No independent audit has been performed.
