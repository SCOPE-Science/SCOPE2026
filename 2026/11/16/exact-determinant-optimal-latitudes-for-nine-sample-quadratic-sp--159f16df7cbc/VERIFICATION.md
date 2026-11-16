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

# Verification record

The normalized harmonic collocation determinant was evaluated independently using an explicit Python 3 standard-library implementation with partial-pivot Gaussian elimination. The accompanying `check.py` passed 83 supplementary comparison tests across both ordering chambers, rotated regular polygons, and the two analytic critical points. Direct determinant squares agreed with the exact factorization to the displayed tolerance; the critical stationarity equations and reference gain were checked. These finite checks are corroboration, not an exhaustive proof of the continuum of heights.

The universal result is proved by the Fourier-block determinant reduction, strict concavity on both chambers, polynomial elimination of the stationary system, and an exact rational comparison of the resulting maxima. A distinct research priority risk is an unindexed older equivalent determinant optimization; no independent mathematical verification is claimed.
