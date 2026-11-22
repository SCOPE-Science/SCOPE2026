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
# Verification evidence and scope

`python3 verify_masks.py` was executed from the package and returned:

```text
VERIFY_OK mask_periods=49 language_lengths=16 periodic_language_stability=16
```

The checker examines finite periodic masks, cluster counts, fundamental periods, prefix discrepancies, and all admissible binary words up to length 16. It also builds minimal forbidden finite words from admissible prefixes and suffixes and checks a second cutoff for period stability. The statement for infinitely many periods and words is proved symbolically in `RESULT.md`; finite computations do not establish infinite quantifiers. The equality of generating-forbidden and minimal-forbidden entropies uses the published strict-gap theorem of Wu--Zhang (2026), not a computed limiting count. Historical priority and independent validation remain open.
