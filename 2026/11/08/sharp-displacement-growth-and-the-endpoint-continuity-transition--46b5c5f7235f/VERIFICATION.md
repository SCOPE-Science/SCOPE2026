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

Use a Python 3 standard-library interpreter: `python CHECK.py`. The checker prints the number of successful finite assertions. In this package it passed 376 checks on the radial-transport geometry, the coherent-state error-function formula, the projective displacement identity, the endpoint discontinuity witness, and a large-displacement asymptotic.

The calculations do not certify the infinite-dimensional theorem by enumeration. The proof is the self-contained analytical argument in `RESULT.md`, in particular the submean inequality for a Gaussian-gauged entire function, the elementary weighted radial interval bound, and the projective group law. The Banach-space completeness/density inputs are also available in the cited 2026 mixed-norm Fock paper. Spectral conclusions use the standard spectral radius formula for complex Banach spaces, not any numerical eigenvalue computation.

The exact leading constant of the *operator norm* is not claimed. The explicit error-function formula is only for the coherent-state lower witness. Publication priority has not been independently verified.
