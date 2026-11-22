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

# Verification checks and limits

The standalone `verify.py` is executable using Python 3 standard library only. It checks exact finite-state identities in rational arithmetic and computes an independent four-state Markov semigroup from two independent spin-transition kernels.

Observed checks:

- Exact Krawtchouk eigenvalue equations and weighted orthogonality for urn sizes \(N=1,2,\ldots,11\): PASS.
- Exact polynomial multiplication and prescribed rational crossing-root identities for those sizes: PASS.
- Strictly positive, normalized four-state spin preparations and Walsh mode eigen-equations: PASS.
- Exact double-root gap factorization and nine independently evaluated stationary-weighted distance differences: PASS (absolute differences below \(10^{-13}\)).
- Example crossing times: \(0.11157177565710488\) and \(0.2554128118829953\), both positive and simple.

The proof of the general state-count ceiling is the induction/Rolle zero-count argument, not an inference from finitely many numerical cases. The proof of all-size attainability is the exact generating-function and polynomial-factorization construction. This package does not experimentally certify arbitrary state counts, publication priority, thermal-Gibbs applicability or any nonreversible extension.
