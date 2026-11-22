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

# Verification scope and reproducibility

The exact mathematical proof is contained in `RESULT.md`: finite active-block representation; positive derivative weights for arbitrary site losses; signed-step proof of the path-variation contraction; continuous finite-selection transfer; equality witnesses; and power-loss smoothing. The proof does not rely on finite enumerations to establish infinite-dimensional parameter claims.

Run `python verify.py` with a standard Python 3 interpreter. It checks all consecutive-block partitions through nine sites with nine random positive-mass sets and every single-step direction, using `fractions.Fraction` for exact arithmetic. It also enumerates small path active patterns and verifies 180 heterogeneous power-loss constrained fit pairs with finite floating-point tolerance, plus explicit attainment and fully fixed-slope cases.

Observed output:

```text
EXACT_CONSECUTIVE_BLOCK_STEP_NORMS_PASS 32274
HETEROGENEOUS_POWER_SLOPE_BOX_PAIRS_PASS 180
SHARP_ONE_VERSUS_ZERO_DICHOTOMY_PASS
ALL_SLOPE_BOX_BV_CHECKS_PASS
```

The floating-point active-set enumerator is a diagnostic at small dimensions and does not constitute exhaustive verification of the general convex program. Bibliographic originality comparisons involve original algorithmic literature and exact stability results, but absolute historical priority is not independently established. This file records no independent validation or external certification.
