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

# Verification of the all-length fiber classification

Run the two independent Python 3 standard-library programs from this extracted directory:

```
python3 verify_direct.py
python3 verify_series.py
```

`verify_direct.py` exhaustively enumerates every binary word avoiding `11` for all lengths from zero through 23. It computes the full multiplicity vectors of every contiguous factor of lengths one, two and three, groups words by equal vectors, and checks every group's size against the stated binomial formula. It also checks the full profile-count and singleton-count formulas. It finished with `VERIFY_DIRECT_OK`, including \((C_{23},U_{23})=(355,53)\).

`verify_series.py` independently computes the coefficients of the two claimed rational functions via integer recurrence, enumerates all feasible parameter tuples and their fiber sizes for lengths through 130, and checks the resulting total word counts against the Fibonacci recurrence. It finished with `VERIFY_SERIES_OK`, including \((C_{130},U_{130})=(12419,266)\).

The complete universal proof is not a computational induction: it follows from the run-decomposition bijection and exact formal-power-series identities in `RESULT.md`. Exhaustive numerical tests by themselves would not justify the all-length theorem. These programs use no external data, random inputs or third-party dependencies; they make no independent scientific-certification claim.
