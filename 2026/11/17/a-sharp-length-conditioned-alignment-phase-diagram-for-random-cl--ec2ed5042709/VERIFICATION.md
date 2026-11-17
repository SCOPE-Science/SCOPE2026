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

# Reproducibility and limits

Running `python checker.py` with NumPy and SciPy samples independent Haar-Stiefel frames by Gaussian QR, verifies the matrix determinant/angular identity, checks fixed-length conditional cosine means at several edge counts against numerical angular integrals, and compares the elliptic alignment boundary with its defining equation and values on both sides. The expected final line is `STIEFEL_EDGE_ANGLE_CHECKS_OK`.

The proof of the two-row marginal uses a standard matrix polar-coordinate Jacobian; independent computational verification of this general geometric-measure theorem is not claimed. Numerical integration and Monte Carlo cannot prove all-dimensional stochastic ordering or uniqueness of the critical threshold; both are proved analytically in the result. External independent review has not been performed.
