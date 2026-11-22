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

# Reproducibility and limits

Run `python3 check.py` with Python 3.9+; only standard-library modules are used. The exact-fraction computations check 40 identities, including the strictly positive derivative via Bernstein coefficients, both population contrasts, the exact negative limit, the cubic sign decomposition, the null projection variance, and nine exact pooled-label enumerations for sample pairs with sizes three through six. The published statistic is defined here for sample sizes at least four.

The proof of asymptotic power zero is analytical: the bounded two-sample U-statistic strong law produces the fixed negative alternative limit; Hoeffding projections and the classical central limit theorem yield the null chi-square law. Finite enumeration or floating-point simulation alone would not establish either limit. No external channel has independently audited the work.
