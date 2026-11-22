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

# Reproducible checks and boundaries

Run `python3 checker.py` with NumPy installed. The self-contained script enumerates one-parent-per-row exact rational cases up to dimension six at three rational dominance ratios. It also samples signed matrices with arbitrary subcritical row budgets and probes the explicit comb family with exact expected leaf-response norms. Expected successful output:

```
PASS: 15117 exact-rational parent-forest row assertions; 369 finite numerical matrix/comb cases
```

The infinite-dimensional-size assertions follow from the general row-recursion and matching construction in RESULT.md. These finite tests do not assert exhaustive coverage of all real or complex matrix entries, and no external or independent validation has been performed. The supplied reproducibility script uses IEEE floating-point computation for its supplementary numerical tests, distinct from the exact-arithmetic theorem.
