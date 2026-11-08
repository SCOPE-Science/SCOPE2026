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

The proof is analytical. `CHECK.py` uses exact Python fractions for the beta-binomial zero-pool law as both a direct product and an alternating sum of beta moments. It checks the finite-difference identity and monotonic threshold factor for admissible rational parameter triples. Numerical diagnostic tests compare first-crossing pool sizes and costs at multiple small prevalence values with the proven limits. Execute `python CHECK.py` with Python 3 and no third-party packages.

Checks cannot by themselves certify an asymptotic or all-parameter assertion; the finite-difference sign, monotonicity, gamma-ratio asymptotic, and uniform small-\(\alpha\) log expansion are proved in `RESULT.md`. The earlier clustered-testing and subsequent correlated-pooling literature is explicitly compared. No independent audit has been performed. Limitations include perfect assays, infinite exchangeability, and no pool-size constraint.
