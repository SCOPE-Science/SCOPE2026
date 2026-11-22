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

# Verification record

The attached `verify.py` was executed with Python 3 and no third-party dependencies. It returned `PASS 1360 exact-rational assertions (n=3..30; all 2^n signs for n=3..8).`

The checks use exact rational matrices: spectral moments, the one- and two-node orthogonal polynomials, exact inverse-Hermite residual matrices, finite-dimension Rademacher variances, binomial signs for every probe configuration in dimensions three through eight, deterministic global-Lanczos deficit inequalities, and perturbation examples in four dimensions. The validator independently constructs the Hermite residual from the matrix and the computed moments rather than substituting the closed-form asserted matrices.

The proof in RESULT.md, not the finite checker, justifies all dimensions, all positive sample counts and the limiting irreducible variance ratio. Neither the finite runs nor the algebraic proof constitutes independent mathematical validation by a separate party.
