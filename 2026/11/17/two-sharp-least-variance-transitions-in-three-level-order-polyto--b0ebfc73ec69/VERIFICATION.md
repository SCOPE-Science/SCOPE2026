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

Run `python3 check_covariance.py` in a standard Python 3 environment; no third-party packages or network access are required. The program independently reconstructs each block of the covariance from exact covariance sums of consecutive uniform order statistics, then verifies the closed block expressions, within-block contrast eigenvalues, and all exact characteristic-polynomial sign identities and integer transition ranges. It tests 480 parameter profiles and 850,040 rank-pair covariance summands, including the boundary \(q=1\), the first transition, and the exact equality \(q=p+3\).

Observed output:

```
THREE_LEVEL_ORDER_COVARIANCE_EXACT_PASS profiles=480 order_statistic_pairs=850040
```

This is finite evidence only. The universally quantified proof is the factorization and inequalities provided in `RESULT.md`. There has been no independent mathematical audit.
