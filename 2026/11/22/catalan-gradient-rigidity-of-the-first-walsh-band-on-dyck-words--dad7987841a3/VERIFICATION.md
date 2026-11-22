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

# Verification

Run `python3 verify_dyck_firstband.py`; standard-library Python suffices. The independent recursive generator enumerates every balanced nonnegative prefix word for semilengths 1–10, without using the claimed Catalan-gradient formula to generate words. It verifies the total Catalan count, both positional formulas, the strict zero locations, and the sharp smallest nonzero coefficient. The supplied program printed: `PASS: all positional Walsh coefficients, zero positions, sharp nonzero gap` and `Semilengths 1..10, first-order multipliers checked: 110`.

The complete proof for arbitrary semilength is in `RESULT.md`. No exhaustive test beyond semilength 10 and no higher-order Walsh classification is claimed.
