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

# Reproducibility

Run `python3 verify.py` using Python 3 standard library only. The program exhausts nine unequal boards with small sides, compares every directly enumerated covariance entry with the moment identity, verifies four mode eigenvectors with exact fractions, and performs 1,596 additional rational spectral profiles. It also checks the generalized Laguerre polynomial coefficient identity and illustrates the fixed-short-side asymptotics at a large value of the long side. Expected output begins `RECTANGULAR_MATCHING_INERTIA_CHECKS_PASSED`.

These are finite tests only. The infinite spectral inequality uses simple positive zeros of generalized Laguerre polynomials; they are not certified by the checker. The infinite asymptotic is proved by bounded ratios of top matching-size weights, not by numerical extrapolation.

The only relevant probability measure is uniform over all distinct partial permutation vertices; the Frobenius metric on matrix coordinates is unscaled.
