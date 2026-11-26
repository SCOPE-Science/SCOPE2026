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

# Exact rational diagnostics

Run `python3 checker.py` with Python 3.9 or later. This unchanged standard-library checker has expected output `PASS 14412 exact assertions`. It verifies the exact derivative-sign factorization at rational tuples with integer powers 2 through 5, the strict elevation of the exponent, both rational examples, and selected cases of the classical pointwise height envelope.

The continuum temporal classification, uniqueness, endpoint case and sharp contrast for possible positive-time peaks follow from the sign proof in `RESULT.md`, not from finite samples. The square-law pointwise threshold is credited as a consequence of the Kantorovich envelope.
