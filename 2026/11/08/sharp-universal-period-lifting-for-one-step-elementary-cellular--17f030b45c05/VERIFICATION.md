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

# Verification of the period-lifting classification

From a directory containing `verify.py`, `verify_bits.py` and `classification.json`, run:

```
python3 verify.py
python3 verify_bits.py
```

The tested extracted programs print `VERIFY_OK {1: 156, 2: 82, 4: 6, 6: 12}` and `VERIFY_BITS_OK {1: 156, 2: 82, 4: 6, 6: 12}` respectively. `verify.py` independently compares all word-relation decisions for output word lengths 1–3 against direct exhaustive cyclic input enumeration for every elementary rule and multiplier 1–4; it also regenerates the classification table. `verify_bits.py` is a separate bit-packed implementation using different relation composition and traversal routines. The scripts use only standard-library integer and Boolean operations, with no empirical floating-point thresholds.

The all-length claim follows from finite monoid exhaustion and the four-vertex cycle lemma, not from the short-ring checks. The source files provide code and results sufficient to rerun, but the supplied verification has not undergone an independent external audit. This result does not address temporal periods, output words not in the full-shift image, or rules of larger radius.
