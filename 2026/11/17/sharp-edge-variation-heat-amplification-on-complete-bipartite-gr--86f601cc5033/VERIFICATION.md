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

# Reproducibility
Execute `python3 verify.py` using Python 3 and the standard library only. It constructs heat flow from exact rational spectral factors, tests all two-color cut indicators across systematic complete bipartite sizes, checks the two independent centering inequalities, verifies sharp singleton witnesses, checks random rational inputs and exact semigroup composition, and evaluates the initial growth formula algebraically.

The run reported:

```text
EXACT_ALL_BIPARTITE_CUT_HEAT_AND_CENTERING_TESTS_PASSED 6850
EXACT_RATIONAL_INPUT_CENTERING_AND_HEAT_TESTS_PASSED 2080
EXACT_HEAT_SEMIGROUP_COMPOSITION_TESTS_PASSED 2080
EXACT_SHARP_INITIAL_GROWTH_THRESHOLDS_PASSED 435
ALL_BIPARTITE_BV_HEAT_TESTS_PASSED
```

The universal theorem is established by the finite coarea reduction, exact cross-cut centering bound, spectral decomposition, and explicit attaining indicators given in `RESULT.md`. Finite enumeration is not used to infer a theorem for arbitrary sizes. Independent validation has not been performed.
