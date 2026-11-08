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

The attached `verify.py` was executed directly after construction of the proof, with output:

```
VERIFY_OK direct_binomial_rows=85 finite_identity_rows=85 global_pairs=10000 min_margin=0 dyadic_pairs=510 attained_bound=15 digit_lemma_pairs=39800 binary_weight_samples=20000 tail_precision_cases=25
```

The checks use Python `fractions.Fraction` for exact rational arithmetic and independent direct `comb` summation. They cover finite rectangles only. The proof for all integers is the recurrence, 2-adic series identity, digit lemma, and ultrametric valuation argument. A calculation yielding positive residual valuation for a truncated 2-adic series is not by itself proof of the infinite identity.

No independent audit has been performed.
