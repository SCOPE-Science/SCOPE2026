---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

# Exact rational witnesses

Run `python3 verify.py` with `certificate.json` in the same directory. For the three step sizes shown in `RESULT.md`, the standard-library checker verifies the integer cyclic equations in every coordinate, the mass identity, and the signed minima of the eight first-column entries. The calculation is exact; analytically, invertibility identifies the columns and continuity gives distinct positive-step components. The three witnesses do not determine the entire positivity set.
