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

# Mathematical verification
The exact proof reduces to three pointwise vector-field identities, the invariant-generator formula for compactly supported measures, and a strictness argument using invariance of supports. The embedded `check_flux.py` performs symbolic checks of the vector field, unique equilibrium and pointwise algebraic relations, and prints `WILHELM_FLUX_IDENTITIES_OK` on success. The conditional-law step additionally uses differentiation of arbitrary smooth test functions, which is proved analytically in RESULT.md and not certified by finitely many computations. No unconditional stability, global basin, stochastic kinetics or independent audit is asserted.
