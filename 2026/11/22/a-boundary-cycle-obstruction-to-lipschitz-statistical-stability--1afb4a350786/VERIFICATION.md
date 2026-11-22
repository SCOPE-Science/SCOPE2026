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

The complete proof appears in `RESULT.md`. The finite exact rational checks in `CHECK.py` verify polynomial test-function pushforwards of the right, bottom and left edge measures, as well as their total masses, and check both affine branch determinants by direct constants. Execute with `python CHECK.py` (Python standard library only). The infinite-dimensional statements are proved analytically by the change of variables in the moving cap, exact pushforward measures, Cesàro averages, Banach--Steinhaus and weak-* compactness. No finite computation proves those infinite steps.

The family-specific ACIP existence/uniqueness for parameters \(\tau\le t\le1\) is used from Pumariño et al. (2015), as explicitly recalled and applied by Alves--Etubi (2024). Only failure of finite-signed-measure differentiability at the one-sided endpoint, and the resulting strong non-Lipschitz bound, are claimed. External independent auditing has not been performed.
