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

# Reproducible checks and their limits

The supplied `verify.py` is standalone Python 3 code, using integer and `fractions.Fraction` arithmetic only. Execute `python3 verify.py` alongside this document.

It checks the analytic finite cut formula against separately enumerated locally realizable max-selector chambers, not merely against a second implementation of the same arc formula. For 36 positive-weight profiles on cycles of size three through eight it exhausts all strict selector sign patterns and all proper binary perturbations; it also constructs and verifies 3,984 genuinely nonlinear strict-chamber pairs realizing prescribed boundary options. Uniform-weight contraction, two-periodic exact factors, and the four-vertex nonlocal-vs-singleton gap have further exact tests.

Observed output:

```
EXACT_CHAMBER_CUT_AND_COMPACT_FORMULAS_PASS 36
EXACT_STRICT_TWO_INPUT_WITNESSES_PASS 3984
UNIFORM_CONTRACTION_AND_ALTERNATING_SHARPNESS_PASS
FOUR_CYCLE_TWO_WALL_VERSUS_SINGLETON_GAP_PASS 2 4/3
ALL_CYCLIC_DILATION_VARIATION_CHECKS_PASS
```

These finite checks do not establish the result for arbitrarily large cycles or arbitrary positive real weights. Those assertions depend on the strict-selector, layer-cake, and boundary-realization arguments in RESULT.md. No external audit has been performed.
