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

Running `python verify.py` with standard Python 3 produces `FRIENDSHIP_MATCHING_COVARIANCE_CHECKS_PASSED` with seven fully enumerated cases, 4,092 vertices, 1,827 exact matrix-entry comparisons, and 499 finite spectral-order profiles. Exact rational characteristic-polynomial identities are checked for 999 values of the family parameter. Each enumerated vertex is an actual matching-incidence vector.

The general, unbounded parameter statement follows from the algebraic proof in `RESULT.md`; the finite tests do not certify the infinite theorem. Positive definiteness, eigenvalue exhaustiveness, normalization and all strict comparisons are reconstructed explicitly in that proof. No external or independent audit has been performed.
