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

Executed `python3 verify.py` using Python 3 standard library only. Recorded result:

```
UNIFORM_WEAK_ORDER_LDIM_PASS 28 independent literal cases 19180 version states 155 abstract cases first_entropy_gap_height_5
```

The literal engine constructs the actual named poset ideals and recursively solves the complete adversarial mistake-tree game on subsets of hypotheses. Independently, the abstract engine solves the Boolean-cube sequence root recurrence. The tests compare both with the formula on all widths one through four, heights one through seven, and compare abstract recurrence and formula on widths one through five, heights one through thirty-one. The checks also independently count all ideals and test the first gap at height five for widths two through five. They are finite checks: the induction written in RESULT.md is the evidence for all positive widths and heights.

No external or independent audit has been performed. No claim about ranks for nonuniform weak orders is certified here.
