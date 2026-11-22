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

The standard-library `verify.py` contains two independently constructed paths: a direct pair-of-parent-history enumeration and an exact rational finite-product evaluator, including a separate checker for shared sibling pairs with different parent labels. They agree for \(n=3,4,5,6\) and \(r\in\{0,1/4,1/2,1\}\), totaling 32 grouped exhaustive comparisons. Endpoint identities were checked at all \(3\le n\le19\). Additional finite numerical tests check approach to the fixed-rate density, the square-root crossover, and the bounded mismatched-parent limit. The standalone script reports `PASS 57 grouped exact and asymptotic assertions` and `PASS 21 extra mismatch checks`.

The analytical proof, not these bounded tests, establishes arbitrary integer \(n\), arbitrary real \(r\in[0,1]\), the fixed-rate limit, and the sequence-dependent vanishing-copying expansion. No independent mathematical audit has been performed.
