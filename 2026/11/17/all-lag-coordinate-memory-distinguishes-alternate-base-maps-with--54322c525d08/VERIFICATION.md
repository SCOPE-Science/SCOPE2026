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

# Reproducible verification

The file `verify_alternate_base.py` is a self-contained Python 3 program using only the standard library. Run `python verify_alternate_base.py` in the directory containing the file. The program directly integrates products of piecewise-affine fractional-part functions with exact rational arithmetic, without assuming the conditional covariance identities used in the proof. Its tests cover ten rational-base configurations, the initial sawtooth moments, and lag formulas from one through four.

Expected successful final line:

```
VERIFY_OK rational_base_cases=10 exact_affine_integral_checks=60 lags=1..4 stationary_component_means=verified
```

The numerical range is finite, so these checks cannot certify the theorem for all rational bases, integer multiples, and time lags. The analytical proof establishes the universal quantifiers through exact inverse-cell conditional expectations. The same-model correctness, originality, and value assessment is recorded in REVIEW.md and AUDIT.json. No independent audit has been performed.
