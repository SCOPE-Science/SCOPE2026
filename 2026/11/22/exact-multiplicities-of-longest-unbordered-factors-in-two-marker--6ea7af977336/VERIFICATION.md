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

The derivation is a symbolic case partition by the zero runs around the two marked letters. `verify_direct.py` independently enumerates all unbordered intervals using the KMP prefix function, for every binary weight-two word up to length 46 (16,215 words); its output is `verify_direct.out`. `verify_series.py` uses integer run-class enumeration and coefficient formulas, checking each joint length/multiplicity count up to length 180; its output is `verify_series.out`. These are finite consistency checks, not proof by finite extrapolation. The infinite classification, generating functions, and joint limit are proved in RESULT.md.
