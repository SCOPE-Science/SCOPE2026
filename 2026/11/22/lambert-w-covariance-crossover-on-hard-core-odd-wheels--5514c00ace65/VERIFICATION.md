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

# Verification and limitations

The mathematical derivation reduces a two-site occupation covariance to path and cycle independence polynomials and then derives the critical Lambert-\(W\) scaling using the two transfer eigenvalues. Direct exhaustive checks of the three marked generating functions were performed at odd rim lengths 7, 9, 11 and 13. Independent asymptotic-bracket and normalized-profile numerical tests were also performed. The attached standard-library `verify.py` repeats them. These checks do not replace the all-size analytic proof.

No uniqueness of covariance zeros is proved. Self-review covered mathematical correctness, literature implication comparison and mathematical value; no independent scientific audit or verification is claimed.
