---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

# Reproducibility and exact-proof scope

Run `python3 verify.py` (standard library only). The checker uses rational partial fractions to recover the transient matrices by a different calculation from the spectral projector polynomial in `RESULT.md`. It checks all two- and three-block schedules in the two stated instances, including strict swap signs and both unique optima. This is an exhaustive comparison only for those instances. The proof that one or two transitions cannot show the obstruction uses the analytical affine normalization and comparison.
