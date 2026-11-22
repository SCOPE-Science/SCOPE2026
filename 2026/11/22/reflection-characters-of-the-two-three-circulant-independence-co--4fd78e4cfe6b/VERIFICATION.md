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

Run `python3 check.py` from this directory; the output must match `EXPECTED.txt` exactly. It verifies the integer transfer identities for an unbounded recurrence and also carries out bounded, independently constructed fold/oriented-face comparisons. The finite cases are corroboration only; the proof of the all-length theorem is in RESULT.md. This is a self-review, not external validation.
