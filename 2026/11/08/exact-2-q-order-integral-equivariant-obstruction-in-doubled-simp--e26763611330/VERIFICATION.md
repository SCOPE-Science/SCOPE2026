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

The script `verify.py` uses Python standard libraries and enumerates signed facets and codimension-one faces for q from 3 through 8. It checks the boundary orientation cancellation, the full hyperoctahedral generating-set action, the signed augmentation period, and the Euler-characteristic rank. Execute `python3 verify.py` from this package.

The exact Ext order for every q>=3 is proved in RESULT.md by the projectivity of the regular flip-group lattice and by a W-equivariant signed-augmentation retraction after multiplying by the number of facets. The finite replay alone is not a proof for unbounded q. No independent mathematical audit has been performed.
