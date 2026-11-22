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
The proof was checked against the exact Doob transition formula and the effective state spaces in Theorem 1.1 of arXiv:2611.16041v1, including its eigenfunction plateau and derivative, and the strictly positive invariant density of Theorem 1.2. The boundary \(a=1/c\) is assigned to the two-step regime. Upper-tail truncations were checked to yield the claimed exact Dobrushin coefficients. The Markov two-step minorization uses only the eigenfunction plateau and positivity; its numerical constant is derived from the bound \(h\le1\). The failure of uniform mixing at positive coupling is an all-finite-lag support argument, not a finite test.

The included `checker.py` was run with Python's standard library and passed 635 exact-rational assertions covering nested-tail total variation, finite-grid transition equations, the common two-step minorizing measure and positive-coupling path support. The grids are finite illustrations of identities and not an exhaustive computation or a proof of infinite/continuous assertions.

A statement-level overlap search was performed against arXiv:2611.16041v1, arXiv:2606.01832v1, arXiv:2609.08794v1, relevant mathematical search results, and published mathematical records. The model-specific phase index was not located; this does not rule out an unindexed derivation. Independent audit and independent validation have not been performed.
