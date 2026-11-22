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

The standalone `check.py` uses Python 3 standard library only. The run of `python3 check.py` reported `PASS: 698 deterministic checks`. It tests the analytic inclusion–exclusion formula, the derivative numerator, polynomial values and slopes at the midpoint, the positive critical root, the strict comparison with independent forcing, and near-threshold noncentral improvements. The mathematical proof is by exact exponential integration, polynomial identities, discriminant bounds and compactness; these finite computations do not imply unrestricted global uniqueness. Above the stability boundary the global optimum is not classified. No independent scientific review has been performed.
