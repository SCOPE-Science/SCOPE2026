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

# Mathematical reproducibility

Run `python3 verify.py` with standard Python 3; the script requires no external packages. This code checks all strict input coordinate orders for dimensions two through eight, computes all induced binary-cut operator-norm candidates for each such order, tests an integer occupancy/global-winner bound over dimensions through 120, and compares exactly rational arbitrary two-input pairs and sharp one-peak witnesses.

Actual command output from the reviewed implementation:

```
EXACT_ALL_ORDER_CHAMBER_GINI_NORMS_PASSED 362878
EXACT_OCCUPANCY_AND_GLOBAL_PEAK_BOUNDS_PASSED 1537066
EXACT_ARBITRARY_TWO_INPUT_INEQUALITIES_PASSED 1672
EXACT_GLOBAL_PEAK_ATTAINMENT_PASSED 209
ALL_CYCLIC_DILATION_GINI_CHECKS_PASSED
```

The occupancy loop checks extremal and midpoint candidate sizes, rather than every integer cut size for each large parameter; a concavity reduction in the analytical proof justifies that choice. All experiments are finite. The proof of the infinite family is in `RESULT.md`, via cut coarea, two exact algebraic inequalities, the long-window global-maximum restriction, and the explicit sharp witness. Neither external independent review nor independently hosted certification has taken place. Primary literature was partially available; priority remains subject to independent checking.
