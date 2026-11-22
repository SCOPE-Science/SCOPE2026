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

# Verification and reproducibility

The theorem is proved in `RESULT.md`. Run `python checker.py` with Python 3 and NumPy to replay 89 numerical assertions. The checker evaluates the unconditioned Gaussian integrals directly by tensor Gauss-Hermite quadrature, verifies the algebraic sharp threshold at selected inputs, checks the exact high-dimensional mixed-moment rate, and compares the alternative mean log likelihood ratio against a separately simulated normal sample with a fixed random seed.

The mathematical proof, not a finite computation, establishes the strict moment divergence at the boundary and the limit for all dimensions. The observed checker output was: `PASS: 89 deterministic quadrature, asymptotic, boundary, and simulation assertions`.

The model assumes a fully specified standard multivariate Gaussian point null and deterministic shrinkage. Composite nulls, unknown covariance and tuning based on test data remain outside the result. The numerical test is not an independent audit and does not imply formal certification.
