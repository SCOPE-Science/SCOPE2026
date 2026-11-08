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

# Mathematical verification

The principal analytic checks are (i) the precise \(4\pi\) Laplace-variable scaling in \(P_S(\omega)=e^{-2\pi\omega^2}F_S(4\pi\omega)\); (ii) uniqueness of Fourier transforms of the positive finite Gaussian-weighted spectral measures; (iii) the factor \(a^2/(8\pi)\) in the raw-PSD orbit; (iv) exponential growth on the appropriate tail when \(a\ne0\); and (v) the Gaussian moment-generating-function argument for constant first intensity. Each step is proved in `RESULT.md` with the necessary assumptions.

The included `CHECK.py` was executed in Python 3 and returned `ALL_COLORED_NOISE_FIBER_CHECKS_PASSED`. Its Gaussian, rational-tail and compact-band quadrature tests verify many choices of deformation and frequency; its second-derivative comparisons check the posterior-variance expression. No numerical test proves the infinite-dimensional result. No external or independent audit has been performed.

The established colored-noise first-intensity formula is from arXiv:2609.18689, Theorem 1.1 and equation (4.1). The present classification is not a claim that the cited paper first proved the new raw-PSD identifiability statements. The model is pure stationary Gaussian noise; adding a deterministic signal changes the first-intensity formula.
