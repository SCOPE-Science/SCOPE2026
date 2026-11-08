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

The finite checker (`checker.py`, Python 3 standard library, with optional NumPy for the assembled-Gram test) was executed directly from the package preparation directory and printed:

```
EXACT_LAYER_VS_NUMERIC_FOURIER_PASS
CROSS_RANK_AND_TAPER_PASS
FULL_GRAM_81_PROJECTORS_PASS
PRIME_POWER_CYCLOTOMIC_GABOR_CHECKS_PASS
```

Randomly sampled integer windows were checked at orders \(4,8,9,25,27,49\). At order \(9\), the checker independently constructed the analysis matrix using all \(81\) rank-one projectors, obtaining rank \(65\). For \(p=3,5,7,11\), exact digit-fiber counts established the predicted flat-cross rank and full rank under taper. The proof uses exact cyclotomic divisibility and a binary uniqueness argument; the finite computations do not independently verify the universal quantifiers. No independent mathematical audit was performed, and no stability bound is claimed.
