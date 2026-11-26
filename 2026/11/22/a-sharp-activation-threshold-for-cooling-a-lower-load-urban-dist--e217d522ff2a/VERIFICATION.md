---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1,
  "record_status": "passed"
}
---
# Verification

Run `python3 verify_thresholds.py` from this directory. The stand-alone standard-library script uses rational arithmetic to replay the exact example and check the peak solution, derivative sign at equalization, and stationary equations on 180 rational parameter and budget cases with 21 grid allocations each. Its output is:

```text
180 exact rational budget cases and the strict objective comparison passed
```

The continuous parameter ranges, the exact aggregate optimizer, the strict ordering of thresholds, and uniqueness are established by the analytic proof in `RESULT.md`. A finite set of examples or grid points alone does not prove any of those universal assertions.
