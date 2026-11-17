---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

# Verification scope

The corrected theorem is proved in `RESULT.md` by a bidegree kernel calculation, a matching-traces dimension argument, and a determinant criterion for the two remaining trigonometric null directions. Independent direct Hermitian-lift rank checks at degrees 1, 2, and 3 confirm generic full rank for balanced sites. The existing `verify.py` supplies additional examples concerning the earlier circle-ambiguity geometry, not a proof of the corrected all-degree statement. No formal Lean or expert attestation is claimed, and an execution log by itself is not proof.
