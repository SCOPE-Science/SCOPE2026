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

The stated STFT convention uses the kernel \(e^{-2\pi i\xi t}\) and window \(e^{-\pi a t^2}\); the signal has a common phase \(e^{\pi i c t^2}\). The intensity normalization in `RESULT.md` was reconstructed directly from the complex Gaussian integral, and the derivative analysis was checked symbolically.

Run `python CHECK.py` with `mpmath` and `sympy`. The checker directly integrates the original windowed signal at independent numerical parameter choices, verifies the closed-form intensity, compares exact Taylor coefficients and derivative constants using symbolic simplification, and tests the quartic-root maxima and positive-frequency saddle-node with high-precision root finding. These tests are finite corroboration; the analytic implicit-function and concavity argument is required for the quantified local result.

The remaining unverified matter is independent mathematical review and publication-priority comparison against a recent source whose complete text was unavailable. No independent certification is implied.
