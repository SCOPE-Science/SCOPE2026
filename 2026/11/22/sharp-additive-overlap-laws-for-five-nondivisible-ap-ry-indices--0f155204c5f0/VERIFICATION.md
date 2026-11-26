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

The retained `verify.py`, using only Python's standard library, is a bounded diagnostic for the ordinary-carry calculation, the support criterion, and the two extremal levels for positive shifts below \(5^7\). For replay, place it beside this file and run `python3 verify.py`. The balanced-digit proof in `RESULT.md` establishes the extremal classification for unbounded shifts. The script is not formal verification of that assertion.
