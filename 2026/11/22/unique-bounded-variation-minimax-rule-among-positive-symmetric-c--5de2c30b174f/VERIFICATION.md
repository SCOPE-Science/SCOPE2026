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

The packaged standard-library checker `check_quadrature.py` was executed against the same formulas used in the proof. It returned:

```
CUBIC_UNIQUE_ROOT_RATIONAL_BRACKET_PASS
MOMENT_EXACTNESS_AND_SHARP_DISCREPANCY_FORMULA_PASS
CLASSICAL_RULE_BENCHMARKS_PASS
POSITIVE_RULE_PARAMETER_GRID_PASS 20001
SHARP_DISCONTINUOUS_STEP_WITNESSES_PASS
INDEPENDENT_RANDOM_JUMP_FUNCTIONS_PASS 2500
ALL_THREE_NODE_CUBIC_EXACT_BV_CHECKS_PASS
```

The first check uses `fractions.Fraction` and exactly evaluates the cubic at rational endpoints. The moment and discrepancy checks independently compute the weighted evaluations and distribution-function jumps. The random jump tests measure actual Jordan variation by the sum of signed-jump magnitudes. The finite tests do not certify the universal quantifiers; the proof in `RESULT.md` establishes the global bound and unique optimizer. No independent audit has been performed.
