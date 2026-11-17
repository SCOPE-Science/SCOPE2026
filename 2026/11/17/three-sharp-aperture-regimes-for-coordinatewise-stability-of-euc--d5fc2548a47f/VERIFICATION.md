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

# Reproducibility and checks
Run `python3 verify.py` with the standard Python library. Its deterministic random seed reproduces the exact numerical output:

```
MIDDLE_JACOBIAN_AND_GLOBAL_ROW_BOUNDS_PASS 5250
THREE_APERTURE_REGIMES_ASYMPTOTIC_CHECKS_PASS
THREE_DISTINCT_EVENTUAL_ACTIVE_ROW_BRANCHES_PASS
ALL_SCALED_CONE_PROJECTION_CHECKS_PASS
```

The script computes the projector independently from the Jacobian and compares first-order finite differences at 5,250 interior configurations, checks every induced derivative row against the proposed optimizing bound, confirms the previously published \(\kappa=1,d=4\) benchmark, and tests the predicted branch transitions and limiting growth in sample dimensions. The global two-point bound is not inferred from these samples: it follows from the analytical row-sum and segment-integration proof. The asymptotic envelope is proved by the scalar maximum and uniform error bounds; sample large dimensions cannot establish it alone.

Limits: The checker uses floating-point arithmetic and does not constitute independent certification. No complete search of every historical research source is asserted. Only \(d\ge2\), \(\kappa>0\) and the Euclidean projector measured in the coordinate maximum norm are covered.
