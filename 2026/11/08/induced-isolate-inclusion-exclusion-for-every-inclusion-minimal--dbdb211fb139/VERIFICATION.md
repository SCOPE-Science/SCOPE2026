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

The original covering rule was checked by exhaustive selection of each vertex subset and edge subset, not by using the structural theorem. For every directly feasible cover, each selected element was independently deleted and coverage recomputed. `verify.py` reconstructs the proposed receiver-map sets and calculates inclusion–exclusion counts, then compares both with the direct oracle.

Run: `python3 verify.py` using Python 3 standard library only. Expected summary:

```
ALL_LABELLED_GRAPHS_N1_TO_N4_OK 75
ADDITIONAL_GRAPHS_N5_N6_OK 40
FORMULA_COUNT 6 {4: 3, 5: 48, 6: 6}
FORMULA_COUNT 7 {5: 14, 6: 98, 7: 2}
FORMULA_COUNT 8 {7: 28, 8: 57, 10: 70, 13: 56, 17: 28, 22: 8, 28: 1}
VERIFY_OK
```

All simple labelled graphs with up to four vertices were checked; only the stated finite sample of larger graphs was tested. The unrestricted result rests on the mathematical proof. Independent mathematical validation remains unperformed.
