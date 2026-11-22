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

# Exact verification

Run `python3 checker.py` with Python 3 standard library. The two deterministic exact rational tests cover 8-by-8 and 6-by-6 triangulations of the full fundamental square and assert that one common integer-translated radius-3/8 or radius-1/3 diamond contains the three vertices of each triangle. These tests completed:

```text
four centers covered: 64 square cells, 128 triangles, exact rational
five centers covered: 36 square cells, 72 triangles, exact rational
All 200 rational triangle inclusion certificates passed.
```

The lower bound is a symbolic fiber-counting argument, not inferred from the finite checker; every displayed threshold and endpoint is proved in `RESULT.md`. The integer translates searched are sufficient because all centers and triangles lie in the unit fundamental square, and any alternate closest translate farther than one coordinate unit cannot improve containment. The verification establishes neither uniqueness of optimizers nor exact covering numbers for radii smaller than 1/3. Independent audit has not been performed.
