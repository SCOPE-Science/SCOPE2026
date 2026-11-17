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
# Reproduction and scope

Run `python checker.py` with Python, NumPy and SciPy. The program forms a signed-coefficient primal linear program with explicit absolute-value epigraph variables; its objective is the maximum of the exact tree-transport expressions. It compares that numerical program against rational candidate formulas for \(73\) parameter profiles, checks uniqueness using coordinate extrema over the optimal face, and checks the critical interval by maximization and minimization of coordinates and their differences. A separate Lipschitz-potential dual LP tests the tree-norm identity.

Expected terminal lines:

```
EXACT_FORMULA_VS_SIGNED_LP_PASS profiles= 73
SEPARATE_METRIC_DUAL_VS_TREE_ABSOLUTE_SUM_PASS
ONE_DEFECT_STAR_OPTIMAL_EXTENSION_ALL_CHECKS_PASS
```

These finite checks are consistency tests, not an exhaustive verification of all real parameters. The all-parameter proof and the precise signed equality arguments appear in RESULT.md. No independent mathematical audit is claimed.
