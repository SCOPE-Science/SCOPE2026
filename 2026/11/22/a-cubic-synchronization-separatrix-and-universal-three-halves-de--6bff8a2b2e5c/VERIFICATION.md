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

The analytic argument proves the result for every real initial deviation in the stated sector and does not rely on finite experiments. Independent mathematical audit has not been performed.

A standalone Python 3 checker (`check.py`) evaluates the exact source-model reduction at \(\mu=0\), verifies the two algebraic invariance-series identities as rational equalities, checks examples of rigorous below-threshold and finite-crossing regimes, and reports long-run diagnostics for a high-order *approximation* to the threshold. Its finite tests cannot independently certify the existence or uniqueness of the threshold or the infinite-time limits. The critical proof is the order comparison, infinite Riemann-sum inequality, and telescoping inverse-square increment in `RESULT.md`.
