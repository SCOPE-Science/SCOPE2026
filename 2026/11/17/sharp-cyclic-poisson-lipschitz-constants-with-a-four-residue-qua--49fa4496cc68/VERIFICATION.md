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

The self-contained `check_cycle_inverse.py` was executed on the standalone file in this package using CPython and Python standard-library exact `fractions.Fraction` arithmetic. Observed outputs:

```
ALL_FOUR_RESIDUE_FORMULAS_PASSED 197
INDEPENDENT_DISCRETE_GREEN_RESIDUALS_PASSED 250
EXHAUSTIVE_ZERO_SUM_CUBE_VERTEX_EVALUATIONS_PASSED 4850
ALL_CYCLE_LIPSCHITZ_POISSON_CHECKS_PASSED
```

The first check compares four closed rational expressions with median deviations for each cycle size from 3 to 199. The second checks every coordinate of the Green row residual for sizes 3 to 22. The third enumerates all extreme points of the zero-sum unit cube for sizes 3 to 12 and obtains the predicted row norm. This validates implementation and arithmetic on the stated finite cases. The proof in RESULT.md, rather than enumeration, establishes the theorem for all cycle lengths and all equality inputs. No external audit has been performed.
