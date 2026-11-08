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

The self-contained `verify.py` is a reproducibility check of the exact incomplete-beta integral and its direct-quadrature expression. It was executed successfully before this package was constructed, returning `BETA_INTEGRAL_AND_GAUSSIAN_SCALING_OK`; its complete outputs included `d=1 positivity_defect=0.333333333333` and `d=3 positivity_defect=0.512`.

The all-dimensional kernel identity, strict boundary maximization, equality cases and Gaussian limit are proved analytically in RESULT.md. Finite numerical checks do not prove those universal conclusions. No independent audit has been performed.
