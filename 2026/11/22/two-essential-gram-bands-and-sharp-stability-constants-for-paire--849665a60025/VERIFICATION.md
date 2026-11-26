---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and verification

The core evidence is the exact Poisson moment identity, the opposite-parameter inverse disk automorphism, the explicit parity block Toeplitz symbol and its inverse, and the monotone eigenvalue branches. The essential-spectrum argument uses the symbol product identity modulo compacts and weakly null near-boundary test functions, and both sharp norm bounds use exact compression inequalities.

Run `python spectral_checks.py` with NumPy. The program checks the symbol-inverse product and Hermitian symmetry for representative real and complex parameters, samples the symbol eigenvalues against the interval bounds, tests the gap-width identity, and compares extremal eigenvalues of two finite-section sizes to the predicted edges. These comparisons do not test all finite-section eigenvalues for gap membership or prove infinite-dimensional convergence. The theorem does not provide the entire Gram spectrum or the location or multiplicity of isolated gap eigenvalues.
