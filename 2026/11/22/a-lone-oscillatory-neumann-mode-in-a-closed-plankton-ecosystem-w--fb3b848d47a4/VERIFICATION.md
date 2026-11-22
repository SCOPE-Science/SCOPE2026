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

Run `python verify_npzd.py` with SymPy installed. The checker starts from the original nonlinear reaction vector field, independently differentiates it, and reconstructs the exact linear dispersion polynomial and Routh determinants. It then checks all quoted rational values for the homogeneous, first and second nonconstant harmonics; the negative discriminant proving positivity of the dispersion constant term; and strictly positive shifted coefficients in six polynomial inequalities for **all** squared wavenumbers at least \(9/4\). The proof, not a numerical scan, establishes the infinite tail.

The model and certificate support only linear spectral claims at one prescribed equilibrium, not existence, stability or biological observability of a nonlinear spatial pattern. Scientific originality remains subject to ordinary historical-priority limits; no independent scientific validation has been performed.
