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

# Reproducibility and verification

The accompanying `check.py` requires only Python 3's standard library. Executing `python check.py` yields:

```
HP_CAP_EXACT_RATIONAL_PASS dimensions=3..12 cases=60
HP_CAP_ALL_BRANCH_ORDER_TRACE_PASS
HP_CAP_FIXED_VOLUME_SCALING_NUMERIC_PASS
```

The checker computes the relevant beta integrals *independently* by polynomial expansion and exact rational antiderivatives, without using the closed eigenvalue formulas to evaluate the integrals. It checks exact agreement for ten quaternionic dimensions and six rational heights each, including both critical heights; validates all three pairwise spectral differences and the multiplicity-weighted trace identity; and tests the analytic limiting profiles numerically at fixed scaled heights.

The universal correctness arguments are the algebraic sector decomposition, conditional beta-law computation and factored eigenvalue differences in `RESULT.md`. A finite collection of code checks cannot establish the theorem at every dimension, nor can it establish originality. No independent audit has been performed.
