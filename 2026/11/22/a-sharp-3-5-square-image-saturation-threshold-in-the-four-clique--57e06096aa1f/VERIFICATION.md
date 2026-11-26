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
# Verification of the finite certificate

Run `python3 check_deficit_27.py` from this directory. The proof reduces the algebra question to coverage by translates of the negative square set including zero. The script constructs the field, generates every translated triple and quartet from that set, and counts the resulting sets exactly. Expected output:

```text
covered triples=2925; covered quartets=16146
uncovered quartets=1404; normalized quartets=52
missing ordered targets=1248; square-image size=18435
```

The algebraic reduction and orbit sizes are proved in `RESULT.md`. The enumeration proves the stated finite counts only, not a threshold over field extensions or a distribution of all fiber sizes.
