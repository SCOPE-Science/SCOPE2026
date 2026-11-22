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

# Finite reproducibility and proof boundaries

Run `python verify.py` with Python 3 and no nonstandard dependencies. The verifier solves each Fourier Vandermonde system directly and checks the five harmonic moments and the independently evaluated sign formula. Deterministic randomized tests and exact endpoint perturbation examples returned `VERIFY_OK 1059 trigonometric_quadrature_checks alpha_star 0.201459422460511`.

The infinite family of perturbation boxes is established in RESULT.md via an exact four-variable derivative argument; random finite tests cannot prove universal positivity. Numerical tolerances reflect floating-point arithmetic only and are not certified interval arithmetic. The source date and classification were checked against arXiv:2610.32699v1.
