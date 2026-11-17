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

# Reproducible verification

Run `python verify.py` using Python 3 with the standard library. The checker builds each product design and the weighted \(L^2\) affine projector directly, forms all grid graph edges, tests every nonconstant binary cut for seven uniform designs through twelve vertices and one nonuniform weighted two-by-three design, and confirms the exact step-function witness. Representative output:

```text
EXACT_COAREA_CUT_ENUMERATION_PASS [2, 2] value 1 cuts 14
EXACT_COAREA_CUT_ENUMERATION_PASS [2, 3] value 1 cuts 62
EXACT_COAREA_CUT_ENUMERATION_PASS [3, 3] value 1 cuts 510
EXACT_COAREA_CUT_ENUMERATION_PASS [2, 4] value 6/5 cuts 254
EXACT_COAREA_CUT_ENUMERATION_PASS [3, 4] value 6/5 cuts 4094
EXACT_COAREA_CUT_ENUMERATION_PASS [2, 2, 2] value 1 cuts 254
EXACT_COAREA_CUT_ENUMERATION_PASS [2, 2, 3] value 1 cuts 4094
EXACT_COAREA_CUT_ENUMERATION_PASS [2, 3] value 869/137 cuts 62
SHARP_UNIFORM_FOUR_SITE_ONSET_AND_3_OVER_2_ENVELOPE_PASS
ALL_PRODUCT_GRID_AFFINE_BV_DIAGNOSTICS_PASS
```

The finite tests are supporting diagnostics, not a proof over arbitrary dimensions or continuous weights. That proof consists of the orthogonal coefficient decomposition, an exact positive weighted prefix-sum identity, a termwise variation inequality and an equality witness for every candidate edge. The source was read, computations were run locally in exact rational arithmetic, and no independent mathematical audit was undertaken.
