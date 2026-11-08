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

Run the included standalone scripts using Python 3:

```sh
python verify_direct.py
python verify_earliest.py
```

`verify_direct.py` enumerates all possible palindromes of feasible lengths and compares their minimal-absence test against a separate factor-derived generator for all binary words of lengths 1 through 12. It also directly checks the exact construction for lengths 3 through 29. Its success marker is `DIRECT_VERIFY_OK`.

`verify_earliest.py` exhaustively enumerates all binary input words of lengths 1 through 16, checks distinct endpoint assignments, and verifies the sharp maximum and finite equality cases within that tested interval. Its success marker is `EARLIEST_VERIFY_OK`.

Both checks were executed with these success markers before packaging. These are finite regression tests. The arbitrary-length upper bound is proved by the injection argument in `RESULT.md`, not extrapolated from the checks. No independent scientific audit was performed.
