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

Analytic correctness rests on the explicit cubic inverse, the strictly convex Jacobian numerator for every \(a<-1\), and the exact critical factorization at \(a=-1\). Bisection and rational discriminant sample checks are illustrative and do not certify all reals in isolation.

The included standard-library script \(\texttt{check.py}\) verifies representative one-, two- and three-preimage cases by exact integer-rational discriminants, checks derivative and cubic identities in rational arithmetic, and tests the limiting neck-opening coefficient. All tests passed in the packaged scientific record.

No independent mathematical audit has been performed. No code execution implies exhaustive prior-literature coverage.
