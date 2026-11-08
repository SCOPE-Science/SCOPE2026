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

Run `python check.py` with Python 3; the script uses the standard library only. Its output on the packaged source is:

```
PASS: literal voter-subset cases 2457
PASS: extended type-aggregate cases 1110400
PASS: boundary example
```

The literal check enumerates every nonempty subset of each outside candidate's supporters for all three quoted axioms, including overlapping candidate support. The aggregated checker instead covers over a million type-inventory/committee/quota configurations with exact rational comparisons. These are independent implementations of the critical axiom tests, not independent scientific audits. The all-size claim depends on the proof in RESULT.md, particularly the exhaustion and clamping cases. Larger elections and three or more ballot types are not certified by finite enumeration.
