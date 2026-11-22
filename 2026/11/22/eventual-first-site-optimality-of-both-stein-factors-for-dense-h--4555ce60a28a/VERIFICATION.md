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

# Reproducibility and proof checks

Run `python check.py` (Python standard library only). It runs deterministic exact-fraction computations on 36 fixed integer parameter families, including shape one, nonzero offsets, and two, three and four rows. Recorded output: `PASSED 6156 exact rational assertions over 36 parameter families`.

The code checks normalization via a rational generating function, birth/death recurrence, the rate gap, strict first-site upper bounds for fixed limiting sites, and the exact finite-fugacity signed-coefficient formula for the first-difference factor. It is finite diagnostic evidence; global uniform control and eventual maximizer existence are proved analytically in RESULT.md. No empirical test provides a certified universal numerical fugacity threshold.
