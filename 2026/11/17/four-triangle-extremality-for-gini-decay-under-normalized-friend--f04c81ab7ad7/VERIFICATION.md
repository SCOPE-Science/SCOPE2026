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

The standalone `verify.py` contains an exact rational matrix construction of the normalized graph generator, its three spectral projections, and checks of their matrix identities. It performs exhaustive cut-*orbit* testing for eight graph sizes and direct sharp-witness checks; it also checks 1,920 additional signed inputs and exact dimension coefficients.

Verified checker output:

```
EXACT_EIGENPROJECTION_AND_NORMALIZED_GENERATOR_IDENTITIES_PASSED 8
EXHAUSTIVE_PAIR_ORBIT_BINARY_CUT_BOUNDS_PASSED 8
EXACT_FULL_PAIR_SHARPNESS_AND_SIGNED_SIGNAL_CHECKS_PASSED 1920
UNIQUE_FOUR_TRIANGLE_GLOBAL_COEFFICIENT_BOUND_PASSED
ALL_FRIENDSHIP_NORMALIZED_GINI_CHECKS_PASSED
```

The arbitrary-dimension and all-real-time claims are mathematical consequences of the analytical proof in `RESULT.md`, not of a finite computation. No independent external audit has been carried out.
