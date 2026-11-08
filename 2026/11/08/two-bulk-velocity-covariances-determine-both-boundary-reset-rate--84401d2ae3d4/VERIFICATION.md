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

The attached `verify.py` is a reproducibility aid. Run `python verify.py` from the extracted package. It checks exact-rational two-exponential identities, 42 rate-pair inversions, exact lower-edge equal-rate cases, and Simpson quadrature against the analytic Fourier coefficient. If NumPy and SciPy are installed, it additionally solves the stationary 102-dimensional covariance Lyapunov equation for 50 sites, using two OU boundary forces matched to the resetting-wall second-order covariance, and compares six central bulk spatial covariances with the thermodynamic formula.

These finite checks confirm examples and model consistency, not the limit for every chain length or all positive parameters. The general sharp image, unique inversion and minimality follow from the complete analytical proof in `RESULT.md`; the approximation from a finite chain is not an exact finite-size theorem. Independent scientific audit has not been performed.
