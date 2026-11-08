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

The complete analytic derivation is in `RESULT.md`; it is self-contained and does not rely on the finite checker. Run `python3 check.py` with Python standard library (3.8 or later). The checker tests the contractive run/off recurrence, exact mean-cycle and scale constants, and upper/lower analytic bounds approaching unity for stationary density and small-ball asymptotic factors under three parameter choices. It executes a deterministic generator of inactive durations solely as an illustrative recurrence check. Finite diagnostic assertions verify calculations only; they cannot establish the infinite-time asymptotics, originality or expert validation. External independent audit is not performed.
