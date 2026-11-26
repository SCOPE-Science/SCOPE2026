---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

Run `python3 verify_unequal.py` from the package directory. The expected output is `PASS: 20 ordered unequal pairs`. This exact rational calculation compares both triangular Fubini expressions and their coefficient ranks for all unequal pairs from one to five. The degree and moment argument in `RESULT.md` proves the result for all distinct positive integer orders; the script tests only the stated finite range.
