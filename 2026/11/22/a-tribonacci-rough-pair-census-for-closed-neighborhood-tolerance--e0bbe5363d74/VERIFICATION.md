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

# Reproducible checks

Run `python3 verify.py` with Python 3 (standard library only). The checker directly builds the lower–upper masks from each subset on paths of every length from 1 to 16, independently constructs the determinized subset automaton, and compares its counts to the stated seven-orbit transfer model through length 35. It also confirms all asserted recurrence instances within that range.

Actual observed output:

```
VERIFY_OK: 16 exhaustive direct subset enumerations, 36 DFA/quotient counts, 31 recurrence tests
```

The complete proof of the formula for every positive integer is the subset-construction and finite transfer-equation derivation in RESULT.md. Tests of finitely many sizes do not establish the recurrence for all lengths. Literary comparisons involve the operator definitions and relation types, with remaining full-text access limitations as described in REVIEW.md and AUDIT.json.
