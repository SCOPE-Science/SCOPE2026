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

# Reproducibility
Run `python3 check_exceedance.py` (Python standard library only). It checks exact residual polynomial identities using rational arithmetic, independently recomputes severity superlevel interval measures, numerically counts exceedances under both stated sampling laws, and checks sign-reversal separation. Tests are finite corroboration and do not establish the universal range or independent mathematical validation; see `RESULT.md` for the complete analytical proof. Endpoint equalities have zero sampling measure, and the ratio is undefined at the two initial minimizers, a null set.
