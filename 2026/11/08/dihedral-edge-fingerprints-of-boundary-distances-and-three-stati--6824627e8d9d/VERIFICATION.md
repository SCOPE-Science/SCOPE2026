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

The mixed-statistic inverse is proved in `RESULT.md` from the previously published exact short-distance box law and the explicitly rederived second moment, followed by Vieta inversion and a Jacobian minimality argument. Independent area-weighted second-moment checks at four boxes corroborated the formula. The original `check_boundary_pairs.py` also numerically investigates the earlier surface-distance law and box moments; it is not evidence that the published general edge coefficient is new. No Lean or expert attestation has been performed.
