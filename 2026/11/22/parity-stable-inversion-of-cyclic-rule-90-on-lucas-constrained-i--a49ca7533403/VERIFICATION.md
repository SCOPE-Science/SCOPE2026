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

# Verification protocol

Run `python3 CHECK.py` in this directory. The standard-library script exhausts all admissible inputs for lengths 2 through 16, iterates their image sets through two steps beyond the predicted stabilization time, and checks each explicit strict-step witness separately. The expected output is `VERIFY_OK n=2..16: image counts and all strict-step witnesses`.

The all-length and all-time theorem follows from the polynomial kernel calculation and admissibility of the periodic witnesses. The finite check does not prove generality or address publication priority.
