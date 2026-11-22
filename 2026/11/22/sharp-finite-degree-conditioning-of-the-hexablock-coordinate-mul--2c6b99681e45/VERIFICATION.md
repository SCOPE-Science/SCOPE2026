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

The one-variable Fourier coefficient identity reduces the claimed lower bound to a finite symmetric tridiagonal eigenproblem. Equality follows from a self-reciprocal polynomial and its simple root parity at minus one; the Jacobi-node description follows from the block beta weights.

`check.py` uses SciPy to test degree cutoffs 0 through 40, the predicted least eigenvalues and multiplicities, and the explicit Toeplitz eigenvector. Its 123 checks passed. This numerical test is not an exhaustive proof, and independent audit has not been performed.
