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
# Verification record

The proof establishes an all-real, all-integer-\(m\) theorem using an exact finite priority-stack count, then an exact \(m\)-step cancellation argument. It does not extrapolate a finite test to infinitely many initial conditions.

A standalone exact-rational regression checker is provided as `checker.py`. Running `python3 checker.py` yielded:

```
PASS 3403 finite tests: exact entry, strict pre-entry, m-step periodicity, and sharp examples
```

The checker independently tests the exact threshold count, the full vector at entry, every prior strict-width failure, four consecutive whole-block recurrences, and unbounded-integer entry examples. A deterministic lowest-index tie convention is used for reproducibility. No formal-machine proof or independent audit is claimed. Source-priority comparison includes one historically relevant abstract-only paper, which limits the originality assessment.
