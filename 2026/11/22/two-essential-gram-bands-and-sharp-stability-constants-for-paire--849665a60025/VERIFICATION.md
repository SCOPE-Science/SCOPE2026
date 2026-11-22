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

The core evidence is the exact Poisson moment identity, the explicitly displayed parity block Toeplitz symbol, its algebraic inverse, monotone eigenvalue branches, and the standard continuous Hermitian matrix-Toeplitz essential-spectrum theorem. All infinite-dimensional bounds are derived by compression inequalities and weakly-null near-boundary test functions; numerical experiments cannot establish those theorems.

Run `python spectral_checks.py` with NumPy. The program checks representative real and complex parameters, formulas for the symbol's eigenvalues and its inverse, finite-section extremal convergence, and the absence of finite-section bulk eigenvalues in the predicted gap except for possible boundary outliers. A finite-section outlier does not falsify the essential-spectrum classification.

The theorem does not establish the entire Gram spectrum or the location/multiplicity of isolated gap eigenvalues. Its source date is that of the motivating publicly available arXiv version rather than the date of a journal revision.
