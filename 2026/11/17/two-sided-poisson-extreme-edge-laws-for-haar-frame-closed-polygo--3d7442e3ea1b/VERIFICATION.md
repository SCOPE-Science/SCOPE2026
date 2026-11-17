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

The derivation relies on the exact Gaussian polar-factor representation of Haar orthonormal two-frames, an exponentially concentrated two-by-two sample covariance matrix, the explicit chi-square (planar) or gamma (spatial) row norm law, and Laplace convergence of two disjoint rare-event bins. These analytic steps prove the distribution limits and mark-process independence. The shared covariance sandwich supplies the finite-\(n\) comparison and is uniform over all edge indices.

`check_extremes.py` (run using `python check_extremes.py`, with NumPy installed) performs numerical checks of exact frame normalization, polygon closure, perimeter two, edge-length formulas, the pathwise row-norm sandwich, independent-reference formulas, and finite-sample frequencies. The expected final marker is `STIEFEL_TWO_SIDED_EXTREMES_CHECKS_OK`. These computations do not replace the proof and do not constitute external certification.

The independent audit was not performed. Relevant mathematical limitations and comparison scope are stated in `RESULT.md` and `REVIEW.md`.
