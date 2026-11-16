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

The proof derives the exact interpolation weights, the two Gram-matrix eigenvalues, all grounded Dirichlet eigenvalues, a full Krylov minimal-polynomial argument and multidimensional variational bounds. These are symbolic arguments valid at all stated dimensions and sizes.

Execute `python verification/check.py` from the extracted finding directory after installing `verification/requirements.txt`. The supplied checker passed 544 deterministic tests: harmonic equations, host Fourier analysis transfer, frame spectra, exact-rational endpoint formulas, path Dirichlet spectra and conditioning, multidimensional Rayleigh/Poincaré inequalities, and exact integer Krylov ranks.

The checker is finite supplementary evidence rather than an infinite proof or external independent audit. Its finite samples do not establish any claim outside the explicitly proved range. No numerical-tolerance CG complexity guarantee or arbitrary-host classification is asserted.
