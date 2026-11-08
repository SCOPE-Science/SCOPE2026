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

# Reproducibility and verified limits

The standalone `verify.py` depends on Python 3, NumPy and SciPy. From the extracted package directory run `python verify.py`. The output reports the finite assertion count, independent numerical comparison between the exact one-dimensional entropy identity and direct two-dimensional squared-block joint information, the stationary log-variance entropy, and a weak-contrast profile value.

The checker verifies algebraic normalization and variance moment equations at several positive parameter choices; it compares the direct joint-density information integral with the closed-form three-entropy reduction; and it compares finite-group numerical convolutions with the fixed-contrast and local-contrast limits. All integrals are computed over finite grids with normalization controls and Gaussian-/log-Gamma-tail margins. Such checks establish numerical consistency only, not the global entropic convergence or the infinite-population theorem, which are proved analytically in `RESULT.md`.

No external independent review, expert validation, or certification has been performed. The full limits require strictly positive diffusion, stiffnesses and rates, and the contrast crossover uses an explicitly prescribed parameter sequence. The mathematics and source attributions should be independently checked before citing as a published original result.
