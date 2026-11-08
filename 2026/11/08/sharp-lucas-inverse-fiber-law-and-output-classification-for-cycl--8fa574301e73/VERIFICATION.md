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

The accompanying standalone program `verify_rule28.py` uses only Python's standard library. Execute `python3 verify_rule28.py` in the directory containing the program. The checker forms every indexed input word for lengths 1 through 17, performs synchronous Rule 28 updates using the truth-table bits of integer 28, tallies predecessor multiplicities independently, and compares all output fibers with the exact gap-matrix expression and the predicted optimizer classification. It also tests transfer identities and long Lucas profiles. Successful output is:

```
VERIFY_OK exhaustive_outputs=262142 n=1..17 longer_profiles=596
```

This does not exhaust larger lengths or independently certify an infinite theorem. The proof of the matrix identities and the monotone trace comparison appears in `RESULT.md`. The sources used for scientific comparison, including the nearest 1989 primary predecessor-enumeration treatment, appear in the references of that file.
