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

# Verification

The mathematical argument is self-contained in `RESULT.md` and uses an exact five-jet of the reduced Chialvo map, a whole-domain derivative bound, and a summable-increment theorem. It does not depend on a numeric experiment for the infinite-limit claim.

To check the reproducible auxiliary identities, run `python checker.py` in this directory with SymPy and mpmath installed. The checker tests all critical derivatives and exact Taylor coefficients, the exact normalizing coefficients \(A,D,H\), sample high-precision trajectories from both sides of the fixed point, and the consistency of the local fold-opening coefficient. The symbolic identities and all finite assertions passed during the review.

Finite-time numerical estimates of the logarithmic coefficient converge slowly and are not asserted to equal the limiting value at any finite horizon. The cutoff cannot prove the full recurrence asymptotic. The proof establishes the limit \(C(x_0)\) separately. Independent mathematical audit has not been performed.
