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

# Verification and limits

Two implementations independently construct \(U_n\), enumerate prime parts, compute Möbius transforms and test the predicted repairs and splitting criterion. These test finitely many primes, parameters and indices; they are not a proof of the unrestricted result.

`python3 verify.py` checks \(P=1,\ldots,16\), odd primes up to \(79\), and all indices through \(240\); the classical \(P=1\) instance is included only as a regression check, not part of the new theorem.

`python3 independent_verify.py` checks \(P=2,\ldots,20\), all primes up to \(71\), and indices through \(180\), including finite minimal-denominator tests wherever the relevant rank is within the range.

The unrestricted proof depends on the general Lucas valuation theorem and exact Möbius convolution. Independent mathematical audit has not been performed.
