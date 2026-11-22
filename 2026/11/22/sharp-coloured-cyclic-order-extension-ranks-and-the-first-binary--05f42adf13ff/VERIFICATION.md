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

## Reproducibility

Run `python3 checker.py` in the same directory as this document using Python 3 standard library. It independently evaluates the abstract one-point-extension game over every marked subset and the circular gap reduction, comparing all resulting ranks on 1,616 finite host words, then checks periodic minimum-host constructions and the complete two-colour eight-point extremal census.

Expected success lines:

```
GAME_FORMULA_COMPARISONS_OK 1616
PERIODIC_OPTIMAL_WITNESSES_OK
BINARY_EIGHT_POINT_CENSUS_OK 62 9 [2, 4, 8, 8, 8, 8, 8, 8, 8]
```

The all-parameter argument is a written induction, not a claim that the finite tests certify infinitely many parameters. Results beyond the tested finite ranges rely on the proof, and historical priority is not independently validated.
