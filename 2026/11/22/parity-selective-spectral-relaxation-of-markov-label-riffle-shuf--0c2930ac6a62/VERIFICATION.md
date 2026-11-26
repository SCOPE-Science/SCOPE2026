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

Run `python3 check.py` with standard Python. The parameter is the literal retention probability. The script enumerates binary words up to length 11 at six rational retention probabilities (including both deterministic endpoints), compares the signed transfer, initial values and recurrence with these exact means, and checks rare-switch counts through length 30. It also compares the signed transfer with the stated limiting profiles on a finite growing-deck grid; this last test is numerical. The general recurrence, expansions and limits rely on the proof in `RESULT.md`, not on extrapolation from the checks.
