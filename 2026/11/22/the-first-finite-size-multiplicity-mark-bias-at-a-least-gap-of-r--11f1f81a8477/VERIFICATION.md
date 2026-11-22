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

The source code `verify_gap_marks.py` is standalone Python 3 with standard-library imports only. Execute it with `python verify_gap_marks.py`. Its expected output is:

```
REGULAR_GAP_MARK_EXACT_OK 300 27
```

The first value is the number of exact marked-vector tests comparing the coefficient formula with independent recursive enumeration of all restricted partitions. The second is the number of numerical first-correction diagnostics using exact partition counts at larger finite sizes. The diagnostic tolerance is explicitly specified in the code; a finite trend is not an infinite proof. The proof's analytic requirements and limits are recorded in RESULT.md.

Independent audit status remains not performed.
