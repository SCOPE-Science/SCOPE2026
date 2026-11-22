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

The accompanying `check.py` is a standalone deterministic Python program using SymPy and mpmath. It verifies by exact symbolic algebra the inverse-Gaussian null influence variance, the three-point cancellation factorization, and the noncancellation formula at sample size two. It performs numerical quadrature of the defining two weighted integrals in the generic and exactly exceptional three-point examples and compares them with their proven leading terms; it reports 13 successful assertions.

The mathematically decisive arguments are the identity \(G_n(t)=Bt\) below the first observed sample point, the endpoint CDF jump when \(B=0\), and the multivariate central limit/delta-method covariance computation in `RESULT.md`. The finite calculations alone do not establish those general results. The proof treats fixed samples and then a separate large-sample limit, not a simultaneous growth regime. No independent external audit or validation has been performed.
