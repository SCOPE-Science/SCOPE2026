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

# Reproducibility

Use `python3 artifacts/verify.py` in the package root; Python's standard library is sufficient. The checker constructs the undirected subdivision graph, its directed non-backtracking adjacency matrix, and exact closed-walk traces. Newton identities recover the characteristic polynomial in integers for parameters one through three, then compare each coefficient against the independently specified symbolic product. It also tests the incidence-gram spectral power sums through parameter eleven and the exact small-integer Ramanujan threshold arithmetic through parameter 79.

Successful replay prints:

```
EXACT_NONBACKTRACKING_CHARPOLY_OK 1 degree 12
EXACT_NONBACKTRACKING_CHARPOLY_OK 2 degree 48
EXACT_NONBACKTRACKING_CHARPOLY_OK 3 degree 108
INCIDENCE_SINGULAR_SPECTRUM_OK a=1..11
SHARP_LOWER_EDGE_AND_REAL_COUNT_OK a=2..79
VERIFY_OK
```

These finite checks are reproducibility evidence. They do not prove the formula for all parameter values or establish historical priority. The complete symbolic argument appears in `RESULT.md`.
