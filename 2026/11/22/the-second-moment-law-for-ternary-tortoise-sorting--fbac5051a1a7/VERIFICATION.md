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

# Reproduction and limits

Use the Python standard library, from the package root:

```bash
python3 verification/exhaustive.py
python3 verification/series.py
```

The provided `verification/exhaustive_output.txt` and `verification/series_output.txt` are actual outputs of these commands. The first implements two independent algorithms for the ternary tortoise transformation and checks each predicted fiber on all input and output words through length nine (29,524 of each), as well as the squared-fiber sums. The second checks all 8,191 binary words through length twelve, then compares rational coefficient recurrences through degree eighty.

These finite calculations are checks, not an independent or infinite mathematical certification. The all-length identity is derived by the explicit factorization and geometric-series proof in RESULT.md. None of the scripts contacts an external service or relies on an unavailable package.
