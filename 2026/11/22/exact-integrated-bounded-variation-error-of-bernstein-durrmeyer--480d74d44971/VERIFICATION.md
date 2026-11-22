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

# Mathematical verification
The theorem's critical identities are proved in RESULT.md: symmetry of the positive Markov kernel, the beta–binomial tail identity, a strict derivative in the Bernoulli-pair disagreement parameter, and central-binomial telescoping. The extension from steps to arbitrary distributional-BV functions uses signed Radon measures and Fubini. Equality forces the derivative measure to concentrate at the unique worst jump.

## Reproducible computation
Run `python check.py` using Python 3 (standard library only). Exact rational checks cover degrees 0–15 at nine rational jump locations, independent polynomial and binomial formulas, and the sharp centered constant. Additional exact normalization/reflection tests and 30 approximate four-jump tests are included. Reported successful output:

```
EXACT_NORMALIZATION_BINOMIAL_BETA_SHARP_TESTS_PASS 144
SYMMETRY_AND_SIGNED_JUMP_TESTS_PASS 30
ALL_BERNSTEIN_DURRMEYER_BV_TESTS_PASS
```

Finite checks do not verify the universal BV quantifier or the complete literature; the analytic proof and identified sources supply those comparisons. No formal or independent certification was performed.
